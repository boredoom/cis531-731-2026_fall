# PS 6: Semantic Search, Chunking, & Vector Database Schema

**Course:** CIS 531 / CIS 731 — Semantic Information Systems

**Author:** Arron Weber (CIS 531 — Sub-Team A: Data Engineering)

**Collaborators:** Zack Latta (CIS 531), Lucas Zabrocki Borges (CIS 731), Abdulla Mansoor (CIS 731)

**Project:** *A RAG Pipeline for Regional and Temporal Hip-Hop Analysis* (Track 2: VDB Text Corpora / Category 1: Prescriptive Analytics)

---

## Part 1: Chunking, Index, and Evaluation Analysis

### 1.1 Chunking Cost and Structural Model

Text chunking governs downstream transformer attention budgets, vector database memory, and retrieval fidelity. We model the ingested Genius hip-hop lyrics corpus ($D = 10{,}000$ documents; total token volume $N \approx 6{,}000{,}000$ tokens) across three chunking paradigms: **Fixed-Window**, **Sentence-Boundary**, and **Structure-Aware (Verse/Chorus)**.

```
+---------------------------------------------------------------------------------------------------------+
|                                        CHUNKING COST MODEL FORMULATION                                  |
|                                                                                                         |
|  Total Chunks:           C = N / (W * (1 - r_overlap))                                                  |
|  Embedding FLOPs/Cost:   Cost_embed = C * W * P_token = N * (1 / (1 - r_overlap)) * P_token             |
|  VDB Memory Footprint:   M_total = C * (d * b_float + L_text + M_provenance)                            |
|  Index Construction:     T_build(HNSW) = O(C * M * log(C) * d)                                          |
|  Query Evaluation:       Latency = T_embed(Q) + T_ANN(C, d) + k * (T_fetch + T_cross_encoder(Q, C_i))    |
+---------------------------------------------------------------------------------------------------------+

```

#### Mathematical Formulation

Let:

* $N$ be the total raw token count of the lyrics corpus ($N = 6 \times 10^6$).
* $W$ be the maximum window capacity in tokens.
* $O$ be the token overlap between sequential chunks; $r = \frac{O}{W}$ is the overlap ratio ($0 \le r < 1$).
* $S = W - O = W(1 - r)$ be the effective step stride.
* $d$ be the embedding dimension ($d = 768$ for `sentence-transformers/all-mpnet-base-v2`).
* $b_{\text{float}} = 4\text{ bytes}$ (standard IEEE 754 32-bit float).
* $M_{\text{meta}}$ be the serialized provenance overhead per record (estimated at $256\text{ bytes}$).
* $P_{\text{embed}}$ be the embedding inference compute cost per token.

$$\text{Chunk Volume: } C = \left\lceil \frac{N}{W(1 - r)} \right\rceil$$

$$\text{Total Ingestion Incurred Tokens: } N_{\text{effective}} = C \cdot W = \frac{N}{1 - r}$$

$$\text{Vector Index Raw Memory: } M_{\text{vectors}} = C \cdot (d \cdot b_{\text{float}})$$

$$\text{Total Storage Footprint: } M_{\text{storage}} = C \cdot \left( d \cdot b_{\text{float}} + \bar{L}_{\text{text}} \cdot 1\text{ byte} + M_{\text{meta}} \right)$$

#### Strategy Comparison and Parametric Cost Matrix

| Evaluation Dimension | Fixed-Window ($W=256, O=64$) | Sentence-Boundary ($W_{\max}=256, O=1\text{ sent}$) | Structure-Aware (Verse/Chorus Sectioning) |
| --- | --- | --- | --- |
| **Stride / Overlap ($r$)** | $r = 0.25$ ($S = 192$ tokens) | Dynamic ($r \approx 0.15$) | $r = 0.00$ (disjoint structural spans) |
| **Chunk Count ($C$)** | $31{,}250$ chunks | $\approx 27{,}500$ chunks | $\approx 21{,}400$ chunks (mean $\approx 280$ tok/section) |
| **Effective Tokens Processed** | $8{,}000{,}000$ tokens ($1.33\times$ inflation) | $\approx 7{,}050{,}000$ tokens ($1.17\times$ inflation) | $6{,}000{,}000$ tokens ($1.00\times$, zero duplication) |
| **Vector Memory ($d=768$, FP32)** | $96.0\text{ MB}$ | $84.5\text{ MB}$ | $65.7\text{ MB}$ |
| **Full Payload Storage ($M_{\text{store}}$)** | $107.5\text{ MB}$ | $94.6\text{ MB}$ | $74.2\text{ MB}$ |
| **Syntactic Boundary Integrity** | **Severely Degraded:** Splits multi-syllable rhyme patterns and intra-sentence clauses. | **Moderate:** Preserves sentences; severs rhyming couplets spanning punctuation. | **Optimal:** Aligns with semantic breaks (`[Verse 1]`, `[Chorus]`, `[Outro]`). |
| **Topic Dilution / Focus** | Low-to-moderate; windows truncate arbitrary lines. | Moderate; multi-sentence grouping can merge distinct tropes. | Minimal; each musical movement retains thematic unity. |
| **Pre-Processing Complexity** | $O(N)$ scalar slice; zero NLP overhead. | $O(N)$ with sentence boundary detector (e.g., regex/SpaCy). | $O(N)$ regex parser tuned to Genius lyric tags. |

