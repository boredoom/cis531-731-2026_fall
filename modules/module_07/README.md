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
 <h2>📦 Module 07: Explore: Data Visualization & Dashboards</h2>
 <p>
 <strong>Phase:</strong> <a href="../../phases/phase_04">Phase 4: Explore & Model</a> | <strong>Maintainer:</strong> William H. Hsu
 </p>
</div>

<hr>

## 📖 Overview

This directory contains the localized pedagogical artifacts, demonstration code, and operational files strictly related to **Module 07**. This module spans `3` lectures and focuses on data visualization, dashboards, embedding-space visualization using UMAP, and generational drift dashboards.

> **⚠️ Module Routing Notice**
> Core lecture markdown files and major assignments live in the top-level `lectures/` and `assignments/` directories to maintain structural parity. Use this module directory exclusively for localized data snippets, lab code examples, module-specific images, or environment configs required for this week's content.

<hr>

## 🗂️ Module Artifacts

| Subdirectory / File | Description |
| :--- | :--- |
| `lab7.ipynb` | Lab 7: Generational drift dashboards and UMAP embedding-space visualization notebook |
| `README.md` | This module overview and index. |

<hr>

## 🔗 Associated Course Materials

* **Lectures:** [Lec 22](../../lectures/lecture-22.md) | [Lec 23](../../lectures/lecture-23.md) | [Lec 24](../../lectures/lecture-24.md)
* **Active Assignments:** [Lab 7 Notebook](../../assignments/homework/lab7.ipynb) | MP7 Released *(MP6 due prior day)*
* **Required Reading:** Fundamentals of Data Visualization (Wilke); UMAP-learn "Basic UMAP Parameters"

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

# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **Phase 4:** Explore & Modell | **Module 7:** Explore: Data Visualization & Dashboards | **Lectures 22-24** | Mon 19 Oct - Fri 23 Oct 2026 |

---

## Lecture 22: Explore: Data Visualization & Dashboards (Mon 19 Oct)

1. **Exploratory Data Analysis (EDA) Principles:** Defining the role of visualization in uncovering structural anomalies, latent patterns, and data quality issues prior to formal modeling.
2. **Visual Encoding Constraints:** Mapping continuous, discrete, and categorical variables to spatial positioning, color gradients, and geometric marks while avoiding perceptual distortion.
3. **High-Dimensional Data Challenges:** Identifying the limitations of standard bivariate scatter plots and pair plots when analyzing dense embeddings or multi-feature datasets.
4. **Dashboard Architecture (Dash/Streamlit):** Structuring interactive, web-based analytics dashboards linking UI components (sliders, dropdowns) directly to underlying Python backend callbacks.
5. **Interactive Filtering:** Implementing cross-filtering mechanics allowing users to dynamically slice datasets and immediately observe changes across multiple synchronized visualizations.

---

## Lecture 23: Embedding-Space Visualization (UMAP) (Wed 21 Oct)

1. **Dimensionality Reduction Fundamentals:** Comparing the objectives of Principal Component Analysis (PCA), t-SNE, and Uniform Manifold Approximation and Projection (UMAP).
2. **The UMAP Algorithm:** Understanding the topological mechanics of UMAP—specifically how it constructs local fuzzy simplicial sets and optimizes the low-dimensional cross-entropy.
3. **Hyperparameter Tuning (`n_neighbors` & `min_dist`):** Controlling the balance between preserving local neighborhood clusters versus revealing global macroscopic structures in embedding space.
4. **Vector Database Projection:** Extracting high-dimensional text or image embeddings from a VDB and projecting them into 2D or 3D space for visual cluster analysis.
5. **Semantic Clustering & Annotation:** Applying clustering algorithms (e.g., HDBSCAN) on UMAP projections to automatically label dense semantic regions and identify out-of-distribution artifacts.

---

## Lecture 24: Generational Drift Dashboards Lab; Wrap-Up (Fri 23 Oct)

1. **Time-Series Embedding Analysis:** Tracking the centroid shifts of specific semantic clusters (e.g., tropes or genres) across chronologically ordered datasets.
2. **Dashboard Integration (UMAP + Callbacks):** Embedding dynamic UMAP projections into a Streamlit or Dash application, allowing the user to scrub through time and observe cluster migration.
3. **Quantifying Generational Drift:** Utilizing cosine distance or structural similarity metrics to quantify how the semantic representation of a concept diverges across different eras or media generations.
4. **Data Storytelling Construction:** Translating the mathematical observations of embedding drift into a coherent analytical narrative demonstrating cultural or linguistic evolution.
5. **MP6 Checkpoint & MP7 Release:** Verifying completion of Machine Problem 6 (Model Selection) and outlining the deliverables for Machine Problem 7 (Exploratory Dashboards).
