<!-- ASSIGNMENT-META
id: PS 6
phase: Phase 3: Scrub & Embed
module: Module 05: Scrub (Chunking, Embedding Generation, VDB Schema Design)
released: Fri 16 Oct 2026
due: Sun 25 Oct 2026
prev: assignments/machine_problems/mp5_structured_streaming.md
next: assignments/machine_problems/mp7_genre_classification.md
-->
# PS 6: Semantic Search, Chunking, & VDB Schema
**Chunking and index trade-off analysis, retrieval evaluation design, and a provenance-bearing vector-database schema**

**🗓️ Released:** Fri 16 Oct 2026 | **📅 Due:** Sun 25 Oct 2026 | **💯 Points:** 100 | **👥 Team:** Individual

> **🚨 CRITICAL SUBMISSION POLICY**
> **Schema Authority (INV-11):** CIS 531 submissions must adopt the instructor-provided trope ontology schema unmodified; CIS 731 submissions must derive their own. A 531 submission containing a self-designed schema, or a 731 submission reusing the unmodified instructor schema, fails the `register_trope_schema` contract check.

## 1. Overview
Written analysis and schema specification for the Scrub phase: a chunking cost model, an approximate-nearest-neighbor trade-off analysis, a retrieval evaluation protocol, and a provenance-bearing vector-record schema that extends the MP 5 chunk record. Work on your chosen corpus (lyrics, YA literature, xianxia/wuxia excerpts, or ASR transcript segments). FAISS is the required index for all teams; Milvus is permitted for CIS 731 only (INV-6). Corpus content is limited to public-domain or instructor-provided material (INV-9). Show derivations; unsupported numeric claims earn no credit.

**Cadence Notice:** Two explicit exceptions to the standard 6-day inter-assignment gap apply around this assignment: MP 5 (due Tue 20 Oct 2026) to PS 6 (due Sun 25 Oct 2026) is 5 days, and PS 6 to MP 7 (due Fri 30 Oct 2026) is 5 days. Both are applied to maintain assignment cadence without forcing a due date on Halloween (Sat 31 Oct).

**Required Readings:**
* [Speech and Language Processing, 3rd ed. draft (Jurafsky & Martin, 19 Aug 2026), Ch. 11](https://web.stanford.edu/~jurafsky/slp3/): retrieval, dense embeddings, retrieval-augmented generation, and ranked-retrieval evaluation.
* [Sentence Transformers: “Semantic Search”](https://www.sbert.net/examples/applications/semantic-search/README.html): symmetric vs. asymmetric search, bi-encoder retrieval with cross-encoder re-ranking, and approximate nearest-neighbor search.

**Upstream inputs:** MP 5 chunk record and contracts; MP 3 corpus and provenance manifest; PS 4 track.  
**Downstream consumers:** MP 7 (label space and index records); MP 9 (relevance protocol is the basis of the gold-standard codebook); PS 8 (architecture and ontology version); HW 12 (final schema).

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Cost Model Drafting:** Use the AI Kit to draft the chunking cost derivations, then verify the arithmetic independently.
2. **Index Trade-off Matrix:** Tabulate `IndexFlatIP`, `IndexIVFFlat` (`nlist`, `nprobe`), and `IndexHNSWFlat` (`M`, `efSearch`) costs; check every claim against FAISS documentation.
3. **Schema Synthesis:** Generate the JSON Schema (Draft 2020-12) extending the MP 5 record and validate it with a validator recorded in your lockfile.
4. **Contract Drafting:** Write `deal` contracts for `admit_document` and `vdb_upsert`, each with a plain-language invariant.
5. **Adversarial Review:** Ask the AI Kit to find provenance holes (orphan vectors, unlicensed documents, duplicate `chunk_id`); log findings and fixes in `GenAI.pdf`.

## 3. Required Document Structure
Your submission must be a **typeset PDF (at most 8 pages) delivered with a `schema/` directory under Git tag `ps6-submission`** containing the following sections exactly as named below. 

* **Chunking Cost Model:** Compare fixed-window (n tokens, stride s), sentence-boundary, and structure-aware (stanza, chapter, speaker turn) chunking: chunks per document, index storage `N_chunks × d × 4` bytes, overlap inflation 1/(1 − ρ) with ρ = 1 − s/n, and a chunk-length cap tied to the embedding model's maximum sequence length and trope granularity.
* **Index and Similarity Analysis:** Prove cosine similarity equals inner product for unit-normalized vectors and why `IndexFlatIP` is exact; contrast IVF and HNSW on query complexity, build/memory cost, and recall degradation; model re-ranking latency `T = T_enc + T_ann + k·T_ce` for k = 50 re-ranked to 10.
* **Retrieval Evaluation Protocol:** Define P@k, Recall@k, and MRR for few-shot trope retrieval and the relevance-judgment protocol for a ‘relevant’ chunk (carried into the MP 9 codebook); state which metrics are gradable only against instructor sets (INV-12) until you build your own gold standard (INV-17).
* **Record Schema and ID Mapping:** JSON Schema for `chunk_id`, `doc_id`, `source_hash` (SHA-256), `license_class`, `corpus_type`, `release_year` (VDB) or `broadcast_ts` (ASR), `trope_ids[]`, `embedding_model`, `embedding_dim`, `vector`, `created_ts`; the FAISS int64-id to `chunk_id` mapping layer (`IndexIDMap2`) with update and delete semantics.
* **Contracts and Ontology:** `deal` contracts for `admit_document` (precondition on `license_class`; postcondition `provenance_verified`) and `vdb_upsert` (exactly one vector per `chunk_id`) implementing EmbeddingCompleteness and NoOrphanEmbeddings. CIS 531: mapping table from your fields to the instructor ontology classes. CIS 731: derived ontology (class hierarchy, relation types, cardinalities), granularity justification, and at least three competency questions.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (100 Points Total)

This assignment is worth 100 points total.

**Part 1: Chunking, Index, and Evaluation Analysis (50 pts)**
* **Chunking cost model (20 pts):** Correct storage and overlap derivations and a defensible chunk-length cap.
* **Index and similarity analysis (15 pts):** Correct exact-vs-approximate trade-offs and re-ranking latency model.
* **Retrieval evaluation protocol (15 pts):** Well-defined relevance protocol and metrics; gold-set eligibility stated correctly.

**Part 2: Schema and Contracts (45 pts)**
* **Record schema and provenance (20 pts):** All provenance fields present; schema validates; ID mapping specified.
* **Contracts and invariants (15 pts):** Contracts implement the two named invariants; plain-language statements are precise.
* **Section-specific ontology deliverable (10 pts):** 531 mapping complete and unmodified; 731 ontology coherent with its competency questions.

* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.

---

## Assignment Navigation

| ⬅️ Previous | 📝 Index | Next ➡️ |
|:---|:---:|---:|
| [MP 5: Data Analytics Pipelines (Structured Streaming)](../machine_problems/mp5_structured_streaming.md) | [All Assignments]({{ASSIGNMENTS_INDEX_URL}}) | [MP 7: Few-Shot Trope/Genre Classification (GenAI)](../machine_problems/mp7_genre_classification.md) |

[🏠 Course Home]({{COURSE_HOME_URL}}) · [⬆️ Module]({{MODULE_URL}}) · [⏫ Phase]({{PHASE_URL}})
