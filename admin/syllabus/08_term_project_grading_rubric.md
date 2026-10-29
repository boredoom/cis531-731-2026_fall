---
yaml_schema_version: "2.1"
document_version: "1.0"
document_last_updated_date: "2026-10-29"
document_monotonicity: "REQUIRED"
---

# Term Project Grading Rubrics
**CIS 531 / CIS 731 Point Distributions, Milestone Weights & HW 12 Substance Criteria**

## 🎯 Capstone Architecture & Final Deliverable Breakdown
The CIS 531/731 Term Project is evaluated across **Process Milestones (90 points: PS 4, PS 8, and HW 12 Milestone)** and **Final Deliverable Substance (300 points on the course capstone scale; scored via the 200-point HW 12 portal rubric + 50-point presentation/defense)**. In addition, Machine Problems and Problem Sets (`MP 5`, `PS 6`, `MP 7`, `MP 9`, `MP 10`, `PS 11`; 30 normalized points each) directly build the modular components of your final system.

| Capstone Deliverable Component | HW 12 Portal Rubric (200 pts) | 300-Pt Substance Scale | Share of Substance |
| :--- | ---: | ---: | ---: |
| **1. Final Technical Report (`REPORT.pdf`, $\le 12$ pp)**<br>*Provenance, architecture, 50–200 gold standard & IAA, 95% CIs, BH significance tests, PS 11 ethics mitigations.* | 100 pts | 150 pts | **50.0%** |
| **2. Reproducible Pipeline, Contracts & MLOps (`hw12-final`)**<br>*Digest-pinned CPU container, `make verify`, MLflow lineage & registry, serving path, PSI/KS drift runbook, `GenAI.pdf`.* | 100 pts<br>*(95 Code + 5 GenAI)* | 100 pts | **33.3%** |
| **3. Oral Presentation, Dashboard Demo & Q&A Defense**<br>*Slide delivery, PS 11 storyboard/dashboard walkthrough, and individual answers to the 3 Reflection Questions.* | Evaluated Live<br>*(Dead Week / EC)* | 50 pts | **16.7%** |
| **Total Substance Weight (plus 90 pts Process Milestones = 390 pts):** | **200 pts** | **300 pts** | **100.0%** |

---

## 📊 Track Expectations: CIS 531 (Undergraduate) vs. CIS 731 (Graduate)
While both sections share the same 30-point normalized homework scale and 390-point capstone structure, **CIS 731 (Graduate)** enforces advanced requirements in data sourcing, custom ontology/schema engineering, and model architecture:

| Dimension / Milestone | CIS 531: Undergraduate Track | CIS 731: Graduate Track |
| :--- | :--- | :--- |
| **Data Source Tier (`PS 4` / `PS 8`)** | 🟢 **Tier 1 (Golden Path)** | 🟡 **Tier 2 (Real-World API / Benchmark)** |
| **Ontology & Schema (`PS 6` / `PS 8` / `HW 12`)** | Adopt instructor schema **unmodified (`INV-11`)** | **Custom JSON Schema (Draft 2020-12)**, ontology hierarchy, change log & competency questions |
| **Container & FAISS Setup (`MP 2` / `MP 3`)** | Standard CPU DevContainer & in-memory `IndexFlatL2` / `IndexFlatIP` | Conditional GPU/CPU image pull & `faiss.write_index` / `read_index` disk I/O |
| **Cohort Convolution (`MP 9`)** | Fixed smoothing `[0.25, 0.5, 0.25]` & first-difference `[-1, 1]` kernels | Fixed kernels + **learned 1-D PyTorch convolutional kernel** forecast comparison |
| **Process Milestones (`PS 4`, `PS 8`, `HW 12`)** | **90 pts** ($3 \times 30$ pts) | **90 pts** ($3 \times 30$ pts) |
| **Final Deliverable Substance** | **300 pts** (200-pt HW 12 Scale) | **300 pts** (200-pt HW 12 Scale) |
| **Total Capstone Points** | **390 pts** | **390 pts** |

---

## 🔬 Detailed HW 12 Final Deliverable Rubric (200-Point Portal Breakdown)

### Part 1: Final Technical Report (`REPORT.pdf` — 100 Points / 50% of Substance)

| Criterion | Weight | Assessment Standard |
| :--- | :--- | :--- |
| **Report Completeness & Clarity** | **30 pts** | All required sections ($\le 12$ pages) are complete, consistent, and clearly written: Problem, Data & Provenance (`license_class` / whitelist ID; no Yelp/SEC data per `INV-1`), Methods & Architecture, Evaluation, Ethics/Limitations, and MLOps/Serving. (`CIS 731` includes final ontology schema, change log, and competency-question results). |
| **Evaluation Rigor** | **30 pts** | Correct primary and secondary metrics (Macro-F1, P@$k$/Recall@$k$/MRR/nDCG@$k$, or NIST WER), 95% bootstrap confidence intervals, ablations, paired statistical significance tests (paired bootstrap $B \ge 10,000$ or McNemar's test), Benjamini–Hochberg FDR control across $\ge 6$ comparisons, cohort-stratified results, and error analysis. |
| **Gold Standard & Agreement Evidence** | **25 pts** | Complies with the **50–200 labeled-example range gate (`INV-21`)**, documents codebook and annotation effort, and reports 2-way/3-way Cohen's $\kappa$ IAA with 95% CIs and adjudication rules (or $\le 1\%$ validation-fraction evidence for solo projects per `INV-17`). |
| **Ethics, Limitations & Reflection** | **15 pts** | Carries forward PS 11 findings (provenance/PII redaction, ecological fallacy, selection bias, ASR disparity, prompt injection/hallucination) with concrete mitigations actually implemented in the pipeline, plus reflection on which invariants proved hardest. |

### Part 2: Reproducible Pipeline, MLOps & GenAI Audit (`hw12-final` — 100 Points: 95 Code + 5 GenAI)

| Criterion | Weight | Assessment Standard |
| :--- | :--- | :--- |
| **Reproducibility & `make verify`** | **35 pts** | Digest-pinned `Dockerfile`/DevContainer and lockfile (`INV-14`); `make verify` passes cleanly on the CPU baseline (`INV-15`) and reproduces every headline metric in `REPORT.pdf` within stated tolerance from raw admitted data. |
| **MLflow Lineage & Registry Practice** | **25 pts** | Complete MLflow tracking export logging parameters, metrics, artifacts, Git SHA, data hash, and lockfile hash for every run, with the final model registered with an explicit version and stage. |
| **Serving & Drift Monitoring** | **20 pts** | Working serving path (checkpointed Structured Streaming job with documented restart for ASR track; retrieval/classification CLI or HTTP service with smoke test for VDB track) plus a Population Stability Index (PSI) or Kolmogorov–Smirnov (KS) drift check with alert threshold and runbook. |
| **Contracts & CI Integration** | **15 pts** | All `deal` contracts, unit tests, and the 50–200 gold-standard range gate execute automatically in CI. |
| **GenAI Audit Verification** | **5 pts** | Includes the complete `GenAI.pdf` audit log or an explicit attestation that no Generative AI was used. |
