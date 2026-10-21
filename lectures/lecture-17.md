# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase [X]:** [Phase Name] | **Module 6:** GenAI & LLMs: Candidates, Code, Classification | **Lecture 17:** GenAI & LLMs: Candidates, Code, Classification | Monday, October 05, 2026 |

---

## Slide 1: Welcome to Module 6
### CIS 531/731 - Lecture 17
* **Transition:** From Semantic Search/VDBs to Generative AI capabilities.
* Language Modeling Fundamentals ($N$-grams to Neural).
* Transformer Architecture Overview.
* The Pretraining & Fine-Tuning Paradigm.
* LLMs as Classifiers (Not just Chatbots).
* Prompting vs. Fine-Tuning Trade-offs.

**Speaker Notes:**
Welcome to Module 6. Over the last two weeks, we scrubbed data and built Vector Databases to execute semantic searches. We learned how to represent text as numbers. Today, we bridge the gap from *representing* text to *generating* and *classifying* it using Large Language Models. Our primary goal in this module is to break the habit of treating GenAI as a magical chatbot. In data science, an LLM is a function. It takes an input, calculates probabilities, and returns an output. We are going to learn how to lock that function down so we can use it to classify massive datasets reliably.

---

## Slide 2: Language Modeling Fundamentals
### From Counting to Predicting
* **The Goal of a Language Model:** To calculate the probability of the next word given the previous words: $P(w_t | w_{1:t-1})$.
* **$N$-gram Models (The Old Way):** Counting how often words appear together in a corpus. 
 * *Limitation:* The curse of dimensionality (you can't count sequences that never appeared).
* **Neural Language Models (The New Way):** Using dense embeddings to guess the next word based on semantic meaning, not just exact string matches.
* **Perplexity:** The standard metric. How "surprised" is the model by the actual next word? Lower is better.

**Speaker Notes:**
Before Transformers existed, language modeling was fundamentally a counting game. If you wanted to know the next word after "I drink", you looked at a massive database and counted whether "water" or "coffee" showed up more often. These were $N$-gram models. They were brittle. If a phrase never appeared in the training data, its probability was zero. Neural models changed this by using the embeddings we learned about in Module 5. Because "water" and "juice" are close in embedding space, the model can predict "juice" even if it never saw that exact sentence before.

---

## Slide 3: Transformer Architecture Overview
### The Attention Mechanism
* **The Problem with RNNs/LSTMs:** They process text sequentially. They forget the beginning of a long paragraph by the time they reach the end.
* **The Solution:** The Transformer (Vaswani et al., 2017 - "Attention Is All You Need").
* **Self-Attention:** Every word in the input sequence looks at *every other word* simultaneously to calculate relevance weights.
* **Parallelization:** Because there is no sequential bottleneck, Transformers can be trained on thousands of GPUs simultaneously.

**Speaker Notes:**
In 2017, natural language processing changed permanently. Before Transformers, neural networks read text like humans do: one word at a time, left to right. This is slow and prone to forgetting context. The Transformer architecture threw out sequential reading. It looks at the entire paragraph at once. It uses a mathematical operation called "Self-Attention," where every single word asks every other word, "How relevant are you to my current meaning?" Because it processes everything at once, we could suddenly train models on internet-scale data using massive GPU clusters.

---

## Slide 4: The Pretraining Paradigm
### Building the Foundation
* **Pretraining (Self-Supervised Learning):** Training a model on terabytes of raw internet text.
* **The Task:** "Predict the next token." (Autoregressive language modeling).
* **The Result:** A Base Model (e.g., Llama-3-Base). It understands grammar, facts, and logic, but it doesn't know how to follow instructions.
* **Cost:** Millions of dollars and thousands of GPU-hours. You will likely never do this yourself.

**Speaker Notes:**
How do you build a model like ChatGPT? Step one is Pretraining. You take a massive Transformer and feed it a significant chunk of the public internet. You don't give it labels or tasks; you just play a game. You hide the next word, make the model guess, and penalize it if it's wrong. Over trillions of words, the model learns grammar, history, coding, and reasoning just by figuring out the statistical patterns of human language. This produces a "Base Model." It's incredibly smart, but it's like a library with no librarian—it just wants to autocomplete text, not answer your questions.

---

## Slide 5: The Fine-Tuning Paradigm
### Teaching the Model to Be Useful
* **Supervised Fine-Tuning (SFT):** Training the Base Model on thousands of high-quality Q&A pairs to teach it a specific format (Instruction Tuning).
* **Alignment (RLHF):** Reinforcement Learning from Human Feedback. Training the model to be polite, helpful, and avoid generating toxic content.
* **The Result:** An Instruct Model (e.g., Llama-3-Instruct).
* **Data Science Application:** You can fine-tune a model on *your specific data* (e.g., medical records) for a few hundred dollars.

**Speaker Notes:**
To make the Base Model useful, we have to Fine-Tune it. We give it thousands of examples of a human asking a question and a human providing a perfect answer. This teaches the model the "Instruction" format. Then, companies apply RLHF—having humans rate the AI's answers to teach it to be polite and safe. For data science, fine-tuning is your secret weapon. You don't need a supercomputer. You can take an open-source Base model and spend $50 on a cloud GPU to fine-tune it on 5,000 examples of your company's proprietary data, creating a highly specialized expert.

---

## Slide 6: LLMs as Classifiers
### Breaking the Chatbot Illusion
* **Generative Mode:** "Write me a poem about data science." (High temperature, high variance).
* **Classification Mode:** "Given this text, output ONLY the word 'POSITIVE' or 'NEGATIVE'."
* **The Data Science Mandate:** When using LLMs in a pipeline, we must aggressively constrain their output.
* **Logit Extraction:** Instead of reading the text output, we can look at the raw probability scores (logits) the model assigned to the tokens "POSITIVE" and "NEGATIVE".

**Speaker Notes:**
Most people interact with LLMs through a chat interface, generating emails or brainstorming ideas. As data scientists, we often want the exact opposite. If I have a database of 100,000 product reviews, I don't want the AI to talk to me. I want a script that feeds in a review, and the AI outputs exactly one word: Positive, Negative, or Neutral. We must engineer our prompts and API calls to strip away the chatbot persona and turn the LLM into a deterministic classification engine. If the AI outputs "Sure, I'd be happy to help! The sentiment is Positive," it just broke your Python pipeline.

---

## Slide 7: Zero-Shot vs. Few-Shot Prompting
### Guiding the Classification
* **Zero-Shot:** Giving the model the task with no examples.
 * *Prompt:* "Classify this review: 'The battery died in an hour.' Sentiment:"
* **Few-Shot:** Giving the model 3-5 high-quality examples of the exact input/output format you expect.
 * *Prompt:* "Review: 'Loved it' -> POSITIVE. Review: 'Terrible' -> NEGATIVE. Review: 'The battery died' ->"
* **The Benefit of Few-Shot:** Drastically reduces hallucinations and forces the model to mimic your exact required output syntax.

**Speaker Notes:**
When you ask an LLM to classify data without giving it any examples, that is called Zero-Shot prompting. It works okay for simple tasks, but it's brittle. The model might output "Negative" one time and "Very Bad" the next time. To lock the pipeline down, we use Few-Shot prompting. You embed 3 to 5 perfect examples directly into your prompt string. You show the model exactly what the input looks like, and exactly the rigid format you expect for the output. Transformers are incredible pattern matchers; if you show them a pattern three times, they will almost always follow it on the fourth.

---

## Slide 8: Prompting vs. Fine-Tuning Trade-offs
### The Engineering Decision
| Feature | Few-Shot Prompting | Fine-Tuning |
| :--- | :--- | :--- |
| **Setup Time** | Minutes (Write a prompt) | Days (Format dataset, train) |
| **Cost to Build** | ~$0 (Just API calls) | ~$50 - $500 (GPU rental) |
| **Inference Cost** | High (Sending huge prompts every time) | Low (Short prompts) |
| **Performance** | Good (General tasks) | Excellent (Niche/Domain specific) |

**Speaker Notes:**
In your projects, you will face a choice: Do I just write a really good prompt (Few-Shot), or do I actually fine-tune the model weights? Few-shot prompting is fast and cheap to test. But there is a hidden cost: if your prompt includes 5 long examples, you pay for all those input tokens every single time you classify a new row in your database. Fine-tuning takes a lot of upfront work to build a dataset, but once the model is trained, you only have to send the raw input. For a massive pipeline running millions of rows, fine-tuning is almost always cheaper in the long run.

---

## Slide 9: MP5 Release & Logistics
### Candidates, Code, Classification
* **The Task:** You will use an open-weight model via Hugging Face to classify a dataset of text excerpts into specific Tropes or Genres.
* **The Constraint:** You must use Python to iterate over a dataframe. You cannot use a web chat interface.
* **The Deliverable:** A Jupyter Notebook demonstrating Zero-Shot failure vs. Few-Shot success, plus the final classified output `.csv`.
* **Due Date:** Thursday before Week 8 wrap-up.

**Speaker Notes:**
This brings us to MP5, which is released today. You are going to build a classification pipeline. You will take a dataset of text—like movie plots or book summaries—and use a Hugging Face model to classify them into specific tropes. You will be writing Python code that passes data to the model and parses the response. A major grading criteria is demonstrating the difference between Zero-Shot and Few-Shot. I want to see the model fail to format correctly on a Zero-Shot prompt, and then I want to see you fix it by passing a well-engineered Few-Shot prompt. 

---

## Slide 10: Preparation for Wednesday
### Deep Dive into Hugging Face & Trope Classification
* **Wednesday's Lecture:** We will look at the exact Python code required to load a model using the Hugging Face `pipeline` API.
* **The Problem of Ambiguity:** How do we handle texts that don't fit neatly into one category?
* **Reading Assignment:** Complete Jurafsky & Martin, Chs. 6–8. 
* **Action Item:** Make sure your Python environment has `transformers` and `torch` installed before class.

**Speaker Notes:**
On Wednesday, we are moving from theory to code. We will open up a notebook and write the actual pipeline to load a model locally using Hugging Face. We will also talk about the messy reality of data science: what happens when your text contains two conflicting tropes? How do we extract the probability scores instead of just the text? Please ensure you have read the chapters on Language Models in Jurafsky and Martin, and make sure your DevContainers or local environments have the Hugging Face `transformers` library installed so you can follow along.