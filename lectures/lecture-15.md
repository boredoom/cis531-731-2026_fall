# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 2:** Pipeline Execution | **Module 5:** Scrub: Chunking & Embedding Generation | **Lecture 15:** Embeddings, Semantic Proximity, and VDB Schema Design | Wednesday, September 30, 2026 |

---

## Slide 1: The "Scrub" Phase — From Chunks to Vectors
### CIS 531/731 - Lecture 15
* **Review:** On Monday, we sliced raw ASR streams into semantically bounded chunks with contextual stride.
* **The Problem:** Neural networks do not understand English syntax or character strings; they perform linear algebra on matrices.
* **The Solution (Embedding):** A deterministic transformation mapping discrete text chunks into a continuous high-dimensional vector space.
* **Objective Today:** Understand the mathematical transformation of text into dense vectors, and how to architect a database designed specifically for spatial retrieval.

**Speaker Notes:**
Welcome back. On Monday, we took our messy, continuous ASR transcripts and chunked them into logical overlapping windows. But a text string is just a string. Machine learning models cannot do math on ASCII characters. To make our data computable, we have to translate it into geometry. Today, we look at Embeddings: the process of turning a sentence into a high-dimensional vector, and Vector Databases (VDBs): the architecture required to store and retrieve those vectors efficiently.

---

## Slide 2: The Vector Space & Semantic Proximity
### CIS 531/731 - Lecture 15
* **Vector Representation:** A 1D array of floating-point numbers (e.g., $[0.12, -0.45, 0.89, \dots]$).
* **The Manifold Hypothesis:** Real-world data, like natural language, concentrates on low-dimensional manifolds within a high-dimensional space.
* **Semantic Topology:** Models are trained so that concepts with similar meanings cluster physically closer together in the vector space.
* **Example:** The vector for "King" minus "Man" plus "Woman" lands geographically adjacent to the vector for "Queen".

**Speaker Notes:**
An embedding is simply a list of coordinates. If we have a 3D space, an embedding is just X, Y, and Z. But language is incredibly complex, so we use spaces with hundreds or thousands of dimensions. The fundamental principle here is semantic proximity. The models that generate these vectors are explicitly trained to plot similar meanings near each other. "Dog" and "Canine" will have nearly identical coordinates. Even if they share no overlapping letters, the machine knows they are semantically adjacent because their vectors point in the same direction.

---

## Slide 3: Generating Embeddings (Transformer Architecture)
### CIS 531/731 - Lecture 15
* **Bi-directional Encoder Representations:** BERT-family models read the entire chunk of text in both directions to establish context.
* **Sentence Transformers (SBERT):** Fine-tuned specifically to generate mathematically comparable sentence-level embeddings rather than token-level embeddings.
* **Pooling Strategies:** 
  * *Mean Pooling:* Averaging the vectors of all tokens in a chunk.
  * *CLS Pooling:* Using the special `[CLS]` classification token vector to represent the whole sequence.
* **Our Target Model:** `all-MiniLM-L6-v2` (Fast, local, open-weight, 384 dimensions).

**Speaker Notes:**
How do we actually get these numbers? We use Transformer models, specifically encoder-only models like BERT. But standard BERT outputs a vector for every single word. To compare whole chunks of an ASR transcript, we need one single vector for the entire paragraph. Sentence Transformers solve this by applying a pooling operation—usually averaging all the word vectors together (Mean Pooling) to create a single, unified dense vector representing the whole concept. In our lab, we will use the `all-MiniLM-L6-v2` model. It is exceptionally fast, runs locally on a CPU, and produces highly accurate vectors.

---

## Slide 4: Dimensionality and Compute Trade-offs
### CIS 531/731 - Lecture 15
* **Information Density:** Higher dimensions can capture deeper semantic nuance (e.g., sarcasm, domain-specific jargon).
* **Common Architectures:**
  * `all-MiniLM-L6-v2`: $d = 384$ (Lightweight / Edge compute).
  * `text-embedding-3-small`: $d = 1536$ (Cloud standard).
  * `Llama-3-Embeddings`: $d = 4096$ (High resolution / Compute heavy).
* **The Cost of Dimensions:** 
  * Memory footprint scales linearly with dimension size.
  * Search latency increases due to the "Curse of Dimensionality."

**Speaker Notes:**
When you select an embedding model, you are choosing your dimensionality. A 384-dimensional vector is small, fast, and cheap to store. A 4096-dimensional vector is massive and expensive, but it can capture incredible subtlety in the text. As data scientists, you must balance information density against compute costs. If you are building a semantic search for a million documents on standard hardware, storing 4096 floating-point numbers per chunk will obliterate your RAM and spike your search latency.

---

## Slide 5: The Relational Limit (SQL vs. Semantics)
### CIS 531/731 - Lecture 15
* **Relational Databases (RDBMS):** MySQL, PostgreSQL.
* **Lexical Search (BM25/TF-IDF):** Keyword matching. Fails when vocabulary differs (e.g., "automobile" vs. "car").
* **The Need for Spatial Search:** How do you run a SQL `SELECT` query on a concept? You can't.
* **Vector Databases (VDBs):** Qdrant, Milvus, Chroma. Built from the ground up to execute spatial distance calculations.

**Speaker Notes:**
Now we have our vectors. Where do we put them? If you put them in a standard SQL database, they are useless. SQL is designed for exact matches: `SELECT * WHERE keyword = 'car'`. If the transcript says "automobile," SQL returns zero results. We need a system that can take our query, turn it into a vector, and find the nearest neighbors in the high-dimensional space. That requires a Vector Database.

