# MP 7 Experimental Protocol: Few-Shot Trope/Genre Classification

**Author:** Individual Course Submission (CIS 531/731)  
**Track:** VDB Track (PS 6 Custom Ontology)  
**Protocol Status:** LOCKED (Committed prior to experimental sweep per Rubric Part 1A)

---

## 1. Label Space Specification ($\mathcal{Y}$)
The label space consists of $L = 8$ mutually exclusive thematic trope and subgenre categories derived from the PS 6 ontology instances:

1. `Hustle_Narrative`: Socio-economic ascent, financial striving, street entrepreneurship.
2. `Regional_Authenticity`: Geographic rootedness, neighborhood allegiance, local pride.
3. `Lyrical_Sovereignty`: Technical virtuosity, complex rhyme schemes, competitive battle stance.
4. `Systemic_Critique`: Institutional critique, socio-political resistance, civil rights commentary.
5. `Boom_Bap`: East Coast aesthetic characterized by acoustic drum breaks and unquantized cadences.
6. `G_Funk`: West Coast melodic funk synthesizers, laid-back cadence, and rolling basslines.
7. `Trap`: Southern syncopated 808 sub-bass, rapid hi-hat rolls, and street realism.
8. `Chopper`: Fast-cadence polysyllabic flow velocities characteristic of the Midwest corridor.

---

## 2. Shot Sweep & Seed Schedule
Experiments evaluate three distinct classifier architectures across a five-point shot sweep:
* **Shot Counts ($k$):** $k \in \{0, 1, 3, 5, 8\}$ exemplars per class.
  * For $k = 0$, baseline prototype and zero-shot LLM are evaluated.
  * For $k \in \{1, 3, 5, 8\}$, demonstrations are class-balanced (total exemplars $N = k \times |\mathcal{Y}|$).
* **Random Seeds:** $\mathcal{S} = [42, 123, 456, 789, 2026]$ (5 distinct random seeds).
* **Demonstration Permutation:** For each seed $s \in \mathcal{S}$, the presentation order of exemplars within the LLM prompt context is pseudo-randomly permuted using seed $s$ to eliminate demonstration-position and recency bias.

---

## 3. Classifier Architectures & Runtime Contracts
All classifiers implement a unified `Classifier` abstract base class enforcing `@deal` runtime contracts on `predict_proba`:
1. **Embedding Prototype Classifier:** Class centroids $\mathbf{c}_y = \frac{1}{|\mathcal{D}_y|} \sum_{\mathbf{x} \in \mathcal{D}_y} \mathbf{x}$ computed in normalized embedding space ($d=384$ or $768$). Scoring via cosine similarity with softmax temperature scaling ($\tau = 0.1$).
2. **$k$-Nearest Neighbor Classifier:** Built over FAISS `IndexFlatIP`. Retrieves top-$k$ nearest exemplars; predicts empirical class posterior distribution.
3. **Fixed-Demonstration Few-Shot LLM:** Instruction-tuned CPU model (`Qwen/Qwen2.5-0.5B-Instruct` or `Qwen/Qwen2.5-1.5B-Instruct`) utilizing logit evaluation over calibrated verbalizer tokens.

### Deal Runtime Invariants:
* **Post-condition 1:** $\forall i, j: \hat{P}(Y=j | X=i) \ge 0.0$ (Non-negativity).
* **Post-condition 2:** $\forall i: \left| \sum_{j} \hat{P}(Y=j | X=i) - 1.0 \right| \le 10^{-6}$ (Unit-sum probability simplex).
* **Post-condition 3:** Output probability matrix has shape $(N, 8)$, matching the declared label space.

---

## 4. Evaluation Source Separation & Statistical Reporting (INV-12)
* **Primary Graded Metric:** Macro-Averaged F1 score computed strictly via `compute_graded_metric` on `eval_mp7.jsonl`.
* **Confidence Interval Procedure:** Non-parametric bootstrap percentile method ($B = 1,000$ resamples) at $\alpha = 0.05$ (95% two-sided confidence interval).
* **Fine-Grained Reporting:** Per-class Precision, Recall, and F1 reported for the highest-performing overall classifier configuration.
* **Development Metrics:** Any ablation or hyperparameter tuning on development splits is computed via `compute_dev_metric` with `grading_eligible=False`.
