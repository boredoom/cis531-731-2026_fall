<!-- ASSIGNMENT-META
id: MP 7
phase: Phase 3: Scrub & Embed
module: Module 06: GenAI & LLMs (Few-Shot Trope/Genre Classification)
released: Wed 21 Oct 2026
due: Tue 03 Nov 2026 (originally Fri 30 Oct 2026)
prev: assignments/homework/ps6_semantic_search_vdb_schema.md
next: assignments/homework/ps8_interim_report.md
REVIEW R-3: Evaluation-set provenance. INV-12 (instructor-provided held-out set) and INV-17 (GTAs do not pre-build gold sets) both apply before MP 9. Draft assumes `eval_mp7.jsonl` is instructor-built from public-domain or instructor-provided material.
REVIEW R-4: ASR-track label space (`asr_label_set.yaml`) is a drafted assumption; no INV defines it.
-->
# MP 7: Few-Shot Trope/Genre Classification (GenAI)
**Prototype, kNN, and fixed-demonstration LLM classifiers compared under a controlled few-shot protocol**

**🗓️ Released:** Wed 21 Oct 2026 | **📅 Due:** ~~Fri 30 Oct 2026~~ **Tue 03 Nov 2026, 11:59 PM CST** | **💯 Points:** 100 (Normalized to 30 in Gradebook) | **👥 Team:** Individual

> **🚨 CRITICAL SUBMISSION POLICY**
> * **Evaluation Source Separation (INV-12):** Graded metrics must be computed with `compute_graded_metric` against the instructor-provided evaluation set (`eval_mp7.jsonl`). Metrics on your own splits must use `compute_dev_metric` (`grading_eligible=False`) and are advisory only.
> * **Environment & Quota Constraints (INV-14/INV-15/INV-18):** Use an instruction-tuned model small enough for CPU inference or a free-tier hosted API under the team quota killswitch (INV-18); record the exact model identifier and revision hash. All work must be solvable on the pinned CPU DevContainer; GPU access is optional and never required.
> * **Schedule Note:** The due date for MP 7 has been extended to **Tue 03 Nov 2026**; all subsequent assignment due dates (PS 8, MP 9, MP 10, PS 11, HW 12) remain unchanged.

---

## 1. Overview & Pipeline Lineage
Build an embedding index from provenance-admitted chunks (FAISS `IndexFlatIP`) and compare three classifiers on the instructor-provided evaluation set: **(i) embedding-prototype**, **(ii) kNN over the exemplar index**, and **(iii) few-shot LLM prompting with fixed, class-balanced demonstrations**. Retrieval-conditioned demonstration selection is deferred to MP 9; calibration, significance testing, and error taxonomy are deferred to MP 10. Report **macro-F1 with 95% bootstrap CIs only**.

* **VDB Track Label Space:** 8–12 trope/genre labels from the ontology (**CIS 531:** instructor-provided unmodified schema per INV-11; **CIS 731:** your custom PS 6 ontology).
* **ASR Track Label Space:** Drawn from the instructor-provided `asr_label_set.yaml`.
* **Upstream Inputs:** PS 6 schema and label space; MP 5 chunk records; MP 3 corpus.
* **Downstream Consumers:** MP 9 (reuses the `Classifier` interface, prompt harness, and exemplar index; the fixed-demonstration result is the baseline for retrieval-augmented comparison); MP 10 (best model is interpreted); PS 8 (preliminary baselines).

