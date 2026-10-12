<!-- ASSIGNMENT-META
id: MP 9
phase: Phase 4: Explore & Model
module: Modules 08–09: Model & Evaluate (Retrieval-Augmented Classification, Gold-Standard Construction)
released: Sat 07 Nov 2026
due: Mon 16 Nov 2026
prev: assignments/homework/ps8_interim_report.md
next: assignments/machine_problems/mp10_interpretability_metrics.md
REVIEW R-4: ASR-track details are drafted assumptions: each gold object is an audio segment of at most 15 seconds with a reference transcript and a segment label; the ordered cohort axis is the event-time window index.
REVIEW R-5: Annotation-partner assignment and `overlap_ids.txt` (20 shared objects) are drafted mechanisms. Pooling team members' adjudicated files toward the 50–200 HW 12 range is intended continuity.
-->
# MP 9: Retrieval-Augmented Classification & Convolutions (INV-17/21)
**Human-in-the-loop gold-standard construction, weak-supervision expansion, retrieval-augmented classification, and cohort convolution analysis**

**🗓️ Released:** Sat 07 Nov 2026 | **📅 Due:** Mon 16 Nov 2026 | **💯 Points:** 100 | **👥 Team:** Individual (annotation overlap with an assigned partner)

> **🚨 CRITICAL SUBMISSION POLICY**
> **Annotation Ceiling and CI/CD Gate (INV-17/INV-21):** Annotate at most 50 data objects or 2 hours, whichever is lower. Your raw labeled file (`gold_raw.csv` or `gold_raw.jsonl`) is validated by a deterministic row-count check; more than 50 rows fails the pipeline and returns a zero for this assignment. The 2-hour limit is self-attested in `attestation.md` and bounded structurally by the row cap. A CI row-count zero is recorded separately from a quota-exhaustion zero (INV-18).

## 1. Overview
Construct a gold-standard set, expand it by weak supervision, and evaluate a retrieval-augmented classifier plus a convolution analysis along an ordered cohort axis. Gold labels must be assigned by you; AI-generated labels are permitted only in the weak-supervision pool and must carry `source=silver`. ASR track: each gold object is an audio segment of at most 15 seconds with a reference transcript and a segment label.

Weak supervision: use your MP 7 classifier and simple labeling functions to produce silver labels for an unlabeled pool of at least 1,000 chunks, aggregate by weighted vote, and measure silver-vs-gold agreement on your gold objects. Retrieval-augmented classification: retrieve top-k exemplars (k ∈ {3, 5, 10}) from the MP 7 FAISS index to condition classification and compare against the MP 7 fixed-demonstration baseline. Convolution: bin chunks along the ordered cohort axis (VDB track: release decade, `generation_cohort := f(release_decade)`; ASR track: event-time window index), form per-cohort trope-frequency vectors, and convolve with a smoothing kernel [0.25, 0.5, 0.25] and a first-difference kernel [-1, 1] to estimate cohort-to-cohort drift with bootstrap CIs. CIS 731 additionally fits a learned 1-D convolutional kernel (PyTorch 2.x, CPU) and compares held-out forecast error against the fixed kernels.

All work must be solvable on the pinned CPU DevContainer (INV-14/INV-15); GPU access is optional and never required.

