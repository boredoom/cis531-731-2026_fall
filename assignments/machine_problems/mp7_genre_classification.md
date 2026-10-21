<!-- ASSIGNMENT-META
id: MP 7
phase: Phase 3: Scrub & Embed
module: Module 06: GenAI & LLMs (Few-Shot Trope/Genre Classification)
released: Wed 21 Oct 2026
due: Fri 30 Oct 2026
prev: assignments/homework/ps6_semantic_search_vdb_schema.md
next: assignments/homework/ps8_interim_report.md
REVIEW R-3: Evaluation-set provenance. INV-12 (instructor-provided held-out set) and INV-17 (GTAs do not pre-build gold sets) both apply before MP 9. Draft assumes `eval_mp7.jsonl` is instructor-built from public-domain or instructor-provided material.
REVIEW R-4: ASR-track label space (`asr_label_set.yaml`) is a drafted assumption; no INV defines it.
-->
# MP 7: Few-Shot Trope/Genre Classification (GenAI)
**Prototype, kNN, and fixed-demonstration LLM classifiers compared under a controlled few-shot protocol**

**🗓️ Released:** Wed 21 Oct 2026 | **📅 Due:** Fri 30 Oct 2026 | **💯 Points:** 100 | **👥 Team:** Individual

> **🚨 CRITICAL SUBMISSION POLICY**
> **Evaluation Source Separation (INV-12):** Graded metrics must be computed with `compute_graded_metric` against the instructor-provided evaluation set. Metrics on your own splits must use `compute_dev_metric` (`grading_eligible=False`) and are advisory.

## 1. Overview
Build an embedding index from provenance-admitted chunks (FAISS `IndexFlatIP`) and compare three classifiers on the instructor-provided evaluation set: (i) embedding-prototype, (ii) kNN over the exemplar index, and (iii) few-shot LLM prompting with fixed, class-balanced demonstrations. Retrieval-conditioned demonstration selection is deferred to MP 9; calibration, significance testing, and error taxonomy are deferred to MP 10. Report macro-F1 with 95% bootstrap CIs only.

VDB track: the label space is 8–12 trope/genre labels from the ontology (CIS 531: instructor-provided; CIS 731: your PS 6 ontology). ASR track: the label space is drawn from the instructor-provided `asr_label_set.yaml`. Use an instruction-tuned model small enough for CPU inference or a free-tier hosted API under quota killswitch (INV-18); record the exact model identifier and revision hash. All work must be solvable on the pinned CPU DevContainer (INV-14/INV-15); GPU access is optional and never required.

**Cadence Notice:** PS 6 (due Sun 25 Oct 2026) to MP 7 (due Fri 30 Oct 2026) is 5 days, an explicit exception to the standard 6-day inter-assignment gap, applied to maintain assignment cadence without forcing a due date on Halloween (Sat 31 Oct).

**Required Readings:**
* [Speech and Language Processing, 3rd ed. draft (Jurafsky & Martin, 19 Aug 2026), Chs. 6–8](https://web.stanford.edu/~jurafsky/slp3/): neural networks, large language models and in-context learning, and the transformer architecture.
* [Hugging Face Transformers: “Text Classification”](https://huggingface.co/docs/transformers/tasks/sequence_classification): tokenization, sequence-classification heads, the `Trainer` workflow, and metric computation.

**Upstream inputs:** PS 6 schema and label space; MP 5 chunk records; MP 3 corpus.  
**Downstream consumers:** MP 9 (reuses the `Classifier` interface, prompt harness, and exemplar index; the fixed-demonstration result is the baseline for retrieval-augmented comparison); MP 10 (best model is interpreted); PS 8 (baselines).

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Protocol Lock:** Commit `protocol.md` (label space, shot sweep k ∈ {0, 1, 3, 5, 8}, at least 5 seeds, bootstrap CI method) before generating any results.
2. **Prompt Template Synthesis:** Draft the instruction, demonstration format, label verbalizers, constrained decoding, and output parser with the AI Kit; audit for label leakage and demonstration-position bias.
3. **Index and Baseline Build:** Embed admitted chunks, build the FAISS index, and implement the prototype and kNN baselines.
4. **Sweep Execution:** Run the shot sweep across seeds with quota logging; compute graded metrics only via `compute_graded_metric`.
5. **Results Audit:** Re-derive each reported number from `predictions.jsonl`; reject any AI-generated analysis that cannot be reproduced.

## 3. Required Document Structure
Your submission must be a **`report.md` (at most 3 pages) delivered with an executed notebook and `predictions.jsonl` under Git tag `mp7-submission`** containing the following sections exactly as named below. 

* **Protocol and Label Space:** The committed `protocol.md` contents: label space, shot sweep, seeds, and CI method.
* **Prompt Specification and Failure-Mode Controls:** Prompt template, and three failure modes (majority-label bias, demonstration-position bias, label leakage) with a control for each, including demonstration-order permutation.
* **Classifier Implementations:** Three classifiers behind one `Classifier` interface; `deal` contracts on `predict_proba` (non-negative, sums to 1 within 1e-6, labels in the label space).
* **Shot-Sweep Results:** Macro-F1 (mean ± std over seeds; 95% bootstrap CI) per classifier and shot count; per-class precision/recall at the best configuration.
* **Reproducibility and Quota Log:** Pinned environment, model identifier and revision hash, API usage versus quota, and CPU-only confirmation.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (100 Points Total)

This assignment is worth 100 points total.

**Part 1: Experimental Design (30 pts)**
* **Protocol and label space (15 pts):** Complete and committed before results.
* **Prompt specification and controls (15 pts):** Template is precise; each failure mode has a concrete control.

**Part 2: Implementation and Results (65 pts)**
* **Classifier implementation and contracts (25 pts):** Three classifiers behind one interface; contracts hold on all outputs.
* **Shot-sweep rigor (25 pts):** Seeds, CIs, and graded-metric sourcing correctly applied and reported.
* **Reproducibility and quota log (15 pts):** Pinned environment; runs on the CPU baseline; quota usage documented.

* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [PS 6: Semantic Search, Chunking, & VDB Schema](../homework/ps6_semantic_search_vdb_schema.md) | [[All Assignments]](../README.md#schedule) | [PS 8: Interim Report (Mandatory Milestone)](../homework/ps8_interim_report.md) |

[🏠 Course Home](../../README.md) · [⬆️ Module](../../modules/module_06/README.md) · [⏫ Phase](../../phases/phase_03/README.md)
