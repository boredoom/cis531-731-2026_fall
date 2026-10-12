# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase [X]:** [Phase Name] | **Module 6:** GenAI & LLMs: Candidates, Code, Classification | **Lecture 19:** Model Selection & Embedding-Backed Classification Lab | Monday, October 12, 2026 |

---

## Slide 1: Agenda & Overview
### CIS 531/731 - Lecture 19
* **MP6 Release & Requirements:** Reviewing the expectations for the embedding-backed classification machine problem.
* **Embedding Models vs. Generative Models:** Understanding why a specialized embedding model (e.g., `sentence-transformers`) is often superior to a generative LLM for clustering and similarity-based classification.
* **Distance Metrics for Classification:** Utilizing Cosine Similarity and Euclidean distance in the embedding space to classify unknown texts against known trope/genre anchors.
* **Building the Reference Index:** Constructing the "gold standard" vector database of known tropes to serve as the classification lookup table.
* **Thresholding and Confidence:** Establishing mathematical thresholds for "Unknown" or "Mixed" classifications when distance metrics fall in the boundary zones.

**Speaker Notes:**
Welcome back. Today we are officially kicking off Machine Problem 6. We are shifting our focus from generative text creation (the "chat" aspect of LLMs) toward representation—specifically, how we can use dense vector embeddings to mathematically classify and organize text. This lab session will bridge the theoretical concepts from last week with practical implementation.

---

## Slide 2: MP6 Release & Requirements
### Embedding-Backed Classification
* **The Goal:** Build a robust, non-generative classification pipeline using semantic embeddings.
* **The Data:** A corpus of unlabelled media synopses and text excerpts that must be categorized into specific tropes and genres.
* **The Deliverable:** A programmatic pipeline that ingests raw text, embeds it, calculates distances against known anchors, and assigns a classification label without invoking a generative text completion.

**Speaker Notes:**
For MP6, you are not writing prompts asking an LLM to guess a genre. Instead, you are building a deterministic system. You will take text, convert it into an embedding vector, and perform mathematical distance calculations against a known database. This is a crucial skill because it is significantly faster, cheaper, and more reproducible than zero-shot generative prompting.

---

## Slide 3: Embedding Models vs. Generative Models
### Choosing the Right Tool
* **Generative Models (e.g., GPT-4, Llama 3):** Autoregressive models optimized for next-token prediction. Computationally heavy and prone to hallucination.
* **Embedding Models (e.g., `sentence-transformers`, BERT):** Encoder-only models optimized for understanding semantic relationships and generating fixed-length dense vectors.
* **The Advantage:** Embedding models capture deep semantic meaning in a compact, easily comparable format, making them vastly superior for clustering and similarity-based tasks.

**Speaker Notes:**
Why aren't we just using a standard text generation model for this? Because classification is fundamentally a grouping problem, not a writing problem. Generative models are too slow and expensive for bulk classification. Specialized embedding models like `sentence-transformers` map semantic meaning into a continuous vector space where math does the heavy lifting, allowing us to classify thousands of documents in the time it takes an LLM to generate a single paragraph.

---

## Slide 4: Distance Metrics for Classification
### Navigating the Vector Space
* **Cosine Similarity:** Measures the angle between two vectors. Excellent for comparing semantic meaning regardless of document length. (Range: -1 to 1).
* **Euclidean Distance ($L2$ Norm):** Measures the straight-line distance between two points in the vector space. Highly sensitive to vector magnitude.
* **Application:** To classify an unknown text, we embed it and find the closest known "anchor" vector using these mathematical distance metrics.

**Speaker Notes:**
Once your text is converted into an array of numbers, classification becomes a geometry problem. Cosine similarity is generally our go-to metric for NLP tasks because it focuses on the direction of the vector (the core semantic meaning) rather than its magnitude (which can be skewed by document length). If the vector for an unknown synopsis points in the exact same direction as our "Enemies to Lovers" trope anchor, we have our classification.

---

## Slide 5: Building the Reference Index
### The "Gold Standard" Lookup Table
* **Establishing Anchors:** Curating high-quality, definitive examples of each trope and genre to serve as ground truth.
* **Vector Database:** Embedding these anchors and storing them in an index (e.g., FAISS, ChromaDB, or a simple NumPy array for smaller datasets).
* **K-Nearest Neighbors (KNN):** Using the reference index to quickly query the top $K$ most similar known examples to our input text.

**Speaker Notes:**
Your classification system is only as good as its reference index. You must construct a "gold standard" database of anchor texts. If you want to classify sci-fi tropes, you need mathematically embedded examples of "Cyberpunk," "Space Opera," and "Time Travel." When a new synopsis comes in, your pipeline will query this database and find the nearest semantic neighbors.

---

## Slide 6: Thresholding and Confidence
### Handling Ambiguity
* **Distance Boundaries:** Defining the minimum similarity score required to confidently assign a label.
* **"Unknown" Classifications:** If a text's embedding falls too far away from *all* known anchors, the system must gracefully categorize it as "Unknown" rather than forcing a bad fit.
* **"Mixed" Classifications:** Handling scenarios where an input vector sits perfectly equidistant between two distinct anchors (e.g., a text that is equally "Horror" and "Comedy").

**Speaker Notes:**
Real-world data is messy. What happens when an input text doesn't look like any of your anchors? Without thresholding, your system will just guess the "least wrong" answer. You must establish strict mathematical boundaries. If the cosine similarity drops below 0.75, your pipeline needs the logic to say "I don't know" or to flag the text for human review.

---

## Slide 7: Summary & Next Steps
### Preparing for Wednesday's Workshop
* **Key Takeaway:** Semantic embeddings transform subjective text classification into objective, distance-based mathematics.
* **Next Class (Wednesday):** Trope/Genre Classification Workshop. We will live-debug environment setups and evaluate classifier performance metrics (Precision, Recall, F1).
* **Action Item:** Review the MP6 documentation and begin constructing your reference index of known tropes before Wednesday's session.

**Speaker Notes:**
That covers the theoretical architecture for MP6. Your primary task right now is to identify and curate your gold-standard anchor texts. On Wednesday, we will move into the workshop phase, where we will troubleshoot your pipeline integration and discuss how to rigorously evaluate the F1 performance of your classifiers. See you then.
