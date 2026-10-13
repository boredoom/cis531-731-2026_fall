---
yaml_schema_version: "2.5"
doc_version: "2.1"
updated: "2026-10-12"
versioning_rules: "Strict monotonicity. Reject regressions."
routing_clearance: "GENERAL - STUDENT FACING (CIS 531/731 INFRASTRUCTURE)"
anti_cwa: "ALWAYS ASK, NEVER INFER. Ground every claim in supplied context."
---

# Generative AI Project Kit v2.1 (CIS 531/731)
**Scope: MP 5, PS 6, MP 7, and PS 8 (Interim Report)**

## IDENTITY & MISSION
This document outlines the Approved Data Science Workflows and Meta-Prompts for LLM Assistance in CIS 531/731. Generative AI tools (ChatGPT, Gemini, Claude, Perplexity) may be used to structure and debug your data pipeline, provided all interactions are audited via your `GenAI.pdf` file. 

This v2.1 kit acts as a **Tollbooth**. The AI will not write your pipeline from scratch; it will adapt the required assignments (MP5, PS6, MP7, PS8) to your specific PS 4 proposal—but *only* if you provide the required artifacts and explicitly state your team composition to pay the toll.

---

## 🚨 COURSE POLICY: TEAM COMPOSITION & SCHEMA INFERENCE
Your level of AI access depends on your course enrollment track (531 vs. 731). Before using the Tollbooth prompts, you must abide by the following schema inference rules:

1. **CIS 531 Teams (Undergraduate ONLY):** Must use a verified "Golden Path" (Tier 1) data source from GenAI Kit v1 or the course defaults. CIS 531 teams **must adopt the instructor-provided ontology schema unmodified** (INV-11). You may not use the AI to generate custom schema topologies.
2. **CIS 731 Teams (Graduate ONLY):** A "Real-World API or Benchmark" (Tier 2) source is expected. You **must** utilize the AI to perform schema inference and derive your own custom ontology (class hierarchy, relation types, cardinalities). Reusing the unmodified instructor schema will result in an automatic failure of the contract check.
3. **Mixed 531/731 Teams:** The team is permitted to use Tier 2 sources. However, **any schema inference tasks** during the Obtain, Scrub, and Explore phases must be explicitly claimed and executed by the **CIS 731 members** of the team.

---

## INITIALIZATION & GROUNDING (START HERE)
Copy and paste the prompt below to initiate your project environment. 

> **[SYSTEM INSTRUCTION: CIS 531/731 PROJECT TOLLBOOTH]**
> You are the Research Design Coordinator for CIS 531/731. Your primary function is to act as a strict tollbooth. You will help me adapt assignments MP 5, PS 6, MP 7, and PS 8 to my specific pipeline, but you must NOT generate code or schemas *ab initio*. 
> 
> **Step 1: The Intake Check**
> Do not provide any advice yet. First, ask me to provide:
> a) My exact PS 4 specifications: Analytical Category, Topic, and OSEMN stages claimed.
> b) My team composition (CIS 531 Only, CIS 731 Only, or Mixed).
> 
> **Step 2: The Green-Light / Yellow-Light Evidence**
> Ask me to provide the "Green-Light" or "Yellow-Light" evidence from my PS 4 proposal regarding my data source. If I do not have this evidence, advise me to query GenAI Kit v1 to establish it, or offer me the "Course Default" option (see Step 3). *(Note to student: If you have already replaced Kit v1 with v2 in this chat, feed the v1 prompt directly back into this project).*
> 
> **Step 3: The Affordance / Course Default**
> If I tell you "I skipped PS 4" or "A - I skipped this assignment, help me with the course default," you must default all downstream advice to the standard course pipeline: **"Satellite radio caller analytics utilizing local Whisper ASR transcription and FAISS VDB ingestion."** 
> 
> Acknowledge these instructions and execute Step 1.

*(Student Note: Ensure you have attached the files `04_term_project_guidelines.md`, `05_term_project_taxonomy.md`, and `06_term_project_sourcing_guide.md` to the chat before sending this).*

---

## PHASE 3 & 4: EXECUTION PROMPTS (THE TOLLBOOTHS)

Use the prompts below to unlock help for specific assignments. **You must fill in the bracketed properties before sending.**

### MP 5: Structured Streaming Tollbooth
> **[PROMPT]** I am working on MP 5 (Structured Streaming). Based on my established PS 4 data source, I need help defining the `deal` contracts and the `StructType` schema. 
> *Here is the Toll:* [Paste a sample of your raw JSON/data payload]. 
> *Properties:* My required chunk duration limit is [XX] seconds, and my lateness distribution p95 is [YY] seconds.
> Do not write the PySpark code for me. Evaluate my raw payload and tell me which fields are structurally mandatory for Event-Time Windowing, justify their nullability, and calculate the appropriate watermark delay based on my provided p95 metric.

### PS 6: Semantic Search & VDB Schema Tollbooth
> **[PROMPT]** I am working on PS 6. I need to calculate the chunking cost model and select a FAISS index (`IndexFlatIP`, `IndexIVFFlat`, or `IndexHNSWFlat`) for my specific corpus. 
> *Here is the Toll:* [State your corpus size in MB/GB, average token length per document, and embedding model maximum sequence length]. 
> *Properties:* My team composition is [531/731/Mixed].
> Based on these numbers, output a trade-off matrix comparing the build/memory costs of the three FAISS indices. If my team includes CIS 731 students, help me draft the custom JSON Schema (Draft 2020-12) extending the MP 5 chunk record.

### MP 7: Few-Shot Classification Tollbooth
> **[PROMPT]** I am working on MP 7. I need to build the prompt template for few-shot in-context learning to classify my vector chunks. 
> *Here is the Toll:* [Provide your specific 8-12 trope/genre label space]. 
> *Properties:* My chosen shot sweep *k* values are [e.g., 0, 1, 3, 5], and my instruction-tuned model identifier is [e.g., meta-llama/Llama-3.2-3B-Instruct].
> Do not write the Hugging Face pipeline code. Help me design the strict formatting constraints and system instructions for the LLM prompt to ensure the output perfectly matches the label space without hallucinating labels. Suggest controls to prevent demonstration-position bias.

### PS 8: Interim Report (Risk Red-Team)
> **[PROMPT]** I am writing my PS 8 Interim Report. I need you to red-team my Risk Register. 
> *Here is the Toll:* [Paste your current pipeline architecture and list of 3 known risks]. 
> *Properties:* My annotation plan targets [50-200] examples, and my team size requires [IAA protocol / solo validation fraction].
> Attack my architecture. Identify two omitted failure modes specific to my pipeline that I have not accounted for, and verify that my proposed annotation plan complies with the course scale limits.

---

## THE "KEEP MOVING" AFFORDANCE (ACTION BRANCHES)
If you are stuck and the AI gives you generic advice, paste this at the end of your prompt to break ambiguity:

> **[ACTION BRANCHES REQUIREMENT]**
> Do not end with a generic question. Provide exactly three [ACTION BRANCHES] for me to choose from: 
> * **[OPTION A]** - Broaden the literature/documentation based on my domain.
> * **[OPTION B]** - Deepen the math/logic check on a specific schema assumption I provided.
> * **[OPTION C]** - Generate an explicitly bounded test case for my architecture.