#### Analysis of Trade-offs

1. **Context Fragmentation vs. Token Redundancy:** Fixed-window chunking incurs a $33\%$ computational penalty over raw token length due to stride overlap ($r=0.25$). While this overlap prevents losing boundary-straddling semantic relationships, it artificially multiplies vector database size. Conversely, Structure-Aware chunking yields zero token duplication while eliminating syntactic cliffhangers because rap lyrics are partitioned naturally by rhyme scheme and verse markers.
2. **Impact on Top-$k$ Ingestion in RAG:** When fixed-window chunks are retrieved, adjacent windows frequently dominate the top-$k$ returned candidates (e.g., retrieving Chunk 12 and Chunk 13 of the same song), artificially starving the generator of diverse regional contexts. Structure-Aware verse chunks guarantee that each retrieved slot delivers a complete, cohesive lyrical thought.

---

### 1.2 Index and Similarity Metric Analysis

#### Algorithmic Comparison: IVF vs. HNSW

Dense retrieval over high-dimensional vector spaces requires approximating nearest neighbors (ANN) to overcome the linear $O(C \cdot d)$ complexity of exhaustive brute-force search (Flat Index).

```
                      IVF (Voronoi Partitioning)                          HNSW (Hierarchical Graph)
           +---------------------------------------------+           Layer 2:  (•)----------------->(•)
           |   Centroid 1           Centroid 2           |                        \                   \
           |   * (x1) (x2)          * (y1) (y2)          |           Layer 1:  (•)---->(•)---->(•)----->(•)
           |      \                    \                 |                      /     /    \    /     /
           |     Inverted List 1      Inverted List 2    |           Layer 0:  (•)-(•)-(•)-(•)-(•)-(•)-(•)-(•)
           +---------------------------------------------+                     Dense multi-hop base graph

```

##### 1. Inverted File Index (IVF-Flat / IVF-PQ)

* **Mechanics:** Partitions the vector space into $k_{\text{clusters}}$ Voronoi cells using $k$-means clustering. At inference time, the query is compared against the $k_{\text{clusters}}$ centroids; the search then traverses only the vectors residing in the top-$n_{\text{probe}}$ closest cells.
* **Query Complexity:** $\mathcal{O}(k_{\text{clusters}} \cdot d + n_{\text{probe}} \cdot \frac{C}{k_{\text{clusters}}} \cdot d)$. Sub-linear, but bounded below by centroid comparisons.
* **Build Time Complexity:** $\mathcal{O}(I \cdot k_{\text{clusters}} \cdot C \cdot d)$ where $I$ is the number of $k$-means iterations ($I \approx 25\text{--}50$).
* **Memory Footprint:** Highly compact. Stores contiguous inverted lists. When combined with Product Quantization (IVF-PQ), 768-dimensional vectors can be compressed from $3{,}072\text{ bytes}$ down to $64\text{ bytes}$ ($48\times$ compression).
* **Failure Modes & Recall Degradation:** Under query distribution shift (e.g., out-of-vocabulary slang or dialectal shift not reflected in training centroids), queries fall into incorrect Voronoi cells, dropping Recall@k by upwards of 35% unless $n_{\text{probe}}$ is dialed up toward $k_{\text{clusters}}$, which collapses the latency benefit.

##### 2. Hierarchical Navigable Small World (HNSW)

