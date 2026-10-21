# CIS 531/731 Term Project  
# Data Sourcing & OSEMN Execution Guide

**Course:** Introduction to Programming Techniques for Data Science and Analytics  
**Audience:** CIS 531 upper-division undergraduate students and CIS 731 graduate students  
**Applies to:** PS4 project proposals and all subsequent OSEMN term-project work

---

## Choose Data First

> **Teams must secure and validate their data source before committing to a specific model, framework, or architecture.**

A sophisticated recommender system, RAG pipeline, XGBoost model, streaming application, or deep-learning workflow is not a viable project if the team cannot reliably obtain and clean the required data.

**Obtain** and **Scrub** failures are the leading cause of term-project collapse. Common failures include:

- Choosing a source that requires unavailable credentials, paid access, or institutional approval.
- Depending on a brittle web scraper rather than a documented dataset or API.
- Underestimating malformed JSON, missing fields, duplicate records, rate limits, pagination, or schema drift.
- Selecting raw satellite imagery or raw audio while lacking a tractable preprocessing environment.
- Discovering too late that the dataset does not contain a target variable, timestamp, label, geographic coordinate, text field, or relationship needed for the intended analysis.
- Designing a model first and only later attempting to locate data that fits it.

Your first project milestone is not model selection. It is a **reproducible, inspectable, and accessible source-to-Bronze ingestion path**.

The course taxonomy defines projects across three analytical categories—Prescriptive, Descriptive, and Predictive—five media types, and five OSEMN stages: Obtain, Scrub, Explore, Model, and iNterpret. Teams may claim a subset of stages, but they must have a credible automation plan for the remaining stages. [2]

---

## Tier List for Data Sources

Use the following hierarchy when selecting a source. Tier 1 is strongly preferred for most teams.

| Tier | Source class | Recommended use | Main benefit | Main risk |
|---|---|---|---|---|
| 🟢 **Tier 1** | Golden Path | Default choice for most projects | Stable access, known schemas, low setup burden | Less novelty in acquisition |
| 🟡 **Tier 2** | Real-world API or benchmark | Teams deliberately studying API ingestion, JSON normalization, streaming, or practical source variability | Realistic source engineering experience | Rate limits, pagination, authentication, schema variation |
| 🔴 **Tier 3** | Tarpit | Only with a clear technical justification and an instructor-approved feasibility plan | Specialized domain experience | High probability that Scrub consumes the project |

### 🟢 Tier 1: Golden Path

Tier 1 sources are natively available, well-documented, or highly accessible. They allow teams to focus on Spark SQL, Delta Lake, distributed feature engineering, embeddings, retrieval, machine learning, evaluation, and communication rather than spending most of the term repairing data acquisition.

| Source | Best taxonomy rows | Typical projects | Obtain method |
|---|---|---|---|
| Databricks native `samples.wanderbricks` | Prescriptive or Descriptive Structured/Relational | Recommenders, customer segmentation, booking analytics, next-best action, support analytics | Query tables through Unity Catalog and persist a reproducible project snapshot |
| Databricks native `samples.tpcds_sf1` | Descriptive or Predictive Structured/Relational | Association rules, retail analytics, SQL pipelines, dashboarding, customer and sales analysis | Query sample fact/dimension tables through Unity Catalog |
| Hugging Face `wikimedia/wikipedia` | Prescriptive or Descriptive Text Corpora | RAG, semantic search, document clustering, topic modeling, text classification | Load through `datasets`, then write raw and normalized outputs to Parquet or Delta |
| Hugging Face `librispeech_asr` | Predictive or Descriptive Multimedia | Whisper/ASR evaluation, transcript analysis, speech workflow experiments | Load a bounded split and use the course-supported ASR workflow |
| Public Open-Meteo or NOAA endpoints | Time-Series / Sequential | Forecasting, seasonality analysis, anomaly detection, weather-driven decision support | Script parameterized requests, archive raw JSON, ingest with Auto Loader or batch reads |
| USGS Earthquake GeoJSON feeds | Spatial / Georeferenced | Spatial density mapping, event visualizations, time–space clustering | Persist GeoJSON payloads to Bronze storage and flatten into typed tables |

