# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase IV:** Explore & Model | **Module 7:** Explore: Data Visualization & Dashboards | **Lecture 24:** Generational Drift Dashboards Lab; Wrap-Up | Friday, October 23, 2026 |

---

## Slide 1: Generational Drift Dashboards Lab - Agenda
### CIS 531/731 - Lecture 24
- **Time-Series Embedding Analysis:** Tracking centroid shifts across temporal data.
- **Dashboard Integration:** Injecting UMAP projections into interactive web apps.
- **Quantifying Drift:** Using mathematical metrics to measure semantic evolution.
- **Data Storytelling:** Translating coordinate migration into cultural insights.
- **MP6 Checkpoint & MP7 Release:** Verifying model selection and moving to EDA.

**Speaker Notes:**
Welcome to the final lecture of Module 7. In the previous two lectures, we discussed the core principles of Exploratory Data Analysis and the mathematics behind UMAP embedding projections. Today is a hands-on lab. We will combine those concepts by building a Generational Drift Dashboard. The goal is to visually and mathematically track how semantic concepts—like a specific genre trope or linguistic pattern—migrate through embedding space over chronological time. We will conclude with a checkpoint for MP6 and outline the requirements for MP7.

---

## Slide 2: Time-Series Embedding Analysis
### Adding the Temporal Axis
- **Chronological Ordering:** Sorting textual or multimedia datasets strictly by their creation or release timestamp before embedding extraction.
- **Cluster Centroids:** Calculating the geometric center (centroid) of a specific semantic cluster within a defined time window.
- **Temporal Slicing:** Partitioning the dataset into distinct eras (e.g., decades, years) to isolate the state of a semantic concept at a given moment.

**Speaker Notes:**
Up until now, we've treated vector databases as static collections of data. But real-world data evolves. To track this, we introduce the temporal axis. By slicing our dataset into chronological chunks—say, 1980s, 1990s, and 2000s—we can run clustering algorithms on each slice independently. We then calculate the centroid, or the average position, of those clusters. By tracking how that centroid moves across the slices, we can mathematically model how a concept evolves over time.

---

## Slide 3: Dashboard Integration
### UMAP Meets Streamlit/Dash
- **The Callback Architecture:** Using UI components (like a time slider) to trigger backend Python functions that filter the embedding data.
- **Dynamic Projection Updates:** Re-rendering the UMAP scatter plot in real-time as the user scrubs through the chronological timeline.
- **State Management:** Ensuring the dashboard maintains the global UMAP coordinate space so that points do not randomly jump when the time slice changes.

**Speaker Notes:**
To make this analysis accessible, we embed it in a dashboard. You will use a framework like Streamlit or Dash. The core mechanism is the callback. You build a slider representing time. When the user moves the slider, a Python function intercepts that input, queries your vector database for embeddings from that specific era, and updates the graph. Crucially, you must fit your UMAP model on the *entire* dataset globally first, and then project the temporal slices into that fixed space. If you refit UMAP on every slice, the coordinate system will warp, and the drift will be meaningless.

---

## Slide 4: Dashboard Integration
### Interactive Hover States
- **Metadata Binding:** Attaching the original raw text, metadata, and timestamps to the UMAP coordinate points.
- **Tooltip Design:** Configuring the plotting library (e.g., Plotly) to display rich HTML tooltips when a user hovers over a data point.
- **Exploratory Verification:** Allowing users to read the underlying data to verify that a dense cluster actually represents a coherent semantic theme.

**Speaker Notes:**
A scatter plot of unlabeled dots is useless for exploratory data analysis. We must bind the original metadata to the 2D coordinates. When the user hovers over a point on your dashboard, a tooltip should reveal the underlying text, the author, and the date. This allows you to perform an exploratory verification. If HDBSCAN identifies a dense cluster, you can hover over those points to confirm that they actually share a semantic theme, validating that your embedding model and UMAP projection are working correctly.

---

## Slide 5: Quantifying Generational Drift
### Beyond Visual Inspection
- **The Illusion of 2D:** Visual distance in a UMAP projection is an approximation; we must calculate drift in the original high-dimensional space.
- **Cosine Distance:** Measuring the angular shift between the centroid of a cluster in Time A and the centroid of the same cluster in Time B.
- **Structural Similarity:** Evaluating if the density or dispersion of the cluster changes across generations, indicating a broadening or narrowing of the concept.

