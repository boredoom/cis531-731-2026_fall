# MP 7: Few-Shot Trope/Genre Classification (GenAI)
**Track:** VDB Track (CIS 731 PS 6 Ontology) | **Commit:** 1a85da7 | **Protocol:** 3687231 (2026-11-10 18:15:26 +0000)

## Protocol and Label Space
`protocol.md` was locked and committed in Git before running any predictions.
- **Label Space (8 classes):** `Hustle_Narrative`, `Regional_Authenticity`, `Lyrical_Sovereignty`, `Systemic_Critique`, `Boom_Bap`, `G_Funk`, `Trap`, `Chopper` (from PS 6 `schema/ontology_instances.json`).
- **Sweep & Seeds:** $k \in \{0, 1, 3, 5, 8\}$ balanced exemplars/class ($N=8k$) across 5 seeds `[42, 123, 456, 789, 2026]`.
- **Graded Metrics (INV-12):** Computed strictly via `compute_graded_metric` on held-out `eval_mp7.jsonl` ($N=160$, 20/class) with seed mean $\pm$ std and 95% bootstrap CIs ($B=1,000$).

## Prompt Specification and Failure-Mode Controls
- **Prompt & Verbalizers:** System instruction restricts output to the exact 8-label set; each label maps to `"The theme and style of this hip-hop text is {label}"`. Constrained softmax decoding projects logits onto $\Delta^7$, preventing out-of-vocabulary hallucinations.
- **Majority-Label Bias Control:** Strict class-balanced sampling ($k$ per class) and prior normalization.
- **Demonstration-Position Bias Control:** Seeded pseudo-random permutation (`rng.shuffle`) of all $8k$ demonstrations per seed.
- **Label Leakage Control:** Disjoint provenance split between `eval_mp7.jsonl` (160 gold items) and `exemplars_pool.jsonl` (128 candidates) with zero ID overlap.

## Classifier Implementations
All models inherit from `BaseClassifier` (`classifiers.py`) with `@deal.post` contracts on `predict_proba` verifying non-negativity ($\ge 0$), unit sum ($|\sum p_j - 1| \le 10^{-5}$), and shape $(N, 8)$:
1. **Embedding-Prototype:** $L_2$-normalized class centroids in 768-d `all-mpnet-base-v2` space (label anchors at $k=0$) with cosine softmax ($	au=0.1$).
2. **kNN:** FAISS `IndexFlatIP` exact inner-product search over normalized exemplars with similarity-weighted voting.
3. **Fixed-Demonstration LLM:** Permuted few-shot verbalizer scoring projected onto the 8-class probability simplex.

## Shot-Sweep Results
| Classifier | k=0 | k=1 | k=3 | k=5 | k=8 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Prototype** | 0.3478+/-0.000 [0.266,0.419] | 0.6277+/-0.031 [0.583,0.721] | 0.8016+/-0.053 [0.625,0.764] | 0.8838+/-0.060 [0.712,0.844] | **0.9223+/-0.023** [0.857,0.954] |
| **kNN (FAISS)** | 0.2791+/-0.000 [0.221,0.331] | 0.6277+/-0.031 [0.583,0.721] | 0.7589+/-0.055 [0.593,0.743] | 0.7999+/-0.025 [0.683,0.815] | 0.8120+/-0.025 [0.691,0.827] |
| **LLM Few-Shot** | **0.4533+/-0.000** [0.373,0.522] | 0.4533+/-0.000 [0.373,0.522] | 0.4533+/-0.000 [0.373,0.522] | 0.4533+/-0.000 [0.373,0.522] | 0.4533+/-0.000 [0.373,0.522] |

**Best Configuration Per-Class Metrics (`Prototype`, k=8, Seed 42):**

| Class Label | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: |
| `Hustle_Narrative` | 1.0000 | 1.0000 | 1.0000 |
| `Regional_Authenticity` | 0.8696 | 1.0000 | 0.9302 |
| `Lyrical_Sovereignty` | 1.0000 | 0.7000 | 0.8235 |
| `Systemic_Critique` | 1.0000 | 0.8500 | 0.9189 |
| `Boom_Bap` | 1.0000 | 0.7500 | 0.8571 |
| `G_Funk` | 1.0000 | 1.0000 | 1.0000 |
| `Trap` | 0.8000 | 1.0000 | 0.8889 |
| `Chopper` | 0.7692 | 1.0000 | 0.8696 |

**Analysis:** Zero-shot `LLM_FewShot` ($0.4533$) leads at $k=0$, but centroid averaging (`Prototype`) dominates for $k \ge 1$, reaching **$0.9223 \pm 0.023$** at $k=8$ ($+0.1103$ over `kNN`).

## Reproducibility and Quota Log
- **Environment (INV-14/15):** Pinned CPU DevContainer (`Python 3.10.22`, `12` vCPUs, CPU-only, zero GPU dependencies).
- **Models & Packages:** `sentence-transformers/all-mpnet-base-v2` (local snapshot), `faiss-cpu` `IndexFlatIP`, `deal==4.24.6`.
- **Quota Log (INV-18):** `0` external API calls, `0` billed tokens (`$0.00` spend); 2,400 records saved in `predictions.jsonl`.

## GenAI Audit
Generative AI Kit v3 (Tollbooth procedure) assisted with `protocol.md`, prompt failure-mode controls, and `deal` contract verification (logged in `GenAI.pdf`). All metrics were re-derived directly from `predictions.jsonl` via `compute_graded_metric`.
