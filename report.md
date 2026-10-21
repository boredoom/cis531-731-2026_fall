```markdown
# MP 5 Technical Report: Structured Streaming Pipeline for Hip-Hop Corpus Chunks

**Student:** Arron Weber (CIS 531 Undergraduate / Data Engineering Lead)  
**Track:** Prescriptive Analytics | Text Corpora | Track 2 (VDB Text Corpora & Trope Ontologies)  
**Git Tag:** `mp5-submission`  
**Execution Baseline:** Pinned CPU DevContainer (OpenJDK 17, Python 3.11, PySpark 3.5.1, deal 4.24.4)

---

## Schema and Contracts

Undergraduate CIS 531 teams are required by course policy (INV-11) to adopt the instructor-provided ontology schema unmodified rather than inferring custom topologies. For Track 2 (VDB Text Corpora), the instructor-specified record contract is `CorpusChunk`.

```python
from pyspark.sql.types import (
    DoubleType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

CorpusChunkSchema = StructType(
    [
        StructField("record_id", StringType(), nullable=False),
        StructField("track", StringType(), nullable=False),
        StructField("source_id", StringType(), nullable=False),
        StructField("ts_start", TimestampType(), nullable=False),
        StructField("ts_end", TimestampType(), nullable=False),
        StructField("text", StringType(), nullable=False),
        StructField("ingest_ts", TimestampType(), nullable=False),
        StructField("license_class", StringType(), nullable=False),
    ]
)

```

### Nullability Justifications

* **`record_id` (non-nullable):** Serves as the primary deduplication key and trace anchor linking Bronze JSONL payloads to Silver chunks. Null IDs cause non-deterministic record drops and corrupt downstream FAISS vector indexing.
* **`track` (non-nullable):** Represents the canonical song identity required for entity grouping and artist-level trope analysis. Null track identifiers create untraceable orphan records.
* **`source_id` (non-nullable):** Governs origin filtering against approved data providers (`genius`, `spotify`, `musicbrainz`, `rym`). Null sources bypass provenance admission gates.
* **`ts_start` (non-nullable):** The lower temporal boundary of the lyric chunk. Required to compute chunk duration and enforce the temporal monotonicity constraint ($\text{ts\_start} < \text{ts\_end}$).
* **`ts_end` (non-nullable):** Serves as the streaming event-time timestamp driving `withWatermark()` and window assignment. Spark Structured Streaming drops records containing null event timestamps.
* **`text` (non-nullable):** The natural language payload. Null strings exhaust state store memory while generating zero tokens during sliding window text tokenization.
* **`ingest_ts` (non-nullable):** System landing-zone arrival time. Required to compute operational lateness ($L = \text{ingest\_ts} - \text{ts\_end}$) and verify pipeline liveness constraints (INV-5).
* **`license_class` (non-nullable):** Provenance gate field indicating corpus legal classification (e.g., `fair_use`). Null classifications violate intellectual property admission gates.

### Deal Contracts

Enforced in `contracts.py` via the `deal` library:

1. **BoundedChunking Gate:**

$$\text{ts\_start} < \text{ts\_end} \quad \text{and} \quad (\text{ts\_end} - \text{ts\_start}) \le 30.0\text{ seconds}$$


2. **Whitelist Gate:**

$$\text{source\_id} \in \{\text{'genius'}, \text{'spotify'}, \text{'musicbrainz'}, \text{'rym'}\}$$


3. **Provenance Gate:**

$$\text{license\_class} \in \{\text{'fair\_use'}, \text{'public\_domain'}, \text{'cc\_by\_sa'}, \text{'all\_rights\_reserved\_educational'}\}$$


4. **Causality Gate:**

$$\text{ingest\_ts} \ge \text{ts\_end}$$



---

## Watermark and State Analysis

### Lateness Distribution

Lateness ($L = \text{ingest\_ts} - \text{ts\_end}$) was measured by replaying 14,000 serialized lyric chunk records through the rate-controlled file micro-batch landing zone:

* **p50 Lateness:** 2.41 seconds
* **p95 Lateness:** 14.82 seconds
* **p99 Lateness:** 28.15 seconds
* **Max Observed Lateness:** 34.20 seconds

### Watermark Delay and Trade-Off

The watermark delay is set to **15 seconds** based on the empirical p95 lateness threshold:

```python
watermarked_stream = filtered_stream.withWatermark("ts_end", "15 seconds")

```

* **Completeness vs. Latency:** Setting the watermark delay to 15 seconds bounds trigger latency while admitting 95.2% of all late-arriving chunks. Extending the watermark to 30 seconds to capture the remaining 4.8% tail increases state memory retention time by 100%, delaying window finalization without altering dominant trope frequencies.
* **Required Output Mode:** **Append Mode**. Spark Structured Streaming requires Append mode for streaming window aggregations when writing to file sinks (Parquet). Windows are emitted only after $\text{watermark} \ge \text{window.end}$, guaranteeing that emitted window rows are final and immutable.
* **State-Growth Bound:** Let $W$ be window duration, $S$ slide duration, and $D$ watermark delay. An aggregation bucket is retained in state until:

$$\text{current\_event\_time} - D \ge \text{window.end}$$



The maximum number of concurrent active windows $N_{\text{active}}$ maintained in state per key is bounded by:

$$N_{\text{active}} \le \left\lceil \frac{W + D}{S} \right\rceil$$


* For the 60-second tumbling window ($W=60\text{s}, S=60\text{s}, D=15\text{s}$):

$$N_{\text{active}} \le \left\lceil \frac{60 + 15}{60} \right\rceil = 2\text{ active windows}$$


* For the 5-minute sliding window ($W=300\text{s}, S=60\text{s}, D=15\text{s}$):

$$N_{\text{active}} \le \left\lceil \frac{300 + 15}{60} \right\rceil = 6\text{ active windows}$$



Because key cardinality within any 315-second horizon is physically bounded by track count ($K \le 1,400$), total state operator memory cannot exceed $O(K \times 6)$, preventing unbounded state growth.



---

## Query Design

The streaming pipeline computes two concurrent event-time window aggregations over sanitized `CorpusChunk` records:

### Window Specifications

1. **60-Second Tumbling Window:** Captures short-term burstiness in lyric ingest and distinct vocabulary size:
```python
tumbling_query = tokenized_stream.groupBy(
    F.window("ts_end", "60 seconds")
).agg(
    F.count("record_id").alias("record_count"),
    F.approx_count_distinct("token", 0.05).alias("approx_distinct_tokens"),
    F.avg("latency_sec").alias("mean_ingest_latency_sec")
)

```


2. **5-Minute Sliding Window (1-Minute Slide):** Smooths lexical variation and tracks rolling topical drift:
```python
sliding_query = tokenized_stream.groupBy(
    F.window("ts_end", "5 minutes", "1 minute")
).agg(
    F.count("record_id").alias("record_count"),
    F.approx_count_distinct("token", 0.05).alias("approx_distinct_tokens"),
    F.avg("latency_sec").alias("mean_ingest_latency_sec")
)

```



### Top-10 Term Aggregation & Sink Architecture

Top-10 terms are extracted per window using an array aggregate over bounded token counts. Both streams sink to append-mode Parquet partitions backed by dedicated checkpoint directories:

```python
query = (
    tumbling_query.writeStream
    .format("parquet")
    .outputMode("append")
    .option("checkpointLocation", "/workspace/checkpoints/tumbling_sink/")
    .option("path", "/workspace/output/tumbling_sink/")
    .trigger(processingTime="10 seconds")
    .start()
)

```

---

## Fault-Tolerance Reconciliation

### Fault Injection & Restart Procedure

To verify recovery semantics under ungraceful worker termination:

1. The streaming query was executed against 20 landing zone micro-batches.
2. During micro-batch 8 execution, `SIGKILL` (kill -9) was issued to the Python driver process.
3. The checkpoint state directory was inspected:
* `offsets/8`: Present (batch 8 source offsets locked).
* `commits/8`: Missing (batch 8 uncommitted at crash time).
* Partially written Parquet parts remained in `/workspace/output/tumbling_sink/`.


4. The pipeline was re-instantiated with identical code and checkpoint location.
5. Spark detected uncommitted batch 8, re-read the exact offsets recorded in `offsets/8`, recomputed the aggregations, wrote final part files, and committed `commits/8` before advancing to batch 9.

### Reconciliation Results

```text
Pre-Failure Windows Processed (Batches 0-7):  42 windows (1,840 records)
Crash Point: Batch 8 (120 records in-flight)
Post-Restart Windows Processed (Batches 8-19): 78 windows (3,460 records)
Total Reconciled Window Keys:                  120 unique windows
Duplicate Window Keys:                         0
Missing Window Keys:                           0
Row Count Discrepancy:                         0 records

```

### Exactly-Once Guarantees

* **Checkpointing Role:** Guarantees deterministic source offset replay and internal state store recovery. The write-ahead log records exact file splits assigned to each batch, preventing lost event ranges.
* **Idempotent Sink Role:** Append-mode Parquet relies on Spark's `FileCommitProtocol`. Files produced by aborted batch attempts are omitted from the metadata transaction log (`_spark_metadata`). Downstream readers reading via Spark ignore zombie files, ensuring end-to-end exactly-once delivery.

---

## Metrics and Reproducibility

### StreamingQueryProgress Summary

Performance metrics collected over a continuous 20-batch run on the pinned CPU DevContainer:

| Metric | Measured Value | Requirement / Target |
| --- | --- | --- |
| **`inputRowsPerSecond`** | 48.6 rows/s | Paced landing zone replay (~50 rows/s) |
| **`processedRowsPerSecond`** | 62.4 rows/s | Must exceed input rate for liveness (INV-5) |
| **`batchDuration`** | 1,842 ms | Strictly less than 10s trigger interval |
| **`stateOperators.numRowsTotal`** | 184 rows (peak) | Strictly bounded by $O(K \times 6)$ |
| **State Memory Allocated** | 3.42 MB | Prevents DevContainer container OOM |

### Pinned Environment & CI Verification

* **Environment:** CPU-only DevContainer (x86_64, 2 vCPU cores, 4 GB RAM allocation, Ubuntu 22.04 LTS).
* **Software:** OpenJDK 17.0.10, Python 3.11.8, PySpark 3.5.1, `deal` 4.24.4, PyArrow 15.0.0.
* **CI Status:** GitHub Actions workflow `mp5-ci.yml` passing on standard `ubuntu-latest` CPU runners.
* **ASR Track Quota:** N/A. Because the pipeline executes rate-controlled file micro-batch replay for `CorpusChunk` rather than caller ASR audio, AssemblyAI quota consumption is 0 units ($0.00 spent).

---

## GenAI Audit

* **Tool Utilized:** Gemini via Generative AI Project Kit v2.3 Tollbooth workflow.
* **Prompts Applied:** MP 5 Structured Streaming Tollbooth prompt asserting Track 2 specifications:
* Input payload: Sample lyric JSON records from Genius/Spotify Bronze Parquet.
* Properties asserted: `chunk_duration <= 30s`, `p95 lateness = 14.82s`, CIS 531 undergraduate enrollment.


* **Synthesis Boundaries:** AI was used to derive the structural `deal` contract constraints and draft the window aggregation skeleton. In accordance with policy INV-11, the `CorpusChunk` schema was adopted unmodified from instructor specifications.
* **Verification:** The student manually implemented `contracts.py`, performed fault injection with `SIGKILL`, validated zero duplicate window keys in the reconciliation script, and verified CPU baseline execution within the DevContainer environment.
* **Documentation:** Full audit logs, raw prompt receipts, and diffs are archived in `GenAI.pdf`.

```