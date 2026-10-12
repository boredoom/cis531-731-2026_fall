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

**🗓️ Released:** Thu 29 Oct 2026 | **📅 Due:** Sat 07 Nov 2026 | **💯 Points:** 100 | **👥 Team:** Term-project team (as registered); solo permitted

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

## 3. Required Document Structure
Your submission must be a **single PDF (at most 10 pages) delivered with figure sources in `interim/` under Git tag `ps8-submission`** containing the following sections exactly as named below. 

* **Scope Delta and Proposal Responses:** Restated PS 4 objective and track, each change with justification, and a response to every proposal comment.
* **Data Provenance:** Table of every corpus or stream: source, `license_class` or whitelist id, size, ingest method, and filtering; confirmation that no Yelp or SEC-filing data is used (INV-1).
* **Architecture and Invariants:** Pipeline diagram (ingest, embed or transcribe, index, retrieve or analyze, evaluate), component-version table keyed to the course manifest (INV-14), and the invariants you enforce with `deal` excerpts.
* **Exploratory Analysis and Baselines:** At least three figures, including UMAP over `n_neighbors` ∈ {5, 15, 50} and `min_dist` ∈ {0.0, 0.1, 0.5} with fixed `random_state` and `sklearn.manifold.trustworthiness`; a cohort or event-time drift plot with uncertainty; at least one baseline against your method with 95% CIs, labeled advisory.
* **Risk Register and Revised Plan:** At least 5 risks (likelihood, impact, trigger, mitigation) including compute/quota with a CPU-baseline fallback (INV-15, INV-18); work breakdown; team contribution matrix or solo scope statement; annotation plan.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (100 Points Total)

This assignment is worth 100 points total.

**Part 1: Report Content (60 pts)**
* **Scope continuity (10 pts):** Clear delta from PS 4; every comment addressed.
* **Data provenance (15 pts):** Complete table; INV-1 and INV-9 compliance demonstrated.
* **Architecture and invariants (15 pts):** Diagram, version table, and contract excerpts are mutually consistent.
* **Exploratory analysis (20 pts):** UMAP sensitivity, trustworthiness, drift plot, and baselines are sound and well presented.

**Part 2: Risk and Plan (35 pts)**
* **Risk register (20 pts):** Quantified, defensible risks with triggers and mitigations.
* **Plan alignment and annotation plan (15 pts):** Plan matches downstream due dates; annotation plan fits the 50–200 range and the IAA or validation-fraction rule.

* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [MP 7: Few-Shot Trope/Genre Classification (GenAI)](../machine_problems/mp7_genre_classification.md) | [[All Assignments]](../README.md#schedule) | [MP 9: Retrieval-Augmented Classification & Convolutions (INV-17/21)](../machine_problems/mp9_rag_classification_gold_standard.md) |

[🏠 Course Home](../../README.md) · [⬆️ Module](../../modules/module_07/README.md) · [⏫ Phase](../../phases/phase_04/README.md)