### 🟡 Tier 2: Real-World APIs and Benchmarks

Tier 2 is appropriate when real-world ingestion is part of the learning objective. These sources require intentional planning for request limits, pagination, API errors, changing schemas, and raw-payload retention.

| Source | Best taxonomy rows | Obtain requirements | Main feasibility concern |
|---|---|---|---|
| NOAA Climate Data API | Time-Series / Sequential | Token-aware or documented request workflow, pagination, raw JSON storage | Rate limits, historical coverage variation, missing observations |
| Open-Meteo API | Time-Series / Sequential | Parameterized location/date requests and JSON archival | Nested arrays, unit consistency, missing intervals |
| USGS Earthquake Feed | Spatial / Georeferenced | GeoJSON fetch, timestamp parsing, coordinate validation | Event revisions, duplicate event IDs, spatial aggregation |
| Kaggle IEEE-CIS Fraud Detection | Predictive Structured/Relational | Kaggle API credentials, secure `kaggle.json` handling, reproducible download script | Account/token management, table joining, target leakage |
| Other documented public REST APIs | Any appropriate row | API terms review, fallback plan, Bronze archive, error handling | Unstable availability, undocumented response changes |

### 🔴 Tier 3: Tarpits

Tier 3 sources are not prohibited. However, they are **not recommended** unless the difficult sourcing or preprocessing work is explicitly part of the project’s educational objective and the team has a detailed feasibility plan.

| Source type | Why it is high risk | Preferred alternative |
|---|---|---|
| Raw STAC / Sentinel-2 / multispectral imagery | Requires cloud masking, coordinate reference system management, raster tiling, large-object storage, spatially valid train/test splits, and specialized distributed image tooling | Use pre-extracted tabular remote-sensing features, a small curated benchmark, or choose a non-raster spatial source |
| Raw audio processing and MFCC extraction from scratch | Audio decoding, resampling, feature extraction, worker memory pressure, dependency incompatibility, and distributed-library failures can consume the project | Use `librispeech_asr`, transcript-first analysis, precomputed embeddings, or the supported Whisper workflow |
| Web-scraping-dependent datasets | HTML changes, bot protections, robots/terms restrictions, rate limits, missing provenance, and fragile parsers make Obtain unreliable | Use a public API, government bulk-data release, Hugging Face dataset, Kaggle dataset, or Databricks sample |
| Unbounded social-media collection | API changes, access restrictions, deleted records, incomplete metadata, and scale uncertainty | Use a static public corpus or a bounded, documented archive |
| Proprietary or enterprise-gated sources | Team members may lose access, legal/contract terms may block redistribution, and reviewers cannot reproduce results | Use an openly accessible benchmark or native Databricks sample |

---

## Required Proposal Evidence

Your PS4 proposal must demonstrate that the **Obtain** and **Scrub** stages are feasible. Naming a source is not sufficient.

A proposal should enable another student or instructor to understand how raw data becomes a usable Spark table without relying on manual browser downloads, personal files, or undocumented notebook state.

### Obtain evidence

Include all of the following:

- [ ] **Exact data source identifier:** State the Unity Catalog table, Hugging Face dataset slug, Kaggle competition slug, public endpoint, repository, or documented bulk-data source.
- [ ] **Access method:** State whether access is anonymous, workspace-native, API-token-based, account-based, or requires a Kaggle credential.
- [ ] **Authentication plan:** If using credentials, explain where secrets are stored and confirm that tokens, API keys, and `kaggle.json` are excluded from Git.
- [ ] **Minimal acquisition test:** Demonstrate or describe a successful test that retrieves a bounded sample of the real source data.
- [ ] **Raw landing format:** Identify the raw output format: JSON, GeoJSON, CSV, Parquet, audio manifest, Delta snapshot, or another durable format.
- [ ] **Bronze destination:** Identify where immutable raw inputs will be retained, such as a Unity Catalog Volume, cloud object-storage location, or Bronze Delta table.
- [ ] **Repeatable command or notebook:** Provide a command, script, or notebook cell that another team member can execute without manual download steps.
- [ ] **Source versioning:** Record the dataset split, source revision, extraction date, API parameters, and any relevant date range.
- [ ] **Expected scale:** Estimate row count, file count, storage volume, or time interval so that the team does not accidentally ingest an unmanageable corpus.
- [ ] **Known source risks:** State the expected risks: pagination, rate limits, missingness, schema drift, access expiration, or terms restrictions.

