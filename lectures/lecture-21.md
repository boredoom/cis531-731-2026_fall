# CIS 531/731: Introduction to Data Science
## Lecture 21: Wrap-Up & Module 6 Synthesis
**Date:** Friday, October 16, 2026

---

## 1. MP5 Submission Review: GenAI/LLM Candidates
*Reflecting on yesterday's machine problem submissions.*

### Architectural Successes
* **Structured Output Enforcement:** The most robust pipelines abandoned conversational parsing and utilized strict JSON schemas or Pydantic output parsers to force the LLM to return machine-readable dictionaries.
* **Fallback Mechanisms:** Successful pipelines wrapped their LLM calls in `try/except` blocks with exponential backoff to gracefully handle rate limits and API timeouts.

### Common Pitfalls
* **The "Knowledge Piñata" Anti-Pattern:** Treating the LLM as a database query rather than a reasoning engine. Failing to provide ground-truth text context in the prompt led to hallucinated classifications.
* **Prompt Fragility:** Minor changes in whitespace or instructional phrasing drastically altering output distributions, highlighting the brittleness of zero-shot approaches compared to deterministic code.
* **Missing Error Handling:** Unhandled JSON decoding errors crashing the entire data pipeline when the LLM appended conversational filler (e.g., "Here is your JSON:").

## 2. Computational Cost Realities
*Integrating GenAI into a data pipeline is not free. We must analyze the thermodynamic and financial constraints of these architectures.*

### Cloud API vs. Local Open-Weight (vLLM)
* **Cloud APIs (OpenAI, Anthropic):** High latency (network dependency), pay-per-token models. Highly capable but presents data privacy risks and scales poorly for processing millions of rows in a batch DataFrame.
* **Local Execution:** Zero recurring financial cost, complete data privacy, but bounded by VRAM. Deploying a 7B parameter model in FP16 requires ~14GB of VRAM, making quantization (GGUF/AWQ) a necessity for consumer hardware.
* **Throughput Metrics:** Transitioning from "Time to First Token" (TTFT) to "Tokens per Second." For classification tasks, TTFT is the dominant bottleneck if batching is not implemented.

## 3. Limitations of Few-Shot Prompting
*When does in-context learning fail, and when must we revert to traditional statistical models?*

* **Context Window Saturation:** Stuffing a prompt with 50 examples (K-shot) dilutes the attention mechanism. The model may suffer from the "Lost in the Middle" phenomenon, over-indexing on the first and last exemplars while ignoring the core rules.
* **Deep Semantic Tropes:** Complex, culturally nuanced classifications (e.g., separating "Tsundere" from "Yandere" character tropes) often exceed the capacity of simple few-shot prompting because the semantic boundaries are highly non-linear.
* **The Mathematical Necessity of Trained Classifiers:** If inference latency must be sub-10ms, or if the classification boundary requires finding a complex hyperplane in a dense embedding space, a traditional ML classifier (SVM, XGBoost) trained on LLM embeddings is mathematically and operationally superior to prompting a 70B parameter model.

## 4. Module 6 Synthesis: LLMs as Programmatic Tools
*Moving beyond the chatbot interface.*

* **LLMs as Functions:** In a mature data science pipeline, an LLM is simply a probabilistic function in a Directed Acyclic Graph (DAG). It takes a string, applies a stochastic transformation based on its weights, and returns a string.
* **Separation of Concerns:**
  * Use traditional code (Python/Pandas) for routing, filtering, counting, and deterministic logic.
  * Use embeddings (`sentence-transformers`) for similarity, search, and dense representation.
  * Use generative LLMs *only* for synthesis, summarization, and complex zero-shot classification where rigid heuristics fail.

## 5. Preview of Module 7: Visualization & Generational Drift
*Where do we go from here?*

* **Dimensionality Reduction:** Now that we have high-dimensional embeddings and classifications, how do we plot them? Next week, we introduce **UMAP** and **t-SNE** to project 768-dimensional vectors down to 2D/3D space.
* **Tracking Concept Drift:** Exploring how classifications and clusters move over time (e.g., how the semantic usage of specific words or tropes shifts across generations).
* **Dashboarding:** Transitioning from static Jupyter Notebooks to interactive Streamlit dashboards to visualize the outputs of our OSEMN pipelines.
