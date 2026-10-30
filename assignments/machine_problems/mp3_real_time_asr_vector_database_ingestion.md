# MP 3: Real-Time ASR & Vector Database Ingestion
**Whisper Transcriptions, FAISS Embeddings, & Trope Ontologies**

**📅 Due:** Sun 04 Oct 2026, 11:59 PM CDT | **💯 Points:** 30 | **👥 Team:** Individual (GitHub PR & Canvas submission)

> **🚨 CRITICAL SUBMISSION POLICY**
> **Minimum Quantum of Work (Execution Floor):** This assignment establishes an immutable baseline of execution. You must successfully execute the core regex modification in PySpark and successfully ingest a transcription into your local FAISS database. Do not reduce the scope of the problem if you encounter environment friction; resolve the friction using your DevContainer.

## 1. Overview
Execute the PySpark Scrub pipeline with modified regex to preserve hyphenated compound words, and demonstrate end-to-end integration by transcribing local audio via OpenAI Whisper, mapping it to latent space, and retrieving it via FAISS semantic search.

### Required Laboratory Notebooks
* **Lab 2: The "Scrub" Stage:** Data Cleaning, Text Tokenization & TF-IDF Feature Extraction in PySpark (`lab02.ipynb`).
* **Lab 3a: Local ASR:** Initializing local OpenAI Whisper for audio stream transcriptions (`lab03a.ipynb`).
* **Lab 3b: VDB Acquisition:** Generating latent embeddings via Hugging Face and indexing in FAISS (`lab03b.ipynb`).

## 2. Initiating Your Draft (The AI Kit Procedure)
Use the Generative AI Kit to help structure your submission. Follow these stages to systematically break down your assignment:

1. **Environment Initialization:** Open and execute `lab02.ipynb` within your local or containerized SparkSession.
2. **Regex Modification:** Update the `regexp_replace` function in Part 2 to ensure hyphenated compound words are retained as single tokens.
3. **Corpus Transcription:** Execute `lab03a.ipynb` to download the public-domain WWI Poetry archive, extract Wilfred Owen's "Anthem for Doomed Youth," and run local Whisper transcription.
4. **VDB Ingestion & Integration:** Pass the Whisper transcript text into `lab03b.ipynb` to embed via `all-MiniLM-L6-v2` and index in FAISS.
5. **Semantic Verification & Disk I/O:** Query for `"doomed youth"` to verify retrieval, and (for CIS 731 graduate students) implement disk I/O persistence via `faiss.write_index`.

## 3. Required Document Structure
Your submission must be a **GitHub Pull Request link and completed Jupyter Notebooks (`.ipynb` files) with executed cell outputs submitted via Canvas** containing the following sections exactly as named below. 

* **Part 1: The Scrub Pipeline & Hyphenation Parsing (15 Points):** Completed `lab02.ipynb` notebook showing the modified PySpark SQL regex maintaining hyphenated terms and displaying the resulting TF-IDF sparse vector.
* **Part 2: ASR to VDB Integration (15 Points):** Completed `lab03a.ipynb` and `lab03b.ipynb` notebooks showing successful local Whisper audio transcription, embedding generation, FAISS indexing, semantic query execution, and (for CIS 731) disk serialization routines.
* **GenAI Audit:** Did you use the Generative AI Kit to synthesize this artifact? You must include your `GenAI.pdf` log or explicitly state "No GenAI Used."

## 4. Grading Rubric (30 Points Total)

This assignment is worth 30 points total.

**Part 1: PySpark Scrub & Regex (15 pts)**
* **Regex Hyphenation Handling (15 pts):** Successfully executed the PySpark TF-IDF pipeline with the regex correctly modified to retain hyphenated compound words in the final token array.

**Part 2: ASR & VDB Integration (15 pts)**
* **End-to-End Transcription & Retrieval (15 pts):** Successfully transcribed the LibriVox audio via Whisper, embedded the output, ingested it into FAISS, and executed a semantic trope query. (CIS 731 students graded on disk I/O implementation).
* **GenAI Verification (5 pts):** Includes the required GenAI log (`GenAI.pdf`) or explicitly states AI was not used.
