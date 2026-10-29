---
yaml_schema_version: "2.6"
doc_version: "3.0"
updated: "2026-10-29"
versioning_rules: "Strict monotonicity. Reject regressions."
routing_clearance: "GENERAL - STUDENT FACING (CIS 531/731 INFRASTRUCTURE)"
anti_cwa: "ALWAYS ASK, NEVER INFER. Ground every claim in supplied context."
---

# Generative AI Project Kit v3.0 (CIS 531/731)
**Full Lifecycle Tollbooth Edition: Scope Covers [PS 4](../../assignments/homework/ps4_proposal.md), [MP 5](../../assignments/machine_problems/mp5_structured_streaming.md), [PS 6](../../assignments/homework/ps6_semantic_search_vdb_schema.md), [MP 7](../../assignments/machine_problems/mp7_genre_classification.md), [PS 8](../../assignments/homework/ps8_interim_report.md), [MP 9](../../assignments/machine_problems/mp9_rag_classification_gold_standard.md), [MP 10](../../assignments/machine_problems/mp10_interpretability_metrics.md), [PS 11](../../assignments/homework/ps11_ethics_storytelling_dashboards.md), and [HW 12](../../assignments/homework/hw12_final_deliverables.md)**

## 1. IDENTITY, MISSION & THE TWO PROCEDURAL TOLLBOOTHS
This document outlines the Approved Data Science Workflows, TBox/ABox Workspace Setup, and Meta-Prompts for LLM Assistance in **CIS 531/731**. Generative AI tools (ChatGPT, Gemini, Claude, Perplexity, M365 Copilot, Qwen, Grok) may be used to structure, critique, and debug your data pipeline, provided all interactions are audited via your `GenAI.pdf` file.

To foster research maturity and prevent "knowledge piñata" exploitation, AI usage is bound by two absolute procedural gates:

1. **The Anti-Spooning Stick (No Free Summaries or Gold Labels):** You are strictly forbidden from asking an AI to summarize a paper, invent a project idea *ab initio*, or assign human gold-standard labels (`source=gold` in MP 9 and HW 12). You must supply your own baseline hypothesis, raw schema, or human codebook first.
2. **The Systems Thinking Carrot ("Grammarly on Steroids"):** For reports (`PS 8`, `MP 7`–`MP 10`, `PS 11`, `HW 12`), generative synthesis is allowed **only** when you feed the model non-generative inputs (your own bullet points, schemas, `predictions.jsonl` / `metrics.jsonl` outputs, or MLflow tables). Every numeric claim must be reproduced from your raw files.

---

## 2. COURSE POLICY: TEAM COMPOSITION & SCHEMA INFERENCE (INV-11)
Your level of AI schema generation depends on your course enrollment track (`CIS 531` vs. `CIS 731`):

1. **CIS 531 Teams (Undergraduate ONLY):** Must use a verified "Golden Path" (Tier 1) data source or the course defaults. CIS 531 teams **must adopt the instructor-provided ontology and chunk schema unmodified (`INV-11`)**. You may not use the AI to generate custom schema topologies.
2. **CIS 731 Teams (Graduate ONLY):** A "Real-World API or Benchmark" (Tier 2) source is expected. You **must** utilize the AI Kit to perform schema inference and derive your own custom ontology and JSON Schema (Draft 2020-12: class hierarchy, relation types, cardinalities, change log, and competency questions). Reusing the unmodified instructor schema results in an automatic failure of the contract check.
3. **Mixed 531/731 Teams:** Permitted to use Tier 2 sources, provided **all schema and ontology inference tasks** during Obtain, Scrub, and Explore are explicitly claimed and executed by the **CIS 731 members** of the team.

---

## 3. INITIALIZATION & GROUNDING (ESTABLISHING THE TBOX & BASELINE ABOX)
To prevent context amnesia across the semester, separate the global rules of the course (your **TBox**: Terminological Box, configured once at the **Project / Gem / Notebook / Space level**) from your specific homework payloads (your **ABox**: Assertional Box, attached at the **individual Chat level**).

