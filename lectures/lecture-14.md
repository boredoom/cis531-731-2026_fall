# CIS 531/731: Introduction to Data Science

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase 2:** Pipeline Execution | **Module 5:** Scrub: Chunking & Embedding Generation | **Lecture 14:** Scrub: Chunking & Text Normalization | Monday, September 28, 2026 |

---

## Slide 1: Welcome to the Scrub Phase
### CIS 531/731 - Lecture 14
* **Pipeline Status:** Transitioning from data acquisition (Obtain) to data normalization (Scrub).
* **The Raw Data Reality:** ASR (Automatic Speech Recognition) streams are inherently messy and unstructured.
* **Core Objective 1:** Text normalization and noise reduction.
* **Core Objective 2:** Structural segmentation via text chunking.
* **The Handoff:** Preparing clean, bounded text strings for embedding models.

**Speaker Notes:**
Welcome to Module 5. Last week, we successfully captured and transcribed audio using Whisper. You now have gigabytes of raw ASR data. But if you feed that raw data directly into a machine learning model, the model will choke. Today, we enter the "Scrub" phase of the data science lifecycle. We are going to take that messy, continuous stream of text, clean it up, and chop it into perfectly sized, semantically meaningful blocks that our future embedding models can actually digest.

---

## Slide 2: The Anatomy of Raw ASR Data
### CIS 531/731 - Lecture 14
* **Lack of Punctuation:** Continuous streams often lack periods, commas, or question marks.
* **Disfluencies:** "Um", "uh", stutters, and false starts are transcribed verbatim.
* **Formatting Inconsistencies:** Numbers (7 vs. seven) and acronyms (NASA vs. N.A.S.A.) appear randomly.
* **Timestamp Artifacts:** SubRip (.srt) or WebVTT (.vtt) files contain interleaved metadata.
* **The Imperative:** We must strip the noise before we can extract the signal.

**Speaker Notes:**
Let's look at what Whisper actually gives you. It is not a beautifully formatted essay. If it's a live ASR stream, it often lacks punctuation entirely. It includes every stutter and "um" the speaker uttered. If you pull from a VTT file, the text is surrounded by timestamps and formatting tags. Your first job as a data scientist is to write parsing scripts to strip out the metadata, normalize the acronyms, and filter out the disfluencies so the core semantic meaning is exposed.

---

## Slide 3: Text Normalization Techniques
### CIS 531/731 - Lecture 14
* **Regular Expressions (Regex):** The foundational tool for pattern matching and metadata stripping.
* **Casing:** Converting all text to lowercase to reduce the vocabulary space (when case semantic value is low).
* **Stop Word Removal:** Stripping high-frequency, low-meaning words (the, is, at, which) to dense the data.
* **Lemmatization:** Converting words to their base dictionary form (e.g., "running" to "run").
* **Warning:** Aggressive normalization can destroy the nuanced context required for Large Language Models.

**Speaker Notes:**
To clean the text, we deploy standard NLP normalization techniques. You will use Regex to strip out HTML tags and timestamps. You might use lemmatization to reduce the complexity of the vocabulary. However, a word of warning: while stripping stop words was standard practice ten years ago, modern LLMs and transformer models actually rely on those words to understand sentence structure. You must tailor your normalization strategy to the specific model you intend to use down the pipeline.

---

## Slide 4: The Necessity of Chunking
### CIS 531/731 - Lecture 14
* **Token Limits:** Transformer models (like BERT or LLaMA) have strict maximum context windows (e.g., 512 or 8192 tokens).
* **Memory Constraints:** Passing infinite text requires infinite VRAM.
* **Semantic Dilution:** A massive document contains too many conflicting concepts for a single vector to represent accurately.
* **Retrieval Precision:** Searching for a specific fact is impossible if the database returns an entire 40-page transcript.

**Speaker Notes:**
Once the text is clean, we hit a hardware limit. You cannot pass a 3-hour lecture transcript into an embedding model. Transformer architecture relies on a fixed token window. If the model only accepts 512 tokens, it will simply truncate and ignore anything past that limit. Furthermore, if you embed an entire chapter of a book into one vector, the mathematical meaning gets diluted into a grey slurry. To retrieve specific information later, we must break the document down into bite-sized pieces.

---

## Slide 5: Fixed-Size Chunking
### CIS 531/731 - Lecture 14
* **The Mechanism:** Splitting text by a hard character or token count (e.g., exactly 256 tokens per chunk).
* **Implementation:** Extremely simple array slicing in Python.
* **Advantage:** Guarantees perfect compliance with model input limits.
* **Disadvantage:** Completely blind to linguistic structure.

**Speaker Notes:**
The easiest way to chunk text is Fixed-Size Chunking. You write a Python script that counts 256 tokens, cuts the string, and starts a new chunk. It is fast, computationally cheap, and guarantees you will never crash your embedding model with an oversized input. But it is entirely blind. It doesn't know what a sentence is. It doesn't know what a paragraph is. It just cuts exactly at the character limit, regardless of the context. 

