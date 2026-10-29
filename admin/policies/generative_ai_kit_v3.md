---
yaml_schema_version: "2.6"
doc_version: "3.1"
updated: "2026-10-29"
versioning_rules: "Strict monotonicity. Reject regressions."
routing_clearance: "GENERAL - STUDENT FACING (CIS 531/731 INFRASTRUCTURE)"
anti_cwa: "ALWAYS ASK, NEVER INFER. Ground every claim in supplied context."
---

# Generative AI Project Kit v3.1 (CIS 531/731)
**Full Lifecycle Tollbooth Edition: Scope Covers [PS 4](../../assignments/homework/ps4_proposal.md), [MP 5](../../assignments/machine_problems/mp5_structured_streaming.md), [PS 6](../../assignments/homework/ps6_semantic_search_vdb_schema.md), [MP 7](../../assignments/machine_problems/mp7_genre_classification.md), [PS 8](../../assignments/homework/ps8_interim_report.md), [MP 9](../../assignments/machine_problems/mp9_rag_classification_gold_standard.md), [MP 10](../../assignments/machine_problems/mp10_interpretability_metrics.md), [PS 11](../../assignments/homework/ps11_ethics_storytelling_dashboards.md), and [HW 12](../../assignments/homework/hw12_final_deliverables.md)**

## 1. IDENTITY, MISSION & THE TWO PROCEDURAL TOLLBOOTHS
This document outlines the Approved Data Science Workflows, TBox/ABox Workspace Setup, and Meta-Prompts for LLM Assistance in **CIS 531/731**. Generative AI tools (ChatGPT, Gemini, Claude, Perplexity, M365 Copilot, Qwen, Grok) may be used to structure, critique, and debug your data pipeline, provided all interactions are audited via your `GenAI.pdf` file.

To foster research maturity and prevent "knowledge piñata" exploitation, AI usage is bound by two absolute procedural gates:

1. **The Anti-Spooning Stick (No Free Summaries or Gold Labels):** You are strictly forbidden from asking an AI to summarize a paper, invent a project idea *ab initio*, or assign human gold-standard labels (`source=gold` in [MP 9](../../assignments/machine_problems/mp9_rag_classification_gold_standard.md) and [HW 12](../../assignments/homework/hw12_final_deliverables.md)). You must supply your own baseline hypothesis, raw schema, or human codebook first.
2. **The Systems Thinking Carrot ("Grammarly on Steroids"):** For reports ([PS 8](../../assignments/homework/ps8_interim_report.md), [MP 7](../../assignments/machine_problems/mp7_genre_classification.md)–[MP 10](../../assignments/machine_problems/mp10_interpretability_metrics.md), [PS 11](../../assignments/homework/ps11_ethics_storytelling_dashboards.md), [HW 12](../../assignments/homework/hw12_final_deliverables.md)), generative synthesis is allowed **only** when you feed the model non-generative inputs (your own bullet points, schemas, `predictions.jsonl` / `metrics.jsonl` outputs, or MLflow tables). Every numeric claim must be reproduced from your raw files for the grader to check by hand or automatically.

---

## 2. COURSE POLICY: TEAM COMPOSITION & SCHEMA AUTHORITY
As specified in [`term_project_invariants.md`](./term_project_invariants.md), your level of AI schema generation depends on your course enrollment track (`CIS 531` vs. `CIS 731`):

1. **CIS 531 Teams (Undergraduate ONLY):** Must use a verified "Golden Path" (Tier 1) data source or the course defaults. CIS 531 teams **must adopt the instructor-provided ontology and chunk schema unmodified**, for the grader to check by hand or automatically. You may not use the AI to generate custom schema topologies.
2. **CIS 731 Teams (Graduate ONLY):** A "Real-World API or Benchmark" (Tier 2) source is expected. You **must** utilize the AI Kit to perform schema inference and derive your own custom ontology and JSON Schema (Draft 2020-12: class hierarchy, relation types, cardinalities, change log, and competency questions). Reusing the unmodified instructor schema results in an automatic failure when checked by the grader by hand or automatically.
3. **Mixed 531/731 Teams:** Permitted to use Tier 2 sources, provided **all schema and ontology inference tasks** during Obtain, Scrub, and Explore are explicitly claimed and executed by the **CIS 731 members** of the team.

