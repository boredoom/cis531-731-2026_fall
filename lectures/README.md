<!--
---
yaml_schema_version: "2.2"
document_version: "1.0"
document_last_updated_date: "2026-10-12"
document_monotonicity: "REQUIRED"
routing_clearance: "INTERNAL - RESTRICTED TO COURSE MAINTAINERS"
---
-->

<br>

<div align="center">
 <strong>🏫 Active Course Repositories:</strong> &nbsp;
 🏗️ <a href="https://github.com/kddresearch/course-architecture-base">Architecture Base</a> &nbsp;|&nbsp;
 🤖 CIS 530/730 &nbsp;|&nbsp;
 📊 CIS 531/731 &nbsp;|&nbsp;
 📈 CIS 732 &nbsp;|&nbsp;
 🎨 CIS 536/736 &nbsp;|&nbsp;
 👁️ CIS 798 X &nbsp;|&nbsp;
 🧠 CIS 830
</div>

<div align="center">
 <h1>📊 CIS 531/731 - Data Science Systems</h1>
 <p>
 <strong>Semester:</strong> Fall 2026 | <strong>Instructor:</strong> William H. Hsu<br>
 <strong>Status:</strong> ACTIVE | <strong>Canvas LMS:</strong> <a href="https://k-state.instructure.com/courses/201513">Closed SSO Portal</a>
 </p>
</div>

<hr>

<div align="center">
 <h2>📂 Directory: lectures</h2>
 <p>
 <strong>Status:</strong> ACTIVE | <strong>Maintainer:</strong> Course Maintainers / KDD Lab
 </p>
</div>

<hr>

## 📖 Overview

This directory houses the official lecture schedule, slide decks, module breakdowns, and assigned reading materials for CIS 531/731 (Data Science Systems) for the Fall 2026 semester. The curriculum spans 43 structured lectures across 12 foundational modules, covering PySpark architectures, containerized environments, data streaming, vector database indexing, generative AI applications, EDA visualization, model evaluation, and MLOps deployment.

> **⚠️ Sub-Directory Routing Notice**
> This directory serves a specific pedagogical function. Ensure that artifacts committed here belong in this directory, rather than a different course module or upstream folder.

<hr>

## 🗂️ Directory Structure

| Subdirectory / File | Description |
| :--- | :--- |
| `modules/` | Module-specific lecture notes, code notebooks, and supplementary lab guides. |
| `slides/` | Compiled PDF and HTML slide decks corresponding to each lecture. |
| `README.md` | This file containing the master lecture schedule and reading ledger. |

<hr>

## 📅 Lecture Schedule — CIS 531/731, Fall 2026 (Final, 43 Lectures)

