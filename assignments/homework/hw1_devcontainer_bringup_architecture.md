# HW 1: DevContainer Bring-Up & Term Project Architecture
**PySpark 4 Verification & Multidimensional Matrix Selection**

**📅 Due:** Tue 08 Sep 2026, 11:59 PM CDT | **💯 Points:** 30 | **👥 Team:** Individual or Team (1-3 students)

> **🚨 CRITICAL SUBMISSION POLICY**
> **Semester Foundational Gate:** This assignment locks in your architectural commitments for the term project using the Multidimensional Matrix and verifies your baseline distributed computing setup. (Strict INV-14 environment pinning and hardware probes will follow in MP 2).

## 1. Overview
You must prove your local Docker DevContainer or Beocat cluster access is correctly configured to run PySpark 4 and formally establish your term project team, data track, category, and task allocations.

### Required Readings (Module 0 & 1 Gates)
* **Research Software & Data Principles:**
  * Wilkinson et al.: The FAIR Guiding Principles for Scientific Data Management.
  * Irving et al.: Research Software Engineering with Python.
* **Python & Tooling Foundations:**
  * VanderPlas: Python Data Science Handbook.
  * [Jupyter Documentation](https://jupyter.org/documentation): Environment and Notebook management.

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Environment Setup & Verification:** Initialize your PySpark 4 DevContainer or Beocat environment and verify `SparkSession` instantiation.
2. **Schema & Action Test:** Define a `StructType` schema, instantiate a 3-row DataFrame, and execute `.show()`.
3. **Web UI & Proof Capture:** Launch the Spark Web UI (port 4040) and capture a combined verification screenshot.
4. **Team & Track Selection:** Review the "Guide to Projects by Category, Topic, and Task" matrix and declare your immutable data track.
5. **Matrix Allocation & Problem Statement:** Assign distinct task columns per team member and write a 3–4 sentence pipeline problem statement.

## 3. Required Document Structure
Your submission must be a **single `.zip` archive named `HW1_Firstname_Lastname.zip` containing a `.ipynb` notebook or `.md`/PDF report alongside your verification screenshot** containing the following sections exactly as named below. 

* **Part 1: Environment Verification (30 Points):** Screenshot clearly demonstrating PySpark 4 DataFrame `.show()` output alongside the active Spark Web UI (port 4040).
* **Part 2: Project Architecture & Matrix Selection (70 Points):** Complete answers to the project selection requirements:
  1. **Team Roster & Track:** List team members (1-3 students) and declare your immutable data track (**Track 1: ASR Live Stream** or **Track 2: VDB Text Corpora**).
  2. **Category & Task Allocation:** Specify Category (e.g., Category 2: Descriptive Analytics) and claim one distinct Task column per member (Prediction, Classification, Summarization, Collection Analysis, Retrieval). *Note: No team member may own more than one task. If a task is shared, state who builds the baseline vs. alternative model.*
  3. **Problem Statement:** A 3-4 sentence summary of what your pipeline will do, combining Track, Category, and Task allocations.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (30 Points Total)

This assignment is scored out of 30 total scaled points (representing the 100-point proportioned component weight).

**Part 1: Environment Verification (30 pts)**
* **PySpark 4 & Spark Web UI Proof (30 pts):** Screenshot clearly shows the `.show()` output for a custom schema DataFrame running alongside the active Spark Web UI on port 4040.

**Part 2: Architecture & Matrix Selection (70 pts)**
* **Roster, Track, Category, and Task Allocation (40 pts):** Document includes a valid roster, immutable track selection, valid category mapping, and distinct/compliant task allocations per member.
* **Coherent Problem Statement (25 pts):** A coherent 3-4 sentence project problem statement integrating the track, category, and assigned tasks.
* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.