### Scrub evidence

Include all of the following:

- [ ] **Target schema:** Identify the intended Silver-table columns, data types, unique keys, labels or targets, and timestamp/geographic fields where applicable.
- [ ] **Cleaning operations:** Name at least three concrete cleaning transformations.
- [ ] **Null/missingness policy:** Explain how null values, sentinel values, empty text, missing coordinates, or unknown categories will be handled.
- [ ] **Duplicate policy:** Specify the natural key or duplicate-detection rule.
- [ ] **Type normalization:** Identify date, timestamp, numeric, categorical, text, coordinate, or unit transformations.
- [ ] **Data-quality tests:** Define at least two assertions, such as non-null IDs, valid coordinate ranges, unique event keys, bounded values, or no future-data leakage.
- [ ] **Output handoff:** Specify the versioned Delta or Parquet table that becomes the input to Explore, Model, or iNterpret.

### Minimum Scrub plans by source type

| Source type | Minimum viable Scrub work |
|---|---|
| Databricks native relational samples | Validate primary keys, cast timestamps and numerics, resolve nulls, de-duplicate, and join fact/dimension tables |
| Hugging Face text dataset | Normalize Unicode, remove markup/noise, deduplicate, retain source identifiers, chunk documents, and preserve chunk-to-document lineage |
| Hugging Face ASR dataset | Validate audio/transcript metadata, normalize transcript text, filter unusable records, preserve speaker/language/split fields |
| REST JSON or GeoJSON API | Preserve raw payloads, flatten nested objects, parse timestamps, cast numeric fields, standardize units, and de-duplicate events |
| Kaggle tabular dataset | Join source files, parse types, impute or flag missingness, encode categorical values, and prevent target leakage |
| Spatial point data | Validate longitude/latitude ranges, normalize coordinate reference system assumptions, remove invalid geometries, and check spatial duplicates |
| Time-series observations | Parse times in one timezone, regularize intervals where needed, handle missing intervals, and ensure no future data enters training features |

---

## Golden Path Architectures

The following architectures are recommended because they clearly separate raw acquisition, cleaning, analytics, modeling, and interpretation. Each stage should persist a reproducible artifact rather than passing data through untracked notebook variables.

### Databricks-native structured project

**Best for:** Recommenders, customer segmentation, association rules, retail analytics, SQL-heavy descriptive analytics, next-best action prototypes, and relational ML.

```text
Databricks Unity Catalog sample source
samples.wanderbricks or samples.tpcds_sf1
                |
                v
Spark SQL read / bounded project snapshot
                |
                v
Bronze Delta table
Raw, versioned source snapshot
                |
                v
Silver Delta table
Typed, deduplicated, normalized, joined records
                |
                v
Gold Delta table
Features, aggregates, customer/item entities, metrics
                |
                +-------------------------+
                |                         |
                v                         v
Spark ML / MLflow model             SQL dashboard / visualization
                |                         |
                +------------+------------+
                             v
                    iNterpretation artifact
           Metrics, segments, rules, recommendations, narrative
```

#### Example: Customer segmentation

