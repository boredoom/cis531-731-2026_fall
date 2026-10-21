# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 2:** Pipeline Construction | **Module 4:** Data Analytics Pipelines & Streaming | **Lectures 11-13** | Sep 21 – Sep 25, 2026 |

---

## Lecture 11: Data Analytics Pipelines — Streaming & Data Lakes (Mon 21 Sep)

1. **The Dataflow Model:** Principles of handling massive, unbounded, out-of-order datasets based on the Akidau et al. framework.
2. **Streaming vs. Batch Processing:** Identifying the computational and latency trade-offs between continuous event streams and static batch pipelines.
3. **Data Lakes Architecture:** Decoupling storage from compute to support scalable, heterogeneous data ingestion and schema-on-read paradigms.
4. **Event Time vs. Processing Time:** Defining windowing functions, watermarks, and late data handling in continuous analytics.
5. **HW4 Release:** Introduction to the data stream monitoring assignment constraints and pipeline deliverables.

---

## Lecture 12: Spark Structured Streaming (Wed 23 Sep)

1. **Structured Streaming Model:** Translating DataFrame and Dataset operations onto unbounded streaming tables in Spark 3.5.7.
2. **Triggers and Output Modes:** Configuring micro-batch execution frequencies and Complete, Append, or Update output logic.
3. **Fault Tolerance & Checkpointing:** Ensuring exactly-once fault-tolerance semantics using write-ahead logs and state stores.
4. **Stateful Operations:** Managing arbitrary state across micro-batches for complex event processing and sessionization.
5. **Source & Sink Integration:** Connecting Spark Structured Streaming to distributed message brokers (Kafka) and Data Lake sinks.

---

## Lecture 13: Streaming Lab & Wrap-Up (Fri 25 Sep)

1. **Lab Setup:** Initializing the PySpark streaming context and connecting to a simulated live continuous data feed.
2. **Continuous Query Execution:** Authoring and deploying a windowed aggregation query to compute rolling metrics on the stream.
3. **Watermark Configuration:** Applying late-data thresholds to bound memory usage during stateful aggregations.
4. **Storage Sink Routing:** Ensuring the processed micro-batches are correctly persisted to the designated Data Lake storage path.
5. **MP 3 Debrief & Wrap-Up:** Reviewing the MP 3 (submitted prior day) solutions and verifying readiness for the Module 5 Scrub phase.
