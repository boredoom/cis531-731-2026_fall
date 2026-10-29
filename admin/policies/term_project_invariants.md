# CIS 531/731 Invariants Ledger (INV-1 through INV-21)

* **INV-1 (Data Prohibition):** No milestone, homework, or term project may source training/eval data from Yelp review corpora or SEC filings.
* **INV-2 (Mandatory Pipeline Stage):** Every team pipeline must instantiate at least one of `{VDBEmbeddingRetrieval, ASRStreamIngestion}` as a first-class stage.
* **INV-3 (Track Immutability):** Track selection at Module 3 is fixed through Modules 5, 8, 9, and 10 (no mid-semester track switching).
* **INV-4 (531/731 Differentiation):** Core divergence rule governing graduate vs. undergraduate deliverables.
* **INV-5 (Liveness SLAs):** Streaming latency/throughput requirements handled via separate acceptance/monitoring rubrics rather than pre/post-conditions.
* **INV-6 (VDB Tiering):** FAISS is mandatory for all; Milvus is an optional upgrade path gated to CIS 731 only.
* **INV-7 (ASR Tiering):** Whisper (local) is mandatory baseline; AssemblyAI is mandatory specifically for the Module 4 streaming milestone.
* **INV-8 (Quota Enforcement):** API/compute usage bounded by department-issued limits with automated enforcement.
* **INV-9 (Corpus Provenance):** Every ingested document must carry a `license_class ∈ {public_domain, instructor_provided}` tag.
* **INV-10 (Stream Source Whitelist):** ASR live capture restricted strictly to instructor-maintained whitelisted streams and fallback demo streams.
* **INV-11 (Schema Authority):** CIS 731 teams derive custom schemas; CIS 531 teams adopt the unmodified instructor-provided schema.
* **INV-12 (Gold-Standard Evaluation):** Graded metrics computed against instructor gold sets for Mods 8/10; student-constructed for Mod 9.
* **INV-13 / INV-15 (Two-Tier DevContainer Policy):** The CPU-pinned DevContainer is the normative baseline (100% solvable); GPU container is an optional overlay.
* **INV-14 (Manifest Pinning):** Strict SHA/digest pinning for all container runtimes and dependency lockfiles.
* **INV-16 (Chronological GPU Access Gating):** GPU access unlocked post-proposal greenlight (Week 5 onward).
* **INV-17 (Student-Constructed Gold Sets):** Module 9 annotation limits (≤50 objects / 2 hours for homework; 50–200 labeled examples for term projects).
* **INV-18 ("Broke the Bank" Protocol):** Quota exhaustion triggers automatic CPU/free-tier fallback; persistent failure consumes 1 of 2 permitted assignment drops.
* **INV-19 (Batched Key Provisioning & No-Contact):** All compute allocations flow exclusively through the instructor as sole point of contact.
* **INV-20 (Diagnostic Guillotine):** HW1 and MP2 serve as proficiency diagnostics; early drop exhaustion triggers a course drop advisory.
* **INV-21 (Annotation Ceiling Enforcement):** CI/CD row-count autograder gate on homework annotation files enforcing the ≤50 row limit.
