<!--
---
yaml_schema_version: "2.2"
document_version: "1.0"
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
 <h2>📂 Directory: phases/ (Course Progression Index)</h2>
 <p>
 <strong>Status:</strong> ACTIVE | <strong>Maintainer:</strong> William H. Hsu
 </p>
</div>

<hr>

## 📖 Overview

This directory acts as the master index for the high-level course progression. **Phases** are conceptual, chronological wrappers that group multiple weekly modules together based on major pedagogical milestones or methodological pillars (e.g., Foundations, Obtain/Scrub, Explore/Model, Evaluate). 

Together the phases cover **Modules 00-13** and **43 lectures (Lecture 0-42)**, meeting Mon/Wed/Fri from Mon 24 Aug 2026 through Fri 11 Dec 2026. The progression runs from foundations and tooling (Phase I), through obtaining and ingesting data (Phase II), scrubbing and embedding it (Phase III), exploring and modeling it (Phase IV), to evaluating, interpreting, presenting, and deploying results (Phase V). Class-free days fall inside Phase I (Labor Day, Mon 07 Sep), Phase III (Wildcat Pause Day, Fri 09 Oct), and Phase V (Fall Break, Mon 23 Nov - Fri 27 Nov).

> **⚠️ Parent Directory Routing Notice**
> This directory is strictly for structural routing. All actual course content, scripts, and assignment assets must be placed inside the granular `module_XX/` subdirectories located in the `modules/` repository root or within their respective phase subdirectories.

<hr>

## 🗂️ Phase Directory Structure

| Phase Directory | Pedagogical Objective |
| :--- | :--- |
| [`phase_01/`](phase_01/) | **🔵 Phase I: Foundations & Tooling:** Modules [00](../modules/module_00), [01](../modules/module_01), [02](../modules/module_02) (Mon 24 Aug - Fri 11 Sep 2026; Lectures 0-7). Course orientation, PySpark fundamentals, and the cloud, DevContainer, and AI-tooling baseline. |
| [`phase_02/`](phase_02/) | **🟢 Phase II: Obtain & Ingest:** Modules [03](../modules/module_03), [04](../modules/module_04) (Mon 14 Sep - Fri 25 Sep 2026; Lectures 8-13). ASR stream capture, VDB corpus acquisition, and Structured Streaming ingest architecture. |
| [`phase_03/`](phase_03/) | **🟠 Phase III: Scrub & Embed:** Modules [05](../modules/module_05), [06](../modules/module_06) (Mon 28 Sep - Fri 16 Oct 2026; Lectures 14-21). Chunking, embedding generation, VDB schema design, and few-shot trope/genre classification. |
| [`phase_04/`](phase_04/) | **🟣 Phase IV: Explore & Model:** Modules [07](../modules/module_07), [08](../modules/module_08) (Mon 19 Oct - Fri 30 Oct 2026; Lectures 22-27). Embedding-space visualization, generational drift dashboards, retrieval-augmented classification, and generational convolution. |
| [`phase_05/`](phase_05/) | **🟤 Phase V: Evaluate & Deploy:** Modules [09](../modules/module_09), [10](../modules/module_10), [11](../modules/module_11), [12](../modules/module_12), [13](../modules/module_13) (Mon 02 Nov - Fri 11 Dec 2026; Lectures 28-42). Gold-standard construction and metrics, interpretation, data storytelling, MLOps wrap-up, and special topics. |

<br>
<hr>
<p align="center">
 <i>Maintained by the <a href="https://github.com/kddresearch">Knowledge Discovery in Databases (KDD) Lab</a> at Kansas State University.</i>
</p>