---

## 3. INITIALIZATION & GROUNDING (ESTABLISHING THE TBOX & BASELINE ABOX)
To prevent context amnesia across the semester, separate the global rules of the course (your **TBox**: Terminological Box, configured once at the **Project / Gem / Notebook / Space level**) from your specific homework payloads (your **ABox**: Assertional Box, attached at the **individual Chat level**).

### Step 3.1: Upload the Project-Level Knowledge Files (Once per Semester)
Download the raw `.md` files of the following course documents and upload them to your platform's persistent Project Knowledge / References pane:
1. [`04_term_project_guidelines.md`](../syllabus/04_term_project_guidelines.md) (The Milestone Constraints)
2. [`05_term_project_taxonomy.md`](../syllabus/05_term_project_taxonomy.md) (The 3x5x5 Data Cube)
3. [`06_term_project_sourcing_guide.md`](../syllabus/06_term_project_sourcing_guide.md) (The Tier 1–3 Source Rules)
4. [`term_project_invariants.md`](./term_project_invariants.md) (The Qualitative Course Requirements & Boundaries)
*(Optional for Phase 3–5 statistical verification: also upload [`07_term_project_evaluation.md`](../syllabus/07_term_project_evaluation.md) and [`08_term_project_grading_rubric.md`](../syllabus/08_term_project_grading_rubric.md).)*

### Step 3.2: Paste the Project-Level System Instruction (Once per Semester)
Copy the block below into the persistent **Project Instructions / Custom Instructions / Gem Instructions** field of your chosen platform:

```text
[SYSTEM INSTRUCTION: CIS 531/731 PROJECT TOLLBOOTH v3.1]
You are the Research Design Coordinator for CIS 531/731 (Data Science & Analytics). Your primary function is to act as a strict procedural tollbooth across Phases 1–5 (PS 4, MP 5, PS 6, MP 7, PS 8, MP 9, MP 10, PS 11, and HW 12). You will help me adapt assignments to my specific pipeline, but you must NOT generate code, schemas, gold annotations, or prose ab initio.

Step 1: The Intake Check
Do not provide advice until I supply: (a) My exact PS 4 3x5x5 coordinates (Analytical Category, Media Topic, claimed OSEMN stages, and locked Automatic Speech Recognition [ASR] stream track or Vector Database [VDB] text corpus track, which is fixed from the proposal onward with no mid-semester track switching), and (b) My team composition (CIS 531 Only, CIS 731 Only, or Mixed).

Step 2: The Green-Light / Yellow-Light Evidence & Qualitative Requirement Gate
Require me to provide my data-source provenance and my concrete "Toll" artifact (raw JSON sample, schema draft, protocol.md, codebook, or raw evaluation metrics) before answering any assignment prompt. Enforce the following course-wide requirements (for the grader to check by hand or automatically):
1. Prohibited & Admitted Sources: No milestone, homework, or term project may source training or evaluation data from Yelp review corpora or SEC filings. Every ingested corpus document must carry an explicit `license_class` tag in `{public_domain, instructor_provided}`, and any live ASR capture must come strictly from instructor-maintained whitelisted streams or fallback demo streams.
2. Schema Authority: CIS 531 teams must adopt the unmodified instructor-provided schema; CIS 731 teams (and CIS 731 members on mixed teams) must derive a custom ontology and JSON Schema.
3. Evaluation Source Separation: Graded metrics must be computed strictly against the instructor-provided held-out gold sets (or human-adjudicated gold sets in MP 9, MP 10, and HW 12), never on development splits or weak-supervision silver pools.
4. Runtime Pinning & Quota Fallback: All work must be 100% solvable in the pinned CPU DevContainer baseline with strict container-digest and dependency-lockfile pinning. If API or compute quotas are exhausted, the pipeline must automatically fall back to local CPU Whisper transcription or free-tier execution.

Step 3: The Course Default Affordance
If I state "I skipped PS 4" or request the course default, anchor all downstream advice to the standard course pipeline: "Satellite radio caller analytics utilizing local Whisper ASR transcription and FAISS VDB ingestion."
```

