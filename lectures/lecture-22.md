# CIS 531/731: Programming Techniques for Data Science and Analytics

| Phase | Module | Lecture | Date |
| :--- | :--- | :--- | :--- |
| **Phase IV:** Explore & Model | **Module 7:** Explore: Data Visualization & Dashboards | **Lecture 22:** Explore: Data Visualization & Dashboards | Monday, October 19, 2026 |

---

## Slide 1: Explore: Data Visualization & Dashboards
### CIS 531/731 - Lecture 22
* **Exploratory Data Analysis (EDA):** Visualizing before modeling.
* **Visual Encoding:** Mapping data types to geometric and color marks.
* **High-Dimensional Challenges:** When traditional scatter plots fail.
* **Dashboard Architecture:** Bridging Python backends to interactive frontends.
* **Interactive Filtering:** Cross-filtering and reactive callbacks.

**Speaker Notes:**
Welcome to Phase IV of the course. For the past several weeks, we've focused heavily on the engineering side of the pipeline—capturing streams, indexing vector databases, and generating embeddings. Now that we have the data scrubbed and embedded, we move to Exploration and Modeling. Today, we focus on Exploratory Data Analysis (EDA) and how we use visualization not just to present final results, but to actively investigate our data for anomalies and latent patterns. We will also cover the architecture of interactive dashboards like Streamlit and Dash, which you will use for Machine Problem 7.

---