### Step 3.1: Upload the Project-Level Knowledge Files (Once per Semester)
Download the raw `.md` files of the following three documents and upload them to your platform's persistent Project Knowledge / References pane:
1. [`04_term_project_guidelines.md`](../syllabus/04_term_project_guidelines.md) (The Milestone Constraints)
2. [`05_term_project_taxonomy.md`](../syllabus/05_term_project_taxonomy.md) (The 3x5x5 Data Cube)
3. [`06_term_project_sourcing_guide.md`](../syllabus/06_term_project_sourcing_guide.md) (The Tier 1–3 Source Rules)
*(Optional for Phase 3–5 statistical verification: also upload [`07_term_project_evaluation.md`](../syllabus/07_term_project_evaluation.md) and [`08_term_project_grading_rubric.md`](../syllabus/08_term_project_grading_rubric.md).)*

### Step 3.2: Paste the Project-Level System Instruction (Once per Semester)
Copy the block below into the persistent **Project Instructions / Custom Instructions / Gem Instructions** field of your chosen platform:

```text
[SYSTEM INSTRUCTION: CIS 531/731 PROJECT TOLLBOOTH v3.0]
You are the Research Design Coordinator for CIS 531/731 (Data Science & Analytics). Your primary function is to act as a strict procedural tollbooth across Phases 1–5 (PS 4, MP 5, PS 6, MP 7, PS 8, MP 9, MP 10, PS 11, and HW 12). You will help me adapt assignments to my specific pipeline, but you must NOT generate code, schemas, gold annotations, or prose ab initio.

Step 1: The Intake Check
Do not provide advice until I supply: (a) My exact PS 4 3x5x5 coordinates (Analytical Category, Media Topic, claimed OSEMN stages, and locked ASR or VDB track per INV-3), and (b) My team composition (CIS 531 Only, CIS 731 Only, or Mixed).

Step 2: The Green-Light / Yellow-Light Evidence & Invariant Gate
Require me to provide my data-source provenance (Tier 1 or Tier 2; no Yelp/SEC data per INV-1; valid license_class/whitelist per INV-9/INV-10) and my concrete "Toll" artifact (raw JSON sample, schema draft, protocol.md, codebook, or raw evaluation metrics) before answering any assignment prompt. Enforce INV-11 (unmodified schema for CIS 531; custom ontology/JSON Schema for CIS 731), INV-12 (graded metrics only via compute_graded_metric on held-out/gold sets), and INV-14/INV-15/INV-18 (pinned CPU DevContainer and quota fallback).

Step 3: The Course Default Affordance
If I state "I skipped PS 4" or request the course default, anchor all downstream advice to the standard course pipeline: "Satellite radio caller analytics utilizing local Whisper ASR transcription and FAISS VDB ingestion."
```

### Step 3.3: Platform-Quickstart Summary
* **ChatGPT (Projects) / M365 Copilot (Notebooks):** Create a New Project / Notebook named `CIS 531-731 Term Project`, paste the System Instruction into *Project/Notebook Instructions*, and upload the `04`, `05`, and `06` `.md` files to Project Files / Notebook References.
* **Claude (Projects) / Qwen (Model Studio Agent):** Create a New Project / Agent Application, paste the System Instruction into *Custom Instructions / System Prompt*, and upload the `04`, `05`, and `06` `.md` files to Project Knowledge / RAG Knowledge Base.
* **Google Gemini (Gems / Skills):** Create a New Gem named `CIS 531-731 Project Tollbooth`, paste the System Instruction into *Instructions*, and upload the raw `04`, `05`, and `06` `.md` files under *Knowledge*.
* **Perplexity (Spaces) / Grok (Projects):** Create a Space / Project, paste the System Instruction into *Custom Instructions*, and upload the `04`, `05`, and `06` `.md` files to the Space/Project file store.
* **Chat-Level Execution (The Assignment ABox):** Do *not* upload individual homework specs to Project Knowledge. Attach the specific assignment `.md` file (`mp5`, `ps6`, `mp7`, `ps8`, `mp9`, `mp10`, `ps11`, or `hw12`) directly to the chat message when executing its Tollbooth prompt below.

---

## 4. FULL LIFECYCLE EXECUTION PROMPT LIBRARY (MP 5 – HW 12)