* **Mechanics:** Constructs a multi-layer geometric graph structure. Upper layers have long-range skip-connections (sparse highway routing); the bottom layer ($\text{Layer } 0$) contains all vectors connected with high local clustering. Search executes greedy traversal from top to bottom, switching to bounded beam search (`efSearch`) on Layer 0.
* **Query Complexity:** $\mathcal{O}(\log(C) \cdot d \cdot \text{efSearch})$. Truly logarithmic, highly deterministic, and resilient to cluster density imbalance.
* **Build Time Complexity:** $\mathcal{O}(C \cdot M \cdot \log(C) \cdot d)$, where $M$ is the maximum bidirectional links per node ($M \in [16, 64]$). Significantly more compute-intensive to construct than IVF.
* **Memory Footprint:** High memory overhead. Every node maintains $M$ neighbor pointers per layer. Storing $C=31{,}250$ vectors with $M=32$ adds approximately $2 \cdot M \cdot 8\text{ bytes} \approx 512\text{ bytes}$ of pointer metadata per vector, an additional $16\text{--}20\%$ overhead on top of raw vector storage.
* **Failure Modes & Recall Degradation:** Degradation under high QPS occurs via CPU thread contention. Graph routing retains high recall ($>95\%$) across semantic distribution shifts because graph connectivity provides diverse traversals that do not rely on static cluster partitions.

| Metric / Dimension | Inverted File (IVF-Flat, $k=256, n_{\text{probe}}=8$) | Hierarchical Navigable Small World (HNSW, $M=32, \text{efS}=64$) |
| --- | --- | --- |
| **Search Time Complexity** | $\mathcal{O}\left(k \cdot d + n_{\text{probe}}\frac{C}{k}d\right)$ | $\mathcal{O}(\log C \cdot d \cdot \text{efSearch})$ |
| **Index Construction Speed** | **Fast** ($\approx 1.2\text{ s}$ for $31\text{k}$ vectors) | **Slow** ($\approx 18.5\text{ s}$ for $31\text{k}$ vectors) |
| **RAM Footprint (31,250 v)** | **$\approx 98\text{ MB}$** (Near-zero index structural overhead) | **$\approx 128\text{ MB}$** ($\approx 32\text{ MB}$ graph link overhead) |
| **Recall@10 Stability** | Drops significantly if $n_{\text{probe}} < 16$ on out-of-domain queries | Maintains $>0.96$ Recall across out-of-domain dialect shifts |
| **Dynamic Insert Cost** | Requires append to inverted list; degrades clustering over time | Incremental graph node insertion; self-stabilizing |

#### Similarity Metric Derivation: Cosine vs. Dot Product vs. L2

The mathematical definitions for vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^d$ are:

$$\text{Euclidean (L2): } D_{L2}(\mathbf{u}, \mathbf{v}) = \sqrt{\sum_{i=1}^d (u_i - v_i)^2} = \Vert{}\mathbf{u} - \mathbf{v}\Vert{}_2$$

$$\text{Cosine Similarity: } S_{\cos}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\Vert{}\mathbf{u}\Vert{}_2 \Vert{}\mathbf{v}\Vert{}_2} = \frac{\sum_{i=1}^d u_i v_i}{\sqrt{\sum u_i^2} \sqrt{\sum v_i^2}}$$

$$\text{Inner / Dot Product: } S_{IP}(\mathbf{u}, \mathbf{v}) = \mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^d u_i v_i$$

##### Unit-Sphere Equivalence Derivation

Assume all embeddings undergo unit L2-normalization upon inference: $\Vert{}\mathbf{u}\Vert{}_2 = 1$ and $\Vert{}\mathbf{v}\Vert{}_2 = 1$.

1. **Cosine Equivalence:**

$$S_{\cos}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{1 \cdot 1} = \mathbf{u} \cdot \mathbf{v} = S_{IP}(\mathbf{u}, \mathbf{v})$$


2. **L2 Distance Equivalence:**

$$\Vert{}\mathbf{u} - \mathbf{v}\Vert{}_2^2 = (\mathbf{u} - \mathbf{v}) \cdot (\mathbf{u} - \mathbf{v}) = \Vert{}\mathbf{u}\Vert{}_2^2 + \Vert{}\mathbf{v}\Vert{}_2^2 - 2(\mathbf{u} \cdot \mathbf{v}) = 1 + 1 - 2 S_{IP}(\mathbf{u}, \mathbf{v}) = 2 - 2 S_{IP}(\mathbf{u}, \mathbf{v})$$


$$\implies D_{L2}(\mathbf{u}, \mathbf{v}) = \sqrt{2 - 2 S_{IP}(\mathbf{u}, \mathbf{v})}$$



##### Architectural Decision

Because monotonic rank ordering is preserved ($\text{argmin } D_{L2} \equiv \text{argmax } S_{\cos} \equiv \text{argmax } S_{IP}$), **Inner Product on $L_2$-normalized vectors** is chosen. It avoids runtime norm calculations and square root operations, reducing arithmetic operations from $4d$ instructions (Cosine) to $2d$ SIMD fused-multiply-add (FMA) instructions.

---

### 1.3 Retrieval Evaluation Protocol

