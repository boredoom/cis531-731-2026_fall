<!--
---
yaml_schema_version: "2.2"
document_version: "1.3"
document_last_updated_date: "2026-10-26"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
---
-->

<br>

<div align="center">
 <strong>🏫 Active Course Repositories:</strong> &nbsp;
 🏗️ <a href="https://github.com/kddresearch/course-architecture-base">Architecture Base</a> &nbsp;|&nbsp;
 🤖 CIS 530/730 &nbsp;|&nbsp;
 📊 <a href="https://github.com/kddresearch/cis531-731-2026_fall">CIS 531/731</a> &nbsp;|&nbsp;
 📈 CIS 732 &nbsp;|&nbsp;
 🎨 <a href="https://github.com/kddresearch/cis536-736-2026_fall">CIS 536/736</a> &nbsp;|&nbsp;
 👁️ CIS 798 X &nbsp;|&nbsp;
 🧠 CIS 830
</div>

<div align="center">
 <h1>📊 CIS 531/731 - Programming Techniques for Data Science and Analytics</h1>
 <p>
 <strong>Semester:</strong> Fall 2026 | <strong>Instructor:</strong> William H. Hsu<br>
 <strong>Status:</strong> ACTIVE | <strong>Canvas LMS:</strong> <a href="https://k-state.instructure.com/courses/201513">Closed SSO Portal</a>
 </p>
</div>

<hr>

<div align="center">
 <h2>📦 Module 04: Data Analytics Pipelines: Streaming & Data Lakes</h2>
 <p>
 <strong>Phase:</strong> <a href="../../phases/phase_02">Phase 2: Obtain & Ingest</a> | <strong>Maintainer:</strong> William H. Hsu
 </p>
</div>

<hr>

## 📖 Overview

This directory contains the localized pedagogical artifacts, demonstration code, and operational files strictly related to **Module 04**. This module spans `3` lectures and focuses on data analytics pipelines, streaming architectures, data lakes, Spark Structured Streaming, and streaming labs.

> **⚠️ Module Routing Notice**
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

<hr>

## 🗂️ Module Artifacts

| Subdirectory / File | Description |
| :--- | :--- |
| `lab04.ipynb` | Lab 4: Spark Structured Streaming and data lakes lab notebook |
| `README.md` | This module overview and index. |

<hr>

## 🔗 Associated Course Materials

- **Lectures:** [Lec 11](../../lectures/lecture-11.md) | [Lec 12](../../lectures/lecture-12.md) | [Lec 13](../../lectures/lecture-13.md)
- **Active Assignments:** [Lab 04 Notebook](../../assignments/homework/lab04.ipynb) | [MP5 Specification](../../assignments/machine_problems/mp5_structured_streaming.md) *(HW4 released, MP3 due)*
- **Required Reading:** "The Dataflow Model" (Akidau et al.); Structured Streaming Programming Guide, Spark 3.5.7

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

- **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
- **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
- **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

<br>
<hr>
<p align="center">
 <i>Maintained by the <a href="https://github.com/kddresearch">Knowledge Discovery in Databases (KDD) Lab</a> at Kansas State University.</i>
</p>

---

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| [**Phase 2:** Obtain & Ingest](../../phases/phase_02) | **Module 4:** Data Analytics Pipelines & Streaming | **Lectures 11-13** | Sep 21 – Sep 25, 2026 |

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
