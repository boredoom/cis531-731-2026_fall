# CIS 531/731: Term Project Taxonomy (3x5x5 Data Cube)

**Rules of Engagement:**
* **Category:** Each team (1-3 students) MUST choose exactly ONE category (Prescriptive, Descriptive, or Predictive).
* **Topic (Media):** Each team MUST choose a focal topic. If a team splits (e.g., a 5-student mega-team dissolving into a 3 and a 2), the exit strategy requires branching the Git repository and selecting orthogonal OSEMN tasks to prevent collision.
* **Task (OSEMN Stage):** Tasks correspond to the data pipeline. Students may claim 1-2 tasks each. Teams must automate/mock the stages they do not explicitly claim.

---

## Dimension 1: The 3 Analytical Categories (The Goal)

1. **Prescriptive Analytics (RecSys/IR):** Systems that recommend actions, retrieve specific knowledge (RAG), or automate decision-making based on constraints.
2. **Descriptive Analytics (InfoVis/Storytelling):** Systems that expose hidden patterns, generate dashboards, map generational drift, or summarize vast corpora.
3. **Predictive Analytics (Classification/Forecasting):** Systems that classify entities (KYC/AML), predict future states (time series), or identify anomalies.

---

## Dimension 2: The 5 Topics / Media Types (The Input)

1. **Time-Series / Sequential Data:** Financial logs, weather/climate sensors, IoT telemetry, server/traffic logs.
2. **Spatial / Georeferenced Data:** Epidemiological maps, check-in data, logistics routing, satellite/remote sensing features.
3. **Text Corpora:** E-books, conversational transcripts, LLM prompt/response logs, product reviews, historical archives.
4. **Multimedia (Audio/Visual):** ASR (Automatic Speech Recognition) streams, caller speech, video captions, music information retrieval (MIR).
5. **Structured/Relational Data:** Complex database queries, web service/API streams, graph network architectures.

---

## Dimension 3: The 5 OSEMN Tasks / Stages (The Execution)

*Teams execute a subset of these stages natively and automate the rest.*

### Task 1: Obtain (Data Ingestion & Extraction)
* **Prototype:** Building a PySpark streaming consumer that attaches to a live Kafka/AWS Kinesis feed of structured API data, or a web scraper that generates a 10GB raw text corpus.
* **Goal:** Reliable, fault-tolerant acquisition of the raw media type.

### Task 2: Scrub (Cleaning & Chunking)
* **Prototype:** Implementing recursive character chunking with stride on ASR transcripts, or normalizing/imputing missing values in a massive spatial dataset.
* **Goal:** Transforming raw, noisy inputs into uniform, machine-readable structures ready for embedding or EDA.

### Task 3: Explore (EDA & Feature Engineering)
* **Prototype:** Generating UMAP/t-SNE visualizations of semantic embeddings, or building a dashboard that maps the distribution of classes in a time-series log.
* **Goal:** Identifying target variables, understanding latent space clustering, and defining the bounds of the dataset.

### Task 4: Model (Machine Learning & Pipelines)
* **Prototype:** Training an XGBoost classifier for transaction fraud, fine-tuning a HuggingFace Transformer for sentiment, or deploying a FAISS/Qdrant Vector Database for semantic search.
* **Goal:** The mathematical core; applying statistical or neural algorithms to execute the Category goal (Predict, Describe, Prescribe).

### Task 5: iNterpret (Evaluation & Data Storytelling)
* **Prototype:** Calculating and graphing ROC-AUC, BLEU scores, or semantic coherence metrics, and synthesizing the outputs into an interactive Streamlit or PowerBI dashboard.
* **Goal:** Proving the model's efficacy against baselines (INV-17) and translating statistical outputs into actionable human insights.

---

## The 3x5x5 Selection Matrix

*(Teams map their project by selecting one from each of the three tables below)*

### Table A: Prescriptive (RecSys / IR / Automation)
| Topic (Media) | Obtain (T1) | Scrub (T2) | Explore (T3) | Model (T4) | iNterpret (T5) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Time-Series** | Log Ingestion | Anomaly Scrub | Trend EDA | Predictive Maintenance | Alert Dashboard |
| **2. Spatial** | GPS Stream | Boundary Norm. | Heatmaps | Logistics Routing | Route Vis. |
| **3. Text** | API Scraping | Text Chunking | Topic Modeling | RAG Q&A System | Source Auditing |
| **4. Multimedia** | ASR Capture | Audio Denoise | Feature Extract | Content RecSys | Engagement Vis. |
| **5. Structured** | DB Polling | Schema Align | Graph EDA | Knowledge Graph | Node/Edge Vis. |

### Table B: Descriptive (InfoVis / Storytelling)
| Topic (Media) | Obtain (T1) | Scrub (T2) | Explore (T3) | Model (T4) | iNterpret (T5) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Time-Series** | Sensor Polling | Gap Imputation | Seasonality | Clustering | Drift Dashboard |
| **2. Spatial** | GeoJSON Pull | Coord. Clean | Density Maps | Spatial Regress. | Interactive Map |
| **3. Text** | Archive Sync | Stopword/Regex | Word Embeds | Sentiment/Trope | Narrative Vis. |
| **4. Multimedia** | Video Scrape | Frame Extract | Color/Audio | Feature Cluster | Media Timeline |
| **5. Structured** | API Webhooks | Deduplication | Pivot Tables | Assoc. Rules | Summary Dash |

### Table C: Predictive (Classification / Forecasting)
| Topic (Media) | Obtain (T1) | Scrub (T2) | Explore (T3) | Model (T4) | iNterpret (T5) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Time-Series** | Fin/Market API | Outlier Filter | Volatility Vis. | ARIMA/LSTM | Forecast Curves |
| **2. Spatial** | Remote Sense | Image Norm. | Pixel Hist. | CNN Classifier | Accuracy Maps |
| **3. Text** | Social Stream | Tokenization | Term Freq. | Few-Shot LLM | ROC/AUC Curves|
| **4. Multimedia** | Audio Stream | MFCC Extract | Spectrograms | Acoustic Model | WER Metrics |
| **5. Structured** | Transact Logs| Feature Scale | PCA/Correl. | XGBoost/KYC | Precision/Recall|
