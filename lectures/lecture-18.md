# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 3:** LLMs in Data Pipelines | **Module 6:** GenAI & LLMs: Candidates, Code, Classification | **Lecture 18:** Few-Shot Trope/Genre Classification | Wed, Oct 07, 2026 |

---

## Slide 1: Few-Shot Trope/Genre Classification
### CIS 531/731 - Lecture 18
* **The Goal:** Transitioning from conversational chatbots to deterministic classification engines.
* **The Method:** In-Context Learning (ICL) without updating model weights.
* **The Constraint:** Strict prompt engineering to yield parsable JSON or categorical tokens.
* **The Tech Stack:** Hugging Face `pipeline`, local open-weight models, and Python integration.
* **The Edge Cases:** Handling Out-of-Distribution (OOD) data and algorithmic hallucinations.

**Speaker Notes:**
Welcome to Lecture 18. Today, we are officially leaving behind standard, run-of-the-mill Yelp review and SEC filing sentiment grinds. We are moving into advanced generative classification. Our goal is to take complex, subjective cultural media—whether that is parsing the "doomed youth" trope across modern music, or identifying specific xianxia and wuxia role ontologies in Chinese television dramas like *Pursuit of Jade*—and programmatically classify them using LLMs.

---

## Slide 2: The In-Context Learning (ICL) Paradigm
### Pre-trained Knowledge vs. Weight Updates
* **Supervised Fine-Tuning (SFT):** Requires thousands of labeled examples to calculate gradient updates and physically alter model weights.
* **In-Context Learning (ICL):** Uses the frozen foundational model's existing parametric memory to infer relationships.
* **The Workspace:** The context window acts as a temporary, programmable workspace for your classification rules.

**Speaker Notes:**
In classical machine learning, teaching a model to classify a new genre required collecting thousands of labeled examples and calculating gradient updates. In-Context Learning (ICL) changes the physics of the pipeline. We are leveraging the model's vast pre-trained knowledge base to classify text on the fly. You provide the definitions and the task within the prompt itself. The weights of the model are frozen, but the context window acts as your temporary programming environment.

---

## Slide 3: ICL Latency and Trade-offs
### When to Prompt vs. When to Train
* **Speed to Prototype:** ICL allows for zero-day deployment of new classification categories.
* **Inference Latency:** Sending a massive prompt with definitions and examples for every query heavily increases token processing time.
* **Context Limits:** Bounded by the maximum token context window of the target model.

**Speaker Notes:**
Why wouldn't we just use ICL for everything? The trade-off is inference latency and cost. If you fine-tune a small BERT model, you can pass it raw text and get an instant label. With an LLM using ICL, you have to pass your entire instruction set, your definitions, and your examples *every single time* you query it. For a pipeline processing a million social media posts, that token overhead becomes a massive computational and financial bottleneck. We use ICL to prove the schema, and we train models to scale it.

---

## Slide 4: Prompt Engineering for Classification
### Forcing Deterministic Pipeline Outputs
* **The Parsing Problem:** Downstream dataframes (Pandas/PySpark) crash if the LLM outputs conversational filler (e.g., "I think this is...").
* **Formatting Constraints:** Designing system instructions that explicitly prohibit conversational prefixes.
* **Schema Enforcement:** Utilizing JSON schemas or exact string-matching arrays (e.g., `["Sci-Fi", "Fantasy", "Horror"]`).

**Speaker Notes:**
If your LLM returns "I think this text represents the 'Chosen One' trope," your data pipeline instantly breaks. We are building automated systems, not chat interfaces. Prompt engineering for classification requires writing instructions that physically constrain the model's output. You must force the LLM to output clean, parsable classification labels—like a raw JSON object or a single string token—so that your downstream data engineering stages can ingest the results without throwing parsing errors.

---

## Slide 5: Role Prompting & System Instructions
### Anchoring the Latent Space
* **System Prompting:** The top-level instruction that defines the model's operational boundary.
* **Role Assignment:** "You are an expert media trope classifier operating in a strict data pipeline."
* **Negative Constraints:** Explicitly defining what the model must *not* do (e.g., "Do not provide explanations for your label").

**Speaker Notes:**
To get reliable classifications, you must anchor the model's latent space using the System Prompt. You are setting the rules of the game. By telling the model "You are an expert media trope classifier," you are statistically biasing its token generation toward academic or analytical distributions rather than creative writing. Furthermore, you must employ negative constraints: explicitly forbidding the model from explaining its reasoning, unless you have specifically requested a Chain-of-Thought output for a separate analysis pipeline.

