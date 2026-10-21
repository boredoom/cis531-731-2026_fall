# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture(s) | Date(s) |
| :--- | :--- | :--- | :--- |
| **Phase [X]:** [Phase Name] | **Module 6:** GenAI & LLMs: Candidates, Code, Classification | **Lectures 17-21** | Mon 05 Oct - Fri 16 Oct 2026 |

---

## Lecture 17: GenAI & LLMs: Candidates, Code, Classification (Mon 05 Oct)

1. **Language Modeling Fundamentals:** Introduction to $N$-gram models, perplexity, and the transition from count-based to dense neural representations (Jurafsky & Martin, Ch. 6).
2. **Transformer Architecture Overview:** The attention mechanism, self-attention, and the foundational architecture underlying modern Large Language Models.
3. **The Pretraining & Fine-Tuning Paradigm:** Understanding how foundational models acquire broad language representations and are subsequently tuned for specific downstream data science tasks.
4. **LLMs as Classifiers:** Shifting from generative text completion to using LLM token probabilities and embeddings for strict classification mapping.
5. **Prompting vs. Fine-Tuning Trade-offs:** Analyzing the computational cost, accuracy, and latency differences between zero/few-shot prompting and full model fine-tuning.

---

## Lecture 18: Few-Shot Trope/Genre Classification (Wed 07 Oct)

1. **The In-Context Learning (ICL) Paradigm:** Leveraging the LLM's pre-trained knowledge base to classify text (e.g., media tropes) without updating model weights.
2. **Prompt Engineering for Classification:** Designing strict formatting constraints and system instructions to force the LLM to output clean, parsable classification labels.
3. **The Few-Shot Exemplar Selection:** Determining how to select high-leverage $K$-shot examples that define the boundary conditions of complex genres or tropes.
4. **Hugging Face `pipeline` API:** Utilizing the `transformers` library to initialize local, open-weight text classification models.
5. **Handling Out-of-Distribution Data:** Strategies for managing LLM hallucinations or default behaviors when presented with novel genres or unseen media data.

*(Note: Friday 09 Oct 2026 – NO CLASS / Wildcat Pause Day)*

---

## Lecture 19: Model Selection & Embedding-Backed Classification Lab (Mon 12 Oct)

1. **MP6 Release & Requirements:** Reviewing the expectations for the embedding-backed classification machine problem.
2. **Embedding Models vs. Generative Models:** Understanding why a specialized embedding model (e.g., `sentence-transformers`) is often superior to a generative LLM for clustering and similarity-based classification.
3. **Distance Metrics for Classification:** Utilizing Cosine Similarity and Euclidean distance in the embedding space to classify unknown texts against known trope/genre anchors.
4. **Building the Reference Index:** Constructing the "gold standard" vector database of known tropes to serve as the classification lookup table.
5. **Thresholding and Confidence:** Establishing mathematical thresholds for "Unknown" or "Mixed" classifications when distance metrics fall in the boundary zones.

---

## Lecture 20: Trope/Genre Classification Workshop (Wed 14 Oct)

1. **Execution Troubleshooting:** Live debugging of Hugging Face environment setups, CUDA/CPU execution issues, and memory management constraints.
2. **Pipeline Integration:** Connecting the output of the semantic search (Module 5) directly into the classification prompt or embedding comparator.
3. **Evaluating Classifier Performance:** Transitioning from subjective "looks good" evaluations to rigorous metrics (Precision, Recall, F1) for the trope classifications.
4. **Handling Ambiguous Media:** Strategies for classifying multi-genre media or texts containing conflicting tropes using weighted probabilities.
5. **Code Review & Refactoring:** Peer review of classification pipelines to ensure robust error handling and adherence to FAIR principles.

---

## Lecture 21: Wrap-Up (Fri 16 Oct)

1. **MP5 Submission Review:** Common pitfalls and architectural successes observed in the GenAI/LLM Candidates submission (due prior day).
2. **Computational Cost Realities:** Analyzing the latency and hardware requirements of the deployed classification pipelines.
3. **Limitations of Few-Shot Prompting:** When does the LLM fail to capture deep semantic tropes, and when is a dedicated trained classifier mathematically necessary?
4. **Module 6 Synthesis:** Summarizing the integration of LLMs into the data science pipeline as robust, programmatic tools rather than conversational chatbots.
5. **Preview of Module 7:** Transitioning from data extraction and classification to visualization (UMAP) and generational drift dashboarding.