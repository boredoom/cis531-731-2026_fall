<!--
---
yaml_schema_version: "2.2"
document_version: "1.1"
document_last_updated_date: "2026-10-22"
document_monotonicity: "REQUIRED"
routing_clearance: "PUBLIC - STUDENT FACING"
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
 <h2>📦 Directory: modules/ (Weekly Content Index by Phase)</h2>
 <p>
 <strong>Status:</strong> ACTIVE | <strong>Maintainer:</strong> William H. Hsu
 </p>
</div>

<hr>

## 📖 Overview

This directory acts as the master index for the weekly, topic-based execution of the course, organized by OSEMN-aligned Phases. Each **Module** spans one to three lectures and encompasses a specific technical concept, homework assignment, or laboratory exercise. 

> **📚 Quick Links:** 
> [📚 View Master Lectures Schedule](../lectures/README.md) | [📂 Phases Index](../phases/README.md) | [📝 Assignments Index](../README.md#schedule)

<hr>

## 🗂️ Modules Index by Phase

### 🔵 PHASE I: FOUNDATIONS & TOOLING
| Module | Date Range | Topic & Description | Lectures |
| :--- | :--- | :--- | :--- |
| [`module_00/`](module_00/) | Mon 24 Aug 2026 | **Welcome & Course Overview** | [00](../lectures/lecture_00.md) |
| [`module_01/`](module_01/) | Wed 26 Aug - Wed 02 Sep 2026 | **PySpark Intro:** RDDs, DataFrames; Projects, Experiment Design | [01](../lectures/lecture_01.md) • [02](../lectures/lecture_02.md) • [03](../lectures/lecture_03.md) • [04](../lectures/lecture_04.md) |
| [`module_02/`](module_02/) | Fri 04 Sep - Fri 11 Sep 2026 | **Tools:** Cloud & Hosted Services, DevContainers, AI/LLMs *(Note: Labor Day Break Mon 07 Sep)* | [05](../lectures/lecture_05.md) • [06](../lectures/lecture_06.md) • [07](../lectures/lecture_07.md) |

### 🟢 PHASE II: OBTAIN & INGEST
| Module | Date Range | Topic & Description | Lectures |
| :--- | :--- | :--- | :--- |
| [`module_03/`](module_03/) | Mon 14 Sep - Fri 18 Sep 2026 | **Obtain:** ASR Stream Capture / VDB Corpus Acquisition | [08](../lectures/lecture_08.md) • [09](../lectures/lecture_09.md) • [10](../lectures/lecture_10.md) |
| [`module_04/`](module_04/) | Mon 21 Sep - Fri 25 Sep 2026 | **Data Analytics Pipelines:** Structured Streaming, ASR Ingest Architecture | [11](../lectures/lecture_11.md) • [12](../lectures/lecture_12.md) • [13](../lectures/lecture_13.md) |

### 🟠 PHASE III: SCRUB & EMBED
| Module | Date Range | Topic & Description | Lectures |
| :--- | :--- | :--- | :--- |
| [`module_05/`](module_05/) | Mon 28 Sep - Fri 02 Oct 2026 | **Scrub:** Chunking, Embedding Generation, VDB Schema Design | [14](../lectures/lecture_14.md) • [15](../lectures/lecture_15.md) • [16](../lectures/lecture_16.md) |
| [`module_06/`](module_06/) | Mon 05 Oct - Fri 16 Oct 2026 | **GenAI/LLMs:** Few-Shot Trope/Genre Classification *(Note: Wildcat Pause Day Fri 09 Oct)* | [17](../lectures/lecture_17.md) • [18](../lectures/lecture_18.md) • [19](../lectures/lecture_19.md) • [20](../lectures/lecture_20.md) • [21](../lectures/lecture_21.md) |

### 🟣 PHASE IV: EXPLORE & MODEL
| Module | Date Range | Topic & Description | Lectures |
| :--- | :--- | :--- | :--- |
| [`module_07/`](module_07/) | Mon 19 Oct - Fri 23 Oct 2026 | **Explore:** Embedding-Space Visualization, Generational Drift Dashboards | [22](../lectures/lecture_22.md) • [23](../lectures/lecture_23.md) • [24](../lectures/lecture_24.md) |
| [`module_08/`](module_08/) | Mon 26 Oct - Fri 30 Oct 2026 | **Model:** Retrieval-Augmented Classification, Generational Convolution | [25](../lectures/lecture_25.md) • [26](../lectures/lecture_26.md) • [27](../lectures/lecture_27.md) |

### 🟤 PHASE V: EVALUATE & DEPLOY
| Module | Date Range | Topic & Description | Lectures |
| :--- | :--- | :--- | :--- |
| [`module_09/`](module_09/) | Mon 02 Nov - Fri 06 Nov 2026 | **Evaluate:** Gold-Standard Construction (student-built, INV-17), Retrieval/WER Metrics | [28](../lectures/lecture_28.md) • [29](../lectures/lecture_29.md) • [30](../lectures/lecture_30.md) |
| [`module_10/`](module_10/) | Mon 09 Nov - Fri 13 Nov 2026 | **Interpret:** Applying Models to Live/Held-Out Data | [31](../lectures/lecture_31.md) • [32](../lectures/lecture_32.md) • [33](../lectures/lecture_33.md) |
| [`module_11/`](module_11/) | Mon 16 Nov - Fri 20 Nov 2026 | **Presenting Results:** Data Storytelling, Dashboards | [34](../lectures/lecture_34.md) • [35](../lectures/lecture_35.md) • [36](../lectures/lecture_36.md) |
| [`module_12/`](module_12/) | Mon 30 Nov - Fri 04 Dec 2026 | **PaaS/IaaS, MLOps/AIOps; Project Wrap-Up:** MLflow Tracking & Deployment *(Note: Fall Break Mon 23-Fri 27 Nov; Take-home final exam due Fri 04 Dec)* | [37](../lectures/lecture_37.md) • [38](../lectures/lecture_38.md) • [39](../lectures/lecture_39.md) |
| [`module_13/`](module_13/) | Mon 07 Dec - Fri 11 Dec 2026 | **Special Topics:** Agentic AI Systems, Frontier Directions, Course Synthesis & Wrap-Up *(Note: Dead Week / Optional Extra Credit Presentations)* | [40](../lectures/lecture_40.md) • [41](../lectures/lecture_41.md) • [42](../lectures/lecture_42.md) |

<br>
<hr>
<p align="center">
 <i>Maintained by the <a href="https://github.com/kddresearch">Knowledge Discovery in Databases (KDD) Lab</a> at Kansas State University.</i>
</p>
