# PS 4: Self-Service Feedback & Iteration Guide

**Repository Path:** `admin/policies/ps4_self_service_feedback_guide.md`
**Version:** 1.1

This guide provides the necessary infrastructure to generate rigorous, rubric-aligned feedback on your PS 4 Term Project Proposal and execute pipeline feasibility audits.

## 1. Establish Your GenAI Kit v2 Workspace
To prevent context amnesia and "knowledge piñata" exploitation, you must set up a persistent AI workspace. 
* Follow the instructions in the [Generative AI Kit v2 How-To](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/policies/generative_ai_kit_howto_v2.md) to initialize your platform. 
* Copy the full system instructions from the [Generative AI Kit v2](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/policies/generative_ai_kit_v2.md) and paste them into your project's custom instructions or system prompt field.

## 2. Prime the Workspace (The TBox)
Your workspace must be strictly grounded in the course ontology (the TBox). Upload the following raw Markdown files directly to your project's knowledge base:
* [04_term_project_guidelines.md](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/04_term_project_guidelines.md)
* [05_term_project_taxonomy.md](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/05_term_project_taxonomy.md)
* [06_term_project_sourcing_guide.md](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/06_term_project_sourcing_guide.md)

## 3. Grounding Specialized Auditor Personas
To execute objective self-critique, we have adapted three specialized KDD Lab personas for CIS 531/731. You will load these instructions into secondary AI windows (like Claude or Perplexity) to audit your pipelines.

* **Claude Critical Review Coordinator**
  * **Public Repo Path:** `admin/policies/prompts/claude_critical_review_coordinator.md`
  * **Role:** Evaluates your PS 4 proposal text against the course rubric. It operates exclusively on the text you supply; if it requires external verification, it will halt and output `[RETRIEVAL REQUIRED]` rather than hallucinating.
* **Perplexity Project Lifecycle Coordinator (PLC)**
  * **Public Repo Path:** `admin/policies/prompts/perplexity_project_lifecycle_coordinator.md`
  * **Role:** Adapted from the lab's research coordinator to explicitly govern the PS 4 to HW 12 OSEMN pipeline. It enforces the "Anti-Spooning Stick" (requiring a 1-sentence hypothesis before analyzing literature) and the "Systems Thinking Carrot" (requiring a defined impact metric before designing pipelines).
* **Perplexity Systems Engineering Auditor (SEA)**
  * **Public Repo Path:** `admin/policies/prompts/perplexity_systems_engineering_auditor.md`
  * **Role:** Adapted to evaluate data science pipelines, dataset APIs, and PySpark/Databricks scaling. It conducts adversarial interoperability audits backed by official documentation to identify rate limits, schema variation, and ingestion bottlenecks.

## 4. Team Composition & Greenlight Stipulations
When using the specialized auditor personas to evaluate your proposal, your project's approval is strictly governed by your team's enrollment track. You must ensure your project meets these conditions before proceeding:

1. **CIS 531-Only Teams:** Your project will only be greenlit if the AI kit returns a "Golden Path" (Tier 1) result on your data sourcing plan.
2. **CIS 731-Only Teams:** There must be no "Tarpit" (Tier 3) or indeterminate results; only green (Tier 1) and yellow (Tier 2) sources are permitted. Furthermore, when applying the rubric, each edition of the AI kit must be prompted to require best practices for implementing any "yellow" OSEMN stages for which the 731 student is responsible.
3. **Mixed 531/731 Teams:** Every OSEMN stage associated with a "yellow" (Tier 2) data source MUST have a 731 student explicitly responsible for it.

## 5. Execution Prompts

### a) Maintaining State Across Platforms
When using the Perplexity PLC or SEA personas to discover data sources or audit code, **you must attach the raw output from those queries back into your main GenAI Kit v2 workspace** to maintain project continuity.

### b) Generic Sourcing Prompt (For the Perplexity PLC)
*Use this in Perplexity to advance your literature or pipeline design while satisfying the Tollbooth constraints.*
```text
I am proposing an OSEMN data science pipeline. 
[ANTI-SPOONING TOLL]: I hypothesize that the core gap in current baseline models for this dataset is [Insert 1-Sentence Hypothesis]. 
[SYSTEMS THINKING TOLL]: The impact metric of my system is [Insert Metric], which matters because [Insert Scientific Gap]. 

Based on this, evaluate my proposed pipeline design for the Scrub and Explore stages, and provide exactly three [ACTION BRANCHES] for me to choose from to advance the pipeline.
```

### c) Prompt to Generate a Custom PLC Query (For GenAI Kit v2)
*Use this in your main GenAI Kit v2 workspace to generate a tailored version of prompt (b).*
```text
I have attached the feedback on my PS 4 proposal from the Claude Critical Reviewer (or the PI). My team composition is [CIS 531 Only / CIS 731 Only / Mixed]. 

Based on this feedback, the course taxonomy, and the Team Composition Greenlight Stipulations, generate a strict sourcing prompt for the Perplexity Project Lifecycle Coordinator. 

Ensure the generated prompt explicitly:
1. Includes my 1-sentence hypothesis to unlock the Summary Function.
2. Includes my impact metric justification to unlock the Pipeline Design function.
3. Instructs the PLC to enforce the greenlighting rules for my team composition (e.g., verifying 531 teams have a Golden Path source, ensuring 731 students own all yellow-tier OSEMN stages, and demanding best practices for yellow stages).
```

### d) Generic Auditing Prompt (For the Perplexity SEA)
*Use this in Perplexity to validate your datasets and code.*
```text
Conduct an interoperability and feasibility audit on my proposed data source [Dataset/API] and my target data pipeline [PySpark / Databricks / Local]. 

Evaluate API rate limits, schema stability, and PySpark version compatibility. Provide a structured Markdown interoperability matrix and an adversarial audit identifying potential integration bottlenecks for the Obtain and Scrub stages. Ground all claims in official API documentation.
```

### e) Prompt to Generate a Custom SEA Query (For GenAI Kit v2)
*Use this in your main GenAI Kit v2 workspace to generate a tailored version of prompt (d).*
```text
I have attached my PS 4 feedback. Based on my identified Tier 1/Tier 2 data source and my assigned OSEMN tasks, generate an auditing prompt for the Perplexity Systems Engineering Auditor. 

The prompt must direct the SEA to:
1. Evaluate the specific API limitations, Python library versioning requirements, and data ingestion bottlenecks unique to my proposed architecture.
2. Explicitly apply the Greenlight Stipulations for my [CIS 531 Only / CIS 731 Only / Mixed] team composition, verifying that any "yellow" source stages are properly assigned to 731 students and accompanied by best practices.
```