| Week | Date | Lecture # | Topic | Assigned Reading |
|---|---|---|---|---|
| 1 | Mon 24 Aug 2026 | 0 | Module 0 – Welcome & Course Overview | FAIR Guiding Principles (Wilkinson et al.); Jupyter Notebook Documentation |
| 1 | Wed 26 Aug 2026 | 1 | Module 1 – PySpark Intro: RDDs & DataFrames | Python Data Science Handbook (VanderPlas) |
| 1 | Fri 28 Aug 2026 | 2 | Module 1 – Experiment Design & Reproducible Projects | Research Software Engineering with Python (Irving et al.) |
| 2 | Mon 31 Aug 2026 | 3 | Module 1 – RDD Transformations & Actions Lab | — |
| 2 | Wed 02 Sep 2026 | 4 | Module 1 – Wrap-Up | — |
| 2 | Fri 04 Sep 2026 | 5 | Module 2 – Tools: Cloud & Hosted Services (MP2 released) | Research Software Engineering (Brett et al.) |
| 3 | Mon 07 Sep 2026 | — | **NO CLASS — Labor Day** | — |
| 3 | Wed 09 Sep 2026 | 6 | Module 2 – DevContainers & Docker | Docker "Get Started" |
| 3 | Fri 11 Sep 2026 | 7 | Module 2 – AI/LLM Tooling Overview; Wrap-Up (HW1 due) | — |
| 4 | Mon 14 Sep 2026 | 8 | Module 3 – Obtain: ASR Stream Capture & VDB Corpus Acquisition (MP3 released) | Speech and Language Processing, 3rd ed. draft (Jurafsky & Martin) |
| 4 | Wed 16 Sep 2026 | 9 | Module 3 – Whisper Architecture & Local Transcription | OpenAI Whisper repository |
| 4 | Fri 18 Sep 2026 | 10 | Module 3 – Corpus Acquisition Lab; Wrap-Up (MP2 due prior day) | — |
| 5 | Mon 21 Sep 2026 | 11 | Module 4 – Data Analytics Pipelines: Streaming & Data Lakes (HW4 released) | "The Dataflow Model" (Akidau et al.) |
| 5 | Wed 23 Sep 2026 | 12 | Module 4 – Spark Structured Streaming | Structured Streaming Programming Guide, Spark 3.5.7 |
| 5 | Fri 25 Sep 2026 | 13 | Module 4 – Streaming Lab; Wrap-Up (MP3 due prior day) | — |
| 6 | Mon 28 Sep 2026 | 14 | Module 5 – Scrub: Chunking & Embedding Generation | Speech and Language Processing, Ch. 11 (Jurafsky & Martin) |
| 6 | Wed 30 Sep 2026 | 15 | Module 5 – Semantic Search & VDB Schema Design | Sentence Transformers "Semantic Search" |
| 6 | Fri 02 Oct 2026 | 16 | Module 5 – Embedding Lab / VDB Indexing; Wrap-Up (HW4 due prior day) | — |
| 7 | Mon 05 Oct 2026 | 17 | Module 6 – GenAI & LLMs: Candidates, Code, Classification (MP5 released) | Speech and Language Processing, Chs. 6–8 (Jurafsky & Martin) |
| 7 | Wed 07 Oct 2026 | 18 | Module 6 – Few-Shot Trope/Genre Classification | Hugging Face Transformers "Text Classification" |
| 7 | Fri 09 Oct 2026 | — | **NO CLASS — Wildcat Pause Day** | — |
| 8 | Mon 12 Oct 2026 | 19 | Module 6 – Model Selection & Embedding-Backed Classification Lab (MP6 released) | — |
| 8 | Wed 14 Oct 2026 | 20 | Module 6 – Trope/Genre Classification Workshop | — |
| 8 | Fri 16 Oct 2026 | 21 | Module 6 – Wrap-Up (MP5 due prior day; 5-lecture module absorbs the Pause Day gap) | — |
| 9 | Mon 19 Oct 2026 | 22 | Module 7 – Explore: Data Visualization & Dashboards (MP7 released) | Fundamentals of Data Visualization (Wilke) |
| 9 | Wed 21 Oct 2026 | 23 | Module 7 – Embedding-Space Visualization (UMAP) | UMAP-learn "Basic UMAP Parameters" |
| 9 | Fri 23 Oct 2026 | 24 | Module 7 – Generational Drift Dashboards Lab; Wrap-Up (MP6 due prior day) | — |
| 10 | Mon 26 Oct 2026 | 25 | Module 8 – Modeling: Retrieval-Augmented Classification (MP8 released) | "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al.) |
| 10 | Wed 28 Oct 2026 | 26 | Module 8 – Feature Extraction Pipelines | scikit-learn "Sample Pipeline for Text Feature Extraction" |
| 10 | Fri 30 Oct 2026 | 27 | Module 8 – Generational Convolution Models Lab; Wrap-Up (MP7 due prior day) | — |
| 11 | Mon 02 Nov 2026 | 28 | Module 9 – Evaluating Models: Inferential Statistics (HW9 released) | An Introduction to Statistical Learning with Applications in Python (James et al., 2023) |
| 11 | Wed 04 Nov 2026 | 29 | Module 9 – ASR Evaluation Methodology & Gold-Standard Design | NIST OpenASR 2020 Challenge Evaluation Plan |
| 11 | Fri 06 Nov 2026 | 30 | Module 9 – Gold-Standard Construction Lab (INV-17/INV-21); Wrap-Up (MP8 due prior day) | — |
| 12 | Mon 09 Nov 2026 | 31 | Module 10 – Interpret: Applying Models for Data Science (MP10 released) | An Introduction to Statistical Learning with Applications in Python (James et al., 2023) |
| 12 | Wed 11 Nov 2026 | 32 | Module 10 – Model Metrics & Scoring | scikit-learn "Metrics and Scoring" |
| 12 | Fri 13 Nov 2026 | 33 | Module 10 – Interpretation Lab; Wrap-Up (HW9 due prior day) | — |
| 13 | Mon 16 Nov 2026 | 34 | Module 11 – Presenting Results: Data Storytelling (MP11 released) | Technical Writing Essentials (Last) |
| 13 | Wed 18 Nov 2026 | 35 | Module 11 – Documentation & Notebook Presentation Standards | Jupyter Notebook Documentation |
| 13 | Fri 20 Nov 2026 | 36 | Module 11 – Dashboard Design Workshop; Wrap-Up (MP10 due prior day) | — |
| 14 | Mon 23 Nov 2026 | — | **NO CLASS — Fall Break** | — |
| 14 | Wed 25 Nov 2026 | — | **NO CLASS — Fall Break** | — |
| 14 | Fri 27 Nov 2026 | — | **NO CLASS — Fall Break** | — |
| 15 | Mon 30 Nov 2026 | 37 | Module 12 – PaaS/IaaS, MLOps/AIOps (HW12 released) | "MLOps Principles" (ML-Ops.org) |
| 15 | Wed 02 Dec 2026 | 38 | Module 12 – MLflow Tracking & Deployment | MLflow Tracking Documentation |
| 15 | Fri 04 Dec 2026 | 39 | Module 12 – Wrap-Up (MP11 due prior day; **Take-Home Final Exam due today**) | — |
| 16 | Mon 07 Dec 2026 | 40 | Module 13 – Special Topics: Agentic AI Systems Overview *(Extra-Credit Presentations begin after this lecture)* | Software Engineering at Google (Winters et al.); Docker "Get Started" |
| 16 | Wed 09 Dec 2026 | 41 | Module 13 – Special Topics: Frontier Directions in Responsive Analytics | — |
| 16 | Fri 11 Dec 2026 | 42 | Module 13 – Special Topics: Course Synthesis & Wrap-Up (last day of classes) | — |

<hr>

## 🦅 Standard Operating Procedures (SOPs)

All instructional staff interacting with this directory must adhere to the following protocols:

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown files in this directory must be updated first, and the HTML mirrored from them to preserve the GitOps ledger.
* **Protocol 2 (Schedule Integrity):** Any changes to lecture dates, topics, or assigned readings must be synchronized across the master schedule table and corresponding module READMEs.
* **Protocol 3 (Resource Archival):** Past semester lecture archives must be moved to `archive/` following final grade submission and verification.

<br>
<hr>
<p align="center">
 <i>Maintained by the <a href="https://github.com/kddresearch">Knowledge Discovery in Databases (KDD) Lab</a> at Kansas State University.</i>
</p>
