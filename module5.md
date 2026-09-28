# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 2:** Pipeline Execution | **Module 5:** Scrub: Chunking & Embedding Generation | **Lectures 14-16** | Sep 28 – Oct 02, 2026 |

---

## Slide 1: Module 5 Overview
### CIS 531/731 - Lecture 14 (Mon 28 Sep)
* **The "Scrub" Phase:** Transitioning from raw data ingestion to structured, machine-readable representations.
* **Text Chunking:** Strategies for dividing long-form ASR (Automatic Speech Recognition) transcripts into semantically coherent segments.
* **Embedding Generation:** Transforming chunked text into dense vector representations.
* **Vector Database (VDB) Schema Design:** Structuring metadata for efficient semantic retrieval.
* **Reading Assignment:** *Speech and Language Processing, Ch. 11* (Jurafsky & Martin).

**Speaker Notes:**
Welcome to Module 5. Last week, we built the ingestion pipeline to capture ASR streams. But raw, continuous text is largely useless to a machine learning model. This week, we enter the "Scrub" phase. Our objective is to take that raw text, break it down into logical chunks, convert those chunks into mathematical vectors, and store them in a database designed specifically for semantic search. This is the foundational architecture of Retrieval-Augmented Generation.

---

## Slide 2: Text Chunking Strategies
### CIS 531/731 - Lecture 14
* **Fixed-Size Chunking:** Splitting text by a hard character or token limit (e.g., 512 tokens).
* **The Boundary Problem:** Fixed chunks often sever sentences or concepts, destroying semantic meaning.
* **Recursive Character Chunking:** Attempting to split on paragraphs, then sentences, then words to preserve structure.
* **Semantic Chunking:** Using NLP boundaries (like pauses in the ASR stream or sentence markers) to create logical divisions.
* **Overlap (Stride):** Retaining 10-20% of the previous chunk in the next chunk to preserve context across boundaries.

**Speaker Notes:**
If you feed an entire one-hour lecture transcript into an embedding model, the model will either crash due to token limits or dilute the meaning so much that retrieval becomes impossible. We have to chunk the text. A naive approach is just chopping it every 500 words. But if you chop a sentence in half, you lose the context. Today we will look at recursive chunking and semantic chunking, and why adding a "stride"—or overlap—between chunks prevents context loss at the boundaries.

---

## Slide 3: Introduction to Embeddings
### CIS 531/731 - Lecture 15 (Wed 30 Sep)
* **The Vector Space:** Representing words, sentences, or documents as high-dimensional arrays of floating-point numbers.
* **Semantic Proximity:** Vectors that point in similar directions represent concepts that share semantic meaning.
* **The Architecture:** Utilizing transformer-based models (like Sentence Transformers) to generate dense vectors.
* **Dimensionality:** Understanding the tradeoff between vector size (e.g., 384 vs 1536 dimensions) and computational cost/accuracy.
* **Reading Assignment:** Sentence Transformers "Semantic Search" documentation.

**Speaker Notes:**
Now that we have clean chunks of text, we need to convert them into a format the machine understands. Enter Embeddings. An embedding is just a list of numbers—a vector—that plots a piece of text into a high-dimensional space. The magic of embeddings is that texts with similar meanings are plotted physically close together in that space. We will use the Sentence Transformers library today to convert our ASR chunks into dense vectors.

---

## Slide 4: Vector Database (VDB) Schema Design
### CIS 531/731 - Lecture 15
* **Relational vs. Vector Databases:** SQL matches exact keywords; VDBs match mathematical proximity (Cosine Similarity, Dot Product).
* **The Payload (Metadata):** Storing the original text, timestamp, and speaker ID alongside the vector.
* **Indexing Algorithms:** HNSW (Hierarchical Navigable Small World) for rapid approximate nearest neighbor search.
* **Hybrid Search:** Combining vector similarity with traditional metadata filtering (e.g., "Find this topic, but only in transcripts from 2024").
* **Schema Definition:** Designing the collection parameters before ingestion.

**Speaker Notes:**
A standard SQL database is terrible at finding similar concepts; it only knows how to find exact word matches. Vector databases, like Qdrant or Milvus, are built to calculate the distance between vectors rapidly. But a vector alone is useless if you don't know what text it represents. Your schema design must include the payload—the metadata. You must store the original transcript chunk, the timestamp, and the speaker ID alongside the vector so that when the VDB finds a match, it returns human-readable context.

---

## Slide 5: Lab 3 Execution — Embedding & Indexing
### CIS 531/731 - Lecture 16 (Fri 02 Oct)
* **Objective:** Ingest the raw ASR corpus from Module 3 into a local VDB instance.
* **Step 1:** Implement a recursive character chunker with a defined overlap.
* **Step 2:** Initialize a local embedding model (e.g., `all-MiniLM-L6-v2`).
* **Step 3:** Define the VDB schema and generate embeddings for all chunks.
* **Step 4:** Execute a semantic search query against the VDB to verify retrieval accuracy.

**Speaker Notes:**
Today is Lab day. We are taking the theories from Monday and Wednesday and executing the pipeline. You have your raw ASR corpus. You will write a Python script to chunk that text, generate embeddings using a local Hugging Face model, and push those vectors into your Vector Database. Your final deliverable for today is to run a semantic search query against your own database and prove that it returns the correct chunk of text based on the meaning of your query, not just exact keyword matches.

---
