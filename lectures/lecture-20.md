# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 3:** Scrub & Embed | **Module 6:** GenAI & LLMs: Candidates, Code, Classification | **Lecture 20:** Trope/Genre Classification Workshop | Wednesday, October 14, 2026 |

---

## Slide 1: Workshop Overview & Agenda
### CIS 531/731 - Lecture 20
* **Execution Troubleshooting:** Live debugging of Hugging Face environments, CUDA/CPU execution, and memory constraints[cite: 31].
* **Pipeline Integration:** Connecting semantic search outputs (Module 5) to classification prompts[cite: 31].
* **Evaluating Performance:** Transitioning from subjective evaluations to rigorous metrics (Precision, Recall, F1)[cite: 31].
* **Handling Ambiguous Media:** Strategies for multi-genre media and conflicting tropes via weighted probabilities[cite: 31].
* **Code Review & Refactoring:** Ensuring robust error handling and adherence to FAIR principles[cite: 31].

**Speaker Notes:**
Welcome to Lecture 20. Today is a hands-on workshop. We are moving from the theory of few-shot classification into the engineering reality of making these pipelines run without crashing our clusters. We will cover environment troubleshooting, how to properly stitch your vector database outputs into your LLM prompts, and how we actually score these models mathematically rather than just saying "the output looks right."

---

## Slide 2: Execution Troubleshooting: The Environment
### Managing Hugging Face, CUDA, and Memory
* **The DevContainer Baseline:** Ensure your isolated VS Code DevContainer is properly mounting the hardware resources.
* **OOM (Out of Memory) Errors:** Loading a 70B parameter model on a single GPU will crash; understand your VRAM constraints.
* **Hardware Fallbacks:** Implementing graceful CPU execution fallbacks for testing when CUDA/GPU clusters (Beocat/Bridges-2) are saturated[cite: 31].
* **Quantization:** Utilizing 4-bit or 8-bit loading to fit capable classifiers into available VRAM.

**Speaker Notes:**
The first blocker most of you hit this week isn't algorithmic; it's physics. VRAM is finite. If you are trying to load a massive Hugging Face model without quantization, you will hit an OOM error. Today we are enforcing the DevContainer workflow so that your environments are reproducible. If you cannot get a GPU node right now, your code must have a graceful fallback to CPU execution so you can verify your pipeline logic using a smaller distilled model.

---

## Slide 3: Pipeline Integration: Bridging the Gap
### Connecting Semantic Search (Module 5) to Classification (Module 6)
* **The Integration Handshake:** Vector database retrieval must feed seamlessly into your inference engine[cite: 31].
* **Context Injection:** Passing the top-$K$ semantic search results as context payloads inside the LLM prompt.
* **Token Limits:** Ensuring the retrieved context plus your few-shot exemplars do not exceed the model's maximum context window.
* **Deterministic Formatting:** Enforcing strict JSON outputs to prevent the LLM from generating un-parsable conversational text.

**Speaker Notes:**
We do not use LLMs in this course as chatbots; we use them as functional components. This means Pipeline Integration is critical. You must take the semantic search outputs you built in Module 5 and inject them as context into your Module 6 classifier. The pipeline will break if you don't manage your token limits or if you let the LLM output conversational fluff. You must enforce deterministic, parsable outputs.

---

## Slide 4: Evaluating Classifier Performance
### Moving Beyond "Looks Good"
* **Subjectivity is not Data Science:** We cannot evaluate trope classification by eye; we need mathematical baselines[cite: 31].
* **Precision:** Out of all the items the model classified as Trope X, how many were actually Trope X?[cite: 31]
* **Recall:** Out of all the true Trope X items in the dataset, how many did the model successfully find?[cite: 31]
* **The F1 Score:** The harmonic mean of Precision and Recall, providing a single robust metric for unbalanced datasets[cite: 31].

**Speaker Notes:**
If your evaluation plan is "I read the outputs and they look right," you do not have an evaluation plan. We are evaluating classifier performance rigorously. Because tropes and genres are often highly unbalanced in datasets, accuracy is a misleading metric. We must calculate Precision, Recall, and the F1 Score to prove our pipeline is actually functioning as a reliable classifier.

---

## Slide 5: The Evaluation Artifact
### Structuring the Metrics Output
* **The Evaluation Script:** Your pipeline must include a dedicated script (e.g., `evaluate_classifier.py`) to compute these metrics.
* **Confusion Matrices:** Visualizing false positives and false negatives to diagnose where the model's boundary logic fails.
* **Automated Logging:** Utilizing tracking tools (e.g., MLflow) or simple JSON/CSV ledgers to record evaluation metrics across different prompt versions.

