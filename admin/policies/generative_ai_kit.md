---
yaml_schema_version: "2.3"
doc_version: "1.0"
updated: "2026-10-05"
versioning_rules: "Strict monotonicity. Reject regressions."
routing_clearance: "GENERAL - STUDENT FACING (CIS 531/731 INFRASTRUCTURE)"
anti_cwa: "ALWAYS ASK, NEVER INFER. Ground every claim in supplied context."
---

# Generative AI Project Kit (CIS 531/731)

## IDENTITY & MISSION
This document outlines the Approved Data Science Workflows and Meta-Prompts for LLM Assistance in CIS 531/731. Generative AI tools (ChatGPT, Gemini, Claude, Perplexity) may be used throughout your term project, provided all interactions are strictly audited via your `GenAI.pdf` file. To foster research maturity and prevent "knowledge piñata" exploitation, your use of AI is bound by absolute structural constraints.

## STRICT PROCEDURAL DEPENDENCIES (THE TOLLBOOTHS)

**1. The Anti-Spooning Stick (No Free Summaries)**
You are strictly forbidden from asking an AI to summarize a paper or extract claims UNLESS you provide your own baseline artifact first.
*   **DO NOT ASK:** "Summarize this paper" or "Do a lit review on X."
*   **DO ASK:** "Here is my 1-sentence hypothesis of this paper's core gap. Audit my claim against the text."

**2. The Systems Thinking Carrot (No Free Pipelines)**
Do not chase incremental code fixes without defining the scientific impact. You must provide an impact justification before asking for architectural design.
*   **DO NOT ASK:** "How do I build this pipeline?" or "Write the PySpark code for X."
*   **DO ASK:** "The impact metric of my system is X, which matters because Y. Based on this, help me design the feature extraction architecture."

---

## PHASE 1: PROJECT PROPOSALS & SCOPING
GenAI may be used for **editing, critique, and debugging** only. You may not use it to generate your core intellectual ideas from scratch. Before asking an LLM for help evaluating your proposal, copy and paste this block to ground it in the CIS 531/731 taxonomy.

> **[SYSTEM INSTRUCTION]**
> You are the Research Design Coordinator for CIS 531/731 (Data Science). Provide CRITIQUES ONLY. Do NOT write the proposal, literature review, or pipeline code for me. [COURSE CONTEXT] Apply adversarial self-critique: identify what most efficiently refutes my claim, and what hidden assumptions carry it. Ensure every major assertion is traceable. Evaluate my proposal against these constraints: (1) Mathematical & Technical Soundness, (2) Empirical Rigor (Metrics/Baselines), and (3) Reproducibility.

---

## PHASE 2: THE "GRAMMARLY ON STEROIDS" SYNTHESIS
For your Interim Report, generative writing is allowed under the **"Grammarly on Steroids" policy**. The LLM must act strictly as a synthesizer of *your* original thoughts. You must provide the model with non-generative input (your raw bullet points, architecture choices, or raw DataFrame schemas). **You must include your raw notes in this prompt to receive credit.**

> **[SYSTEM INSTRUCTION]**
> You are an expert technical academic editor. I am providing my original bullet points, raw data schemas, and architectural choices below. Please synthesize this into a formal, concise academic response for my Interim Report. Do NOT add new claims, invent data, hallucinate citations, or alter my original intellectual intent. 
> 
> **[MY ORIGINAL INPUT]** 
> *Section:* [e.g., Methodology / Baselines / Feature Extraction] 
> *My Raw Notes/Data:* 
> - [Insert your first raw thought/fact/schema here] 
> - [Insert your second raw thought/fact/schema here]

---

## PHASE 2 & 3: EXECUTION PROMPT LIBRARY
Use these specific prompts to bulletproof your metrics and evaluate your system. **Always start by attaching your accepted Project Proposal PDF to the chat context.**

### 1. Systems Engineering Audit (Tool Selection)
> **[PROMPT]** You are the Systems Engineering Auditor. Conduct an interoperability audit based on my attached proposal. Compare my proposed data pipeline tools against industry standards. Identify integration bottlenecks, API deprecations, or version mismatches that threaten my architecture. Provide your findings in a structured Markdown interoperability matrix.

### 2. Evaluating Metrics & Baselines
> **[PROMPT]** I am currently using [Insert Metric] to evaluate my model. Are there more robust secondary metrics that are industry-standard for this specific task? What are the most common failure modes, distribution shifts, or biases when evaluating models on this type of data? Help me design a specific baseline test to measure these vulnerabilities.

---

## THE "KEEP MOVING" AFFORDANCE (ACTION BRANCHES)
If you are stuck and the AI gives you generic advice, force it to give you concrete options by pasting this at the end of your prompt to break ambiguity:

> **[ACTION BRANCHES REQUIREMENT]**
> Do not end with a generic question. Provide exactly three [ACTION BRANCHES] for me to choose from: 
> *   **[OPTION A]** - Broaden the literature based on my domain.
> *   **[OPTION B]** - Deepen the math/logic check on a specific assumption I provided.
> *   **[OPTION C]** - Execute the pipeline code based on my specified impact metric.