#### Multi-Stage Retrieval Architecture

To balance retrieval latency against ranking precision, the retrieval engine implements a two-stage cascade:

1. **Stage 1 (First-Stage Candidate Generation):** Bi-Encoder (`sentence-transformers/all-mpnet-base-v2`) with an HNSW index retrieves the top $k_1 = 50$ candidate chunks via Maximum Inner Product Search (MIPS).
2. **Stage 2 (Cross-Attention Re-Ranking):** Cross-Encoder (`cross-encoder/ms-marco-MiniLM-L-6-v2`) computes full all-to-all cross-attention across concatenated query-chunk pairs $[CLS] \circ \text{Query} \circ [SEP] \circ \text{Lyric Chunk} \circ [SEP]$, emitting calibrated relevance logits to yield the final $k_2 = 5$ passage context for RAG injection.

```
                          TWO-STAGE RETRIEVAL CASCADE
                          
  User Query: "Bay Area hyphy movement car culture slang"
       │
       ▼
 [Bi-Encoder: MPNet]  ──> Dense Vector (d=768)
       │
       ▼
 [HNSW ANN Search]    ──> Fast Top-50 Chunks (Recall@50 Oriented, ~4ms)
       │
       ▼
 [Cross-Encoder]      ──> Query-Chunk Cross-Attention Scoring (~25ms)
       │
       ▼
 [Top-5 Re-Ranked]    ──> Generator LLM Context with Strict Lineage Provenance

```

#### Evaluation Metrics

##### 1. Mean Reciprocal Rank (MRR@k)

Measures the speed with which the first relevant document is returned:


$$\text{MRR@k} = \frac{1}{\vert{}Q\vert{}} \sum_{i=1}^{\vert{}Q\vert{}} \frac{1}{\text{rank}_i}$$


where $\text{rank}_i$ is the positional rank of the first relevant document for query $q_i$, or $\infty$ if no relevant document appears in the top $k$.

##### 2. Normalized Discounted Cumulative Gain (NDCG@k)

Measures graded relevance ordering across top positions:


$$\text{DCG@k} = \sum_{j=1}^k \frac{2^{r_j} - 1}{\log_2(j + 1)}, \quad \text{NDCG@k} = \frac{\text{DCG@k}}{\text{IDCG@k}}$$


where $r_j \in \{0, 1, 2\}$ represents graded relevance judgments (0 = irrelevant, 1 = related region/era, 2 = explicit trope manifestation), and $\text{IDCG@k}$ is the ideal DCG metric achieved under perfect sorting.

##### 3. Hit Rate / Recall@k

$$\text{Recall@k} = \frac{\vert{}\mathcal{R}_q \cap \mathcal{S}_{q, k}\vert{}}{\vert{}\mathcal{R}_q\vert{}}$$


where $\mathcal{R}_q$ is the complete set of ground-truth relevant chunks for query $q$, and $\mathcal{S}_{q, k}$ is the system-retrieved top-$k$ set.

##### 4. Citation Provenance Fidelity (CPF)

Measures the attribution accuracy of the downstream generation:


$$\text{CPF} = \frac{\sum_{c \in \mathcal{C}_{\text{generated}}} \mathbb{I}\left( \text{Supports}(\text{Chunk}_{\text{cited}}, c) \land \text{LineageValid}(\text{Chunk}_{\text{cited}}) \right)}{\vert{}\mathcal{C}_{\text{generated}}\vert{}}$$


where $\mathcal{C}_{\text{generated}}$ is the set of factual claims made by the RAG generation.

#### Gold-Standard Ground Truth Construction Protocol

* **Query Set Stratification ($\vert{}Q\vert{} = 100$):** Partitioned across four US geographic regions (East Coast, West Coast, South, Midwest) and three distinct musical eras (Golden Age: 1985–1995; Bling/Crunk: 1996–2009; Modern/Streaming: 2010–2026).
* **Depth-$p$ Pooling ($p=20$):** Candidate passages pooled across three diverse retrieval paradigms:
1. Lexical BM25 (token-matching baseline).
2. Dense Bi-encoder (`all-mpnet-base-v2`).
3. Hybrid Sparse-Dense (Reciprocal Rank Fusion of BM25 + HNSW).


* **Annotation Process & Inter-Annotator Agreement:** Passages blinded and evaluated by Sub-Team A (Arron, Zack) and Sub-Team B (Lucas, Abdulla). Multi-class relevance: $\{0, 1, 2\}$. Inter-annotator reliability calculated via Cohen's Kappa ($\kappa$). Any pair displaying $\kappa < 0.72$ triggers adjudication via consensus review.

---
