<!--
yaml_schema_version: "2.2"
document_version: "1.0"
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

### 📂 Directory: admin/policies

Status: ACTIVE | Maintainer: William H. Hsu

## 📖 Overview

This directory contains administrative doctrine, operational procedures, governance constraints, and approved workflow frameworks used throughout CIS 531/731. Unlike assignment specifications or lecture materials, the artifacts in this directory define how students, instructional staff, and AI-assisted project workflows are expected to operate within the course ecosystem.

Many of these documents serve as reusable infrastructure that supports project planning, AI-assisted development, proposal evaluation, office-hours coordination, and reproducible execution of term-project activities.

> **⚠️ Sub-Directory Routing Notice**
>
> This directory is intended for standing policies, workflow frameworks, and operational procedures that may be referenced across multiple assignments, project phases, or semesters.
>
> Assignment specifications belong under `assignments/`.
> Project deliverables and grading requirements belong under `term_project/`.
> Technical implementation documentation belongs under `docs/`.

## 🗂️ Directory Structure

| Subdirectory / File | Description |
| :--- | :--- |
| [`prompts/`](./prompts/) | Specialized AI-auditor and workflow-coordination prompts used by approved project-review pipelines. |
| [`generative_ai_kit.md`](./generative_ai_kit.md) | Baseline GenAI workflow framework governing approved AI-assisted project practices. |
| [`generative_ai_kit_v2.md`](./generative_ai_kit_v2.md) | Updated version of the GenAI workflow framework with expanded controls and routing behavior. |
| [`generative_ai_kit_howto.md`](./generative_ai_kit_howto.md) | Student onboarding guide for establishing and using the GenAI Kit workflow. |
| [`generative_ai_kit_howto_v2.md`](./generative_ai_kit_howto_v2.md) | Updated onboarding guide corresponding to GenAI Kit v2. |
| [`office_hours_scheduling.md`](./office_hours_scheduling.md) | Procedures and expectations for office-hours scheduling and coordination. |
| [`ps4_self_service_feedback_guide.md`](./ps4_self_service_feedback_guide.md) | Structured workflow for proposal self-review, AI-assisted auditing, and project feasibility assessment. |
| [`term_project_invariants.md`](./term_project_invariants.md) | Cross-cutting project principles and constraints that remain stable across deliverables and project phases. |
| [`README.md`](./README.md) | This file. |

## 🦅 Standard Operating Procedures (SOPs)

* **Protocol 1 (SSOT Paramountcy):** Do not update content directly in Canvas. Markdown artifacts in this repository remain the system of record, with downstream publishing occurring from Git-managed sources.
* **Protocol 2 (Governance Scope):** Only place documents here when they define standing rules, operational procedures, reusable workflows, or project-governance mechanisms. Assignment instructions should not be stored in this directory.
* **Protocol 3 (Workflow Stability):** When updating AI workflow frameworks, preserve backward compatibility where possible and clearly version major revisions to maintain auditability across semesters.
* **Protocol 4 (Policy vs. Deliverable Separation):** Project-specific grading criteria, rubrics, and submission requirements should reside in `term_project/` or `assignments/` and only be referenced from this directory when necessary.
