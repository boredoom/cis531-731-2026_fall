# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase IV:** Explore & Model | **Module 7:** Explore: Data Visualization & Dashboards | **Lecture 23:** Embedding-Space Visualization (UMAP) | Wednesday, October 21, 2026 |

---

## Slide 1: Embedding-Space Visualization (UMAP) - Agenda
### CIS 531/731 - Lecture 23
* **The High-Dimensional Problem:** Sparsity and the curse of dimensionality.
* **Dimensionality Reduction Survey:** PCA, t-SNE, and UMAP comparisons.
* **UMAP Mechanics:** Topological data analysis and fuzzy simplicial sets.
* **Hyperparameter Tuning:** Balancing local structure vs. global topography.
* **VDB & Clustering Pipelines:** Applying HDBSCAN to projected embeddings.

**Speaker Notes:**
Welcome back. In the previous lecture, we covered standard 2D data visualization and dashboard architectures. Today, we transition to a fundamental problem in modern AI pipelines: how do we visualize data that has 768 or 1536 dimensions? We cannot natively plot transformer embeddings. To interpret vector database spaces and identify semantic drift, we must project these embeddings down to 2D or 3D. Today we focus exclusively on Uniform Manifold Approximation and Projection (UMAP), its mathematical underpinnings, and how to tune it for exploratory data analysis.

---

## Slide 2: The Curse of Dimensionality
### Navigating High-Dimensional Space
* **Volume Expansion:** As dimensions increase, the volume of the space increases exponentially, making available data extremely sparse.
* **Distance Metric Breakdown:** In high-dimensional space, the ratio between the nearest and farthest data points approaches 1, rendering Euclidean distance less meaningful.
* **The Necessity of Projection:** To perform visual EDA or clustering, we must force this high-dimensional manifold into a visually interpretable 2D or 3D coordinate system.

**Speaker Notes:**
When we extract text embeddings from a model like BERT or sentence-transformers, we typically get a 768-dimensional float array. The "curse of dimensionality" means that in a 768-dimensional space, almost all points are incredibly far apart, and standard distance metrics start to behave counter-intuitively. If we want to verify that our embedding model actually separates "news articles" from "fiction," we have to compress that space down to a screen. But we must do so carefully to avoid destroying the inherent relationships.

---

## Slide 3: Dimensionality Reduction Survey
### PCA vs. t-SNE vs. UMAP
* **Principal Component Analysis (PCA):** Linear projection preserving global variance; extremely fast but fails to capture complex, non-linear manifolds.
* **t-SNE:** Non-linear projection excellent for separating local clusters; highly computationally expensive and actively destroys global distance relationships.
* **UMAP:** Non-linear topological projection; preserves both local clustering and global macro-structure, with superior computational scaling over t-SNE.

**Speaker Notes:**
Historically, data scientists started with PCA. It's fast and deterministic, but it's a linear transformation. If your embeddings form a complex, folded shape like a Swiss roll, PCA will just flatten it, destroying the clusters. For a long time, t-SNE was the gold standard for non-linear clustering, but it scales terribly with large datasets and destroys global context—a cluster in the top left of a t-SNE plot isn't necessarily related to the cluster next to it. UMAP is the modern standard because it is mathematically grounded in topology, runs significantly faster, and preserves the global distances between distinct clusters.

---

## Slide 4: UMAP Fundamentals
### Topological Data Analysis (TDA)
* **Manifold Assumption:** Real-world high-dimensional data is distributed along lower-dimensional manifolds embedded within the high-dimensional space.
* **Local Riemannian Geometry:** UMAP assumes that the data is uniformly distributed on this manifold, defining a customized local distance metric for each data point.
* **Topological Representation:** The algorithm builds a mathematical representation of this manifold before attempting any dimensionality reduction.

**Speaker Notes:**
The core idea behind UMAP is Topological Data Analysis. It assumes your 768-dimensional embeddings aren't just random noise; they form a lower-dimensional shape, or manifold. UMAP's brilliant assumption is that the data is uniformly distributed on this shape. Because data in the real world is rarely uniform, UMAP bends the concept of "distance." For points in sparse regions, the distance ruler is stretched; for points in dense clusters, the ruler is shrunk. This creates a uniform topological structure we can then map.

---

## Slide 5: UMAP Mechanics
### Simplicial Sets and Optimization
* **Fuzzy Simplicial Sets:** UMAP constructs a weighted graph connecting points in the high-dimensional space, representing the structural topology.
* **Low-Dimensional Initialization:** A low-dimensional representation is initialized (often using Spectral Embedding) to serve as the starting canvas.
* **Cross-Entropy Optimization:** Stochastic Gradient Descent (SGD) minimizes the cross-entropy between the high-dimensional graph and the low-dimensional graph to align them.

**Speaker Notes:**
Mechanically, UMAP works in two phases. First, it builds a graph in the high-dimensional space. Points that are close together are connected by strong edges; points far apart have weak or non-existent edges. This is the "fuzzy simplicial set." Second, it creates a 2D canvas and starts moving points around. It uses Stochastic Gradient Descent to minimize a loss function—specifically cross-entropy. It constantly checks the 2D layout against the high-dimensional graph, pulling connected points together and pushing disconnected points apart until the layouts match as closely as possible.