### Step 3.3: Platform-Quickstart Summary
- **ChatGPT (Projects) / M365 Copilot (Notebooks):** Create a New Project / Notebook named `CIS 531-731 Term Project`, paste the System Instruction into *Project/Notebook Instructions*, and upload the `04`, `05`, `06`, and `term_project_invariants.md` files to Project Files / Notebook References.
- **Claude (Projects) / Qwen (Model Studio Agent):** Create a New Project / Agent Application, paste the System Instruction into *Custom Instructions / System Prompt*, and upload the `04`, `05`, `06`, and `term_project_invariants.md` files to Project Knowledge / RAG Knowledge Base.
- **Google Gemini (Gems / Skills):** Create a New Gem named `CIS 531-731 Project Tollbooth`, paste the System Instruction into *Instructions*, and upload the raw `04`, `05`, `06`, and `term_project_invariants.md` files under *Knowledge*.
- **Perplexity (Spaces) / Grok (Projects):** Create a Space / Project, paste the System Instruction into *Custom Instructions*, and upload the `04`, `05`, `06`, and `term_project_invariants.md` files to the Space/Project file store.
- **Chat-Level Execution (The Assignment ABox):** Do *not* upload individual homework specs to Project Knowledge. Attach the specific assignment `.md` file ([MP 5](../../assignments/machine_problems/mp5_structured_streaming.md), [PS 6](../../assignments/homework/ps6_semantic_search_vdb_schema.md), [MP 7](../../assignments/machine_problems/mp7_genre_classification.md), [PS 8](../../assignments/homework/ps8_interim_report.md), [MP 9](../../assignments/machine_problems/mp9_rag_classification_gold_standard.md), [MP 10](../../assignments/machine_problems/mp10_interpretability_metrics.md), [PS 11](../../assignments/homework/ps11_ethics_storytelling_dashboards.md), or [HW 12](../../assignments/homework/hw12_final_deliverables.md)) directly to the chat message when executing its Tollbooth prompt below.

---

## 4. FULL LIFECYCLE EXECUTION PROMPT LIBRARY (MP 5 – HW 12)

### [MP 5](../../assignments/machine_problems/mp5_structured_streaming.md): Structured Streaming Tollbooth
> **[PROMPT]** I am working on [MP 5](../../assignments/machine_problems/mp5_structured_streaming.md) (Structured Streaming). Based on my established [PS 4](../../assignments/homework/ps4_proposal.md) data source, I need help defining the `StructType` schema and the data-validation properties for the grader to check by hand or automatically.
> *Here is the Toll:* [Paste a sample of your raw JSON/data payload].
> *Properties:* My required chunk duration limit is [XX] seconds ($\le 30\text{s}$), and my empirical lateness distribution `ingest_ts - ts_end` (p50/p95/p99) is [X/Y/Z] seconds.
> Do not write the PySpark code for me. Evaluate my raw payload, tell me which fields are structurally mandatory for Event-Time Windowing, justify their nullability, state the required input/output validation properties for the grader to check by hand or automatically (confirming that every chunk duration is at most 30 seconds with `ts_start < ts_end`, every corpus record carries a `license_class` in `{public_domain, instructor_provided}`, and every ASR stream source belongs to the instructor-maintained whitelist), and derive the watermark delay and state bound. (Note: streaming latency and throughput targets are evaluated from `metrics.jsonl` rather than per-record validation checks.)