### MP 5: Structured Streaming Tollbooth
> **[PROMPT]** I am working on MP 5 (Structured Streaming). Based on my established PS 4 data source, I need help defining the `deal` contracts and the `StructType` schema.
> *Here is the Toll:* [Paste a sample of your raw JSON/data payload].
> *Properties:* My required chunk duration limit is [XX] seconds ($\le 30\text{s}$), and my empirical lateness distribution `ingest_ts - ts_end` (p50/p95/p99) is [X/Y/Z] seconds.
> Do not write the PySpark code for me. Evaluate my raw payload, tell me which fields are structurally mandatory for Event-Time Windowing, justify their nullability, specify the `deal` pre/post-conditions (`BoundedChunking`, `INV-9`/`INV-10`), and derive the watermark delay and state bound.

### PS 6: Semantic Search & VDB Schema Tollbooth
> **[PROMPT]** I am working on PS 6. I need to calculate the chunking cost model and select a FAISS index (`IndexFlatIP`, `IndexIVFFlat`, or `IndexHNSWFlat`) for my specific corpus.
> *Here is the Toll:* [State your corpus size in MB/GB, average token length per document, and embedding model maximum sequence length].
> *Properties:* My team composition is [531/731/Mixed].
> Based on these numbers, output a trade-off matrix comparing the build, memory, and query costs of the three FAISS indices. If my team includes CIS 731 students, help me draft and audit the custom JSON Schema (Draft 2020-12) extending the MP 5 chunk record.

### MP 7: Few-Shot Classification Tollbooth (Due Tue 03 Nov 2026)
> **[PROMPT]** I am working on MP 7. I need to build the prompt template for few-shot in-context learning to classify my vector chunks.
> *Here is the Toll:* [Provide your committed `protocol.md` draft with your 8–12 trope/genre or `asr_label_set.yaml` label space].
> *Properties:* My chosen shot sweep $k$ values are $\{0, 1, 3, 5, 8\}$ across $\ge 5$ seeds, and my instruction-tuned model identifier and revision hash are [Insert Model ID & Hash].
> Do not write the Hugging Face pipeline code. Help me design the strict formatting constraints, label verbalizers, constrained decoding rules, and output parser to ensure predictions match the label space without hallucinating labels. Suggest concrete controls for (1) majority-label bias, (2) demonstration-position bias (including permutation), and (3) label leakage.

### PS 8: Interim Report — Risk Red-Team & "Grammarly on Steroids" Synthesis (Due Sat 07 Nov 2026)
> **[PROMPT A — Risk Red-Team & UMAP Audit]** I am writing my PS 8 Interim Report. I need you to red-team my Risk Register and audit my exploratory figure plan.
> *Here is the Toll:* [Paste your pipeline architecture, UMAP `n_neighbors`/`min_dist` sweep parameters, MP 7 baseline numbers, and list of 3 initial risks].
> *Properties:* My annotation plan targets [50–200] examples, and my team size requires [IAA protocol / solo $\le 1\%$ validation fraction].
> Attack my architecture: identify at least two omitted failure modes specific to my pipeline (including `INV-15`/`INV-18` CPU/quota fallback) to bring my Risk Register to $\ge 5$ quantified risks, and verify that my 3 exploratory figures comply with Wilke Part II.
>
> **[PROMPT B — "Grammarly on Steroids" Synthesizer]** You are an academic technical editor. I am providing my original bullet points, raw data schemas, and experimental outputs below. Synthesize this into formal, concise academic prose for Section [X] of my PS 8 Interim Report. Do NOT add new claims, invent data, hallucinate citations, or alter my original intellectual intent.
> *[MY ORIGINAL INPUT]:* [Paste your raw bullet points/tables/contract excerpts here]