---

## Slide 6: Distance Metrics (How We Measure Proximity)
### CIS 531/731 - Lecture 15
* **Euclidean Distance ($L2$):** Straight-line distance between two points in space. Highly sensitive to vector magnitude (length).
* **Cosine Similarity:** Measures the angle between two vectors, ignoring their magnitude.
  $$ \text{Cosine}(A, B) = \frac{A \cdot B}{\|A\| \|B\|} $$
* **Dot Product:** A fast calculation often used when vectors are pre-normalized.
* **Standard Practice:** Cosine Similarity is the default for NLP embeddings because a 10-word sentence and a 50-word paragraph can have the same meaning (same angle) but different magnitudes.

**Speaker Notes:**
When the VDB searches for a match, it is calculating a math equation between the query vector and every vector in the database. The most common metric is Cosine Similarity. We don't care how long the vector is (its magnitude); we only care about the angle it points. A short sentence summary and a long, detailed paragraph might point in the exact same direction conceptually. Cosine similarity calculates that angle. A score of 1.0 means identical direction; 0 means orthogonal (unrelated); -1 means exact opposite meaning.

---

## Slide 7: Indexing at Scale — HNSW
### CIS 531/731 - Lecture 15
* **K-Nearest Neighbors (KNN):** Exhaustive search. Accurate, but computationally impossible at scale ($\mathcal{O}(N)$).
* **Approximate Nearest Neighbor (ANN):** Trading a tiny fraction of accuracy for massive speed gains.
* **HNSW (Hierarchical Navigable Small World):** The industry standard indexing algorithm for VDBs.
* **Mechanism:** A multi-layered graph structure. Searches begin at the sparse top layer and "zoom in" to denser layers to find local neighborhoods in $\mathcal{O}(\log N)$ time.

**Speaker Notes:**
If you have ten million chunks of text in your database, calculating the Cosine Similarity against all ten million vectors for every single search query will bring your server to a halt. We cannot use exhaustive search. VDBs use algorithms called Approximate Nearest Neighbor, or ANN. The most dominant algorithm today is HNSW. It builds a hierarchical graph. It drops your query into a sparse upper layer, finds the general neighborhood, drops down a layer, gets closer, and repeats until it hits the target. It turns a linear time problem into logarithmic time.

---

## Slide 8: VDB Payload Design (Metadata matters)
### CIS 531/731 - Lecture 15
* **The "Naked Vector" Problem:** A retrieved vector `[0.34, -0.12, ...]` is useless if you don't know what text it came from.
* **The Payload:** A JSON object appended to the vector inside the database.
* **Required Provenance Fields for ASR:**
  * `chunk_text`: The actual string of words.
  * `source_file`: The origin video/audio file.
  * `timestamp_start` / `timestamp_end`: For jumping to the video playback.
  * `speaker_id`: For diarization context.

**Speaker Notes:**
This is the most common architectural mistake juniors make when building RAG pipelines. They embed their text, load the vectors into the database, run a search, and the database returns a matching vector. But a vector is just numbers! The database must store the actual text chunk and its provenance data alongside the vector. We call this the Payload or Metadata. For our ASR project, if a semantic search returns a match, we need the payload to contain the exact timestamp so we can click a link and jump directly to that moment in the original video. 

---

## Slide 9: Hybrid Search (Dense Vectors + Keyword Filtering)
### CIS 531/731 - Lecture 15
* **The Limitation of Pure Semantics:** Sometimes you *do* want exact keyword matching (e.g., filtering by a specific Name, Date, or ID).
* **Pre-filtering vs. Post-filtering:**
  * *Pre-filtering:* Filtering the dataset by metadata first, then running the vector search on the remainder (can ruin the HNSW index navigation).
  * *Post-filtering:* Searching the whole vector space, then removing results that don't match the metadata.
* **Hybrid Search Engines:** Modern VDBs (like Qdrant) execute both lexical BM25 (keyword) and dense vector searches simultaneously, merging the results using Reciprocal Rank Fusion (RRF).

**Speaker Notes:**
Vector search is incredible for finding concepts, but it's terrible at exact constraints. If I want to find "discussions about neural networks, but ONLY from the year 2024," semantic search struggles with the "2024" constraint. This is where Hybrid Search comes in. You combine the relational power of metadata filtering with the semantic power of dense vectors. Modern databases let you apply hard filters to the payload before or during the HNSW graph traversal. 

---

## Slide 10: Preparation for Lab 3
### CIS 531/731 - Lecture 15
* **Next Class (Friday):** Hands-on Pipeline Execution.
* **Your Deliverables:**
  1. Load your ASR `.vtt` or `.txt` files.
  2. Instantiate a recursive character text splitter.
  3. Load the `all-MiniLM-L6-v2` embedding model.
  4. Design your Payload JSON schema.
  5. Push the embeddings and payloads into a local Qdrant or Chroma VDB collection.
* **Check your Environment:** Ensure your `sentence-transformers` and vector DB Python clients are installed and tested before the lab begins.

**Speaker Notes:**
That covers the theory of the Scrub phase. On Friday, we build it. Lab 3 requires you to take your raw ASR outputs from last week, chunk them, embed them using MiniLM, and push them into a local vector database instance. Make sure you have thought through your payload schema. What metadata do you need to make your chunks useful when retrieved? Ensure your Python environment is ready. See you on Friday.
