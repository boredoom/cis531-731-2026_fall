<!--
---
yaml_schema_version: "2.2"
document_version: "1.1"
document_last_updated_date: "2026-10-26"
document_last_updated_time: "12:12:00 CDT"
document_monotonicity: "REQUIRED - Ensure document_version and timestamps strictly increment on every update of the target document. Reject regressions."
anti_cwa_cardinal_rule: "ALWAYS ASK, NEVER INFER. Do not hallucinate physical world state, task completion, or implicit preferences."
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
 <h2>📦 Module 08: Model: Retrieval-Augmented Classification & Generational Convolution</h2>
 <p>
 <strong>Phase:</strong> <a href="../../phases/phase_04">Phase 4: Explore & Model</a> | <strong>Maintainer:</strong> William H. Hsu
 </p>
</div>

<hr>

## 📖 Overview

This directory contains the localized pedagogical artifacts, demonstration code, and operational files strictly related to **Module 08**. This module spans `3` lectures and focuses on modeling, retrieval-augmented classification (RAG), deterministic text feature extraction pipelines, and generational convolution models.

> **⚠️ Module Routing Notice**
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

<hr>

## 📅 Lecture Schedule & Learning Objectives

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| [**Phase 4:** Explore & Model](../../phases/phase_04) | **Module 8:** Model: Retrieval-Augmented Classification & Generational Convolution | **Lectures 25-27** | Mon 26 Oct – Fri 30 Oct 2026 |

### Lecture 25: Modeling: Retrieval-Augmented Classification (Mon 26 Oct)
1. **The Retrieval-Augmented Paradigm:** Deconstructing the RAG architecture (Lewis et al.) and how integrating external knowledge bases stabilizes zero-shot and few-shot classification.
2. **Dense vs. Sparse Retrieval:** Contrasting BM25 (lexical) with dense vector embeddings for surfacing semantically relevant context anchors.
3. **Prompt Engineering for Classification:** Designing rigid, instruction-tuned prompts that constrain LLM output to valid class labels based exclusively on retrieved context.
4. **Addressing Hallucination:** Establishing evaluation criteria and temperature bounds to prevent LLMs from generating classification rationale outside the retrieved text.
5. **MP8 Release:** Introduction to the MP8 constraints, mapping the dataset and required retrieval-classification pipeline.

### Lecture 26: Feature Extraction Pipelines (Wed 28 Oct)
1. **The scikit-learn Pipeline:** Constructing deterministic, reproducible feature extraction pipelines that prevent data leakage between training and testing sets.
2. **Text Vectorization:** Implementing `TfidfVectorizer` and `CountVectorizer` for baseline model comparison against embedding-based methods.
3. **Dimensionality Reduction:** Applying `TruncatedSVD` and `PCA` within the pipeline to optimize feature spaces for classical classifiers.
4. **Model Chaining:** Linking feature extractors directly to estimators (e.g., Logistic Regression, SVM) within a single `Pipeline` object.
5. **Hyperparameter Tuning:** Utilizing `GridSearchCV` over pipeline parameters to optimize both extraction weights and estimator bounds simultaneously.

### Lecture 27: Generational Convolution Models Lab; Wrap-Up (Fri 30 Oct)
1. **Generational Drift Modeling:** Applying time-series and rolling-window convolutions to track semantic and sentiment drift across generational cohorts.
2. **Lab Setup:** Initializing the environment and loading the temporal datasets for the convolution exercise.
3. **Implementing the Convolution:** Authoring the script to execute temporal feature extraction and map the generational shift.
4. **Integration with Classification:** Feeding the output of the generational convolution back into the classification pipeline to improve temporal accuracy.
5. **MP 7 Debrief & Wrap-Up:** Reviewing the MP 7 (submitted prior day) solutions and verifying readiness for the Module 9 Evaluation phase.

<hr>

## 🗂️ Module Artifacts

| Subdirectory / File | Description |
| :--- | :--- |
| `lab08.ipynb` | Lab 8: Generational Convolution Models lab notebook. |
| `README.md` | This module overview and index. |

<hr>

## 🔗 Associated Course Materials

* **Lectures:** [Lec 25](../../lectures/lecture-25.md) | [Lec 26](../../lectures/lecture-26.md) | [Lec 27](../../lectures/lecture-27.md)
* **Active Assignments:** [PS8 Interim Report Specification](../../assignments/homework/ps8_interim_report.md) | [Lab 08 Notebook](../../assignments/homework/lab08.ipynb) | [MP8 Specification](../../assignments/machine_problems/mp8_rag_classification.md) *(MP8 released, MP7 due prior day)*
* **Required Reading:** "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al.); scikit-learn "Sample Pipeline for Text Feature Extraction"

<hr>

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
