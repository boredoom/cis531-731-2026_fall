---
yaml_schema_version: "2.1"
document_version: "1.0"
document_last_updated_date: "2026-10-29"
document_monotonicity: "REQUIRED"
---

# Appendix: Evaluation of Models & Statistical Hypotheses
**Formalizing metric derivations, bootstrap confidence intervals, calibration, and multiple-comparison control for MP 7, MP 9, MP 10, and HW 12**

In data science and analytics pipelines, simply reporting that *"Pipeline A achieved 0.78 Macro-F1 and Pipeline B achieved 0.75 Macro-F1"* is insufficient. Because human-adjudicated gold-standard evaluation sets are finite (50 objects in MP 9/MP 10; 50–200 objects in HW 12) and in-context learning / neural initialization contains stochastic variance across seeds and demonstration orderings, point estimates alone cannot separate signal from noise. To receive full credit on MP 7, MP 9, MP 10, and HW 12, **95% confidence intervals, formal hypothesis tests yielding $p$-values, and multiple-comparison control are REQUIRED.**

---

## 1. Defining the Evaluation Measure ($f$) & Source Separation (INV-12)

Before testing for statistical significance, you must purposefully define *what* you are measuring and enforce strict separation between development/silver data and graded gold evaluation data.

### 🛡️ Evaluation Source Separation (INV-12 & INV-17)
* **Graded Metrics (`compute_graded_metric`):** Must be computed strictly against the instructor-provided held-out set (in MP 7) or your human-adjudicated gold-standard dataset (`gold_adjudicated.jsonl` in MP 9, MP 10, and HW 12).
* **Advisory / Development Metrics (`compute_dev_metric`, `grading_eligible=False`):** Metrics computed on your own development splits or on the 1,000-chunk weak-supervision silver pool (`source=silver`) are strictly advisory and are used for hyperparameter tuning, CI-width power curves, and stability analysis.

> **⚠️ Avoid the "Kitchen Sink" & Accuracy-Under-Imbalance Anti-Patterns**
> Do not dump every metric `scikit-learn` offers into an unanalyzed table, and never rely on raw Accuracy when trope, genre, or anomaly classes are imbalanced. In MP 10, you must explicitly construct an imbalance counterexample from your confusion matrices where raw Accuracy and Macro-F1 rank two classifiers in opposite orders.