- **Obtain:** Read customer, booking, property, payment, review, or interaction tables from `samples.wanderbricks`; write a project-specific Bronze snapshot.
- **Scrub:** Standardize currencies and timestamps; remove duplicate transactions; reconcile user IDs; establish the valid analysis period.
- **Explore:** Calculate recency, frequency, monetary value, booking duration, cancellation behavior, property preferences, and review distributions.
- **Model:** Cluster standardized customer behavior features with a reproducible pipeline.
- **iNterpret:** Describe each segment using representative metrics, segment size, revenue contribution, uncertainty, and possible operational actions.

**Recommended project contract:** Each stage writes a named Delta table. For example:

```text
team_project.bronze_wanderbricks_snapshot
team_project.silver_customer_activity
team_project.gold_customer_features
team_project.gold_customer_segments
team_project.gold_segment_interpretation
```

### Hugging Face text / RAG project

**Best for:** Retrieval-augmented generation, semantic search, source-grounded question answering, text clustering, classification, topic analysis, and document analytics.

```text
Hugging Face dataset
wikimedia/wikipedia or approved text corpus
                |
                v
Dataset loader or bounded file export
                |
                v
Bronze Parquet or Delta table
Raw documents, source IDs, titles, metadata
                |
                v
Silver Delta table
Normalized text, deduplicated records, chunked passages
                |
                v
Gold retrieval / feature table
Chunk embeddings, document metadata, vector IDs, labels
                |
                +-------------------------+
                |                         |
                v                         v
Retriever / RAG pipeline           Spark ML text classifier or clustering
                |                         |
                +------------+------------+
                             v
                    iNterpretation artifact
     Retrieval quality, source audit, errors, metrics, examples
```

#### Example: Wikipedia RAG

- **Obtain:** Load a bounded Wikipedia language/configuration/split using a Hugging Face dataset loader or exported files.
- **Scrub:** Preserve page ID, title, source URL or dataset provenance, and original text; normalize Unicode; remove non-content markup; split each document into overlapping chunks.
- **Explore:** Measure document length, chunk length, duplicate frequency, topic distribution, language artifacts, and embedding-neighbor density.
- **Model:** Embed chunks; retrieve top-\(k\) passages for questions; optionally connect retrieval to a generation model.
- **iNterpret:** Report retrieval recall, answer support rate, citation coverage, unsupported-answer rate, and examples of successful and failed retrieval.

**Required RAG rule:** Every chunk must retain a stable link to its original document identifier. If the team cannot trace an answer to a retrieved source chunk, it cannot adequately audit the system’s output.

### REST API time-series / spatial project

**Best for:** Forecasting, anomaly detection, weather analytics, environmental monitoring, event-density mapping, geospatial storytelling, and public-data ingestion.

```text
Public REST / GeoJSON API
NOAA, Open-Meteo, or USGS
                |
                v
Python acquisition script
Pagination, backoff, retries, parameter logging
                |
                v
Bronze object storage or Bronze Delta table
Immutable raw JSON / GeoJSON payload archive
                |
                v
Auto Loader or Spark batch JSON ingestion
                |
                v
Silver Delta table
Flattened, typed, deduplicated observations
                |
                v
Gold feature table
Time windows, lags, spatial aggregates, labels, metrics
                |
                +-------------------------+
                |                         |
                v                         v
Forecasting / anomaly model       Spatial density or map visualization
                |                         |
                +------------+------------+
                             v
                    iNterpretation artifact
     Forecast errors, anomaly explanations, maps, data-quality report
```

#### Example: Weather forecasting with Open-Meteo

- **Obtain:** Use a parameterized Python script to request weather observations for documented coordinates, variables, date ranges, and time intervals.
- **Scrub:** Retain each original JSON response; explode nested time/value arrays into timestamped rows; normalize units; identify and represent missing observations.
- **Explore:** Calculate rolling averages, lag relationships, seasonality, autocorrelation, coverage by station or location, and outlier distributions.
- **Model:** Compare a naïve baseline with a time-respecting regression, classification, or forecasting model.
- **iNterpret:** Plot observed and predicted values; report MAE, RMSE, MAPE where appropriate, residual patterns, and errors by season or weather regime.

