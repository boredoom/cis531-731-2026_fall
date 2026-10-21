# CIS 531/731 Term Project: Requirements, Topics, and Deliverables (Fall 2026)

## 1. Requirements and Assignment Milestones
The term project is the capstone of this course and requires you to synthesize the data science foundations and toolchains (PySpark, Databricks, Hugging Face, LLMs) learned this semester. It consists of the following graded components:

1. **Proposal Draft:** Class participation — post as a plain text comment to the Canvas discussion.
2. **Formal Proposal (PS 4):** Assignment (1-2 pages) — submit as a PDF.
3. **Interim Update:** Class participation — short update documenting baseline data ingestion, pipeline setup, and any changes.
4. **Presentation Slides:** Assignment — submit as PowerPoint, PDF, impress.js, or Prezi file.
5. **Final Report:** Assignment (4-6 pages) — submit as a PDF formatted in APA, AAAI, IEEE, or ACM style.
6. **Code, Data, and Models:** Assignment — submit a manifest linking to a Git repository containing your data pipeline codebase and notebooks (contents must remain available through the grading period).
7. **Generative AI Audit (GenAI.pdf):** Assignment — submit a log of all AI interactions per the *CIS 531/731 GenAI Project Kit*.

---

## 2. Term Project Taxonomy: The 3x5x5 Data Cube
Your project must be mapped onto the course's 3x5x5 Data Cube taxonomy. You must select exactly one analytical category, one topic/media type, and map your work across the OSEMN pipeline.

### Dimension 1: The 3 Analytical Categories (The Goal)
1. **Prescriptive Analytics (RecSys/IR):** Systems that recommend actions, retrieve specific knowledge (RAG), or automate decision-making based on constraints.
2. **Descriptive Analytics (InfoVis/Storytelling):** Systems that expose hidden patterns, generate dashboards, map generational drift, or summarize vast corpora.
3. **Predictive Analytics (Classification/Forecasting):** Systems that classify entities (KYC/AML), predict future states (time series), or identify anomalies.

### Dimension 2: The 5 Topics / Media Types (The Input)
1. **Time-Series / Sequential Data:** Financial logs, weather/climate sensors, IoT telemetry, server/traffic logs.
2. **Spatial / Georeferenced Data:** Epidemiological maps, check-in data, logistics routing, remote sensing features.
3. **Text Corpora:** E-books, conversational transcripts, LLM logs, product reviews, historical archives.
4. **Multimedia (Audio/Visual):** ASR streams, caller speech, video captions, music information retrieval (MIR).
5. **Structured/Relational Data:** Complex database queries, web service/API streams, graph network architectures.

### Dimension 3: The 5 OSEMN Tasks / Stages (The Execution)
1. **Obtain:** Data Ingestion & Extraction (e.g., PySpark streaming, API fetching).
2. **Scrub:** Cleaning & Chunking (e.g., normalizing values, recursive character chunking).
3. **Explore:** EDA & Feature Engineering (e.g., UMAP/t-SNE visualizations, dashboarding class distributions).
4. **Model:** Machine Learning & Pipelines (e.g., XGBoost, Hugging Face Transformers, Vector Databases).
5. **iNterpret:** Evaluation & Data Storytelling (e.g., calculating ROC-AUC, BLEU scores, synthesizing Streamlit dashboards).

---

## 3. Specific Recommendations (Do's and Don'ts)

* **Data at Scale:** The objective is to study PySpark-based OSEMN pipelines handling data at scale. Projects must target gigascale to terascale storage: notionally **1e3 to 1e5 multimedia documents** (e.g., social media video posts) or **1e4 to 1e6 data objects** (e.g., tweets, Reddit posts, Amazon market baskets, anti-fraud transactions).
* **Ground Truth Requirements:** For supervised learning (including supervised fine-tuning), ground truth data *must* be available. If semi-supervised or self-supervised learning is used, models should support few-shot inference. 
* **No Human Annotation:** Human annotation by the student team must NEVER be the source of gold standard data. Pre-annotated datasets may be used with instructor approval, provided a silver standard approach for prelabeling unlabeled instances is feasible.
* **Team Execution:** Teams must explicitly claim 1-2 specific OSEMN stages per member to build natively. You must automate or mock the pipeline stages you do not explicitly claim.
* **CIS 731 (Graduate Level):** 731 students must complete at least 1/3 more work than 531 students. You must define at least one baseline approach and one advanced alternative treatment (e.g., comparing a standard TF-IDF baseline against an advanced semantic embedding model).

---

## 4. Proposals & Rubrics

### Proposal Structure (PS 4 - 1 to 2 Pages)
Your proposal must strictly contain the following sections:
* **Title & Team:** Project title and names of all team members (1-3 max).
* **Taxonomy Alignment:** Explicitly list your target Category (Prescriptive, Descriptive, Predictive) and Topic/Media (Time-Series, Spatial, Text, Multimedia, Structured).
* **Problem Statement:** What specific problem are you solving?
* **Data Sourcing (The Obtain Stage):** Name your Tier 1 or Tier 2 source, identify the raw landing format (JSON, CSV, Parquet), and state how you will handle APIs/authentication.
* **Proposed Methodology (The OSEMN Pipeline):** Detail how you will execute the Scrub, Explore, Model, and iNterpret stages. Detail which 1-2 stages each team member is responsible for. Define your "Method 1" (simple/naive) fallback model.
* **GenAI Audit:** Include your `GenAI.pdf` log or explicitly state "No GenAI Used."

### Grading Rubric Overview
* **Proposal:** Scope & Alignment (10 pts), Feasibility Check (10 pts), Clarity & Format (5 pts), GenAI Verification (5 pts).
* **Interim Update:** Class participation plus discretionary points for progress and substance.
* **Presentation:** Slide prep (20%), delivery/clarity (20%), live demo/dashboard effectiveness (20%), answers to standard questions (20%), discussion/thought-provoking points (20%).
* **Overall Deliverable:** Originality (20%), functional pipeline/demo (20%), completeness of proposed features (20%), evaluation metrics/results (20%), writeup quality (20%).

---

## 5. Frequently Asked Questions (FAQ)

**Q: How many students may work on a team?**
A: 1-3 students.

**Q: Are teams allowed to turn in a single assignment as joint work?**
A: Yes, but for the interim and final milestones only. Separate project proposals sharing *only* the Problem Statement are required from each member of a team. Each of the other proposal sections must be independently written to ensure a reasonable division of accountability. 

**Q: Are 531 and 731 students allowed to be on the same team?**
A: Yes. 731 students are expected to be responsible for any 731-only content in the proposal (e.g., implementing advanced SOTA baselines) and must do at least 1/3 more work.

**Q: What is your policy on ChatGPT and generative AI?**
A: See the official **CIS 531/731 Generative AI Project Kit** in the syllabus. All AI use must be logged, and generative code must be anchored by your own baseline logic and mathematical understanding.

**Q: Our team wrote our proposal together. How should we split these to form individual proposal documents?**
A: Finalize your shared Problem Statement. Then, name specific facets of the OSEMN pipeline that belong to each team member (e.g., Student A handles Obtain/Scrub; Student B handles Model/iNterpret). Write your Data Sourcing and Proposed Methodology sections tailored specifically to your individual subsystem.