---

## Slide 6: The Few-Shot Exemplar Selection
### Calibrating the Decision Boundary
* **$K$-Shot Learning:** Injecting $K$ highly representative examples (input-output pairs) into the prompt.
* **Zero-Shot vs. Few-Shot:** Providing zero examples relies entirely on the model's default alignment; providing examples overrides default biases.
* **Format Mirroring:** Exemplars must perfectly match the exact input structure and desired output schema of the target task.

**Speaker Notes:**
How do you teach a model to identify complex, highly subjective tropes? You use few-shot exemplars. If you are classifying media, giving the model $K=3$ examples is often enough to anchor its understanding. This is called Few-Shot learning. By providing exact input-to-output pairs in your prompt, you show the model exactly how you expect it to format its answer, effectively overriding its RLHF training to be conversational and chatty.

---

## Slide 7: Defining Boundary Conditions
### High-Leverage Edge Cases
* **Selecting Exemplars:** Do not choose obvious examples; choose examples that define the border between classes.
* **Sub-genre Precision:** Distinguishing "Lovecraftian cosmic dread" from standard "slasher horror".
* **Thematic Mashups:** Providing exemplars to handle overlapping boundaries (e.g., distinguishing hard sci-fi from an *Ex Machina* / AI-thriller mashup).

**Speaker Notes:**
The trick to $K$-shot learning is selecting high-leverage examples. If you want it to classify "Lovecraftian lore," don't just give it the most obvious Cthulhu text; give it a subtle example involving shoggoths or non-Euclidean geometry to define the boundary condition of the genre. If you are classifying sci-fi tropes, give it an exemplar separating hard sci-fi from a thematic mashup like *Ex Machina*. The quality of your boundary-condition examples dictates the accuracy of your classifier.

---

## Slide 8: Hugging Face `pipeline` API
### Local Open-Weight Execution
* **The `transformers` Library:** The industry-standard Python ecosystem for downloading and executing language models.
* **Pipeline Abstraction:** Using `pipeline("text-generation")` to abstract away tokenization and tensor operations.
* **Data Sovereignty:** Deploying open-weight models locally (e.g., Llama 3, Qwen) to eliminate API costs and protect proprietary datasets.

**Speaker Notes:**
While commercial APIs are powerful, true data science independence requires owning your execution environment. We will use the Hugging Face `pipeline` API to initialize local, open-weight models. By utilizing the `transformers` library, you can download a model, tokenize your text, and run the classification loop entirely on your own GPU or lab cluster. This eliminates rate limits, protects your data privacy, and ensures your pipeline remains reproducible regardless of external corporate API deprecations.

---

## Slide 9: Handling Out-of-Distribution (OOD) Data
### Detecting Novel Genres and Hallucinations
* **Defining OOD Media:** Texts or tropes that fall completely outside the model's pre-training distribution or few-shot exemplars.
* **The "Eager to Please" Bias:** LLMs will hallucinate a classification rather than admit ignorance unless explicitly permitted to fail.
* **Fallback Mechanisms:** Creating a deterministic "Unknown" or "Other" catch-all category.

**Speaker Notes:**
What happens when your model, which you calibrated for fantasy tropes like *The Lord of the Rings*, suddenly ingests a dataset of modern cyber-security logs? That is Out-of-Distribution (OOD) data. LLMs are notoriously eager to please; if they don't know the answer, they will confidently hallucinate one. Your pipeline must account for this. You need to implement strict fallback strategies in your prompt, explicitly giving the model permission to classify an input as "Unknown" or "Unclassified" rather than polluting your database.

---

## Slide 10: Probability Thresholds & Confidence
### Mathematical Fallbacks for Generative Pipelines
* **Logit Extraction:** Accessing the raw token probabilities (logits) before the model applies a softmax function.
* **Confidence Thresholding:** Rejecting classification outputs where the probability of the top token falls below a defined threshold (e.g., $< 0.85$).
* **Flagging for Human Review:** Routing low-confidence or OOD outputs to a separate queue for manual annotation and future few-shot exemplar inclusion.

**Speaker Notes:**
For true pipeline robustness, we cannot just rely on the text output. When you run local open-weight models through Hugging Face, you can access the raw token probabilities, or logits. If the model outputs "Sci-Fi" but the probability is only 51%, the model is guessing. Your pipeline must establish mathematical thresholds. If the confidence falls below 85%, your script should drop the AI's label and flag that record for human review. Those flagged records often become your best candidates for new few-shot examples in your next iteration.