### Required Readings
* [Speech and Language Processing, 3rd ed. draft (Jurafsky & Martin, 19 Aug 2026), Chs. 6–8](https://web.stanford.edu/~jurafsky/slp3/): neural networks, large language models and in-context learning, and the transformer architecture.
* [Hugging Face Transformers: “Text Classification”](https://huggingface.co/docs/transformers/tasks/sequence_classification): tokenization, sequence-classification heads, the `Trainer` workflow, and metric computation.

---

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the [Generative AI Kit (v3.0)](../../admin/policies/generative_ai_kit_v3.md) to help structure your submission. Follow these five stages:

1. **Protocol Lock:** Commit `protocol.md` (label space, shot sweep $k \in \{0, 1, 3, 5, 8\}$, at least 5 seeds, bootstrap CI method) *before* generating any results.
2. **Prompt Template Synthesis:** Draft the instruction, demonstration format, label verbalizers, constrained decoding, and output parser with the AI Kit; audit for label leakage and demonstration-position bias.
3. **Index and Baseline Build:** Embed admitted chunks, build the FAISS `IndexFlatIP` index, and implement the prototype and kNN baselines.
4. **Sweep Execution:** Run the shot sweep across seeds with quota logging; compute graded metrics only via `compute_graded_metric`.
5. **Results Audit:** Re-derive each reported number from `predictions.jsonl`; reject any AI-generated analysis that cannot be reproduced.

### MP 7 Tollbooth Prompt
```text
[MP 7 TOLLBOOTH PROMPT]
I am working on MP 7. I need to build the prompt template for few-shot in-context learning to classify my vector chunks.
*Here is the Toll:* [Provide your specific 8-12 trope/genre label space or asr_label_set.yaml labels].
*Properties:* My chosen shot sweep k values are {0, 1, 3, 5, 8} across >=5 seeds, and my instruction-tuned model identifier is [e.g., Qwen/Qwen2.5-1.5B-Instruct or meta-llama/Llama-3.2-3B-Instruct].
Do not write the Hugging Face pipeline code. Help me design the strict formatting constraints, verbalizers, and system instructions for the LLM prompt to ensure the output perfectly matches the label space without hallucinating labels. Suggest concrete controls for majority-label bias, demonstration-position bias (including permutation), and label leakage.
```

---

## 3. Required Document Structure
Your submission must be a **`report.md` (at most 3 pages) delivered with `protocol.md`, an executed notebook (`.ipynb`), `predictions.jsonl`, and `GenAI.pdf` under Git tag `mp7-submission`** containing the following sections:

### Part 1: Experimental Design & Prompt Failure-Mode Controls (30 pts raw / 9.0 pts normalized)
* **Protocol and Label Space (15 pts raw / 4.5 pts norm):** The committed `protocol.md` contents: 8–12 label space, shot sweep $k \in \{0, 1, 3, 5, 8\}$, $\ge 5$ random seeds, and 95% bootstrap CI method.
* **Prompt Specification and Failure-Mode Controls (15 pts raw / 4.5 pts norm):** Prompt template, demonstration format, label verbalizers, constrained decoding, output parser, and three failure modes (**majority-label bias**, **demonstration-position bias**, and **label leakage**) with a concrete control for each, explicitly including **demonstration-order permutation**.

### Part 2: Implementation, Shot-Sweep Results & Reproducibility (70 pts raw / 21.0 pts normalized)
* **Classifier Implementations (25 pts raw / 7.5 pts norm):** Three classifiers ((i) embedding-prototype, (ii) kNN over FAISS `IndexFlatIP`, (iii) fixed-demonstration few-shot LLM) behind one `Classifier` interface; `deal` contracts on `predict_proba` (non-negative, sums to `1.0` within `1e-6`, labels strictly in the declared label space).
* **Shot-Sweep Results (25 pts raw / 7.5 pts norm):** Macro-F1 (mean $\pm$ std over seeds; 95% bootstrap CI) per classifier and shot count computed via `compute_graded_metric` (INV-12); per-class precision/recall at the best configuration.
* **Reproducibility and Quota Log (15 pts raw / 4.5 pts norm):** Pinned environment (INV-14), exact model identifier and revision hash, API usage versus quota (INV-18), and CPU-only execution confirmation (INV-15).
* **GenAI Audit (5 pts raw / 1.5 pts norm):** Include your `GenAI.pdf` log or explicitly state `"No GenAI Used."`

---

## 4. Scoring Rubric (100 Points Raw / 30 Points Normalized)

| Component | Raw Weight | Norm (30) | Description |
| :--- | :--- | :--- | :--- |
| **Protocol and Label Space** | 15 pts | 4.5 pts | `protocol.md` is complete and committed before results generation. |
| **Prompt Specification & Controls** | 15 pts | 4.5 pts | Template is precise; concrete controls implemented for majority-label bias, position bias (with permutation), and label leakage. |
| **Classifier Implementation & Contracts** | 25 pts | 7.5 pts | Three classifiers behind one `Classifier` interface; `deal` contracts hold on all outputs. |
| **Shot-Sweep Rigor & Source Separation** | 25 pts | 7.5 pts | Seeds, 95% bootstrap CIs, and `compute_graded_metric` sourcing (INV-12) correctly applied and reproducible from `predictions.jsonl`. |
| **Reproducibility & Quota Log** | 15 pts | 4.5 pts | Pinned environment; runs on the CPU baseline; model hash and quota usage documented. |
| **GenAI Verification** | 5 pts | 1.5 pts | Includes the required `GenAI.pdf` log or explicitly states AI was not used. |

---

## 5. Downstream Assignment Schedule (Unchanged Due Dates)

* **PS 8: Interim Report (Mandatory Milestone)** — *Released:* Thu 29 Oct 2026 | *Due:* **Sat 07 Nov 2026** (30 pts, Team/Solo, tag `ps8-submission`).
* **MP 9: Retrieval-Augmented Classification & Convolutions** — *Released:* Sat 07 Nov 2026 | *Due:* **Mon 16 Nov 2026** (100 pts / 30 norm, Individual with 20-object partner overlap, $\le 50$ gold objects or 2 hours CI gate, tag `mp9-submission`).
* **MP 10: Data Science Interpretability & Metrics Scoring** — *Released:* Mon 16 Nov 2026 | *Due:* **Wed 25 Nov 2026** (100 pts / 30 norm, Individual, tag `mp10-submission`).
* **PS 11: Ethics, Data Storytelling, & Dashboards** — *Released:* Wed 25 Nov 2026 | *Due:* **Fri 04 Dec 2026** (100 pts / 30 norm, Individual, tag `ps11-submission`).
* **HW 12: Final Project Deliverables (Mandatory Milestone)** — *Released:* Sat 05 Dec 2026 | *Due:* **Mon 14 Dec 2026** (200 pts / 300 Substance + 30 Milestone, Team/Solo, 50–200 gold range gate, tag `hw12-final`).

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [PS 6: Semantic Search, Chunking, & VDB Schema](../homework/ps6_semantic_search_vdb_schema.md) | [[All Assignments]](../../README.md#schedule) | [PS 8: Interim Report (Mandatory Milestone)](../homework/ps8_interim_report.md) |

[🏠 Course Home](../../README.md) · [⬆️ Module](../../modules/module_06/README.md) · [⏫ Phase](../../phases/phase_03/README.md)
