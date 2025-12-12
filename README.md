# Final Project for Group 08 aka The Wrecking Crew

Group Members

- Jocelyn Perez
- Claire Kaoru Shimazaki
- Colby Zhang
- Olorundamilola Kazeem


## TODOs

[TODO - PLACE BINDER BADGE HERE](...)

README.md: 
```bash
Write a short self-contained description of the project, including the motivation behind your project and the analysis you conducted. 

Include all relevant information about how to run the analysis, including installation steps (for any packages, environments, etc.), testing, and automation. 

A good README should be short but also provide all the useful information to help the user to start running the analysis.
```

## About the Project
...


### Background

**TODO:** Copy/move to step05_main.ipynb

- Q: What is the application domain or the field analysis/research? 
    - A: Spotify Churn Analysis...
- Q: What is the overarching goal of the project?
    - A: ...

#### Spotify Churn Analysis and Inference

**TODO:** Copy/move to step05_main.ipynb

- Q: What is churn? Why are we interested in analyzing and infering churn? Why is this important or valuable? 
    - A: Defnition of Churn
    - A: Reason for Interest in Analyzing and Inferening Churn
    - A: It is important to...  

```bash

```

### 01. The Dataset

**TODO:** For details `goto` (or Move to) step01_data.ipynb 

- Q: What data are we investigating? 
    - A: [Spotify Dataset for Churn Analysis](https://www.kaggle.com/datasets/nabihazahid/spotify-dataset-for-churn-analysis)

- Q: What are the data and metadata details?
    - A: Describe the data, metadata, datatypes, features, labels, number of samples, etc.

- Q: Is this data publicly available? How is it accessed?
    - A: Downloaded to local directory - ./data/00_raw/spotify_churn_dataset.csv

```bash

```

### 02. The Exploratory Data Analysis 

**TODO:** For details `goto` (or Move to) step02_eda.ipynb

- Q: ...
    - A: ...

```bash

```

### 03. The Features i.e. Data Transformation and Vectorization

**TODO:** For details `goto` (or Move to) step03_features.ipynb

- Q: ...
    - A: ...

```bash

```

### 04. The Modeling i.e. Analysis and Modeling 

**TODO:** For details `goto` (or Move to) step04_modeling.ipynb

- Q: ...
    - A: ...

```bash

```

# Spotify Churn Dataset — Modeling Options Summary Table

| Model Family | Model | Type | Purpose | Why Use It |
|--------------|--------|-------|----------|-------------|
| **Baseline Classical Models** | Logistic Regression | Classification | Predict churn | Simple, interpretable baseline; odds ratios |
| | Naïve Bayes | Classification | Predict churn | Fast, works well with simple assumptions |
| **Tree-Based Models** | Decision Tree | Classification | Predict churn | Easy to visualize; handles nonlinear patterns |
| | Random Forest | Classification | Predict churn | Strong accuracy; handles interactions automatically |
| | Gradient Boosting (XGBoost, LightGBM, CatBoost) | Classification | Predict churn | State-of-the-art for tabular data; highest performance |
| **Other Classical ML** | SVM (Support Vector Machine) | Classification | Predict churn | Good for nonlinear boundaries; strong modeling power |
| | k-Nearest Neighbors (kNN) | Classification | Predict churn | Simple, non-parametric; useful for exploration |
| **Neural Models** | MLP (Feed-forward NN) | Classification | Predict churn | Models nonlinearities; flexible architecture |
| | TabNet / DeepFM / Wide & Deep | Classification | Predict churn | Advanced deep models for tabular data |
| **Probabilistic Models** | Bayesian Logistic Regression | Probabilistic Classification | Predict churn w/ uncertainty | Posterior distributions, uncertainty intervals |
| | Gaussian Process Classification | Probabilistic | Predict churn | Very flexible; handles nonlinear functions |
| **Unsupervised Models** | k-Means | Clustering | Segment users | Useful for churn risk segmentation |
| | Hierarchical Clustering | Clustering | Understand group structure | Visual dendrograms |
| | DBSCAN | Clustering | Detect anomalies | Finds outlier behavior (possible churn risk) |
| **Dimensionality Reduction** | PCA | DR / Visualization | Understand feature structure | Reduces feature space; plot churn clusters |
| | t-SNE | DR / Visualization | Visualize user embeddings | High-quality 2D/3D user maps |
| | UMAP | DR / Visualization | Visualize user embeddings | Preserves local structure extremely well |
| **Survival Analysis** (requires time-based features) | Kaplan–Meier Estimator | Survival | Estimate survival / retention | Nonparametric churn curve |
| | Cox Proportional Hazards Model | Survival Regression | Model hazard of churn | Relates features to time-to-churn |
| | Accelerated Failure Time Model | Survival Regression | Model time-to-event | Interpretable effect on churn timing |
| **Interpretable ML** | SHAP Values | Explanation | Interpret feature impact | Best global + local explainability |
| | Permutation Importance | Explanation | Rank feature impacts | Model-agnostic and simple |
| | Partial Dependence Plots (PDP) | Explanation | Feature–target relationships | Shows effect of features (e.g., skip_rate → churn) |



### 05. The Reporting i.e. Consolidation

**TODO:** For details `goto` (or Move to) step05_main.ipynb

- Q: ...
    - A: ...

```bash

```

## The Project Structure

...

```bash

```

## How to Test the Project

...

```bash

```

## How to Run the Project

...

```bash

```

## Misc.

...

```bash

```