### [PS 6](../../assignments/homework/ps6_semantic_search_vdb_schema.md): Semantic Search & VDB Schema Tollbooth
> **[PROMPT]** I am working on [PS 6](../../assignments/homework/ps6_semantic_search_vdb_schema.md). I need to calculate the chunking cost model and select a FAISS index (`IndexFlatIP`, `IndexIVFFlat`, or `IndexHNSWFlat`) for my specific corpus (FAISS is the mandatory baseline for all students; Milvus is an optional upgrade gated to CIS 731 only).
> *Here is the Toll:* [State your corpus size in MB/GB, average token length per document, and embedding model maximum sequence length].
> *Properties:* My team composition is [531/731/Mixed].
> Based on these numbers, output a trade-off matrix comparing the build, memory, and query costs of the three FAISS indices. If my team is CIS 531 only, confirm how my pipeline maps to the unmodified instructor schema; if my team includes CIS 731 students, help me draft and audit the custom JSON Schema (Draft 2020-12) extending the [MP 5](../../assignments/machine_problems/mp5_structured_streaming.md) chunk record for the grader to check by hand or automatically.

### [MP 7](../../assignments/machine_problems/mp7_genre_classification.md): Few-Shot Classification Tollbooth (Due Tue 03 Nov 2026)
> **[PROMPT]** I am working on [MP 7](../../assignments/machine_problems/mp7_genre_classification.md). I need to build the prompt template for few-shot in-context learning to classify my vector chunks and evaluate graded metrics strictly against the instructor-provided held-out evaluation set.
> *Here is the Toll:* [Provide your committed `protocol.md` draft with your 8–12 trope/genre or `asr_label_set.yaml` label space].
> *Properties:* My chosen shot sweep $k$ values are $\{0, 1, 3, 5, 8\}$ across $\ge 5$ seeds, and my instruction-tuned model identifier and revision hash (runnable on the pinned CPU DevContainer or under the department API quota with CPU fallback) are [Insert Model ID & Hash].
> Do not write the Hugging Face pipeline code. Help me design the strict formatting constraints, label verbalizers, constrained decoding rules, and output parser to ensure predictions match the label space without hallucinating labels, and state the `predict_proba` validation properties (non-negative probabilities summing to `1.0` within `1e-6` over valid labels) for the grader to check by hand or automatically. Suggest concrete controls for (1) majority-label bias, (2) demonstration-position bias (including permutation), and (3) label leakage.

### [PS 8](../../assignments/homework/ps8_interim_report.md): Interim Report — Risk Red-Team & "Grammarly on Steroids" Synthesis (Due Sat 07 Nov 2026)
> **[PROMPT A — Risk Red-Team & UMAP Audit]** I am writing my [PS 8](../../assignments/homework/ps8_interim_report.md) Interim Report. I need you to red-team my Risk Register and audit my exploratory figure plan (confirming that my ASR or VDB track remains unchanged from [PS 4](../../assignments/homework/ps4_proposal.md) and that all development-split metrics are marked advisory).
> *Here is the Toll:* [Paste your pipeline architecture, UMAP `n_neighbors`/`min_dist` sweep parameters, MP 7 baseline numbers, and list of 3 initial risks].
> *Properties:* My annotation plan for the final project targets [50–200] labeled examples, and my team size requires [IAA protocol / solo $\le 1\%$ validation fraction].
> Attack my architecture: identify at least two omitted failure modes specific to my pipeline (including automatic fallback to the pinned CPU DevContainer baseline and local Whisper/free-tier execution if API or compute quotas are exhausted) to bring my Risk Register to $\ge 5$ quantified risks, verify that my component versions match the pinned Docker manifest, and check that my 3 exploratory figures comply with Wilke Part II.
>
> **[PROMPT B — "Grammarly on Steroids" Synthesizer]** You are an academic technical editor. I am providing my original bullet points, raw data schemas, validation properties, and experimental outputs below. Synthesize this into formal, concise academic prose for Section [X] of my [PS 8](../../assignments/homework/ps8_interim_report.md) Interim Report. Do NOT add new claims, invent data, hallucinate citations, or alter my original intellectual intent.
> *[MY ORIGINAL INPUT]:* [Paste your raw bullet points/tables/validation excerpts here]

