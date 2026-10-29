<!--
yaml_schema_version: "2.2"
document_version: "3.0"
document_last_updated_date: "2026-10-29"
-->

<br>

<div align="center">
 <strong>🏫 Active Course Repositories:</strong> &nbsp;
 🏗️ <a href="https://github.com/kddresearch/course-architecture-base">Architecture Base</a> &nbsp;|&nbsp;
 🤖 CIS 530/730 &nbsp;|&nbsp;
 📊 <a href="https://github.com/kddresearch/cis531-731-2026_fall">CIS 531/731</a> &nbsp;|&nbsp;
 📈 CIS 732 &nbsp;|&nbsp;
 🎨 <a href="https://github.com/kddresearch/cis536-736-2026_fall">CIS 536/736</a> &nbsp;|&nbsp;
 👁️ CIS 798 X &nbsp;|&nbsp;
 🧠 CIS 830
</div>

<div align="center">
 <h1>📊 CIS 531/731 - Programming Techniques for Data Science and Analytics</h1>
 <p>
 <strong>Semester:</strong> Fall 2026 | <strong>Instructor:</strong> William H. Hsu<br>
 <strong>Status:</strong> ACTIVE | <strong>Canvas LMS:</strong> <a href="https://k-state.instructure.com/courses/201513">Closed SSO Portal</a>
 </p>
</div>

<hr>

## 📖 Overview

Central repository for CIS 531/731 (Fall 2026) academic execution. This repository manages the DevContainer environments, Machine Problems (MPs), and primary codebase for students learning modern data science programming techniques. 

> **⚠️ Single Source of Truth (SSOT) Notice**
> This repository is the designated SSOT for all public-facing course materials, assignments, and infrastructure. While grades and closed discussions occur in the Canvas SSO environment, all operational state, Machine Problems (MPs), codebases, and structural rubrics MUST be committed here before being mirrored. A non-paywalled HTML mirror of Canvas content is derived from this repository.

<hr>

## 🗂️ Repository Structure

| Directory / File | Description |
| :--- | :--- |
| [`.github/`](.github/) | CI/CD workflows and sync configurations (e.g., `sync_architecture_template.yml`). |
| [`admin/`](admin/) | Course policies and syllabus resources. |
| [`assignments/`](assignments/) | Problem sets (PSs), machine problems (MPs), project milestones, and labs. |
| [`docs/`](docs/) | Supplemental documentation including architecture references, setup instructions, and implementation guides. |
| [`exams_quizzes/`](exams_quizzes/) | Quizzes, exams, and other assessments **that are *taken*, not submitted* **. |
| [`lectures/`](lectures/) | Core lecture materials and related assets. |
| [`modules/`](modules/) | Weekly/topic-based module directories (`module_00` to `module_13`). |
| [`phases/`](phases/) | High-level course progression phase wrappers (`phase_01` to `phase_05`). |
| [`platforms/`](platforms/) | Platform-specific configurations and assets (Canvas, Gemini, Piazza). |
| [`reading_materials/`](reading_materials/) | Assigned papers, texts, and supplementary reading. |
| [`slides/`](slides/) | Slide decks and archived presentations. |
| [`templates/`](templates/) | HTML and Markdown templates for Canvas and other learning management systems. |
| [`term_project/`](term_project/) | Rubrics, sprint specs, and `docker` compute configs for the term project. |
| [`README.md`](README.md) | This file. |

<hr>

## 🚀 Quick Start & Execution

**1. Prerequisites**
* Git client
* Docker Desktop & VS Code (for DevContainer deployment)

**2. Initialization**
```bash
git clone [https://github.com/kddresearch/cis531-731-2026_fall.git](https://github.com/kddresearch/cis531-731-2026_fall.git)
cd cis531-731-2026_fall
# Open in VS Code to initialize the DevContainer
```

## 🦅 Lab Execution Protocols

All Teaching Assistants and GRAs operating in this repository fall under the KDD Lab **Keep Flying Directive v2.1**.

* **Observable State:** Progress is measured by commits, drafts, logs, and reproducible outputs—not intentions.
* **The Triad:** When opening an issue or Pull Request, provide explicit goals, current blockers, and proposed next actions.
* **Artifact-Gated Routing:** Do not request synchronous meetings for routine status updates. Push your grading state or syllabus updates to this repository first.

## 👥 Instructional Staff

