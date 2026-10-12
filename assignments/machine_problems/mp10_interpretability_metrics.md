<!-- ASSIGNMENT-META
id: MP 10
phase: Phase 5: Interpret, Present & Deploy
module: Module 10: Interpret (Interpretability and Metrics Scoring)
released: Mon 16 Nov 2026
due: Wed 25 Nov 2026
prev: assignments/machine_problems/mp9_rag_classification_gold_standard.md
next: assignments/homework/ps11_ethics_storytelling_dashboards.md
REVIEW R-7: Due date Wed 25 Nov 2026 (and PS 11 release on the same day) falls inside Fall Break (22–29 Nov). Dates retained as specified.
-->
# MP 10: Data Science Interpretability & Metrics Scoring
**Metric derivation, permutation importance, calibration, and statistically supported system comparison under small-n constraints**

**🗓️ Released:** Mon 16 Nov 2026 | **📅 Due:** Wed 25 Nov 2026 | **💯 Points:** 100 | **👥 Team:** Individual

> **🚨 CRITICAL SUBMISSION POLICY**
> **Quota Killswitch and Fall Break:** Resampling-heavy analyses must run within your quota or on the CPU baseline (INV-18); exhaustion triggers fallback, not an extension. The due date falls within Fall Break (22–29 Nov 2026); there are no class meetings that week.

## 1. Overview
Build a scoring and interpretability harness for your best MP 7/MP 9 model. Graded evaluation uses your adjudicated MP 9 gold set; the MP 9 silver pool is advisory only (`grading_eligible=False`) and is used for stability and power analysis.

Components: custom metrics with `deal` contracts and unit tests; permutation importance (at least 30 repeats); retrieval-based local explanations for at least 10 misclassified examples; calibration (ECE under 10 and 15 bins; temperature scaling or isotonic regression); a paired comparison of your best two systems (paired bootstrap with B ≥ 10,000, or McNemar's test) with Benjamini–Hochberg control across the family of at least 6 comparisons you run; and a CI-width-versus-n analysis on silver-labeled subsamples. ASR track: WER under explicit normalization (NIST OpenASR 2020 protocol) against your MP 9 reference transcripts, comparing Whisper and AssemblyAI on identical audio.

All work must be solvable on the pinned CPU DevContainer (INV-14/INV-15); GPU access is optional and never required.

**Required Readings:**
* [An Introduction to Statistical Learning with Applications in Python (James et al., 2023), Chs. 4 and 13](https://www.statlearning.com/): classification metrics, ROC/AUC, and multiple testing (Bonferroni, Benjamini–Hochberg).
* [scikit-learn: “Metrics and scoring”](https://scikit-learn.org/stable/modules/model_evaluation.html): scoring parameters, averaging strategies, custom scorers, and probability calibration.

**Upstream inputs:** MP 9 adjudicated gold set, silver pool, and retrieval-augmented classifier; MP 7 models.  
**Downstream consumers:** PS 11 (dashboard metrics and uncertainty); HW 12 (evaluation section and the `evaluate` harness).

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Metric Derivation:** Derive micro/macro/weighted F1 (with an imbalance example where accuracy and macro-F1 rank two classifiers oppositely), P@k, Recall@k, MRR, nDCG@k, and WER (ASR track); verify by hand.
2. **Harness Scaffold:** Generate `evaluate(model, X, y)` with `deal` contracts (bounded metrics in [0, 1]; confusion-matrix entries sum to n) and unit tests; audit scorer usage with probabilistic outputs.
3. **Interpretability Pass:** Run permutation importance, retrieval-based explanations, and linear-term contributions where applicable.
4. **Calibration and Inference:** Produce reliability diagrams, ECE under both bin counts, post-hoc calibration, and the paired comparison with BH control.
5. **Power and Stability Audit:** Subsample the silver pool to chart CI width against n and report cohort-stratified metrics; state what conclusions n ≤ 50 cannot support.

## 3. Required Document Structure
Your submission must be a **`report.md` (`interpretability_report.md`, at most 4 pages) delivered with the `harness/` package and tests, an executed notebook, and `results.json` under Git tag `mp10-submission`** containing the following sections exactly as named below. 

* **Metric Derivations:** Derivations and numeric examples from your own confusion matrices; WER definition and why it can exceed 100% (ASR track).
* **Harness and Contracts:** `evaluate` interface, `deal` contracts, and unit-test coverage.
* **Interpretability Analyses:** Global permutation importance and local retrieval-based explanations for at least 10 misclassified examples, with interpretation.
* **Calibration and Statistical Comparison:** Reliability diagrams, ECE before/after calibration under 10 and 15 bins, the paired comparison with 95% CI and p-value, and BH-adjusted results across the comparison family.
* **Power, Stability, and Cohort Stratification:** CI-width versus n on silver subsamples, metrics by cohort, and an explicit statement of what small n cannot support.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (100 Points Total)

This assignment is worth 100 points total.

**Part 1: Metrics and Inference Theory (30 pts)**
* **Metric derivations (15 pts):** Correct derivations and a valid imbalance counterexample.
* **Inference design and assumptions (15 pts):** Test choice justified; assumptions stated; BH family defined before analysis.

**Part 2: Harness and Analyses (65 pts)**
* **Harness correctness and contracts (20 pts):** Metrics correct; contracts and unit tests pass.
* **Interpretability analyses (15 pts):** Global and local explanations are correct and interpreted.
* **Calibration (10 pts):** Reliability diagrams, bin sensitivity, and before/after comparison.
* **Statistical comparison (10 pts):** Correct paired test, CI, and FDR control.
* **Power, stability, and cohort stratification (10 pts):** Small-n limits quantified; cohort disparity tested and communicated.

* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [MP 9: Retrieval-Augmented Classification & Convolutions (INV-17/21)](mp9_rag_classification_gold_standard.md) | [[All Assignments]](../README.md#schedule) | [PS 11: Ethics, Data Storytelling, & Dashboards](../homework/ps11_ethics_storytelling_dashboards.md) |

[🏠 Course Home](../../README.md) · [⬆️ Module](../../modules/module_10/README.md) · [⏫ Phase](../../phases/phase_05/README.md)
