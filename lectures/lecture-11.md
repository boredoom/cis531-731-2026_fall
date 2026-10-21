# CIS 531/731: Programming Techniques for Data Science and Analytics
**Phase II:** Pipeline Construction
**Module 4:** Data Analytics Pipelines & Streaming
**Lecture 11:** Data Analytics Pipelines — Streaming & Data Lakes
**Date:** Monday, September 21, 2026

---

## Slide 1: Data Analytics Pipelines
### From Static Batches to Continuous Streams
* Phase II: Pipeline Construction | Module 4
* CIS 531/731

**Speaker Notes:**
Welcome to Lecture 11. In Phase I, we covered foundational transformations and actions using RDDs and DataFrames on bounded datasets. Today, we transition to Phase II. We are shifting from static, historical data to unbounded, live data feeds. We will explore how modern data pipelines ingest, process, and route continuous streams using the Dataflow model and Data Lake architectures.

---

## Slide 2: The Dataflow Model
### Akidau et al. & The End of Batch
* **The Paper:** "The Dataflow Model" by Tyler Akidau et al. (Google) fundamentally redefined stream processing.
* **The Core Premise:** Batch processing is just a special subset of stream processing where the data happens to be bounded.
* **Unbounded Datasets:** Data that arrives continuously and infinitely (e.g., IoT sensors, ASR audio streams, server logs).

**Speaker Notes:**
Your reading for today was Tyler Akidau's foundational paper on the Dataflow Model. The most critical paradigm shift in this paper is the realization that batch processing is not a separate discipline from streaming; it is merely stream processing applied to a finite dataset. When dealing with live ASR transcription or continuous telemetry, the dataset is unbounded—it literally never stops. Our architecture must account for infinite data streams without crashing out of memory.

---

## Slide 3: Streaming vs. Batch Processing
### Latency vs. Throughput
* **Batch Processing:** High latency, high throughput. Processes massive chunks of data overnight (e.g., training a deep learning model).
* **Stream Processing:** Low latency, variable throughput. Processes events as they occur (e.g., fraud detection, live dashboards).
* **Micro-batching:** A hybrid approach (used by Spark Structured Streaming) that processes data in very small, continuous chunks to balance latency and fault tolerance.

**Speaker Notes:**
Why not just run everything in a batch? Because batch processing has inherently high latency. If you are detecting credit card fraud or monitoring live server health, waiting until midnight to run a batch job means the damage is already done. Stream processing gives us low latency. Spark Structured Streaming, which we will use in our lab, actually uses 'micro-batching'—it collects stream data for a fraction of a second, processes it as a tiny batch, and repeats, giving us near-real-time latency with batch-level fault tolerance.

---

## Slide 4: Data Lakes Architecture
### Decoupling Storage from Compute
* **Traditional Data Warehouse:** Storage and compute are tightly coupled. Data must be structured before ingestion.
* **The Data Lake:** A centralized repository that allows you to store all structured and unstructured data at any scale (e.g., AWS S3, HDFS).
* **Independent Scaling:** Because storage is separated from the execution engine, you can scale storage infinitely without paying for compute nodes you aren't using.

**Speaker Notes:**
Where do we put this infinite stream of data? We dump it into a Data Lake. A major architectural flaw of older data warehouses was that compute and storage were locked together. If you needed more storage, you had to buy expensive database servers containing CPUs you didn't need. Data Lakes decouple this. We can dump petabytes of raw audio, logs, and JSON into a cheap object store like S3, and spin up Spark compute clusters only when we need to run analytics.

---

## Slide 5: Schema-on-Read vs. Schema-on-Write
### Flexibility in Data Ingestion
* **Schema-on-Write:** Data must be validated and transformed to fit rigid database tables before it can be saved (ETL).
* **Schema-on-Read:** Raw data is stored 'as-is'. The structure is applied only when the data is queried (ELT).
* **Machine Learning Advantage:** Storing raw, unstructured data ensures no features are accidentally discarded before data scientists can explore them.

**Speaker Notes:**
Because a Data Lake accepts unstructured data, we utilize 'Schema-on-Read'. In traditional databases, if a log file had an unexpected extra column, the database would reject the write. In a Data Lake, we just save the raw JSON or Parquet file. We apply the schema—the structure—only when PySpark reads the file. This is vital for machine learning, as it guarantees we never permanently drop raw telemetry that might be useful for a future hypothesis.