**Speaker Notes:**
To calculate those metrics, you need an evaluation artifact. You should be generating confusion matrices to see exactly where your model is struggling. If it's confusing "Cyberpunk" with "Steampunk", the confusion matrix will show that bleed-over, and you can adjust your few-shot exemplars accordingly. 

---

## Slide 6: Handling Ambiguous Media
### Multi-Genre and Conflicting Tropes
* **The Real-World Messiness:** Media rarely fits perfectly into a single, mutually exclusive category.
* **Multi-Label Classification:** Configuring your pipeline to assign multiple valid labels to a single artifact[cite: 31].
* **Weighted Probabilities:** Utilizing model logits or explicitly prompted confidence scores to handle conflicting tropes[cite: 31].
* **Thresholding:** Establishing a mathematical cutoff (e.g., probability > 0.85) before officially accepting a classification label.

**Speaker Notes:**
Handling ambiguous media is where this task gets difficult. Real-world text often contains conflicting tropes. Instead of forcing a single label, your classification strategy should handle multi-genre media using weighted probabilities. If the model is only 51% confident, your pipeline should threshold that out or flag it for manual review rather than accepting a low-confidence hallucination.

---

## Slide 7: Code Review & Refactoring
### Hardening the Pipeline
* **FAIR Principles:** Ensuring your code and data artifacts are Findable, Accessible, Interoperable, and Reusable[cite: 31].
* **Robust Error Handling:** Wrapping API calls and inference steps in `try/except` blocks to prevent single-record failures from crashing the entire batch job[cite: 31].
* **Peer Review Focus:** Identifying hardcoded paths, missing dependencies in the `requirements.txt`, and undocumented functions[cite: 31].

**Speaker Notes:**
We will spend the next block doing live code review and refactoring. I want you focused on robust error handling and FAIR principles. If your pipeline crashes on record 9,999 out of 10,000 because of a malformed Unicode character, and you lose all your compute progress, that is an engineering failure. Wrap your inference steps and save your intermediate states.

---

## Slide 8: Live Workshop: Pipeline Debugging
### Interactive Session
* **Step 1:** Verify local or remote GPU execution environment.
* **Step 2:** Execute a small test batch (e.g., $N=10$) through the full Semantic Search -> Classification pipeline.
* **Step 3:** Review the raw output formatting. Is it strictly structured?
* **Step 4:** Run the evaluation script and verify Precision/Recall metrics calculate without throwing errors.

**Speaker Notes:**
Let's get into the code. I want everyone to verify their environments, run a minimal viable test batch of 10 records, and trace the data through the entire pipeline. Check your outputs. If it's spitting out paragraphs instead of JSON, fix your prompt constraints now before you burn compute time on the full dataset.

---

## Slide 9: Post-Execution Telemetry
### Validating the Results Manifest
* **Artifact First:** The primary deliverable of this pipeline is the empirical data (the classification outputs and metrics).
* **Reproducibility:** Can another student clone your repository, run your DevContainer, and achieve the exact same F1 score?
* **Documenting Limitations:** Honestly logging where the few-shot prompting failed to capture deep semantic tropes[cite: 31].

**Speaker Notes:**
As you finalize your pipelines today, remember our Artifact First policy. Your results manifest and metrics must be committed to your repository. Furthermore, you need to document your limitations. Where does few-shot prompting fail? When do we actually need to train a dedicated classifier? Honesty about your model's limitations is the hallmark of good data science.

---

## Slide 10: Wrap-Up & Next Steps
### Module 6 Conclusion
* **MP5 Deadline Exception:** A reminder that MP 5 (Structured Streaming) is due on Monday, October 19, an exception extended to observe Wildcat Pause Day.
* **Module 6 Synthesis:** We have successfully integrated LLMs as programmatic, evaluatable data science tools[cite: 31].
* **Preview of Module 7:** Next week we transition from extraction and classification to visualization (UMAP) and generational drift dashboarding[cite: 31].
* **Action Item:** Commit all workshop refactoring updates to your repositories before logging off.

**Speaker Notes:**
To wrap up Module 6: we have moved LLMs out of the chat window and into the programmatic data science pipeline. Please remember that MP 5 is due this coming Monday the 19th. Make sure you commit all your code from today's workshop. Next week, we start Module 7, where we will take these high-dimensional embeddings and classifications and visualize them using tools like UMAP. Have a good afternoon.