**Speaker Notes:**
While dashboards are excellent for intuition, we cannot rely solely on visual inspection. UMAP is a non-linear projection; visual distance does not perfectly map to true semantic distance. To quantify generational drift, we must go back to the original 768-dimensional space. We calculate the centroid of the concept in the 1990s and the centroid in the 2000s, and measure the cosine distance between them. This gives us a concrete, falsifiable metric for how much the concept has evolved.

---

## Slide 6: Quantifying Generational Drift
### Isolating the Shift
- **Orthogonal Projections:** Projecting the drift vector onto specific semantic axes to determine *how* the concept changed.
- **Anchor Concepts:** Using stable, invariant semantic concepts as reference points to ensure the measured drift is relative to a fixed baseline.
- **Statistical Significance:** Applying permutation tests to determine if the observed centroid shift is statistically significant or merely sampling noise.

**Speaker Notes:**
Once we know a concept has drifted, we need to know in what direction. We can define orthogonal axes in the embedding space—for example, an axis running from "formal" to "informal" language. By projecting our drift vector onto this axis, we can state mathematically that the language became more informal. It is also critical to use anchor concepts. If everything in the dataset drifts by the same amount, it might be an artifact of the embedding model. We measure drift relative to concepts we assume are stable over time.

---

## Slide 7: Data Storytelling Construction
### Translating Math to Narrative
- **The "So What?" Factor:** A dashboard must answer a specific question or guide a specific decision, not just present raw data.
- **Audience Alignment:** Tailoring the complexity of the visual encodings and the accompanying narrative to the technical literacy of the end-user.
- **Annotated Insights:** Using explicit annotations on the dashboard to guide the user's attention to the key moments of generational drift.

**Speaker Notes:**
Data science is ultimately about communication. Your dashboard must tell a story. Do not just hand the user a complex UMAP plot with a time slider and expect them to find the insight. You must build the narrative. Use text annotations on the graph to highlight the exact year a cluster split into two, or the moment a centroid shifted dramatically. The dashboard should guide the user toward the conclusion that your mathematical analysis supports.

---

## Slide 8: Lab Execution
### Building the Pipeline
- **Step 1:** Pull chronological embedding data from your vector database.
- **Step 2:** Fit a global UMAP model on the entire dataset to establish the coordinate space.
- **Step 3:** Calculate temporal cluster centroids and cosine drift metrics.
- **Step 4:** Build the Streamlit/Dash callback architecture linking a time slider to the projected scatter plot.

**Speaker Notes:**
Let's transition to the lab. You have the theoretical foundation; now we build the pipeline. Start by querying your vector database for a chronologically sequenced dataset. Fit your global UMAP model. Then, calculate your centroids and drift metrics in the high-dimensional space. Finally, construct the UI. Your goal today is to get a functioning slider that updates a Plotly scatter plot dynamically, without the coordinate space shifting under the user's feet.

---

## Slide 9: MP6 Checkpoint & MP7 Release
### Administrative Milestone
- **MP6 Checkpoint:** Ensure your Model Selection and Baseline Evaluation code is committed to your repository.
- **MP7 Overview:** Machine Problem 7 focuses entirely on Exploratory Dashboards and Data Storytelling.
- **MP7 Deliverable:** You will deploy a working interactive dashboard (Streamlit or Dash) that visualizing a core aspect of your term project dataset.

**Speaker Notes:**
Before we begin coding, an administrative checkpoint. MP6, your Model Selection assignment, is wrapping up. Ensure your baseline evaluation scripts are committed. Today's lab serves as the kickoff for MP7. MP7 requires you to build an exploratory dashboard for your actual term project dataset, incorporating the interactive filtering and UMAP projections we have covered this week. The rubric for MP7 is now available on Canvas.

---

## Slide 10: Wrap-Up
### Final Thoughts
- **EDA is Non-Linear:** Exploration often reveals data quality issues that force you back to the Scrub phase.
- **Dashboards Drive Decisions:** Interactive visualizations are the primary interface between data scientists and stakeholders.
- **Next Module:** We move into Phase V: Model & Evaluate, focusing on retrieval-augmented classification and gold-standard construction.

**Speaker Notes:**
To wrap up Module 7: remember that Exploratory Data Analysis is rarely a straight line. Visualizing your embeddings often reveals artifacts or noise that force you to go back and scrub your data again. This is a necessary part of the process. The dashboards you build are how you will communicate the value of your models to non-technical stakeholders. Next week, we enter Phase V, where we will rigorously evaluate the models we selected in MP6 against human-constructed gold standards. Let's get to work on the lab.