**REST API rule:** Always archive the original payloads. Do not rely on a live API as the only copy of your data. A Bronze archive allows your team to revise Scrub logic without re-downloading historical data or exhausting rate limits.

---

## Tarpit Controls

Tier 3 work is permitted only when the team can show that the difficult source-processing work is intentional, bounded, and central to the learning objective.

### Raw STAC and Sentinel-2 imagery

Do **not** select raw satellite imagery as a default spatial-data source.

Raw imagery projects commonly require all of the following:

- Cloud and shadow masking.
- Coordinate reference system handling.
- Band selection and radiometric normalization.
- Large raster storage and distributed file access.
- Spatial tiling and edge handling.
- Label acquisition or land-cover ground truth.
- Spatially valid train/test splitting to avoid geographic leakage.
- Specialized geospatial/raster libraries beyond ordinary Spark SQL workflows.

A project cannot claim feasibility merely because a STAC endpoint returns metadata. The team must demonstrate that it can download, tile, clean, feature-engineer, store, and validate the imagery at a tractable scale.

**Preferred alternative:** Use pre-extracted tabular remote-sensing features, a small curated benchmark, a point-based geospatial dataset, or the USGS earthquake feed.

### Raw audio and MFCC extraction from scratch

Do **not** use generic Spark workers for raw audio feature extraction unless the class provides the precise workflow or the team has demonstrated the full runtime environment.

Common problems include:

- Audio-codec and native-library incompatibility.
- Sample-rate and channel inconsistency.
- Worker-memory exhaustion.
- Slow Python user-defined functions.
- Uneven partition sizes caused by variable-duration clips.
- Failure to reproduce environment-dependent feature extraction.
- Excessive time spent debugging audio dependencies rather than analyzing data.

**Preferred alternatives:**

- Use `librispeech_asr` and the supported Whisper/ASR workflow.
- Use transcript-first NLP analysis if the project question is about language rather than acoustics.
- Use precomputed embeddings or pre-extracted features.
- Work from a small, bounded, instructor-approved audio subset if extraction itself is the intended learning objective.

### Scraping-dependent datasets

Do **not** make a fragile scraper your primary data source.

Scraping may be considered only if the proposal includes:

- A documented reason that no public API, dataset release, or bulk export can meet the need.
- Evidence that access complies with site terms and applicable restrictions.
- Rate limiting, retry, timeout, and backoff behavior.
- A durable raw-data archive.
- Schema-validation tests.
- A fallback dataset or documented failover source.
- A bounded collection plan with estimated scale.
- A plan for handling changed HTML structure, missing pages, blocked requests, and duplicate content.

**Preferred alternative:** Use a public REST API, government bulk release, Hugging Face dataset, Kaggle dataset, Databricks sample, or a static archive with stable metadata.

---

## Team Execution and OSEMN Delegation

Teams are not required to manually implement every stage from scratch. Each member should claim **one or two OSEMN stages** that align with their learning goals, then automate or use well-tested components for the remaining stages.

The goal is not to maximize handwritten code. The goal is to deliver a reproducible end-to-end data-science system with clear ownership, verifiable handoffs, and defensible results.

| Claimed learning goal | Team-owned work | Appropriate automation |
|---|---|---|
| Spark ingestion or streaming | API acquisition script, Structured Streaming, Auto Loader, checkpointing, Bronze design, source-retry logic | Baseline cleaning pipeline, reference model, visualization templates |
| Data engineering and quality | Silver schema, validation tests, deduplication logic, missing-data policy, Delta design, lineage documentation | Source downloader, baseline EDA notebook, baseline ML implementation |
| NLP or RAG | Text normalization, chunking policy, embeddings, retrieval, provenance mapping, source-audit metrics | Hugging Face loader, standard Parquet/Delta write, baseline dashboard |
| Machine learning | Feature pipeline, train/test design, baseline comparison, hyperparameter evaluation, model tracking | Native sample acquisition, standardized cleaning scripts, prebuilt visualization framework |
| Analytics and storytelling | Metric definitions, dashboard, visual narrative, stakeholder-oriented interpretation | Baseline ETL, standard model training, reusable chart helpers |
| Responsible AI and evaluation | Error analysis, calibration, slice metrics, leakage review, provenance audit, limitations statement | Source ingestion, baseline feature engineering, standard modeling tools |