### [MP 9](../../assignments/machine_problems/mp9_rag_classification_gold_standard.md): Gold Codebook, Weak Supervision & Cohort Convolutions Tollbooth (Due Mon 16 Nov 2026)
> **[PROMPT]** I am working on [MP 9](../../assignments/machine_problems/mp9_rag_classification_gold_standard.md). I need to refine my human annotation codebook and design weak-supervision labeling functions and cohort convolution checks.
> *Here is the Toll:* [Paste your draft codebook decision rules, 3 human-labeled boundary examples from your gold set, and your ordered cohort axis definition (`release_decade` or event-time window index)].
> Do NOT assign gold labels for me (`source=gold` must be human-assigned, and my `gold_raw.csv` / `gold_raw.jsonl` file is capped at a maximum of 50 data objects or 2 hours of effort, for the grader to check by hand or automatically). Critique my codebook for ambiguous boundary cases on the 20-object partner overlap (`overlap_ids.txt`), help me specify heuristic labeling functions and vote aggregation for the $\ge 1,000$-chunk silver pool (explicitly tagged `source=silver`), and verify the boundary-handling math for convolving per-cohort trope frequency vectors with the smoothing kernel `[0.25, 0.5, 0.25]` and first-difference kernel `[-1, 1]` (plus the learned 1-D PyTorch conv kernel comparison if CIS 731).

### [MP 10](../../assignments/machine_problems/mp10_interpretability_metrics.md): Interpretability Harness, Calibration & BH Inference Tollbooth (Due Wed 25 Nov 2026)
> **[PROMPT]** I am working on [MP 10](../../assignments/machine_problems/mp10_interpretability_metrics.md). I need to verify my metric derivations, validation properties for `evaluate(model, X, y)`, calibration setup, and multiple-testing family on my adjudicated [MP 9](../../assignments/machine_problems/mp9_rag_classification_gold_standard.md) gold set.
> *Here is the Toll:* [Paste your confusion matrix, draft imbalance counterexample where Accuracy and Macro-F1 rank two models oppositely, and your pre-registered family of $\ge 6$ comparisons].
> Verify my hand derivations for micro/macro/weighted F1, P@$k$, Recall@$k$, MRR, nDCG@$k$ (and NIST OpenASR 2020 WER if ASR track). State the validation properties on `evaluate(model, X, y)` for the grader to check by hand or automatically (confirming that bounded metrics lie in $[0, 1]$ and confusion-matrix entries sum to $n$), check my experimental design for 10/15-bin ECE calibration and paired bootstrap ($B \ge 10,000$) / McNemar's test with Benjamini–Hochberg FDR control, and help me structure the silver-pool CI-width vs. $n$ power analysis.

### [PS 11](../../assignments/homework/ps11_ethics_storytelling_dashboards.md): Ethics Audit, 5-View Wilke Storyboard & Limitations Panel Tollbooth (Due Fri 04 Dec 2026)
> **[PROMPT]** I am working on [PS 11](../../assignments/homework/ps11_ethics_storytelling_dashboards.md). I need to audit my pipeline for concrete ethical/provenance risks and design an audience-specific 5-view dashboard storyboard that runs in the pinned CPU DevContainer image.
> *Here is the Toll:* [Paste your PS 8 provenance table, PII classes and redaction/retention policy, target audience + decision + 1-sentence 'so what', and draft 5-view storyboard].
> Critique my audit to ensure zero generic 'bias/privacy' fluff: verify concrete analysis of `license_class` (`{public_domain, instructor_provided}`) and stream-whitelist compliance, confirm that no song lyrics or copyrighted text are reproduced beyond instructor-provided excerpts (for the grader to check by hand or automatically), and evaluate ecological fallacy (release decade $\ne$ audience demographics), survivorship/selection bias, ASR dialect WER disparity, and prompt-injection/hallucination mitigations. Audit my 5 storyboard views against Wilke Part II (accessible palettes, direct labeling, CI display, and limitations panel fields).

