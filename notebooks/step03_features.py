# ---
# jupyter:
#   jupytext:
#     formats: ipynb:percent,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: IPython - final-group08
#     language: python
#     name: final-group08
# ---

# %% [markdown]
# ---
# title: Step 03 - Featurization, Vectorization, and Pre-Modeling
# subject: Churn Analysis
# subtitle: Step 03 - Featurization, Vectorization, and Pre-Modeling - Churn Analysis
# short_title: Featurization, Vectorization, and Pre-Modeling
# date: 2025-12-17
#
#
# affiliations:
#   - id: "ucb"
#     name: "University of California, Berkeley"
#
# authors:
#   - name: Jocelyn Perez
#     email: jocelyneperez@berkeley.edu
#     orcid: 0009-0009-0231-9254
#     affiliations: ["ucb"]
#
#   - name: Claire Kaoru Shimazaki
#     email: ckshimazaki@berkeley.edu
#     orcid: 0009-0001-0828-3370
#     affiliations: ["ucb"]
#
#   - name: Colby Zhang
#     email: colbyzhang@berkeley.edu
#     orcid: 0009-0005-4786-6922
#     affiliations: ["ucb"]
#
#   - name: Olorundamilola Kazeem
#     email: dami@berkeley.edu
#     orcid: 0000-0003-2118-2221
#     affiliations: ["ucb"]
#
# # https://mystmd.org/guide/frontmatter#frontmatter-downloads
# # https://mystmd.org/guide/website-downloads
# # downloads:
# #   -  ...
#
# # https://mystmd.org/guide/website-downloads#include-exported-pdf
# # exports:
# #   - format: pdf
# #     template: lapreprint-typst
# #     output: exports/my-document.pdf
# #     id: my-document-export
# # downloads:
# #   - id: my-document-export
# #     title: A PDF of this document
#
# exports:
#   - format: pdf
#     template: lapreprint-typst
#     output: ../pdf_builds/step03_features/step03_features_ipynb_to.pdf
#     line_numbers: true
#
# license: BSD-3-Clause
#
# keywords: featurization, vectorization, pre-modeling, churn, spotify
#
# abstract: What are the pre-processing of the features? How is the data being vectorized? 
# ---

# %% [markdown]
# ### The Engagement Hypothesis
# Raw data tell us *what* a user did, but not *how they felt*. To build a robust churn model, we must transform raw metrics into interpretable **Behavioral Signals**.
#
# In this notebook, we focus on three tasks:
# 1.  **Feature Engineering:** Creating interaction terms (like `ads_per_song`) that measure "user friction" better than raw counts.
# 2.  **Stratified Splitting:** Ensuring our training data preserves the Churn/Non-Churn ratio of the real world.
# 3.  **Pipeline Construction:** Building a leak-proof transformation pipeline that handles missing data and scales numerical values for machine learning algorithms.

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn import set_config

import src.step03_features as step03
import src.step00_utils as utils

RAW_DATA_PATH = step03.RAW_DATA_PATH
PROCESSED_DATA_DIR = step03.PROCESSED_DATA_DIR
VECTORIZED_DATA_DIR = step03.VECTORIZED_DATA_DIR
# FIG_DIR = step03.DIR_DATA.parent / "fig_builds" / "step03_features"
FIG_DIR = utils.DIR_OUTPUTS_FIG_BUILDS_03_FEATURES

# %% [markdown]
# # Feature Engineering
#
# We import our custom logic from `src.step03_features`. We hypothesize that churn is driven by "efficiency of use" and "ad tolerance."
#
# - `avg_song_length`: A proxy for engagement intensity. User who listen to longer songs (or don't skip halfway through) likely have a higher "stickiness."
# - `ads_per_song`: A "frustration metric." A high ratio here suggests that user is being bombarded with ads relative to the content they consume, increasing churn risk.

# %%
df = pd.read_csv(RAW_DATA_PATH)

# engineer features
df_engineered = step03.engineer_features(df)

print("New columns created:", [c for c in df_engineered.columns if c in ['ads_per_song', 'avg_song_length']])

plt.figure(figsize=(8, 4))
sns.boxplot(x='is_churned', y='avg_song_length', hue='is_churned', legend=False, data=df_engineered, palette='coolwarm')
plt.title("Does 'Average Song Length' differ by Churn Status?")
plt.ylabel("Avg Song Length (Seconds)")
plt.grid(True, alpha=0.3)

plt.savefig(FIG_DIR / "step03_feature_boxplot.png", bbox_inches='tight', dpi=300)
plt.show()

# %% [markdown]
# # Data Splitting
#
# Churn datasets are often "imbalanced" (fewer people churn than stay). If we split the data randomly, our test set might end up with zero churners, making evaluation meaningless.
#
# We use **Stratified Sampling** (`stratify=y`) to lock the class distribution. This guarantees that if 20% of users churn in reality, exactly 20% of users churn in our training set and our test set.

# %%
# X = features, y = target
X, y = step03.make_X_y(df_engineered)

# train/test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training Data Shape: {X_train.shape}")
print(f"Test Data Shape:     {X_test.shape}")
print(f"Training Churn Rate: {y_train.mean():.1%}")
print(f"Testing Churn Rate:  {y_test.mean():.1%}")

# %% [markdown]
# # The Preprocessing Pipeline
#
# To prepare our data for modeling, we contrusct a **Scikit-Learn Pipeline**. This encapsulates all transformations into a single object, preventing "data leakage" (where test data accidentally influences training calculations).
# - **Numeric Features** -> Imputed (Median) -> Scaled (StandardScalar)
# - **Categorical Features** -> One-Hot Encoded
#

# %%
set_config(display='diagram')

# build and fit preprocessor
preprocessor = step03.build_preprocessor()
preprocessor.fit(X_train)

# transform both sets
X_train_processed = preprocessor.transform(X_train)
X_test_processed = preprocessor.transform(X_test)

print(f"Original Shape:  {X_train.shape}")
print(f"Processed Shape: {X_train_processed.shape}")

preprocessor

# %%
# save preprocessor and processed data for step04_modeling
joblib.dump(preprocessor, VECTORIZED_DATA_DIR / "preprocessor.joblib")
joblib.dump({"X": X_train_processed, "y": y_train}, VECTORIZED_DATA_DIR / "train.joblib")
joblib.dump({"X": X_test_processed, "y": y_test}, VECTORIZED_DATA_DIR / "test.joblib")

print("All files saved to:", VECTORIZED_DATA_DIR)

# %% [markdown]
# ### Summary:
# "In this notebook, we established a robust feature engineering pipeline to prepare the data for modeling, directly applying insights from the EDA. We addressed data quality by imputing missing values and scaling distributions, then engineered interaction features such as `ads_per_song` and `avg_song_length` to better capture user dissatisfaction and engagement depth. Finally, we implemented a stratified 80/20 train-test split and applied a preprocessing pipeline—using `StandardScaler` for numeric features and `OneHotEncoder` for categoricals—saving the vectorized datasets to ensure consistent inputs for the subsequent modeling phase."
