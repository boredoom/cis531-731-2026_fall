<!-- ASSIGNMENT-META
id: HW 12
phase: Phase 5: Interpret, Present & Deploy
module: Module 12: PaaS/IaaS, MLOps/AIOps, and Project Wrap-Up
released: Sat 05 Dec 2026
due: Mon 14 Dec 2026
prev: assignments/homework/ps11_ethics_storytelling_dashboards.md
next: none
REVIEW R-6: MLflow tracking and container-digest pinning are first required in this assignment; consider a lightweight tracking checkpoint earlier in the sequence.
-->
# HW 12: Final Project Deliverables (Mandatory Milestone)
**Technical report and a digest-pinned, MLflow-tracked pipeline that reproduces every reported number on the CPU baseline**

**🗓️ Released:** Sat 05 Dec 2026 | **📅 Due:** Mon 14 Dec 2026 | **💯 Points:** 200 | **👥 Team:** Term-project team (as registered); solo permitted

> **🚨 CRITICAL SUBMISSION POLICY**
> **Finals-Week Due Date and Gold-Standard Range Gate:** Due Mon 14 Dec 2026, the first day of Finals Week. Optional extra-credit presentations run during Dead Week after Lecture 40 and do not substitute for any part of this deliverable. Your term-project gold-standard file is validated against the 50–200 labeled-example range gate, which is separate from the 50-row homework gate (INV-21).

## 1. Overview
Final mandatory term-project milestone: a technical report and a digest-pinned, MLflow-tracked pipeline that reproduces every reported number from raw admitted data on the CPU baseline. This assignment integrates all upstream artifacts: the MP 5 pipeline, PS 6 schema, MP 7/MP 9 models, your MP 9-seeded gold standard, the MP 10 harness, and PS 11 ethics findings.

Gold standard: 50–200 labeled examples. Team projects report 2-way or 3-way IAA with CIs and adjudication rules; solo projects keep labeled data in validation at or below 1% (INV-17). CIS 731 includes the final ontology schema, change log, and competency-question results. All work must be solvable on the pinned CPU DevContainer (INV-14/INV-15); GPU access is optional and never required.

**Planning note:** MLflow tracking and container-digest pinning are first required here; begin environment work early.

**Required Readings:**
* [“MLOps Principles” (ML-Ops.org)](https://ml-ops.org/content/mlops-principles): versioning of data, models, and code; continuous training and delivery; drift monitoring.
* [MLflow Tracking Documentation](https://mlflow.org/docs/latest/tracking.html): logging parameters, metrics, and artifacts; comparing runs; the model registry.

**Upstream inputs:** PS 4, MP 5, PS 6, MP 7, PS 8, MP 9, MP 10, PS 11.  
**Downstream consumers:** None (final assignment).

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Integration Audit:** Reconcile every upstream artifact (schema, contracts, models, gold files, harness) against the final repository state and list discrepancies.
2. **Reproducibility Harness:** Build `make verify`: lockfile and image-digest check, contract tests, the gold-standard range gate, and headline-metric reproduction within a stated tolerance on CPU.
3. **MLflow Lineage and Registry:** Log parameters, metrics, artifacts, git SHA, data hash, and lockfile hash for every run; register the final model with a version and stage.
4. **Serving and Monitoring:** ASR track: Structured Streaming job with checkpointing and a documented restart. VDB track: retrieval/classification CLI or HTTP service with a smoke test. Both: drift check (PSI or KS) with an alert threshold and runbook.
5. **Report Assembly:** Draft the sections with the AI Kit; verify every number against the MLflow export.

## 3. Required Document Structure
Your submission must be a **`REPORT.pdf` (at most 12 pages) delivered with the reproducibility package under Git tag `hw12-final` (`Dockerfile` or DevContainer, lockfile, `Makefile`, `reproduce.md`, MLflow export, serving code, gold-standard files)** containing the following sections exactly as named below. 

* **Problem, Data, and Provenance:** Abstract, problem statement, track, related work, and the provenance of every source (`license_class` or whitelist id; no Yelp or SEC-filing data, INV-1).
* **Methods and Architecture:** Architecture, invariants enforced with contract excerpts, and component versions keyed to the course manifest (INV-14).
* **Evaluation:** Gold-standard report (count, codebook, effort), IAA with CIs or validation-fraction evidence, metrics with 95% CIs, ablations, significance tests with multiple-comparison control, cohort-stratified results, and error analysis.
* **Ethics, Limitations, and Reflection:** PS 11 findings carried forward with the mitigations actually implemented; what you would change; which invariants proved hardest.
* **Reproducibility, MLOps, and Serving:** `make verify` results, MLflow lineage and registry entry, serving path, and the drift-monitoring runbook.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (200 Points Total)

This assignment is worth 200 points total.

**Part 1: Final Technical Report (100 pts)**
* **Report completeness and clarity (30 pts):** Required sections complete, consistent, and clearly written.
* **Evaluation rigor (30 pts):** Correct metrics, CIs, significance tests, and multiple-comparison control.
* **Gold standard and agreement evidence (25 pts):** Range compliance and IAA (team) or validation-fraction (solo) evidence.
* **Ethics and limitations (15 pts):** Mitigations are specific and implemented.

**Part 2: Reproducible Pipeline (95 pts)**
* **Reproducibility (35 pts):** Digest-pinned environment; `make verify` passes on the CPU baseline.
* **MLflow and registry practice (25 pts):** Complete lineage; model registered and versioned.
* **Serving and monitoring (20 pts):** Working serving path with restart or smoke test; drift check and runbook.
* **Contracts and CI integration (15 pts):** Contract tests and range gates run in CI.

* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [PS 11: Ethics, Data Storytelling, & Dashboards](ps11_ethics_storytelling_dashboards.md) | [[All Assignments]](../README.md#schedule) | — *(final assignment)* |

[🏠 Course Home](../../README.md) · [⬆️ Module](../../modules/module_12/README.md) · [⏫ Phase](../../phases/phase_05/README.md)
