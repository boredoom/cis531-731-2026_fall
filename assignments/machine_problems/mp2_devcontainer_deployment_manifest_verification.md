# MP 2: DevContainer Deployment & Manifest Verification
**Research Software Engineering, Docker, & Compute Allocation**

**📅 Due:** Tue 22 Sep 2026, 11:59 PM | **💯 Points:** 30 | **👥 Team:** Individual (GitHub PR & Canvas submission)

> **🚨 CRITICAL SUBMISSION POLICY**
> **Strict Version Compatibility:** Every DevContainer image and autograding environment must resolve exactly to the pinned versions and SHA-256 digests in the `course_runtime` manifest. Floating minor versions or "compatible" libraries will fail the autograding checks.

## 1. Overview
Initialize your local or remote workspace using the provided Docker DevContainer configuration. You must modify the base configuration to achieve absolute compliance with the strict version manifest provided in the starter repository, verify your environment digest, and implement hardware compute probing with CPU/GPU fallback routing.

**Required Readings (Module 2 Gates):**
* **Research Software Engineering:** Brett et al. — Foundational practices for reproducible research environments; Course Syllabus (Strict Version Compatibility manifest).
* **Docker Documentation:** [Docker Get Started Guide](https://docs.docker.com/get-started/): Core containerization concepts and DevContainer integration mechanics.

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Environment Setup & Configuration:** Deploy the provided DevContainer configuration and review the `course_runtime` version manifest.
2. **Dependency Pinning:** Pin PySpark 3.5.x, PyTorch 2.x, Transformers, OpenAI Whisper, MLflow, and FAISS to exact required releases.
3. **Environment Verification:** Implement and execute `verify_env.py` to output your environment's SHA-256 digest and verify match against course standards.
4. **Compute Probing:** Author `probe_compute.py` to check for CUDA device availability and configure fallback logic.
5. **PR Submission & Documentation:** Commit modified configuration files, verification logs, and submit your GitHub Pull Request link.

## 3. Required Document Structure
Your submission must be a **GitHub Pull Request link and output logs submitted via Canvas** containing the following sections exactly as named below. 

* **Part 1: DevContainer Build & Manifest Pinning (15 Points):** Modified configuration files pinning exact versions and the output execution log of `verify_env.py` showing the matching SHA-256 digest.
* **Part 2: Compute Allocation & GPU Fallback (15 Points):** `probe_compute.py` script implementation, execution output demonstrating fallback routing, and (for CIS 731 graduate students) conditional base image container pull configuration.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (30 Points Total)

This assignment is worth 30 points total.

**Part 1: Manifest Compliance (15 pts)**
* **Exact Version Matching (15 pts):** The environment perfectly matches pinned dependencies and produces the correct SHA-256 digest required by autograding.

**Part 2: Compute Allocation & Fallback (15 pts)**
* **Compute Probe & Fallback Logic (15 pts):** The script correctly detects the hardware environment and routes to the appropriate GPU/CPU state string. (CIS 731 students graded additionally on conditional container pull configuration).
* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.