---

## Slide 6: The Two Domains of Time
### Event Time vs. Processing Time
* **Event Time:** The exact time the event physically occurred on the device (e.g., when the user clicked a button).
* **Processing Time:** The time the event arrived at the server and was processed by your Spark cluster.
* **The Skew:** Network latency, offline devices, and distributed system lag guarantee that these two times will rarely match.

**Speaker Notes:**
Perhaps the most important concept from Akidau's paper is the distinction between Event Time and Processing Time. If someone plays a game on their phone while on an airplane without Wi-Fi, the 'Event Time' happens at 2:00 PM. But if they connect to Wi-Fi at 5:00 PM, the 'Processing Time' is 5:00 PM. If your analytics pipeline groups data by Processing Time, your metrics will be completely wrong. Accurate analytics must always window data based on Event Time.

---

## Slide 7: Windowing and Late Data
### Bounding the Unbounded
* **Tumbling Windows:** Fixed-size, non-overlapping time intervals (e.g., exactly 1-minute blocks).
* **Sliding Windows:** Overlapping time intervals (e.g., a 1-minute window that updates every 10 seconds).
* **The Out-of-Order Problem:** Because we window by Event Time, we must keep windows 'open' in memory to catch data that arrives late due to network skew.

**Speaker Notes:**
To analyze a continuous stream, we chop it into 'windows'. A tumbling window is like a discrete bucket—data falls into the 1:00 to 1:05 bucket, and then the bucket closes. But because data arrives out of order, we can't instantly calculate the final metric for that bucket at 1:05. A delayed packet might arrive at 1:07 belonging to the 1:00 bucket. This means Spark has to hold that bucket's state in memory, waiting for late stragglers.

---

## Slide 8: Watermarks
### Managing State Memory
* **The Memory Leak Threat:** If we keep windows open infinitely waiting for late data, the cluster will run out of RAM and crash.
* **Watermarks:** A hard threshold that tells Spark how late data is allowed to be before it is permanently ignored.
* **Execution:** If the Watermark is 10 minutes, Spark tracks the maximum event time seen so far. Any data older than (Max Time - 10 mins) is dropped, and the state memory is safely freed.

**Speaker Notes:**
We cannot keep state memory open forever. If a phone reconnects to the internet a year later, we don't want to hold a window open for a year just in case. We enforce a Watermark. A watermark is a trailing threshold. If we set a 10-minute watermark, and our engine sees an event stamped 5:00 PM, it permanently closes any window older than 4:50 PM and clears the RAM. Any data arriving after the watermark is simply dropped.

---

## Slide 9: HW4 Overview
### Data Stream Monitoring
* **The Assignment:** HW4 is released today. You will build a complete PySpark Structured Streaming pipeline.
* **Ingestion:** You will ingest a continuous data feed, applying Schema-on-Read to parse the incoming JSON payload.
* **Aggregation:** You must calculate rolling statistics (e.g., counts per category) using tumbling Event Time windows.

**Speaker Notes:**
HW4 goes live today. This assignment takes everything we've discussed and puts it into code. You will write a PySpark script that connects to a continuous data stream. You will define a schema to extract fields from the raw JSON stream, and you will construct a query that aggregates statistics—like total event counts per category—using Event Time tumbling windows.

---

## Slide 10: HW4 Execution Constraints
### Deliverables and Deadlines
* **Watermark Requirement:** Your pipeline MUST include a functioning watermark. Pipelines that buffer infinite state will fail the auto-grader.
* **Memory Sink:** For testing, route your output to a memory sink so you can query the micro-batches interactively in your Jupyter notebook.
* **Due Date:** HW4 is due Thursday, October 1st at 11:59 PM. Submit your `.ipynb` and HTML export to Canvas.

**Speaker Notes:**
Pay close attention to the constraints in the HW4 spec. You are required to implement a watermark. If you forget the watermark command, your state will grow infinitely, and you will fail the grading script's memory limit test. We will practice the exact syntax for this during Friday's lab. Start reading the assignment now so you know what questions to ask during Wednesday's Spark syntax lecture. See you then.
