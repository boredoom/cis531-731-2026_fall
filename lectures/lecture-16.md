# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 2:** Pipeline Execution | **Module 5:** Scrub: Chunking & Embedding Generation | **Lecture 16:** Embedding Lab / VDB Indexing & Wrap-Up | Friday, October 02, 2026 |

---

## Slide 1: Lab 3b Execution — Connecting ASR to VDB
### CIS 531/731 - Lecture 16
* **Objective:** Ingest the raw ASR corpus from Module 3 (Whisper) into a local Vector Database (FAISS).
* **The Bridge:** We must translate the `result["text"]` string from Lab 3a into a dense semantic vector.
* **Environment Check:** Ensure your DevContainer has successfully built with `faiss-cpu`, `transformers`, and `sentence-transformers`.
* **The Model:** We will initialize `all-MiniLM-L6-v2` to generate the 384-dimensional embeddings.

**Speaker Notes:**
Welcome to Lab day. Today, we close the loop on the Scrub phase. We are taking the raw transcripts you generated using OpenAI's Whisper model back in Module 3, and we are converting them into computable geometry. Your primary task today is to successfully pass your ASR text string into the HuggingFace `SentenceTransformer` model, extract the 384-dimensional vector, and push that vector into a local FAISS index. Verify your Python environments now.

---

## Slide 2: Building the FAISS Index
### CIS 531/731 - Lecture 16
* **FAISS (Facebook AI Similarity Search):** A highly optimized C++ library with Python bindings for dense vector clustering and similarity search.
* **The Index:** `faiss.IndexFlatL2`
* **L2 (Euclidean Distance):** The default metric for a flat index. Measures the straight-line distance between two vectors in space.
* **Dimensionality:** The index must be instantiated with the exact dimension size of your embedding model (384 for MiniLM).

**Speaker Notes:**
For this lab, we are using FAISS. It is not a full-featured, distributed database like Qdrant or Milvus, but it is the industry-standard underlying library for extremely fast vector matching. We will instantiate an `IndexFlatL2`. This means we are not using approximate nearest neighbors (HNSW) today; we are doing an exact, exhaustive search using Euclidean distance. Because our dataset is small—just a few podcast chunks and a poem—an exact search will run in milliseconds. Just ensure you initialize the index with the correct dimension count, or it will reject your vectors.

---

## Slide 3: Ingesting the Corpus (The Deterministic Hit)
### CIS 531/731 - Lecture 16
* **The Simulated Stream:** We provide a few mock ASR chunks to simulate a live radio feed.
* **The Target Payload:** You must paste your exact LibriVox transcript (Wilfred Owen's "Anthem for Doomed Youth") from Lab 3a into the script.
* **Encoding:** The `embedder.encode()` function converts the list of text strings into a Numpy array of vectors.
* **Insertion:** The `index.add()` function pushes the vectors into the FAISS memory space.

**Speaker Notes:**
In your Jupyter notebook, you will see a simulated corpus containing a few random sentences. To prove your pipeline works, you must paste your specific output from Lab 3a—the WWI poetry transcript—into the `lab3a_transcript` variable. When you run the cell, the Sentence Transformer model will encode all of those strings into vectors simultaneously, and push them into FAISS. 

---

## Slide 4: Executing Semantic Search
### CIS 531/731 - Lecture 16
* **The Query:** "doomed youth"
* **The Mechanism:** 
  1. The string "doomed youth" is passed to the embedding model.
  2. The resulting vector is passed to `index.search(query_embedding, k=1)`.
* **The Output (k=1):** The algorithm returns the index of the single closest vector in the database (shortest L2 distance).
* **Verification:** If successful, the script will return your pasted LibriVox transcript, not the mock radio chunks.

**Speaker Notes:**
Once the database is loaded, we test it. We supply the query "doomed youth." Notice that the search query must *also* be converted into an embedding using the exact same model. You cannot compare a text string to a vector. We ask FAISS for `k=1`, meaning the single closest mathematical match. If you set up your pipeline correctly, FAISS will calculate the distances and return the transcript of the poem. 

---

## Slide 5: Module 5 Wrap-Up & HW4 Debrief
### CIS 531/731 - Lecture 16
* **HW4 (Data Analytics Pipelines):** Due yesterday. We will review common bottlenecks and grading expectations.
* **The Transition:** We have successfully obtained data (M3), streamed it (M4), and scrubbed/embedded it (M5).
* **Next Week (Module 6):** Entering the "Model" phase. We will utilize GenAI and LLMs for Few-Shot Trope/Genre Classification based on the embeddings we generated today.
* **MP5 Release:** Machine Problem 5 will be released on Monday, focusing on Hugging Face text classification pipelines.

**Speaker Notes:**
As you finish up Lab 3b, I want to briefly review HW4, which was due yesterday. I've noted a few recurring issues regarding watermark configurations and late-data handling in your Spark streaming scripts, which we will address now. Looking ahead: you have now built the foundational ingestion and storage pipeline. Next week, we begin applying intelligence. Module 6 focuses on using Large Language Models to classify the text we just embedded. We will be identifying literary tropes and genres using few-shot prompting. MP5 drops on Monday. Have a great weekend.
