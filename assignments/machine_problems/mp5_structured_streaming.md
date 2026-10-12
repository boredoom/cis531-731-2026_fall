<!-- ASSIGNMENT-META
id: MP 5
phase: Phase 2: Obtain & Ingest
module: Module 04: Data Analytics Pipelines (Structured Streaming)
released: Fri 09 Oct 2026
due: Tue 20 Oct 2026
prev: assignments/homework/ps4_proposal.md
next: assignments/homework/ps6_semantic_search_vdb_schema.md
REVIEW R-1: Due date conflict. Task list states Tue 20 Oct; constraint 2 text states Mon 19 Oct. Draft uses Tue 20 Oct.
REVIEW R-2: PS 4 release/due dates were not supplied; the gap between PS 4 and MP 5 is unverified.
-->
# MP 5: Data Analytics Pipelines (Structured Streaming)
**Event-time windowed analytics, checkpointed fault tolerance, and contract-validated ingest over replayed and live sources**

**🗓️ Released:** Fri 09 Oct 2026 | **📅 Due:** Tue 20 Oct 2026 | **💯 Points:** 100 | **👥 Team:** Individual

> **🚨 CRITICAL SUBMISSION POLICY**
> **Source Whitelist and Quota Killswitch:** Live ASR capture is restricted to the instructor whitelist and the instructor RTMP demo stream (INV-10); any other URL fails the ingest precondition. API usage is bounded by your team quota; exhaustion triggers an automatic fallback to the CPU baseline or free tier (INV-18) and carries no emergency bailout.

## 1. Overview
Implement a fault-tolerant Spark Structured Streaming job (PySpark 3.5.x) that ingests chunked records, validates them against explicit `deal` contracts, and computes event-time window aggregates with watermarking and checkpointed recovery. The primary source is the MP 3 landing zone replayed at a controlled rate through a file source. ASR-track students additionally stream one saved MP 3 audio segment (at most 10 minutes) to AssemblyAI at real-time rate (INV-7), so the MP 3 Whisper baseline transcript and the AssemblyAI transcript cover identical audio and can be scored later (MP 9, MP 10). VDB-track students replay admitted corpus documents as micro-batches.

All work must be solvable on the pinned CPU DevContainer (INV-14/INV-15); GPU access is optional and never required.

**Cadence Notice:** Released Fri 09 Oct 2026 (Wildcat Pause Day); the Tue 20 Oct 2026 due date provides an 11-day window in observance of the pause day. MP 5 is due 5 days before PS 6 (Sun 25 Oct 2026), an explicit exception to the standard 6-day inter-assignment gap, applied to maintain assignment cadence without forcing a due date on Halloween (Sat 31 Oct).

**Required Readings:**
* [“The Dataflow Model” (Akidau et al., VLDB 2015)](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf): event time vs. processing time; windows, watermarks, and triggers; completeness, latency, and cost trade-offs.
* [Structured Streaming Programming Guide (Spark 3.5.7)](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html): programming model through fault tolerance: window operations, late data and watermarking, output modes, checkpointing, exactly-once semantics.

**Upstream inputs:** MP 3 landing zone and provenance manifest; PS 4 track and data plan.  
**Downstream consumers:** PS 6 (record schema extends this chunk record); MP 7 (chunk stream is the classifier input); PS 8 (architecture and baselines); HW 12 (serving job and `metrics.jsonl` conventions).

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Contract Extraction:** Have the AI Kit derive the record `StructType` and `deal` contracts (BoundedChunking: `chunk_duration_sec <= 30`, `ts_start < ts_end`; whitelist and provenance gates) from this specification, then verify every nullability choice yourself.
2. **Pipeline Scaffold:** Generate the `readStream` / `withWatermark` / `groupBy(window(...))` skeleton with an explicit schema; audit it for schema inference, missing watermarks, unbounded state, and non-idempotent sinks.
3. **Event-Time Calibration:** Replay the landing zone, measure the lateness distribution `ingest_ts - ts_end` (p50/p95/p99), and derive the watermark delay from it.
4. **Fault Injection:** Set `checkpointLocation`, write to an append-mode Parquet sink, kill the query mid-run, restart it, and reconcile row counts and window keys.
5. **Run Report:** Assemble `metrics.jsonl` and the report sections; verify that every reported number reproduces on the CPU baseline.

## 3. Required Document Structure
Your submission must be a **single `report.md` (at most 3 pages) delivered with Git tag `mp5-submission` (code, `contracts.py`, `metrics.jsonl`, reconciliation notebook)** containing the following sections exactly as named below. 

* **Schema and Contracts:** Explicit `StructType` (`TranscriptChunk` for ASR; `CorpusChunk` for VDB: `record_id`, `track`, `source_id`, `ts_start`, `ts_end`, `text`, `ingest_ts`, plus `license_class` for corpus records), nullability justification, and the `deal` contracts.
* **Watermark and State Analysis:** Lateness percentiles, the chosen watermark delay and its completeness-vs-latency trade-off, the required output mode, and the state-growth bound.
* **Query Design:** 60-second tumbling and 5-minute/1-minute sliding windows computing record count, `approx_count_distinct` of tokens, top-10 terms, and mean ingest latency; sink design.
* **Fault-Tolerance Reconciliation:** Restart procedure; row-count and window-key reconciliation showing no duplicate or missing windows; which exactly-once guarantees come from checkpointing versus an idempotent sink.
* **Metrics and Reproducibility:** `StreamingQueryProgress` summary (`inputRowsPerSecond`, `processedRowsPerSecond`, `batchDuration`, `stateOperators.numRowsTotal`), pinned-environment statement, CI status, and the AssemblyAI quota log (ASR track). Throughput and latency targets are liveness properties (INV-5) assessed from the metrics log, not from contracts.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (100 Points Total)

This assignment is worth 100 points total.

**Part 1: Contracts and Event-Time Analysis (30 pts)**
* **Schema and contracts (15 pts):** Explicit schema, justified nullability, and contracts covering BoundedChunking and provenance/whitelist gates.
* **Watermark and state analysis (15 pts):** Watermark derived from measured lateness; output mode and state bound justified.

**Part 2: Streaming Pipeline (65 pts)**
* **Query correctness (25 pts):** Window definitions and aggregates are correct on the reference replay.
* **Fault tolerance (25 pts):** Restart demonstration with exact reconciliation and no duplicate window keys.
* **Metrics and reproducibility (15 pts):** Metrics log complete; pinned environment; CI green on the CPU baseline.

* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [PS 4: Term Project Proposal](../homework/ps4_proposal.md) | [[All Assignments]](../README.md#schedule)  | [PS 6: Semantic Search, Chunking, & VDB Schema](../homework/ps6_semantic_search_vdb_schema.md) |

[🏠 Course Home](../../README.md) · [⬆️ Module](../../modules/module_04/README.md) · [⏫ Phase](../../phases/phase_02/README.md)
