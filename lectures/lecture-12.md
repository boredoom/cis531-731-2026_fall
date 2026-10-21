# CIS 531/731: Programming Techniques for Data Science and Analytics
**Phase II:** Pipeline Construction
**Module 4:** Data Analytics Pipelines & Streaming
**Lecture 12:** Spark Structured Streaming
**Date:** Wednesday, September 23, 2026

---

## Slide 1: Spark Structured Streaming
### CIS 531/731 - Lecture 12
* The Structured Streaming Model
* Triggers and Output Modes
* Fault Tolerance & Checkpointing
* Stateful Operations
* Source & Sink Integration

**Speaker Notes:**
Welcome to Lecture 12. On Monday, we covered the Akidau framework and the fundamental differences between batch and stream processing, setting up our Data Lake architecture. Today, we are moving from theory to execution using Apache Spark 3.5.7. We will explore Spark Structured Streaming, which allows us to treat live data streams as continuously appending relational tables. 

---

## Slide 2: The Structured Streaming Model
### Unbounded Tables in Spark 3.5.7
* **The Core Paradigm:** Treat a live data stream as a table that is being continuously appended.
* **DataFrame/Dataset API:** The exact same API used for batch processing (static DataFrames) is used for streaming queries.
* **Micro-Batch Execution:** Spark's engine incrementally and continuously processes data in small batches, updating the final result.
* **Continuous Processing Mode:** An optional mode for ultra-low latency (~1 ms) without micro-batching.

**Speaker Notes:**
The brilliance of Spark Structured Streaming is its simplicity. It hides the complexity of streaming behind the DataFrame API you already know. Instead of a static table, imagine an "unbounded table." Every new piece of data that arrives on the stream is appended as a new row to this table. You write your standard SQL or DataFrame queries against it, and Spark's execution engine automatically figures out how to run it incrementally as micro-batches.

---

## Slide 3: Triggers and Output Modes
### Controlling Execution and Delivery
* **Triggers:** Define *when* the streaming engine evaluates the query.
  * *Default:* Micro-batch fires as soon as the previous one finishes.
  * *Fixed Interval:* E.g., `Trigger.ProcessingTime("10 seconds")`.
  * *Available-Now:* Process everything currently available, then stop (great for cost-saving cloud architectures).
* **Output Modes:** Define *what* gets written to the sink.
  * *Append:* Only new rows are written (requires operations that don't change past rows).
  * *Complete:* The entire updated result table is written every time.
  * *Update:* Only the rows that have changed since the last trigger are written.

**Speaker Notes:**
Once your query is running, you need to control its cadence and output. "Triggers" tell Spark how often to check for new data. "Available-Now" is particularly powerful in modern cloud environments because you can spin up a cluster, process the backlog, and shut down to save money. "Output Modes" define what gets sent downstream. If you are just logging events, use Append. If you are keeping a live leaderboard of top users, you need Complete or Update mode.

---

## Slide 4: Fault Tolerance & Checkpointing
### Guaranteeing Exactly-Once Semantics
* **The Problem:** Nodes crash, networks fail, and streams drop. How do we prevent data loss or double-counting?
* **Checkpointing:** Spark saves the exact progress (offsets) and intermediate state to durable storage (like HDFS or S3).
* **Write-Ahead Logs (WAL):** Records the intent to process data before execution, ensuring recoverability.
* **Exactly-Once Semantics:** By combining replayable sources (like Kafka) and idempotent sinks, Spark guarantees every record is processed perfectly once, even amid failures.

**Speaker Notes:**
In distributed systems, hardware failure is not a possibility; it's a guarantee. If a worker node crashes mid-stream, we cannot lose data, nor can we accidentally process the same data twice. Spark solves this using Checkpointing and Write-Ahead Logs. By storing its read offsets in a durable Data Lake, a recovering Spark cluster knows exactly where it left off. When paired with a replayable source like Kafka, we achieve the holy grail of streaming: exactly-once fault-tolerance semantics.

---

## Slide 5: Stateful Operations
### Managing State Across Micro-Batches
* **Stateless Operations:** `select()`, `filter()`, `map()`. Operations that only care about the current row.
* **Stateful Operations:** Aggregations, running totals, and sessionization. 
* **The Challenge:** To compute a running average, Spark must remember the previous sum and count across millions of events.
* **State Store:** Spark maintains this intermediate state in memory (backed by rocksDB) and persists it to the checkpoint directory.

**Speaker Notes:**
Filtering out bad records is easy; it's stateless. But what if you want to track a user's session over the last 30 minutes? Or a running sum of transactions? Spark has to remember data from previous micro-batches. This is called a Stateful Operation. Spark manages this by keeping a highly optimized "State Store" in memory. However, state grows infinitely over time if left unchecked, which leads us directly to the concept of Watermarking, which we will implement in Friday's lab.

---

## Slide 6: Source & Sink Integration
### Connecting the Pipeline
* **Sources (Ingestion):**
  * *Kafka:* The industry standard distributed message broker.
  * *Socket:* Great for testing (Netcat).
  * *Cloud Storage (S3/GCS):* Streaming new files as they land.
* **Sinks (Egress):**
  * *Console:* For debugging.
  * *Data Lakes (Delta Lake / Parquet):* For scalable, schema-on-read storage.
  * *Kafka:* Routing processed streams to downstream applications.

**Speaker Notes:**
A stream processing engine doesn't live in a vacuum. It sits between a Source and a Sink. For high-throughput production systems, your source is almost always Apache Kafka. Once Spark processes the data—cleaning it, aggregating it, enriching it—it writes it to a Sink. In modern architectures, this is typically a Data Lake using a format like Delta Lake, which allows downstream data scientists to run batch analytics on the cleaned streaming data. We will build this exact integration on Friday.
