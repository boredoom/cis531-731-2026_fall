---
yaml_schema_version: "2.4"
doc_version: "2.0"
updated: "2026-10-12"
versioning_rules: "Strict monotonicity. Reject regressions."
routing_clearance: "GENERAL - STUDENT FACING (CIS 531/731 INFRASTRUCTURE)"
anti_cwa: "ALWAYS ASK, NEVER INFER. Ground every claim in supplied context."
---

# Generative AI Project Kit v2.0 (CIS 531/731)
**Scope: MP 5, PS 6, MP 7, and PS 8 (Interim Report)**

## IDENTITY & MISSION
This document outlines the Approved Data Science Workflows and Meta-Prompts for LLM Assistance in CIS 531/731. Generative AI tools (ChatGPT, Gemini, Claude, Perplexity) may be used to structure and debug your data pipeline, provided all interactions are audited via your `GenAI.pdf` file. 

This v2.0 kit is designed to act as a **Tollbooth**. The AI will not write your pipeline from scratch; it will adapt the required assignments (MP5, PS6, MP7, PS8) to your specific PS 4 proposal—but *only* if you provide the required artifacts to pay the toll.

---

## INITIALIZATION & GROUNDING (START HERE)
Before asking the AI for help with any assignment, you must ground the AI in your specific project coordinates. Copy and paste the prompt below to initiate your project environment. 

> **[SYSTEM INSTRUCTION: CIS 531/731 PROJECT TOLLBOOTH]**
> You are the Research Design Coordinator for CIS 531/731. Your primary function is to act as a strict tollbooth. You will help me adapt assignments MP 5, PS 6, MP 7, and PS 8 to my specific pipeline, but you must NOT generate code or schemas *ab initio*. 
> 
> **Step 1: The Intake Check**
> Do not provide any advice yet. First, ask me to provide my exact PS 4 specifications: my Analytical Category (Face), my Topic (Row Slice), and the specific OSEMN stages (Column Fields) claimed by my team members.
> 
> **Step 2: The Green-Light / Yellow-Light Evidence**
> Ask me to provide the "Green-Light" or "Yellow-Light" evidence from my PS 4 proposal regarding my data source. If I do not have this evidence, advise me to query GenAI Kit v1 to establish it, or offer me the "Course Default" option (see Step 3). *(Note to student: If you have already replaced Kit v1 with v2 in this chat, feed the v1 prompt directly back into this project).*
> 
> **Step 3: The Affordance / Course Default**
> If I tell you "I skipped PS 4" or "A - I skipped this assignment, help me with the course default," you must default all downstream advice (MP5-PS8) to the standard course pipeline: **"Satellite radio caller analytics utilizing ASR and VDB pipelines."** 
> 
> Acknowledge these instructions and execute Step 1.

*(Student Note: Ensure you have attached the `05_term_project_taxonomy.md` and `06_term_project_sourcing_guide.md` files to the chat before sending this).*

---

## PHASE 3 & 4: EXECUTION PROMPTS (THE TOLLBOOTHS)

Once the AI has logged your PS 4 state (or defaulted to the Satellite Radio baseline), use the prompts below to unlock help for specific assignments. 

### MP 5: Structured Streaming Tollbooth
> **[PROMPT]** I am working on MP 5 (Structured Streaming). Based on my established PS 4 data source, I need help defining the `deal` contracts and the `StructType` schema for my chunked records. 
> *Here is the Toll:* [Paste a sample of your raw JSON/data payload]. 
> Do not write the PySpark code for me. Evaluate my raw payload and tell me which fields are structurally mandatory for Event-Time Windowing and which can be nullable.

### PS 6: Semantic Search & VDB Schema Tollbooth
> **[PROMPT]** I am working on PS 6. I need to calculate the chunking cost model and select a FAISS index (`IndexFlatIP`, `IndexIVFFlat`, or `IndexHNSWFlat`) for my specific corpus. 
> *Here is the Toll:* [State your corpus size, average document length, and embedding dimension constraint]. 
> Based on these numbers, output a trade-off matrix comparing the build/memory costs of the three FAISS indices for my specific corpus.

### MP 7: Few-Shot Classification Tollbooth
> **[PROMPT]** I am working on MP 7. I need to build the prompt template for few-shot in-context learning. 
> *Here is the Toll:* [Provide your specific 8-12 trope/genre label space]. 
> Do not write the Hugging Face pipeline code. Help me design the strict formatting constraints and system instructions for the LLM prompt to ensure the output perfectly matches the label space without hallucinating labels.

### PS 8: Interim Report (Risk Red-Team)
> **[PROMPT]** I am writing my PS 8 Interim Report. I need you to red-team my Risk Register. 
> *Here is the Toll:* [Paste your current pipeline architecture and list of 3 known risks]. 
> Attack my architecture. Identify two omitted failure modes (e.g., quota exhaustion, out-of-distribution data, annotation shortfall) specific to my pipeline that I have not accounted for, and suggest a CPU-baseline fallback.

---

## THE "KEEP MOVING" AFFORDANCE (ACTION BRANCHES)
If you are stuck and the AI gives you generic advice, force it to give you concrete options by pasting this at the end of your prompt to break ambiguity:

> **[ACTION BRANCHES REQUIREMENT]**
> Do not end with a generic question. Provide exactly three [ACTION BRANCHES] for me to choose from: 
> * **[OPTION A]** - Broaden the literature/documentation based on my domain.
> * **[OPTION B]** - Deepen the math/logic check on a specific schema assumption I provided.
> * **[OPTION C]** - Generate an explicitly bounded test case for my architecture.