### [HW 12](../../assignments/homework/hw12_final_deliverables.md): Final MLOps Reproducibility (`make verify`), MLflow Lineage & Drift Runbook Tollbooth (Due Mon 14 Dec 2026)
> **[PROMPT]** I am assembling [HW 12](../../assignments/homework/hw12_final_deliverables.md) (`hw12-final`). I need an end-to-end integration audit across [MP 5](../../assignments/machine_problems/mp5_structured_streaming.md)–[PS 11](../../assignments/homework/ps11_ethics_storytelling_dashboards.md), `make verify`, MLflow tracking, and my serving/drift runbook.
> *Here is the Toll:* [Paste your `Makefile` `verify` target, MLflow logged parameters/metrics/hashes, 50–200 gold-standard range-gate summary, and PSI/KS drift-monitoring threshold].
> Audit my package for reproducibility gaps (for the grader to check by hand or automatically): verify that `make verify` checks the pinned container digest and dependency lockfile, validates all data/metric properties and the 50–200 labeled-example gold-standard range gate (with 2-way/3-way IAA for teams or $\le 1\%$ validation fraction for solo projects, and zero Yelp or SEC-filing data), and reproduces every headline metric on the pinned CPU DevContainer baseline. Check that every number in `REPORT.pdf` traces to an MLflow run export and that my serving path and PSI/KS drift runbook are complete.

---

## 5. THE "KEEP MOVING" AFFORDANCE (ACTION BRANCHES)
Append this block to any prompt when you want concrete, meta-cognitive next steps:

```text
[ACTION BRANCHES REQUIREMENT]
Do not end with a generic question. Provide exactly three [ACTION BRANCHES] for me to choose from:
- [OPTION A] - Broaden the literature/documentation based on my domain.
- [OPTION B] - Deepen the math/logic check on a specific schema or statistical assumption I provided.
- [OPTION C] - Generate an explicitly bounded verification test case for my architecture.
```

---

## 6. HYDRATION & SPECIFICATION GUARD (INSTRUCTOR / TA / AI MAINTENANCE POLICY)
When updating this kit, editing assignment Markdown files, or hydrating course pages into Canvas HTML (even when only a partial subset of course files is attached in context), all human editors and generative AI nodes MUST enforce the following four translation guards:

1. **No Programming-by-Contract Library Leakage:** Do not reference third-party contract-programming libraries (such as Python `deal`), pre/post-condition decorators, or formal requirement-to-specification syntax used by the instructor during course authoring. Those belong strictly to the instructor's internal specification harness, not to student assignment requirements.
2. **No Opaque Invariant Numbers:** Never emit bare or parenthetical invariant identifiers (e.g., `INV-1` through `INV-21`) in student-facing prose, prompts, rubrics, or HTML callouts.
3. **Self-Contained Qualitative Substitution:** Whenever a course invariant applies, replace the identifier with the complete, self-explanatory qualitative requirement from [`term_project_invariants.md`](./term_project_invariants.md) so the student-facing document is 100% self-contained.
4. **Standard Grader Verification Phrasing:** If a property is deterministically checkable (such as row-count ceilings, schema conformance, probability simplex bounds, or lockfile/digest matches), describe the expected property in plain language followed by **"for the grader to check by hand or automatically"**, allowing the instructor, TA, and autograder to populate test assertions without coupling student submissions to a formal specification language.
