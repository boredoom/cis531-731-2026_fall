# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 2:** Pipeline Execution | **Module 5:** Scrub (Chunking & Embedding Generation) | **Lectures 14-16** | Sep 28 – Oct 02, 2026 |

---

## Lecture 14: Scrub — Chunking & Embedding Generation (Mon 28 Sep)

1. **The "Scrub" Phase:** Transitioning from raw data ingestion to structured, machine-readable representations within the data science pipeline.
2. **Text Chunking:** Strategies for dividing long-form ASR (Automatic Speech Recognition) transcripts into semantically coherent segments suitable for downstream processing.
3. **The Boundary Problem:** Analyzing how fixed-size chunking can sever sentences or concepts, and mitigating context loss using recursive character chunking with stride (overlap).
4. **Embedding Generation Introduction:** The mathematical intuition behind transforming chunked text into dense vector representations.
5. **Reading Callout:** Review *Speech and Language Processing, Ch. 11* (Jurafsky & Martin) for foundational NLP processing concepts.

---

## Lecture 15: Semantic Search & VDB Schema Design (Wed 30 Sep)

1. **The Vector Space Model:** Representing concepts as high-dimensional arrays, where semantic proximity is measured mathematically (e.g., Cosine Similarity, Dot Product).
2. **Transformer-Based Embeddings:** Utilizing models like Sentence Transformers to generate dense vectors that capture sentence-level semantic meaning.
3. **Vector Database (VDB) Fundamentals:** Understanding the distinction between traditional relational databases (SQL exact matching) and Vector Databases optimized for semantic similarity search.
4. **VDB Schema Design:** Structuring the collection payload to store the original transcript chunk, timestamp, and speaker ID alongside the vector to ensure context is retained during retrieval.
5. **Reading Callout:** Review the Sentence Transformers "Semantic Search" documentation to understand the programmatic implementation of bi-encoders.

---

## Lecture 16: Embedding Lab & VDB Indexing (Fri 02 Oct)

1. **Lab Setup:** Initializing a local embedding model (e.g., `all-MiniLM-L6-v2`) via the Hugging Face Sentence Transformers library.
2. **Executing the Chunking Script:** Implementing a recursive character chunker with a defined overlap on the raw ASR corpus acquired in Module 3.
3. **Batch Vectorization:** Generating and processing embeddings for the chunked ASR dataset in memory.
4. **Database Ingestion:** Defining the VDB schema and inserting the generated vectors along with their required metadata payloads.
5. **HW4 Wrap-Up:** Final questions and debrief for HW4 (Data Analytics Pipelines), due the previous day, before transitioning to GenAI classification in Module 6.
