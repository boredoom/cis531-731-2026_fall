<!-- ASSIGNMENT-META
id: PS 11
phase: Phase 5: Interpret, Present & Deploy
module: Module 11: Presenting Results (Ethics, Data Storytelling, Dashboards)
released: Wed 25 Nov 2026
due: Fri 04 Dec 2026
prev: assignments/machine_problems/mp10_interpretability_metrics.md
next: assignments/homework/hw12_final_deliverables.md
-->
# PS 11: Ethics, Data Storytelling, & Dashboards
**Provenance and representational-harm audit, plus an audience-specific dashboard specification with a working prototype**

**🗓️ Released:** Wed 25 Nov 2026 | **📅 Due:** Fri 04 Dec 2026 | **💯 Points:** 100 | **👥 Team:** Individual

> **🚨 CRITICAL SUBMISSION POLICY**
> **Dead Week Boundary and Lyric Reproduction:** Due before Dead Week (Mon 07 – Fri 11 Dec 2026); no new homework is assigned in Dead Week. Do not reproduce song lyrics or copyrighted text beyond instructor-provided excerpts in any dashboard or report (INV-9).

## 1. Overview
Audit your own term project for provenance, privacy, representational harm, and LLM/pipeline risk, then specify an audience-specific dashboard and implement a working prototype that consumes your MP 10 outputs (metrics, CIs, calibration, cohort-stratified results). Generic statements about ‘bias’ or ‘privacy’ earn no credit.

Any visualization library you add must be recorded in the lockfile and run in the pinned CPU image (INV-14). **Calendar:** released Wed 25 Nov 2026 during Fall Break (22–29 Nov).

**Required Readings:**
* [Technical Writing Essentials (Last)](https://pressbooks.bccampus.ca/technicalwriting/): audience analysis and document design; presenting data and visuals within an argument.
* [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/): structuring narrative and code cells, Markdown documentation, and exporting notebooks.

**Upstream inputs:** MP 10 results; MP 9 gold set and IAA; PS 8 provenance table; MP 3/MP 5 provenance.  
**Downstream consumers:** HW 12 (ethics and limitations section; dashboard may be linked from the report).

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Risk Inventory:** Compile the provenance, privacy, representational-harm, and LLM-risk inventory from the PS 8 provenance table and the MP 5/MP 10 artifacts.
2. **Audience and Decision Definition:** Name the audience and the decision they must make; write the one-sentence ‘so what’.
3. **Storyboard Generation:** Draft at most 5 views with the AI Kit; revise each against Wilke Part II (accessible palettes, direct labels, uncertainty display).
4. **Prototype Build:** Implement the dashboard as a Jupyter-driven notebook (static HTML export acceptable) that passes restart-and-run-all in the pinned image.
5. **Limitations Panel Review:** Verify the panel shows sources and licenses, uncertainty, known biases, and the last-refresh date.

## 3. Required Document Structure
Your submission must be a **ethics memo PDF (at most 4 pages) delivered with the storyboard and notebook/dashboard export under Git tag `ps11-submission`** containing the following sections exactly as named below. 

* **Provenance, Rights, and Privacy Audit:** `license_class` or whitelist id per source; terms of use for captured broadcast audio; PII classes in call-in speech, redaction method, and retention/deletion policy.
* **Representational Harm and Generational Claims:** Ecological-fallacy risk (release decade is not audience demographics); survivorship and selection bias; ASR error disparity (WER by speaker or dialect group) if your track permits.
* **LLM and Pipeline Risks:** Hallucinated trope attribution and prompt injection through transcript or document text, with a mitigation for each.
* **Audience, Decision, and Storyboard:** Audience, decision, ‘so what’, and a storyboard of at most 5 views (question, encoding, source columns, refresh cadence).
* **Dashboard Prototype and Limitations Panel:** Prototype description, reproducibility evidence (restart-and-run-all), and the limitations and provenance panel.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (100 Points Total)

This assignment is worth 100 points total.

**Part 1: Ethics Audit (50 pts)**
* **Provenance, rights, and privacy (20 pts):** Specific analysis tied to your data; concrete redaction and retention policy.
* **Representational harm (15 pts):** Ecological fallacy, selection bias, and ASR disparity analyzed concretely.
* **LLM and pipeline risks (15 pts):** Risks and mitigations are specific and defensible.

**Part 2: Dashboard (45 pts)**
* **Storytelling and audience fit (15 pts):** Clear audience, decision, and ‘so what’; storyboard supports the argument.
* **Visual design and uncertainty display (15 pts):** Accessible palettes, direct labeling, and CIs shown.
* **Prototype reproducibility and limitations panel (15 pts):** Restart-and-run-all passes; panel shows provenance, bias, and refresh date.

* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [MP 10: Data Science Interpretability & Metrics Scoring](../machine_problems/mp10_interpretability_metrics.md) | [[All Assignments]](../README.md#schedule) | [HW 12: Final Project Deliverables (Mandatory Milestone)](hw12_final_deliverables.md) |

[🏠 Course Home](../../README.md) · [⬆️ Module](../../modules/module_11/README.md) · [⏫ Phase](../../phases/phase_05/README.md)
