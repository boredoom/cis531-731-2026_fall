<!-- ASSIGNMENT-META
id: PS 8
phase: Phase 4: Explore & Model
module: Modules 07–08: Explore & Model (Term Project Interim Milestone)
released: Thu 29 Oct 2026
due: Sat 07 Nov 2026
prev: assignments/machine_problems/mp7_genre_classification.md
next: assignments/machine_problems/mp9_rag_classification_gold_standard.md
-->
# PS 8: Interim Report (Mandatory Milestone)
**Data provenance, architecture, exploratory embedding analysis, preliminary baselines, and a quantified risk and annotation plan**

**🗓️ Released:** Thu 29 Oct 2026 | **📅 Due:** Sat 07 Nov 2026 | **💯 Points:** 30 | **👥 Team:** Term-project team (as registered); solo permitted

> **🚨 CRITICAL SUBMISSION POLICY**
> **Track Immutability and Advisory Metrics:** Your track (ASR or VDB) was fixed at PS 4 and may not change (INV-3). All dev-split numbers in this report are advisory (INV-12).

## 1. Overview
Mandatory term-project milestone (one of three: PS 4, PS 8, HW 12). Write for a technically literate reviewer who has read your PS 4 proposal; every claim must be tied to a figure, table, or contract excerpt.

CIS 731 teams report their ontology schema version and change log; CIS 531 teams confirm use of the unmodified instructor schema (INV-11). Your annotation plan for MP 9 and HW 12 (target labeled-example count within 50–200, the IAA protocol for teams, or the validation-fraction limit for solo projects) must appear in the plan section.

**Required Readings:**
* [Fundamentals of Data Visualization (Wilke), Parts I–II](https://clauswilke.com/dataviz/): mapping data to aesthetics, color scales, and the principles of figure design, including uncertainty and redundant coding.
* [UMAP-learn: “Basic UMAP Parameters”](https://umap-learn.readthedocs.io/en/latest/parameters.html): effects of `n_neighbors`, `min_dist`, `n_components`, and `metric` on embedding structure.

**Upstream inputs:** PS 4 proposal and instructor feedback; MP 3, MP 5, PS 6, and MP 7 artifacts. 
**Downstream consumers:** MP 9 (annotation plan); HW 12 (report skeleton and risk register).

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Delta Audit:** Diff your PS 4 proposal against the current state; list every change with justification and respond to each proposal comment.
2. **Provenance Compilation:** Build the provenance table from the MP 3 manifest and PS 6 schema; confirm INV-1 and INV-9 compliance.
3. **Exploratory Figure Generation:** Generate the UMAP sensitivity sweep and trustworthiness scores; reject figures that violate the Wilke Part II principles.
4. **Risk Red-Team:** Have the AI Kit attack your risk register for omitted failure modes (quota exhaustion, track-specific data gaps, annotation shortfall); keep only risks you can defend.
5. **Plan Alignment:** Align the work breakdown with the MP 9, MP 10, PS 11, and HW 12 due dates.

## 3. Required Document Structure & Grading Rubric (30 Points Total)
Your submission must be a **single PDF (at most 10 pages) delivered with figure sources in `interim/` under Git tag `ps8-submission`**. The document must contain the following sections exactly as named below. The grading rubric is mapped directly to these required sections.

### Section 1: Team & Taxonomy Metadata (2 pts)
* **Requirement:** List the names of all team members. State your project's Analytical Category (Prescriptive, Descriptive, Predictive), Media Type, and claimed OSEMN stages.
* **Integrity Attestation:** You must include the following statement: *"I attest that the written responses provided originate from my own thoughts, code, and bullet points. Where Generative AI was used, it was restricted to the role of an editor/synthesizer in accordance with the course GenAI Kit (v2.0)."*

### Section 2: Scope Delta and Proposal Responses (4 pts)
* **Requirement:** Provide your updated problem statement. Have your objectives changed or narrowed since your PS 4 Proposal? List every change with justification, and provide a direct response to every instructor proposal comment.

### Section 3: Data Provenance & Exploratory Baselines (10 pts)
* **Requirement:** Table of every corpus or stream (source, whitelist id, size, ingest method). Confirm your environment is stable and datasets are loading. 
* **Exploratory Figures:** Include at least three figures, including a UMAP sensitivity sweep over `n_neighbors` and `min_dist` with fixed `random_state`, and a cohort/drift plot with uncertainty. 
* **Baseline:** Confirm your "naive" baseline (e.g., random agent, simple heuristic, or MP7 CPU baseline) and report the initial advisory performance metric.

### Section 4: Architecture, Invariants, & Pillar Alignment (5 pts)
* **Requirement:** Pipeline diagram (ingest, embed or transcribe, index, retrieve or analyze, evaluate). Explain *why* you chose this approach and how it aligns with your specific OSEMN stages. Provide the component-version table keyed to the course manifest (INV-14), and the invariants you enforce with `deal` excerpts.

### Section 5: Risk Register and Revised Plan (5 pts)
* **Requirement:** Based on the literature and your specific track, what are the most common failure modes? Provide at least 5 quantified risks (likelihood, impact, trigger, mitigation) including compute/quota exhaustion with a CPU-baseline fallback (INV-15, INV-18). 
* **Plan Alignment:** Provide your work breakdown and your specific annotation plan (50-200 target range, IAA protocol) aligned with MP 9 and HW 12 due dates.

### Section 6: GitHub Repository Link (2 pts)
* **Requirement:** Provide the URL to your team's active GitHub repository. It must show a commit history demonstrating your working code skeleton and baseline implementation under the `ps8-submission` tag.

### Section 7: GenAI Audit Log & Certificate (2 pts)
* **Requirement:** You must include your `GenAI.pdf` audit log in your repository submission. This document must contain the exact prompts you used, your original draft text/bullet points fed to the AI, and the raw output. *(If you did not use GenAI, include a PDF explicitly stating "No Generative AI was used for PS 8").*

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [MP 7: Few-Shot Trope/Genre Classification (GenAI)](../machine_problems/mp7_genre_classification.md) | [[All Assignments]](../README.md#schedule) | [MP 9: Retrieval-Augmented Classification & Convolutions](../machine_problems/mp9_rag_classification_gold_standard.md) |

[🏠 Course Home](../../README.md) · [⬆️ Module](../../modules/module_07/README.md) · [⏫ Phase](../../phases/phase_04/README.md)
