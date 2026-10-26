<!--
---
yaml_schema_version: "2.2"
document_version: "1.1"
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
 <h2>📦 Module 05: Scrub: Chunking, Embedding Generation & VDB Schema Design</h2>
 <p>
 <strong>Phase:</strong> <a href="../../phases/phase_03">Phase 3</a> | <strong>Maintainer:</strong> William H. Hsu
 </p>
</div>

<hr>

## 📖 Overview

This directory contains the localized pedagogical artifacts, demonstration code, and operational files strictly related to **Module 05**. This module spans `3` lectures and focuses on data scrubbing, document chunking, embedding generation, semantic search, vector database schema design, and embedding/indexing labs.

> **⚠️ Module Routing Notice**
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

<hr>

## 🗂️ Module Artifacts

| Subdirectory / File | Description |
| :--- | :--- |
| `lab5.ipynb` | Lab 5: Chunking, embedding generation, and vector indexing lab notebook |
| `README.md` | This module overview and index. |

<hr>

## 🔗 Associated Course Materials

* **Lectures:** [Lec 14](../../lectures/lecture-14.md) | [Lec 15](../../lectures/lecture-15.md) | [Lec 16](../../lectures/lecture-16.md)
* **Active Assignments:** [Lab 5 Notebook](../../assignments/homework/lab5.ipynb) | [PS6 Semantic Search & VDB Schema](../../assignments/homework/ps6_semantic_search_vdb_schema.md) *(HW4 due prior day)*
* **Required Reading:** Speech and Language Processing, Ch. 11 (Jurafsky & Martin); Sentence Transformers "Semantic Search"

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this module directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files and localized scripts in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Artifact Segregation):** Do not duplicate master assignment files or lecture notes here. Use the "Associated Course Materials" cross-links provided above.
* **Protocol 3 (Deprecation):** Ensure any outdated code snippets in this module are formally tagged as `[ARCHIVED]` if updating for a new semester to prevent student confusion.

<br>
<hr>
<p align="center">
 <i>Maintained by the <a href="https://github.com/kddresearch">Knowledge Discovery in Databases (KDD) Lab</a> at Kansas State University.</i>
</p>

---

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 2:** Pipeline Execution | **Module 5:** Scrub (Chunking & Embedding Generation) | **Lectures 14-16** | Sep 28 – Oct 02, 2026 |

---

## Lecture 14: Scrub — Chunking & Embedding Generation (Mon 28 Sep)

1. **The "Scrub" Phase:** Transitioning from raw data ingestion to structured, machine-readable representations within the data science pipeline.
2. **Text Chunking:** Strategies for dividing long-form ASR (Automatic Speech Recognition) transcripts into semantically coherent segments suitable for downstream processing.
3. **The Boundary Problem:** Analyzing how fixed-size chunking can sever sentences or concepts, and mitigating context loss using recursive character chunking with stride (overlap).
4. **Embedding Generation Introduction:** The mathematical intuition behind transforming chunked text into dense vector representations.
5. **Reading Callout:** Review *Speech and Language Processing, Ch. 11* (Jurafsky & Martin) for foundational NLP processing concepts.

---

## Lecture 15: Semantic Search & VDB Schema Design (Wed 30 Sep)

1. **The Vector Space Model:** Representing concepts as high-dimensional arrays, where semantic proximity is measured mathematically (e.g., Cosine Similarity, Dot Product).
2. **Transformer-Based Embeddings:** Utilizing models like Sentence Transformers to generate dense vectors that capture sentence-level semantic meaning.
3. **Vector Database (VDB) Fundamentals:** Understanding the distinction between traditional relational databases (SQL exact matching) and Vector Databases optimized for semantic similarity search.
4. **VDB Schema Design:** Structuring the collection payload to store the original transcript chunk, timestamp, and speaker ID alongside the vector to ensure context is retained during retrieval.
5. **Reading Callout:** Review the Sentence Transformers "Semantic Search" documentation to understand the programmatic implementation of bi-encoders.

---

## Lecture 16: Embedding Lab & VDB Indexing (Fri 02 Oct)

1. **Lab Setup:** Initializing a local embedding model (e.g., `all-MiniLM-L6-v2`) via the Hugging Face Sentence Transformers library.
2. **Executing the Chunking Script:** Implementing a recursive character chunker with a defined overlap on the raw ASR corpus acquired in Module 3.
3. **Batch Vectorization:** Generating and processing embeddings for the chunked ASR dataset in memory.
4. **Database Ingestion:** Defining the VDB schema and inserting the generated vectors along with their required metadata payloads.
5. **HW4 Wrap-Up:** Final questions and debrief for HW4 (Data Analytics Pipelines), due the previous day, before transitioning to GenAI classification in Module 6.