### Required stage handoff

Every OSEMN stage must hand off a versioned, persistent artifact to the next stage.

```text
Obtain
  |
  v
Bronze Delta / Parquet
Raw immutable source snapshot
  |
  v
Scrub
  |
  v
Silver Delta / Parquet
Cleaned, typed, validated dataset
  |
  v
Explore
  |
  v
Gold feature / summary table
  |
  v
Model
  |
  v
Predictions, clusters, retrieval outputs, or recommendations
  |
  v
iNterpret
  |
  v
Metrics, visuals, source audit, narrative, and project report
```

Do **not** use the following as your only handoff mechanism:

- Manually edited CSV files.
- Local laptop-only files.
- Notebook variables that disappear when a cluster restarts.
- Screenshots of outputs.
- Downloaded files not represented in the repository or storage plan.
- Undocumented manual browser exports.
- A model artifact with no corresponding source-data version.

### Suggested artifact naming

Use explicit, stage-oriented names:

```text
<catalog>.<schema>.bronze_<source>_raw
<catalog>.<schema>.silver_<entity>_clean
<catalog>.<schema>.gold_<feature_or_metric>
<catalog>.<schema>.model_<experiment_or_version>
<catalog>.<schema>.interpret_<evaluation_or_dashboard>
```

For file-based workflows:

```text
/project-data/
  bronze/
    source_name/
      extraction_date=YYYY-MM-DD/
  silver/
    dataset_name/
      version=v1/
  gold/
    feature_set_name/
      version=v1/
```

---

## PS4 Proposal Acceptance Checklist

Your project proposal is operationally credible when every item below is true.

- [ ] The team selected exactly one category: Prescriptive, Descriptive, or Predictive.
- [ ] The team selected exactly one media/topic row: Time-Series, Spatial, Text, Multimedia, or Structured/Relational.
- [ ] The team selected a Tier 1 or Tier 2 source, or justified a Tier 3 exception.
- [ ] The proposal names the exact table, dataset slug, endpoint, competition, or bulk-data release.
- [ ] The team has performed a minimal Obtain test using the actual selected source.
- [ ] The raw data can be persisted in a Bronze Delta table, Parquet dataset, or immutable raw-data directory.
- [ ] The proposal identifies the expected source schema and the intended Silver schema.
- [ ] The Scrub plan names specific transformations, not generic statements such as “clean the data.”
- [ ] The team defines a null-handling, de-duplication, and type-normalization policy.
- [ ] The proposal identifies likely access and feasibility risks: credentials, rate limits, pagination, schema drift, storage volume, terms, or missing labels.
- [ ] The team can run a baseline analysis or model if the advanced model fails.
- [ ] The team assigns ownership for one or two OSEMN stages per member.
- [ ] The team uses versioned Delta or Parquet artifacts for all inter-stage handoffs.
- [ ] The team can reproduce the pipeline from raw source data through a final evaluation or interpretation artifact.

---

## Final Decision Rule

Choose the simplest source that allows your team to demonstrate meaningful work in the OSEMN stages you intend to claim.

For most teams, the preferred order is:

1. **Databricks native samples** for Structured/Relational projects.
2. **Hugging Face datasets** for Text and supported Audio projects.
3. **Documented public APIs** for Time-Series and point-based Spatial projects.
4. **Kaggle benchmarks** for structured predictive projects when secure token management is feasible.
5. **Tier 3 sources only when preprocessing complexity is itself the project objective.**

A successful CIS 531/731 project is not the project with the most exotic model or the most difficult source. It is the project that reliably obtains data, documents cleaning decisions, executes a reproducible Spark workflow, evaluates results against a baseline, and communicates limitations honestly.