---

## Slide 6: Hyperparameter Tuning
### The Role of `n_neighbors`
* **Definition:** Dictates the number of nearest neighboring points used when constructing the initial high-dimensional graph.
* **Low Values (e.g., 5-15):** Forces UMAP to focus strictly on local structure, resulting in highly fragmented, fine-grained clusters.
* **High Values (e.g., 50-200):** Forces UMAP to view the data broadly, preserving the "big picture" global topology at the expense of local detail.

**Speaker Notes:**
UMAP is not a black box; it requires tuning. The most critical parameter is `n_neighbors`. If you set it to a low number like 5, you are telling the algorithm, "Only care about the 5 points closest to you." This creates tightly packed, isolated little islands of data—great for finding micro-genres or edge cases. If you set it to 100, the algorithm considers a wider radius. The clusters will blend together more, but the distances *between* the distinct groups will be much more accurate, giving you a better global map of the semantic space.

---

## Slide 7: Hyperparameter Tuning
### The Role of `min_dist`
* **Definition:** Controls how tightly UMAP is allowed to pack points together in the final low-dimensional projection.
* **Low Values (e.g., 0.0 to 0.1):** Allows points to stack almost on top of each other, creating extremely dense, sharp clusters for clear separation.
* **High Values (e.g., 0.5 to 0.9):** Prevents points from overlapping, resulting in a looser, more evenly dispersed scatter plot.

**Speaker Notes:**
While `n_neighbors` controls the mathematical graph, `min_dist` controls the literal visual aesthetic of the output. It acts as a physical repulsive force in the 2D projection. Setting it near zero allows UMAP to clump points into tight, distinct blobs. This is excellent for clustering tasks where you just want to see group boundaries. However, if you actually want to hover over points and read the underlying text or view the images on a dashboard, a low `min_dist` causes massive overlapping. In that case, you increase `min_dist` to spread the points out so they remain individually visible.

---

## Slide 8: Vector Database (VDB) Integration
### The Projection Pipeline
* **Extraction:** Querying the Vector Database (e.g., Milvus, Qdrant) to retrieve raw dense embeddings and associated metadata.
* **Projection:** Passing the $N \times 768$ matrix into the fitted UMAP transformer to yield an $N \times 2$ or $N \times 3$ matrix.
* **Dashboard Binding:** Injecting the 2D/3D coordinates into plotting libraries (Plotly/Dash) alongside metadata for interactive hovering.

**Speaker Notes:**
In your assignments, UMAP does not exist in a vacuum. It sits downstream from your Vector Database. Your pipeline will typically execute a broad query to extract thousands of vectors, transform them via UMAP, and then push those coordinates into a front-end UI. This pipeline is what transforms a sterile database index into a navigable "map" of semantic meaning. When you connect the metadata—like author, date, or text content—to the scatter plot, you enable powerful exploratory data analysis.

---

## Slide 9: Semantic Clustering
### Applying HDBSCAN
* **The Clustering Challenge:** UMAP provides coordinates, but we need algorithms to definitively assign data points to discrete categories.
* **HDBSCAN:** Hierarchical Density-Based Spatial Clustering of Applications with Noise; an algorithm that excels at finding clusters of varying densities.
* **Out-of-Distribution Detection:** HDBSCAN explicitly models "noise," allowing the pipeline to identify anomalous embeddings that do not belong to any core semantic group.

**Speaker Notes:**
UMAP is for visualization, not clustering. It gives you 2D coordinates, but it doesn't assign labels. To group the data automatically, we apply a clustering algorithm to the UMAP output. K-Means is a poor choice here because UMAP clusters are rarely perfectly spherical. Instead, we use HDBSCAN. HDBSCAN looks for areas of high density and can handle arbitrary shapes. More importantly, it doesn't force every point into a cluster. If an embedding sits in the empty space between clusters, HDBSCAN flags it as noise. This is critical for catching out-of-distribution data or model hallucinations.

---

## Slide 10: Wrap-Up & Transition
### Preparing for Dashboards
* **UMAP's Utility:** The definitive method for compressing semantic embedding spaces while retaining human-interpretable topological structure.
* **Pipeline Readiness:** You now have the mathematical intuition required to tune `n_neighbors` and `min_dist` based on your visualization goals.
* **Next Class: Lab Session:** Friday's lab (Lecture 24) will combine UMAP projections with Streamlit/Dash to build the Generational Drift Dashboard for MP7.

**Speaker Notes:**
To summarize, UMAP is your primary lens for inspecting what your AI models are actually learning. By tuning the neighbors and distance parameters, you can zoom in on local anomalies or zoom out to see the global semantic landscape. On Friday, we will put this into practice. We are going to pull chronologically sequenced embeddings, run them through UMAP, and build a dashboard that tracks how certain tropes or genres migrate across the embedding space over time. Make sure you have reviewed the basic UMAP parameters documentation before the lab.