| Role | Name | GitHub Handle |
| --- | --- | --- |
| **Instructor** | William H. Hsu | [@banazir](https://github.com/banazir) |
| **Teaching Asssistant** | Joshua Garcia | |

## 📂 Repository Structure (Full Tree)

<details>
<summary><b>Click to expand: Course Repository Template Directory Tree</b></summary>

```
Folder PATH listing for volume OS
Volume serial number is DC87-33C6
C:.
|   propagation_log_G.txt
|   propagation_log_H.txt
|   propagation_log_I.txt
|   README.md
|   structure_dump.txt
|   
+---.github
|       .gitkeep
|       
+---admin
|   |   .gitkeep
|   |   
|   +---policies
|   |   |   .gitkeep
|   |   |   generative_ai_kit.md
|   |   |   generative_ai_kit_howto.md
|   |   |   generative_ai_kit_howto_v2.md
|   |   |   generative_ai_kit_v2.md
|   |   |   office_hours_scheduling.md
|   |   |   ps4_self_service_feedback_guide.md
|   |   |   term_project_invariants.md
|   |   |   
|   |   \---prompts
|   |           claude_critical_review_coordinator.md
|   |           perplexity_project_lifecycle_coordinator.md
|   |           perplexity_systems_engineering_auditor.md
|   |           
|   \---syllabus
|           .gitkeep
|           04_term_project_guidelines.md
|           05_term_project_taxonomy.md
|           06_term_project_sourcing_guide.md
|           README.md
|           
+---assignments
|   |   assignment_template.md
|   |   README.md
|   |   
|   +---homework
|   |       hw12_final_deliverables.md
|   |       hw1_devcontainer_bringup_architecture.md
|   |       lab01.ipynb
|   |       lab02.ipynb
|   |       lab03a.ipynb
|   |       lab03b.ipynb
|   |       lab04.ipynb
|   |       lab5.ipynb
|   |       lab6.ipynb
|   |       lab7.ipynb
|   |       ps11_ethics_storytelling_dashboards.md
|   |       ps4_proposal.md
|   |       ps6_semantic_search_vdb_schema.md
|   |       ps8_interim_report.md
|   |       
|   +---machine_problems
|   |       .gitkeep
|   |       mp10_interpretability_metrics.md
|   |       mp2_devcontainer_deployment_manifest_verification.md
|   |       mp3_real_time_asr_vector_database_ingestion.md
|   |       mp5_structured_streaming.md
|   |       mp7_genre_classification.md
|   |       mp9_rag_classification_gold_standard.md
|   |       verify_env.py
|   |       
|   \---project_sprints
|           .gitkeep
|           guidelines.md
|           
+---docs
|   |   .gitkeep
|   |   
|   +---architecture
|   |       .gitkeep
|   |       
|   +---guides
|   |       .gitkeep
|   |       
|   \---setup
|           .gitkeep
|           hw1_mp2_windows11_wsl2_docker_walkthrough.md
|           
+---exams_quizzes
|       .gitkeep
|       
+---lectures
|       lectture-26.md
|       lecture-11.md
|       lecture-12.md
|       lecture-13.md
|       lecture-14.md
|       lecture-15.md
|       lecture-16.md
|       lecture-17.md
|       lecture-18.md
|       lecture-19.md
|       lecture-20.md
|       lecture-21.md
|       lecture-22.md
|       lecture-23.md
|       lecture-24.md
|       lecture-25.md
|       lecture-26.md
|       lecture_10_slide_template.md
|       lecture_template.md
|       README.md
|       
+---modules
|   |   index.html
|   |   module_template.md
|   |   README.md
|   |   
|   +---module_00
|   |       .gitkeep
|   |       README.md
|   |       
|   +---module_01
|   |       .gitkeep
|   |       README.md
|   |       
|   +---module_02
|   |       .gitkeep
|   |       hw1_mp2_windows11_wsl2_docker_walkthrough.html
|   |       README.md
|   |       
|   +---module_03
|   |       .gitkeep
|   |       README.md
|   |       
|   +---module_04
|   |       .gitkeep
|   |       README.md
|   |       
|   +---module_05
|   |       .gitkeep
|   |       README.md
|   |       
|   +---module_06
|   |       .gitkeep
|   |       README.md
|   |       
|   +---module_07
|   |       .gitkeep
|   |       README.md
|   |       
|   +---module_08
|   |       .gitkeep
|   |       README.md
|   |       
|   +---module_09
|   |       .gitkeep
|   |       README.md
|   |       
|   +---module_10
|   |       .gitkeep
|   |       
|   +---module_11
|   |       .gitkeep
|   |       
|   +---module_12
|   |       .gitkeep
|   |       
|   \---module_13
|           .gitkeep
|           
+---phases
|   |   README.md
|   |   
|   +---phase_01
|   |       .gitkeep
|   |       README.md
|   |       
|   +---phase_02
|   |       .gitkeep
|   |       README.md
|   |       
|   +---phase_03
|   |       .gitkeep
|   |       README.md
|   |       
|   +---phase_04
|   |       .gitkeep
|   |       README.md
|   |       
|   \---phase_05
|           .gitkeep
|           README.md
|           
+---platforms
|   +---canvas
|   |       .gitkeep
|   |       
|   +---gemini
|   |       .gitkeep
|   |       
|   +---github
|   |       github_intro.md
|   |       
|   +---moodle
|   |       .gitkeep
|   |       
|   \---piazza
|           .gitkeep
|           
+---reading_materials
|       .gitkeep
|       readings_by_lecture.md
|       README.md
|       
+---slides
|   |   .gitkeep
|   |   
|   \---archive
|           .gitkeep
|           
+---templates
|   +---html_layouts
|   |       Golden Template - Universal Assignment Index Page.html
|   |       Golden Template - Universal Assignment Page.html
|   |       Golden Template - Universal Lecture Page.html
|   |       Golden Template - Universal Module Page.html
|   |       Golden Template - Universal Phase Page.html
|   |       Golden Template - Universal Term Project Proposal Page.html
|   |       Golden-Template.html
|   |       README.md
|   |       
|   \---repo_structures
|           directory_README_academic_template.md
|           module_README_template.md
|           phase_README_template.md
|           
\---term_project
    +---docker
    |       Dockerfile
    |       
    \---rubrics
            ps4_proposal_feedback_rubric.md            
```
</details>