## Slide 2: Exploratory Data Analysis (EDA) Principles
### Finding the Shape of the Data
* **The Role of Visualization:** Moving beyond summary statistics (Anscombe's quartet) to reveal true distributions and structural anomalies.
* **Latent Pattern Discovery:** Identifying hidden clusters, temporal seasonality, or generational shifts prior to training formal classifiers.
* **Data Quality Auditing:** Visually diagnosing missing data, zero-inflation, and out-of-distribution artifacts from your ingestion pipeline.

**Speaker Notes:**
Never blindly feed data into a machine learning model without looking at it first. Summary statistics can lie—Anscombe's quartet is the classic example where four datasets have identical means and variances but look completely different when graphed. EDA is your diagnostic phase. It is where you catch the fact that your ASR stream capture dropped out for 12 hours, or that your LLM classifier defaulted to a zero-state for an entire batch of inputs. Visualization is your first line of defense against pipeline garbage.

---

## Slide 3: Visual Encoding Constraints
### Mapping Variables to Visuals
* **Continuous Variables:** Best mapped to spatial positioning (x/y axes) or sequential color gradients.
* **Discrete/Categorical Variables:** Mapped to distinct geometric marks (shapes), discrete color palettes, or spatial faceting.
* **Pre-Attentive Processing:** Utilizing visual attributes that the human eye detects in milliseconds (e.g., color hue, size, spatial grouping).

**Speaker Notes:**
As covered in Wilke's *Fundamentals of Data Visualization*, choosing the right visual encoding is a science, not an aesthetic preference. The human brain processes spatial positioning with extremely high accuracy, which is why scatter plots and bar charts are so effective for continuous variables. We process color hue categorically, making it perfect for discrete labels like genre or demographic cohorts. If you map a continuous variable to a categorical color palette, you will render the data unreadable.

---

## Slide 4: Avoiding Perceptual Distortion
### Integrity in Data Representation
* **Proportional Scaling:** Ensuring geometric areas scale with the square of the radius, not linearly, to prevent extreme visual exaggeration.
* **Colorblind Accessibility:** Avoiding red-green diverging palettes in favor of viridis, cividis, or colorblind-safe categorical palettes.
* **Axis Manipulation:** The dangers of truncated y-axes in bar charts versus their legitimate use in line graphs to show variance.

**Speaker Notes:**
Visualization is an act of communication, which means it can be used to mislead. A common error in data science portfolios is scaling a circle's radius linearly with a data value, which actually squares the area, massively exaggerating the variance. Furthermore, you must design for accessibility. Roughly 8% of men have some form of color vision deficiency. If you use a red-green gradient to show sentiment shift, a significant portion of your audience will just see a uniform field of brown. Use perceptually uniform palettes like Viridis.

---

## Slide 5: High-Dimensional Data Challenges
### Beyond Bivariate Analysis
* **The Limits of Standard Plots:** 2D scatter plots and line charts fail when observations possess dozens or hundreds of features.
* **Pair Plot Explosion:** Visualizing all pairwise relationships ($O(N^2)$ plots) becomes computationally and perceptually impossible past ~10 dimensions.
* **The Need for Dimensionality Reduction:** Setting the stage for extracting meaningful 2D topological maps from 768-dimensional embedding vectors.

**Speaker Notes:**
Traditional EDA works perfectly when you have five or ten columns in a Pandas DataFrame. You can build a pair-plot matrix and look at the correlations. But in this class, we are dealing with text embeddings and Vector Databases. Every single observation in our dataset has 768 or 1536 dimensions. If you try to build a pair-plot for that, you will crash your machine, and even if it rendered, it would be useless. This introduces the problem we will solve on Wednesday: projecting high-dimensional semantic space into human-readable 2D maps.

---

## Slide 6: Dashboard Architecture Overview
### From Notebooks to Web Applications
* **The Portability Problem:** Jupyter Notebooks are excellent for prototyping but poor for delivering interactive exploratory tools to stakeholders.
* **Python-Native Frameworks:** Tools like Streamlit and Plotly Dash allow data scientists to build reactive web UIs without writing JavaScript or HTML/CSS.
* **State Management:** Maintaining user session data across browser refreshes and callback executions.

**Speaker Notes:**
Up until now, you've done your analysis in Jupyter Notebooks. But you cannot hand a Jupyter Notebook to a non-technical stakeholder or an administrative client and expect them to execute cells to filter data. We need to build web applications. Fortunately, the Python ecosystem has evolved rapidly. Frameworks like Streamlit and Dash allow us to write pure Python backend logic that automatically generates a reactive React.js frontend. 

---

## Slide 7: Streamlit Mechanics
### Rapid Prototyping in Python
* **Top-Down Execution:** Every time a user interacts with a widget, Streamlit reruns the entire Python script from top to bottom.
* **UI Widgets:** Dropdowns, sliders, and date-pickers injected directly into the script execution flow (e.g., `if st.button('Run'):`).
* **Caching (`@st.cache_data`):** Decorators essential for preventing the re-downloading or re-computation of large datasets on every script rerun.

**Speaker Notes:**
Streamlit is optimized for speed of development. Its architecture is incredibly simple: it just runs your script from top to bottom. If I move a slider, the script reruns. Because of this, it is absolutely critical that you cache your data loading functions. If you are querying a Vector Database and returning 50,000 rows, you cannot let Streamlit re-query the database every time the user clicks a checkbox. You wrap the data-loading function in a cache decorator so the dataframe stays in RAM.

---

## Slide 8: Dash / Plotly Mechanics
### Component-Based Reactive Architecture
* **Layouts:** Defining the DOM structure using `dash.html` and `dash.dcc` (Core Components) building blocks.
* **Callbacks:** Python functions decorated with `@callback` that explicitly link the `Output` of a graph to the `Input` of a widget.
* **Granular Control:** Dash provides finer control over CSS grids, responsive design, and localized updates compared to Streamlit's global reruns.

**Speaker Notes:**
If Streamlit is the rapid prototyper, Dash is the enterprise-grade solution. Instead of rerunning the whole script, Dash uses a reactive programming model. You define a static layout of components, and then you write callback functions. When a user changes a dropdown menu, Dash only fires the specific callback linked to that dropdown, and only updates the specific graph targeted by that callback. It takes a bit more boilerplate code to set up, but it is much more efficient for complex, heavy dashboards.

---

## Slide 9: Interactive Filtering & Cross-Filtering
### Dynamic Data Slicing
* **Input Bindings:** Reading user selections (e.g., time range, specific genre tropes) from UI widgets.
* **DataFrame Masking:** Applying boolean masks to the backend Pandas/Spark DataFrame based on widget inputs.
* **Cross-Filtering:** Selecting a subset of data in one visualization (e.g., brushing a scatter plot) to automatically filter and update all other visualizations on the page.

**Speaker Notes:**
The true power of a dashboard is interactivity. We want the user to be able to ask their own questions. Interactive filtering means your backend code takes the value from a UI slider—say, the year 2010 to 2015—and applies a boolean mask to your DataFrame before pushing the data to the charting library. Advanced dashboards implement cross-filtering: if I use my mouse to lasso a cluster of points on a scatter plot, the bar chart next to it instantly updates to show the demographic breakdown of only those lassoed points.

---

## Slide 10: Wrap-Up & MP7 Release
### Transitioning to Exploration
* **MP7 Released:** Machine Problem 7 is now live. You will build a reactive dashboard that connects to your VDB from Phase III.
* **The High-Dimensional Gap:** We know how to build the dashboard, but we still need the math to squash our 768D embeddings into a 2D scatter plot.
* **Next Class (Lecture 23):** We will cover UMAP (Uniform Manifold Approximation and Projection) to solve the high-dimensional projection problem.

**Speaker Notes:**
That covers the architecture of visual exploration. Machine Problem 7 is released today; the specification is in the repository. Your task is to build a dashboard using either Dash or Streamlit that connects to the vector database you populated in MP5. However, to display those vectors, you need a dimensionality reduction algorithm. In Wednesday's lecture, we will dive deep into UMAP, the topological algorithm we use to project embedding space into 2D without destroying the semantic clusters. Have a good afternoon.