### Track-Specific Evaluation Measures ($f$)
Select your primary evaluation measure $f$ to match your **3x5x5 Taxonomy Track and OSEMN Stage**:
* **Few-Shot & RAG Classification (MP 7, MP 9, MP 10):** Report **Macro-F1** (unweighted mean of per-class F1 scores) with 95% bootstrap CIs as your headline metric, accompanied by micro-F1, weighted-F1, and per-class Precision/Recall at the best configuration.
* **Vector Database Retrieval & Grounding (PS 6, MP 9, MP 10):** Report **Precision@$k$ (P@$k$)**, **Recall@$k$**, **Mean Reciprocal Rank (MRR)**, and **nDCG@$k$** for $k \in \{3, 5, 10\}$ against human gold relevance judgments.
* **ASR & Audio Stream Transcription (MP 3, MP 5, MP 9, MP 10):** Report **Word Error Rate (WER)** under the explicit text-normalization rules of the [NIST OpenASR 2020 Evaluation Plan](https://www.nist.gov/itl/iad/mig/openasr-challenge):
  $$\text{WER} = \frac{S + D + I}{N_{\text{ref}}}$$
  where $S$ is substitutions, $D$ is deletions, $I$ is insertions, and $N_{\text{ref}}$ is the number of words in the human reference transcript (which explains why $\text{WER} > 100\%$ is mathematically possible when insertions $I$ are large).
* **Probabilistic Calibration (MP 10):** Report **Expected Calibration Error (ECE)** evaluated at both **10 bins and 15 bins** alongside reliability diagrams before and after post-hoc calibration (temperature scaling or isotonic regression), enforced with `deal` contracts verifying bounded outputs in $[0, 1]$.

---

## 2. Formalizing Statistical Hypotheses & Multiple-Comparison Control

Once your primary measure $f$ is locked in `protocol.md`, formalize your hypotheses before inspecting test outcomes:

* **The Null Hypothesis ($H_0$):** There is no true difference in performance between the proposed pipeline (e.g., Retrieval-Augmented Classifier $M_{\text{RAG}}$) and the baseline (e.g., MP 7 Fixed-Demonstration Classifier $M_{\text{fixed}}$) on measure $f$ over the target distribution:
  $$H_0: \mathbb{E}[f(M_{\text{RAG}})] = \mathbb{E}[f(M_{\text{fixed}})]$$
* **The Alternative Hypothesis ($H_1$):** Conditioning on top-$k$ retrieved exemplars (or learned cohort kernels) yields a statistically significant improvement:
  $$H_1: \mathbb{E}[f(M_{\text{RAG}})] > \mathbb{E}[f(M_{\text{fixed}})]$$
* **Benjamini–Hochberg (BH) False Discovery Rate Control (Required in MP 10 & HW 12):** When you compare multiple shot counts $k \in \{0, 1, 3, 5, 8\}$, retrieval depths $k \in \{3, 5, 10\}$, or cohort slices (a family of $m \ge 6$ comparisons), raw $p$-values inflate Type I error. You must define the comparison family of size $m \ge 6$ *before* running tests and apply the **Benjamini–Hochberg step-up procedure** (`statsmodels.stats.multitest.multipletests(..., method='fdr_bh')`) at $\alpha = 0.05$.

---

## 3. Resampling Protocols, Statistical Tests & Small-$n$ Power Analysis

Select the statistical test that matches your experimental structure and justify its assumptions in your report:

### A. Paired Bootstrap Resampling ($B \ge 10,000$) & Seed Sweep CIs (The Course Standard)
For non-linear metrics like Macro-F1, nDCG@$k$, and Cohen's $\kappa$ evaluated on the same gold test instances, draw $B \ge 10,000$ bootstrap resamples (sampling test indices with replacement) and compute $\Delta_b = f(M_{\text{RAG}}, X_b^*) - f(M_{\text{base}}, X_b^*)$ on identical resamples. Report the 95% percentile/BCa confidence interval and the paired bootstrap $p$-value.
* **Python:** `scipy.stats.bootstrap` (paired index resampling with `n_resamples=10000`, `random_state=42`)

### B. Single Gold Evaluation Set (Classification Disagreements): McNemar's Test
When comparing two classifiers on a fixed gold set ($n \le 50$ in MP 9/MP 10 or $50 \le n \le 200$ in HW 12), use **McNemar's Test** (with exact binomial calculation when discordant cell counts $b + c < 25$). It evaluates the $2 \times 2$ contingency table of instances where Classifier A was correct and Classifier B was wrong ($b$) versus the reverse ($c$).
* **Python:** `statsmodels.stats.contingency_tables.mcnemar(table, exact=True)`

### C. Skewed & Paired Fold/Window Metrics: Wilcoxon Signed-Rank & Paired $t$-Tests
When comparing per-segment WER (Whisper vs. AssemblyAI on identical audio segments), streaming window latencies, or $k$-fold cross-validation scores where differences are skewed and violate normality, use the non-parametric **Wilcoxon signed-rank test** alongside or in place of the paired Student's $t$-test.
* **Python:** `scipy.stats.wilcoxon` | `scipy.stats.ttest_rel` | `mlxtend.evaluate.paired_ttest_5x2cv`

### D. Small-$n$ Power & Stability Analysis on the Silver Pool (MP 10 Section 5)
Because MP 9 caps human annotation at $n \le 50$ objects, your gold-set confidence intervals have a structural floor on resolution ($\propto 1/\sqrt{n}$). In MP 10, you must subsample your 1,000-chunk weak-supervision silver pool across increasing sample sizes $n \in \{25, 50, 100, 250, 500, 1000\}$ to plot **95% CI width versus $n$**, and explicitly state what minimum effect size $\delta$ an evaluation set of $n \le 50$ can and cannot statistically resolve.

---

## 4. Authoritative References & Tooling Documentation
* **James, Witten, Hastie, Tibshirani, & Taylor (2023):** [*An Introduction to Statistical Learning with Applications in Python (ISLP)*](https://www.statlearning.com/) — Chapter 4 (Classification Metrics), Chapter 5 (Cross-Validation & The Bootstrap), and Chapter 13 (Multiple Testing, FWER, and Benjamini–Hochberg FDR).
* **scikit-learn Documentation:** [Metrics and Scoring: Quantifying the Quality of Predictions](https://scikit-learn.org/stable/modules/model_evaluation.html) & [Probability Calibration](https://scikit-learn.org/stable/modules/calibration.html).
* **SciPy & Statsmodels:** [`scipy.stats` (`bootstrap`, `ttest_rel`, `wilcoxon`)](https://docs.scipy.org/doc/scipy/reference/stats.html) & [`statsmodels` (`mcnemar`, `multipletests`)](https://www.statsmodels.org/stable/stats.html).
* **NIST OpenASR Challenge:** [OpenASR 2020 Evaluation Plan (Reference Transcript Normalization & WER Scoring)](https://www.nist.gov/itl/iad/mig/openasr-challenge).
