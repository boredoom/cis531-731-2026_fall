---
document_title: "Feedback Rubric: PS 4 Term Project Proposal (CIS 531/731)"
document_version: "1.0"
document_last_updated_date: "2026-10-16"
status: "ACTIVE"
---

# 🧭 RUBRIC: PS 4 Term Project Proposal (CIS 531/731)

**Scope Guard:** This rubric evaluates whether the student has successfully defined a feasible Data Science system architecture explicitly aligned with the course taxonomy and data sourcing constraints. 

## 📊 Evaluation Criteria & Scoring Weights (35-Point Scale)
*Note: The 30 points map to the formal assignment requirements. 5 points are allocated for class participation.*

### [1] Taxonomy Alignment & Scope Definition (10 Points)
*Does the proposal explicitly anchor to the 3x5x5 data cube?*
* **0-3 pts (Fatal):** The problem statement is vague. No specific Analytical Category or Topic/Media type is identified, or the chosen combination contradicts the taxonomy rules.
* **4-7 pts (Standard):** Identifies a Category and Topic, but the proposed task bridges multiple domains without a clear primary focus or target output.
* **8-10 pts (Sovereign):** Clearly and explicitly names exactly ONE Analytical Category (Prescriptive, Descriptive, Predictive) and exactly ONE Topic/Media type. The problem statement defines a concrete data science task.

### [2] Data Sourcing & Feasibility (Obtain Stage) (10 Points)
*Are the dataset and toolchains verified, realistic, and explicitly documented?*
* **0-3 pts (Fatal):** No specific data source is named (e.g., "We will scrape the web"). Proposes an unmitigated Tier 3 Tarpit (e.g., unbounded social media scraping or raw STAC imagery) without a detailed feasibility/fallback plan.
* **4-7 pts (Standard):** Names a source, but fails to estimate scale, lacks an authentication plan, or fails to define the raw landing format.
* **8-10 pts (Sovereign):** Explicitly identifies a Tier 1 or Tier 2 source (e.g., Databricks samples, Hugging Face). States the raw landing format (JSON, CSV, Parquet) and Bronze destination. Provides an explicit plan for handling authentication/API limits.

### [3] Proposed Methodology & OSEMN Pipeline (5 Points)
*Is the methodology mathematically/architecturally sound, and are team responsibilities partitioned?*
* **0-1 pts (Fatal):** The methodology reads like a narrative goal rather than a technical pipeline. Fails to define a "Method 1" simple baseline. For teams: responsibilities are vague.
* **2-3 pts (Standard):** Baseline is mentioned but not clearly defined. OSEMN pipeline stages (Obtain, Scrub, Explore, Model, iNterpret) are not fully assigned to specific members.
* **4-5 pts (Sovereign):** Explicitly defines the "Method 1" (simple/naive) fallback model. Details execution plans for the Scrub, Explore, Model, and iNterpret stages. For teams: explicit partitioning of 1-2 OSEMN stages to specific members. For solos: clear identification of automated stages.

### [4] GenAI Audit (5 Points)
*Is the GenAI telemetry verifiable?*
* **0 pts (Fatal):** Neither a `GenAI.pdf` log nor an explicit "No GenAI Used" statement is included.
* **5 pts (Sovereign):** Includes the required `GenAI.pdf` log detailing specific execution prompts (e.g., Systems Engineering Audit) OR explicitly states "No GenAI Used."

### [5] Class Participation (5 Points)
*Did the student complete the required participation gate?*
* **0 pts (Fatal):** Did not complete the required class participation exercise.
* **5 pts (Sovereign):** Successfully completed the required class participation exercise.