**Required Readings:**
* [“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks” (Lewis et al.), Sections 2–3](https://arxiv.org/abs/2005.11401): retriever–generator composition, marginalization over retrieved documents, and joint evaluation.
* [scikit-learn: “Sample pipeline for text feature extraction and evaluation”](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html): `Pipeline` and `FeatureUnion` patterns for text features.
* [NIST OpenASR 2020 Challenge Evaluation Plan]({{NIST_OPENASR_2020_URL}}): reference-transcript construction, text normalization, alignment, and WER scoring protocol.
* [An Introduction to Statistical Learning with Applications in Python (James et al., 2023), Ch. 5](https://www.statlearning.com/): resampling: cross-validation and the bootstrap for confidence intervals.

**Upstream inputs:** MP 7 `Classifier` interface, prompt harness, and FAISS index; PS 6 relevance protocol, schema, and ontology; MP 5 time windows (ASR track); PS 8 annotation plan.  
**Downstream consumers:** MP 10 (adjudicated gold set is the graded evaluation set; silver pool is advisory); HW 12 (your gold file seeds the 50–200 term-project gold standard, subject to the HW 12 range gate).

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Codebook Drafting:** Extend the PS 6 relevance protocol into a codebook with decision rules, boundary cases, and exemplars drawn from your labeled objects; the AI Kit may draft wording but may not assign gold labels.
2. **Gold Annotation and Gate Check:** Label at most 50 objects, record start and stop timestamps in `attestation.md`, and run `validate_annotation_submission` locally until it passes.
3. **Weak-Supervision Expansion:** Generate silver labels on the pool with your MP 7 classifier and labeling functions; compute silver-vs-gold agreement and adjudicate IAA disagreements.
4. **Retrieval-Augmented Classification:** Implement top-k exemplar-conditioned classification; report P@k and Recall@k against gold relevance judgments and compare with the MP 7 baseline.
5. **Cohort Convolution and Audit:** Apply the kernels along the cohort axis, bootstrap the drift estimates, and verify that every AI-generated analysis step reproduces from raw files.

## 3. Required Document Structure
Your submission must be a **`report.md` (at most 4 pages) delivered with `gold_raw.*`, `gold_adjudicated.jsonl`, `codebook.md`, `attestation.md`, an executed notebook, and `results.json` under Git tag `mp9-submission`** containing the following sections exactly as named below. 

* **Codebook and Attestation:** Label definitions, decision rules, boundary cases, and exemplars from your labeled objects; annotation start/stop timestamps and total effort (at most 2 hours).
* **Inter-Annotator Agreement and Adjudication:** Cohen's κ with a 95% bootstrap CI, percent agreement, and the confusion matrix on the 20-object overlap (`overlap_ids.txt`) labeled independently by your assigned partner, plus documented adjudication rules.
* **Weak-Supervision Agreement Analysis:** Labeling functions, the vote-aggregation scheme, silver-vs-gold agreement, and failure modes of the silver labels.
* **Retrieval-Augmented Classification Results:** Classifier results against the MP 7 baseline and retrieval P@k/Recall@k, each with 95% bootstrap CIs on your adjudicated set; graded for methodology, not absolute value.
* **Cohort Convolution Analysis:** Cohort axis definition, kernels, drift estimates with CIs, and (CIS 731) learned-kernel forecast-error comparison.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (100 Points Total)

This assignment is worth 100 points total.

**Part 1: Gold-Standard Construction (40 pts)**
* **Codebook and attestation (10 pts):** Unambiguous decision rules; exemplars drawn from labeled objects; attestation complete.
* **IAA and adjudication (15 pts):** Correct κ with CI, confusion matrix, and documented adjudication.
* **Weak-supervision agreement (15 pts):** Silver labeling is sound, marked `source=silver`, and its agreement with gold is analyzed.

**Part 2: Models and Analysis (55 pts)**
* **Retrieval-augmented classification (25 pts):** Correct retrieval metrics and a fair comparison against the MP 7 baseline.
* **Cohort convolution (20 pts):** Kernels applied correctly along the cohort axis; drift estimates with uncertainty.
* **Reproducibility and CI gate (10 pts):** Row-count gate passes; pinned environment; CPU-solvable. A gate failure is a zero for the assignment.

* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [PS 8: Interim Report (Mandatory Milestone)](../homework/ps8_interim_report.md) | [[All Assignments]](../README.md#schedule) | [MP 10: Data Science Interpretability & Metrics Scoring](mp10_interpretability_metrics.md) |

[🏠 Course Home](../../README.md) · [⬆️ Module](../../modules/module_08/README.md) · [⏫ Phase](../../phases/phase_04/README.md)