---

## Slide 6: The Boundary Problem
### CIS 531/731 - Lecture 14
* **Severed Context:** Fixed-size chunking often splits a sentence right down the middle.
* **Pronoun Resolution:** The noun is in Chunk A, but the pronoun ("he", "it") is in Chunk B.
* **Information Loss:** The semantic meaning of the concept is destroyed because the context is split across two database entries.
* **The Result:** The Retrieval-Augmented Generation (RAG) system fails to find the correct answer.

**Speaker Notes:**
Because fixed-size chunking is blind, it creates the Boundary Problem. Imagine a sentence saying: "The primary architect of this system was Dr. Smith, and he designed it in 2026." If the chunk boundary hits right after "Smith," Chunk B starts with "and he designed it in 2026." If you search the database for "Who designed the system?", Chunk B contains the answer, but the model has no idea who "he" is. The semantic link is severed, and your pipeline fails.

---

## Slide 7: Recursive Character Chunking
### CIS 531/731 - Lecture 14
* **The Mechanism:** A hierarchical approach to splitting text, attempting to respect human formatting.
* **The Hierarchy:** Tries to split by double newline (paragraphs), then single newline, then periods, then spaces.
* **The Logic:** If a paragraph exceeds the token limit, it breaks it down by sentences. If a sentence exceeds it, it breaks by words.
* **The Standard:** This is the default chunker used in frameworks like LangChain.

**Speaker Notes:**
To solve the Boundary Problem, we use Recursive Character Chunking. Instead of a hard chop, this algorithm tries to be smart. It looks at the text and tries to split it at double line breaks, keeping paragraphs together. If a paragraph is too long for the token limit, it falls back to splitting by periods, keeping sentences together. Only as a last resort will it split a sentence mid-word. This preserves the human-readable formatting of the document as much as possible.

---

## Slide 8: Semantic and Syntax-Aware Chunking
### CIS 531/731 - Lecture 14
* **NLP Parsing:** Using libraries like `spaCy` or `NLTK` to analyze the grammatical structure of the text.
* **Sentence Boundary Detection (SBD):** Intelligently identifying the end of sentences, even with tricky punctuation (e.g., "Dr. Smith").
* **Topic Modeling:** Segmenting text when the algorithm detects a shift in the underlying subject matter.
* **Tradeoff:** Highly accurate semantic preservation, but significantly higher computational cost during ingestion.

**Speaker Notes:**
If we want to be even more precise, we can deploy Semantic Chunking. Using Natural Language Processing libraries like `spaCy`, we can teach the chunker to understand grammar. It can execute Sentence Boundary Detection to guarantee it never splits a thought in half. Advanced semantic chunkers even analyze the meaning of the words and create a break only when the topic changes. The tradeoff is speed. Parsing grammar takes CPU cycles, making your ingestion pipeline much slower.

---

## Slide 9: The Overlap (Stride) Technique
### CIS 531/731 - Lecture 14
* **The Safety Net:** Intentionally duplicating a portion of text across adjacent chunks.
* **The Parameter:** `chunk_overlap` (usually set to 10-20% of the `chunk_size`).
* **Example:** Chunk 1 ends with words 400-500. Chunk 2 *begins* with words 400-500.
* **The Benefit:** Heals the Boundary Problem by ensuring context and pronouns are preserved across the slice.

**Speaker Notes:**
Regardless of which chunking strategy you use, you must implement a "Stride," also known as Chunk Overlap. This is a safety net. If our chunk size is 500 tokens, we might set an overlap of 50 tokens. This means the last 50 tokens of Chunk 1 are duplicated and become the first 50 tokens of Chunk 2. This guarantees that if a concept or a pronoun spans the boundary line, both chunks contain enough surrounding context for the embedding model to understand the meaning.

---

## Slide 10: Preparing for the Vector Handoff
### CIS 531/731 - Lecture 14
* **The Output:** A Python list or array of perfectly formatted, overlapping string chunks.
* **Metadata Attachment:** Every chunk must retain a reference to its source file, speaker, and timestamp.
* **The Next Step:** Passing these string chunks through a Transformer model to generate vector embeddings.
* **Lab Prep:** Ensure your Python environment has `langchain-text-splitters` and `sentence-transformers` installed before Wednesday.

**Speaker Notes:**
By the end of your Scrub pipeline, you no longer have a massive text file. You have an array of overlapping, clean strings. But before we move to the next step, you must attach metadata to each chunk. A chunk must know what file it came from and who said it, or it will be useless when retrieved. On Wednesday, we will take this array of strings and pass it through a neural network to convert them into mathematical vectors. Please ensure your Python environments are ready.
