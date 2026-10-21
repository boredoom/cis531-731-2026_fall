---
yaml_schema_version: "2.1"
document_version: "1.0"
document_last_updated_date: "2026-10-12"
document_monotonicity: "REQUIRED"
---

# Term Project Guidelines
**Design, Implementation, and Evaluation of a Data Science System**

## 🎯 Architecture & Grading Structure
The Term Project is the capstone of this course. It is evaluated via a dual-grading structure worth a total of **390 points**:

*   **Process Milestones (90 pts):** You earn assignment points for successfully completing the mandatory milestones on time: PS 4 (Proposal), PS 8 (Interim Report), and HW 12 (Final Submission). Each is worth 30 points.
*   **Substance Evaluation (300 pts):** Your final deliverables (the report, the code, and the presentation) are evaluated holistically against a 300-point technical rubric at the end of the semester.

> **The Canonical Taxonomy:** To ensure academic rigor, every project must be explicitly defined across two dimensions: a Category Track and a Methodological Pillar. Review the approved combinations in the `05_term_project_taxonomy.md` file.

## 👥 Teaming Protocols

**Phase 1 & Phase 2: Individual Process Milestones**
*   Even if forming a team (max 3), **EACH** member must submit their own document for the early milestones (PS 4 and PS 8) to earn process points.
*   Teammates may share a jointly developed problem statement, introduction, and background. However, your Methodology, Milestones, and Results sections **must** distinctly detail your individual role and expectations.

**Phases 3, 4, & 5: Unified Team Deliverables**
*   **Presentations:** You will prepare a unified team presentation, with all members taking turns presenting.
*   **Final Submission:** Your team will produce a unified final report and codebase. All members will submit the same URL to a unified GitHub archive shared with the instructor for the HW 12 submission.

---

## Phase 1: Project Proposal (Completed)
*The PS 4 Proposal milestone is now complete. If you are modifying your project scope or changing tracks, you must consult the instructor immediately.*

**💡 Bring Your Own Data / Domain (BYOD)**
If you are proposing a custom domain or bringing your own dataset for a project pivot, your concept must still map strictly to the course framework. Consult the `06_term_project_sourcing_guide.md` and use the **Phase 1 prompts** in the `generative_ai_kit_v2.md` to evaluate your idea. You can feed the AI your BYOD summary and explicitly ask it to verify whether your dataset and task fit crisply into the intersection of an existing Category Track and Methodological Pillar.

---

## Phase 2: Interim Report
The Interim Report evaluates your process, methodology, and initial data pipeline. It is conducted via the PS 8 milestone. You are required to demonstrate a working data ingestion pipeline and a functioning "naive" baseline model.

**🤖 Generative AI Usage & Meta-Prompting**
For the Interim Report, generative writing is allowed under one strict condition: the LLM must be acting as a synthesizer of your original thoughts. You must provide the model with non-generative input—such as your own written specifications, architectural design choices, raw data outputs, or specific literature search results. You may not simply ask the model to "write an interim report based on my proposal." Your AI Audit (`GenAI.pdf`) must explicitly state what original inputs you provided to guide the generation.

See `generative_ai_kit_v2.md` for specific execution prompts tailored to the Interim Report.

---

## Phase 3: Experimentation & Rigorous Evaluation
Once your interim baseline is established, the core computational work of the project begins. You must empirically demonstrate that your proposed architecture or algorithm represents a statistically significant improvement (or meaningful trade-off) compared to your baseline.

> **⚠️ Critical Path Warning**
> **Do NOT wait for the HW 12 (Final Report) assignment to open before beginning Phase 3.** Training models, tuning hyperparameters, and running cross-validation takes significant compute time. Both your Final Presentation and Final Report rely entirely on the data generated during this phase. Begin your comparative training runs immediately after submitting PS 8.

**Model Evaluation & Statistical Testing**
A qualitative assertion that "Model B looks better than Model A" will result in a heavy penalty on your final rubric. You must formally define and test your empirical results. 

*   **Hypothesis Formalization:** Formulate a formal statistical hypothesis for your comparison (e.g., the null hypothesis *H0*: Model A and Model B have equivalent performance on the test distribution).
*   **Statistical Testing:** Utilize an appropriate statistical test to evaluate your hypotheses (e.g., a paired t-test, McNemar's test for classification, or Wilcoxon signed-rank test).

---

## Phase 4: Final Project Presentations
All teams must deliver a unified, live oral presentation of their system, taking turns to present. Your presentation should clearly articulate your problem, your methodological pillar, the statistical evaluation of your baseline comparison, and a live demonstration or visualization of your results.

**Standard Reflection Questions**
In your presentation slides, **EACH** team member must individually answer the following three standard questions:
1. What aspect of data science/machine learning did you find most technically challenging in completing this term project?
2. What aspect of data science/machine learning do you think you learned the most about over the course of the project?
3. What is your top priority for future work, if you were to continue this project as a research project or in independent study?

**📅 Scheduling Protocols**
*   **Early Presentations (Extra Credit):** Thursday of Week 15 through the Sunday prior to Dead Week.
*   **Standard Presentations:** Dead Week (Week 16).
*   **Finals Week (Week 17):** NO presentations will be scheduled during Finals Week unless previously permitted due to an OSSA-confirmed accommodation or special circumstances. All exceptions must be requested and approved in writing before the end of Week 16.

---

## Phase 5: Final Report & Source Code
Your unified final deliverables will be submitted via the HW 12 assignment portal. These artifacts form the bulk of your 300-point substance grade. 

*   **The Report:** Must be formatted strictly using the standard double-column IEEE or ACM conference proceedings template. The text must be 6 to 8 pages in length (excluding references) and contain standard sections: Abstract, Introduction, Background/Related Work, Methodology, Experiments & Results (including your Phase 3 statistical hypotheses), and Conclusion.
*   **The Code:** Must be hosted in a unified team repository (e.g., GitHub) accessible to the instructor. All members will submit the same URL to this archive, and the repository **must be shared with the instructor (@banazir on GitHub)**. It must contain a comprehensive `README.md`, a requirements file (e.g., `requirements.txt` or `environment.yml`), and reproducible scripts.