### MP 9: Gold Codebook, Weak Supervision & Cohort Convolutions Tollbooth (Due Mon 16 Nov 2026)
> **[PROMPT]** I am working on MP 9. I need to refine my human annotation codebook and design weak-supervision labeling functions and cohort convolution checks.
> *Here is the Toll:* [Paste your draft codebook decision rules, 3 human-labeled boundary examples from your $\le 50$ gold set, and your ordered cohort axis definition (`release_decade` or event-time window index)].
> Do NOT assign gold labels for me (`source=gold` must be human-assigned). Critique my codebook for ambiguous boundary cases on the 20-object partner overlap (`overlap_ids.txt`), help me specify heuristic labeling functions and vote aggregation for the $\ge 1,000$-chunk silver pool (`source=silver`), and verify the boundary-handling math for convolving per-cohort trope frequency vectors with the smoothing kernel `[0.25, 0.5, 0.25]` and first-difference kernel `[-1, 1]` (plus the learned 1-D PyTorch conv kernel comparison if CIS 731).

### MP 10: Interpretability Harness, Calibration & BH Inference Tollbooth (Due Wed 25 Nov 2026)
> **[PROMPT]** I am working on MP 10. I need to verify my metric derivations, `deal` contracts for `evaluate(model, X, y)`, calibration setup, and multiple-testing family.
> *Here is the Toll:* [Paste your confusion matrix, draft imbalance counterexample where Accuracy and Macro-F1 rank two models oppositely, and your pre-registered family of $\ge 6$ comparisons].
> Verify my hand derivations for micro/macro/weighted F1, P@$k$, Recall@$k$, MRR, nDCG@$k$ (and NIST OpenASR 2020 WER if ASR track). Audit my `deal` post-conditions (metrics bounded in $[0, 1]$, confusion matrix summing to $n$), check my experimental design for 10/15-bin ECE calibration and paired bootstrap ($B \ge 10,000$) / McNemar's test with Benjamini–Hochberg FDR control, and help me structure the silver-pool CI-width vs. $n$ power analysis.

### PS 11: Ethics Audit, 5-View Wilke Storyboard & Limitations Panel Tollbooth (Due Fri 04 Dec 2026)
> **[PROMPT]** I am working on PS 11. I need to audit my pipeline for concrete ethical/provenance risks and design an audience-specific 5-view dashboard storyboard.
> *Here is the Toll:* [Paste your PS 8 provenance table, PII classes and redaction/retention policy, target audience + decision + 1-sentence 'so what', and draft 5-view storyboard].
> Critique my audit to ensure zero generic 'bias/privacy' fluff: verify concrete analysis of `license_class`/whitelist compliance (including `INV-9` no-lyric-reproduction), ecological fallacy (release decade $\ne$ audience demographics), survivorship/selection bias, ASR dialect WER disparity, and prompt-injection/hallucination mitigations. Audit my 5 storyboard views against Wilke Part II (accessible palettes, direct labeling, CI display, and limitations panel fields).

### HW 12: Final MLOps Reproducibility (`make verify`), MLflow Lineage & Drift Runbook Tollbooth (Due Mon 14 Dec 2026)
> **[PROMPT]** I am assembling HW 12 (`hw12-final`). I need an end-to-end integration audit across MP 5–PS 11, `make verify`, MLflow tracking, and my serving/drift runbook.
> *Here is the Toll:* [Paste your `Makefile` `verify` target, MLflow logged parameters/metrics/hashes, 50–200 gold-standard range-gate summary, and PSI/KS drift-monitoring threshold].
> Audit my package for reproducibility gaps: verify that `make verify` checks the lockfile/container digest (`INV-14`), runs `deal` contract tests and the 50–200 gold range gate (`INV-21`), and reproduces headline numbers on the CPU baseline (`INV-15`). Check that every number in `REPORT.pdf` traces to an MLflow run export and that my serving path and PSI/KS drift runbook are complete.

---

## 5. THE "KEEP MOVING" AFFORDANCE (ACTION BRANCHES)
Append this block to any prompt when you want concrete, meta-cognitive next steps:

```text
[ACTION BRANCHES REQUIREMENT]
Do not end with a generic question. Provide exactly three [ACTION BRANCHES] for me to choose from:
* [OPTION A] - Broaden the literature/documentation based on my domain.
* [OPTION B] - Deepen the math/logic check on a specific schema or statistical assumption I provided.
* [OPTION C] - Generate an explicitly bounded verification test case for my architecture.
```
