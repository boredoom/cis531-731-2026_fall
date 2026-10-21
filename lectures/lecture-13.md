# CIS 531/731: Programming Techniques for Data Science and Analytics
**Phase II:** Pipeline Construction
**Module 4:** Data Analytics Pipelines & Streaming
**Lecture 13:** Streaming Lab & Wrap-Up
**Date:** Friday, September 25, 2026

---

## Slide 1: Streaming Lab & Wrap-Up
### CIS 531/731 - Lecture 13
* Lab Setup & PySpark Context
* Continuous Query Execution
* Watermark Configuration
* Storage Sink Routing
* MP 3 Debrief & Module 5 Transition

**Speaker Notes:**
Welcome to Friday's lab session. Today, we are putting our hands on the keyboard. We are going to initialize a PySpark Structured Streaming context, connect it to a live simulated data feed, and write a continuous query. We will also tackle the biggest danger in stream processing: memory exhaustion from stateful operations, which we will solve using Watermarks. Finally, we will debrief on Machine Problem 3.

---

## Slide 2: Lab Setup
### Initializing the PySpark Streaming Context
* **Environment:** Ensure your DevContainers are running and the Spark 3.5.7 dependencies are loaded.
* **The Entry Point:** `SparkSession`
* **Connecting to the Source:**
  ```python
  streaming_df = spark.readStream \
      .format("rate") \
      .option("rowsPerSecond", 10) \
      .load()
  ```
* **Simulated Feed:** We will use the built-in `rate` source to generate automatic timestamped data for testing before hooking up a real Kafka broker.

**Speaker Notes:**
Let's start by initializing our environment. Ensure your Docker DevContainers are up. In PySpark, everything starts with the `SparkSession`. Instead of `spark.read`, we use `spark.readStream`. For today's lab, to avoid the overhead of spinning up a Kafka cluster, we are using Spark's built-in `rate` source. It acts as a simulated live feed, automatically generating rows with timestamps at a speed we control, giving us a perfect testing ground.

---

## Slide 3: Continuous Query Execution
### Authoring Windowed Aggregations
* **The Goal:** Compute rolling metrics on the live stream (e.g., event counts per 10-second window).
* **Event Time:** We must aggregate based on when the event *actually occurred* (the timestamp in the data), not when Spark processes it.
* **The Query:**
  ```python
  windowed_counts = streaming_df \
      .withWatermark("timestamp", "10 minutes") \
      .groupBy(window(streaming_df.timestamp, "10 seconds", "5 seconds")) \
      .count()
  ```
* **Sliding Windows:** Creates overlapping time boundaries for continuous metric smoothing.

**Speaker Notes:**
Now we write our query. We want to count how many events happen every 10 seconds. Crucially, we group by *Event Time*—the timestamp embedded inside the data payload. If network latency delays a packet, we still want it counted in the correct time window. We achieve this using a sliding window: a 10-second window that updates every 5 seconds, providing a smoothed, rolling metric of our stream's health.

---

## Slide 4: Watermark Configuration
### Bounding Memory and Handling Late Data
* **The Memory Threat:** In stateful aggregations, Spark must keep old windows in RAM just in case late data arrives. Infinite time = infinite RAM crash.
* **The Watermark:** A moving threshold that tells Spark how late data is allowed to be.
* **The Rule:** `Watermark = Max Event Time Seen - Late Threshold`
* **Execution:** Once the watermark passes a window's end time, that window is finalized, the result is outputted, and the state is purged from memory.

**Speaker Notes:**
This is the most critical slide of the day. If you group by time, Spark has to keep that time bucket open in memory forever because a delayed event from three days ago might suddenly arrive. This will crash your cluster. The `withWatermark` function solves this. By setting a watermark of 10 minutes, you tell Spark: "If an event is more than 10 minutes older than the newest data we've seen, drop it." Once a time window is older than the watermark, Spark safely flushes it from RAM and finalizes the output.

---

## Slide 5: Storage Sink Routing
### Persisting the Micro-Batches
* **The Data Lake Sink:** Writing the processed, aggregated data out to durable storage.
* **The Code:**
  ```python
  query = windowed_counts.writeStream \
      .outputMode("append") \
      .format("parquet") \
      .option("path", "/data/lake/output/") \
      .option("checkpointLocation", "/data/lake/checkpoints/") \
      .start()
  ```
* **Checkpointing is Mandatory:** You cannot start a write stream without specifying a persistent directory for the Write-Ahead Logs.

**Speaker Notes:**
Once the data is aggregated and watermarked, we must route it to our sink. We initiate this with `writeStream`. Notice that we define the output format as Parquet, pointing it to our Data Lake directory. The absolute most important line here is the `checkpointLocation`. Spark will physically refuse to start a stateful streaming query without a checkpoint directory, because without it, fault tolerance is impossible. 

---

## Slide 6: MP 3 Debrief & Wrap-Up
### Transitioning to Module 5
* **MP 3 Review:** (Submitted yesterday). We will review the common bottlenecks encountered with the procedural pipelines and pipeline parameterization.
* **Module 5 Preview:** The Data Scrub Phase.
* **Next Week:** We move from raw ingestion to rigorous data quality enforcement, anomaly detection, and schema validation.
* **Action Items:** Ensure your `Lab3_Procedural_Pipelines.ipynb` notebook from today is committed to your assignment repositories before the end of the weekend.

**Speaker Notes:**
To wrap up, let's look at MP 3, which was due yesterday. I'll open the floor for any architectural bottlenecks you faced. Looking ahead, Module 5 introduces the "Scrub" phase of the data science lifecycle. Now that we know how to ingest static and streaming data, we have to deal with the reality that real-world data is dirty, corrupted, and anomalous. Next week, we build the filters. Please ensure today's lab notebook is committed to your repos. Have a great weekend.
