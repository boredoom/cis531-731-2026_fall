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
 <h2>📦 Module 06: GenAI & LLMs: Candidates, Code, Classification</h2>
 <p>
 <strong>Phase:</strong> <a href="../../phases/phase_03">Phase 3: Scrub & Embed</a> | <strong>Maintainer:</strong> William H. Hsu
 </p>
</div>

<hr>

## 📖 Overview

This directory contains the localized pedagogical artifacts, demonstration code, and operational files strictly related to **Module 06**. This module spans `5` lectures and focuses on Generative AI and LLMs, candidate generation, model selection, few-shot trope/genre classification, and embedding-backed classification labs *(Note: Wildcat Pause Day Fri 09 Oct)*.

> **⚠️ Module Routing Notice**
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

<hr>

## 🗂️ Module Artifacts

| Subdirectory / File | Description |
| :--- | :--- |
| `lab6.ipynb` | Lab 6: Model selection and embedding-backed classification lab notebook |
| `README.md` | This module overview and index. |

<hr>

## 🔗 Associated Course Materials

* **Lectures:** [Lec 17](../../lectures/lecture-17.md) | [Lec 18](../../lectures/lecture-18.md) | [Lec 19](../../lectures/lecture-19.md) | [Lec 20](../../lectures/lecture-20.md) | [Lec 21](../../lectures/lecture-21.md)
* **Active Assignments:** [Lab 6 Notebook](../../assignments/homework/lab6.ipynb) | [MP7 Genre Classification Specification](../../assignments/machine_problems/mp7_genre_classification.md) *(MP5 released, MP6 released, MP5 due)*
* **Required Reading:** Speech and Language Processing, Chs. 6–8 (Jurafsky & Martin); Hugging Face Transformers "Text Classification"

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

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| <a href="../../phases/phase_03">**Phase 3: Scrub & Embed**</a> | **Module 6:** GenAI & LLMs: Candidates, Code, Classification | **Lectures 17-21** | Mon 05 Oct - Fri 16 Oct 2026 |

---

## Lecture 17: GenAI & LLMs: Candidates, Code, Classification (Mon 05 Oct)

1. **Language Modeling Fundamentals:** Introduction to $N$-gram models, perplexity, and the transition from count-based to dense neural representations (Jurafsky & Martin, Ch. 6).
2. **Transformer Architecture Overview:** The attention mechanism, self-attention, and the foundational architecture underlying modern Large Language Models.
3. **The Pretraining & Fine-Tuning Paradigm:** Understanding how foundational models acquire broad language representations and are subsequently tuned for specific downstream data science tasks.
4. **LLMs as Classifiers:** Shifting from generative text completion to using LLM token probabilities and embeddings for strict classification mapping.
5. **Prompting vs. Fine-Tuning Trade-offs:** Analyzing the computational cost, accuracy, and latency differences between zero/few-shot prompting and full model fine-tuning.

---

## Lecture 18: Few-Shot Trope/Genre Classification (Wed 07 Oct)

1. **The In-Context Learning (ICL) Paradigm:** Leveraging the LLM's pre-trained knowledge base to classify text (e.g., media tropes) without updating model weights.
2. **Prompt Engineering for Classification:** Designing strict formatting constraints and system instructions to force the LLM to output clean, parsable classification labels.
3. **The Few-Shot Exemplar Selection:** Determining how to select high-leverage $K$-shot examples that define the boundary conditions of complex genres or tropes.
4. **Hugging Face `pipeline` API:** Utilizing the `transformers` library to initialize local, open-weight text classification models.
5. **Handling Out-of-Distribution Data:** Strategies for managing LLM hallucinations or default behaviors when presented with novel genres or unseen media data.

*(Note: Friday 09 Oct 2026 – NO CLASS / Wildcat Pause Day)*

---

## Lecture 19: Model Selection & Embedding-Backed Classification Lab (Mon 12 Oct)

1. **MP6 Release & Requirements:** Reviewing the expectations for the embedding-backed classification machine problem.
2. **Embedding Models vs. Generative Models:** Understanding why a specialized embedding model (e.g., `sentence-transformers`) is often superior to a generative LLM for clustering and similarity-based classification.
3. **Distance Metrics for Classification:** Utilizing Cosine Similarity and Euclidean distance in the embedding space to classify unknown texts against known trope/genre anchors.
4. **Building the Reference Index:** Constructing the "gold standard" vector database of known tropes to serve as the classification lookup table.
5. **Thresholding and Confidence:** Establishing mathematical thresholds for "Unknown" or "Mixed" classifications when distance metrics fall in the boundary zones.

---

## Lecture 20: Trope/Genre Classification Workshop (Wed 14 Oct)

1. **Execution Troubleshooting:** Live debugging of Hugging Face environment setups, CUDA/CPU execution issues, and memory management constraints.
2. **Pipeline Integration:** Connecting the output of the semantic search (Module 5) directly into the classification prompt or embedding comparator.
3. **Evaluating Classifier Performance:** Transitioning from subjective "looks good" evaluations to rigorous metrics (Precision, Recall, F1) for the trope classifications.
4. **Handling Ambiguous Media:** Strategies for classifying multi-genre media or texts containing conflicting tropes using weighted probabilities.
5. **Code Review & Refactoring:** Peer review of classification pipelines to ensure robust error handling and adherence to FAIR principles.

---

## Lecture 21: Wrap-Up (Fri 16 Oct)

1. **MP5 Submission Review:** Common pitfalls and architectural successes observed in the GenAI/LLM Candidates submission (due prior day).
2. **Computational Cost Realities:** Analyzing the latency and hardware requirements of the deployed classification pipelines.
3. **Limitations of Few-Shot Prompting:** When does the LLM fail to capture deep semantic tropes, and when is a dedicated trained classifier mathematically necessary?
4. **Module 6 Synthesis:** Summarizing the integration of LLMs into the data science pipeline as robust, programmatic tools rather than conversational chatbots.
5. **Preview of Module 7:** Transitioning from data extraction and classification to visualization (UMAP) and generational drift dashboarding.
