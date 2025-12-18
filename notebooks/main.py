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
# title: Main - Reporting
# subject: Churn Analysis
# subtitle: Reporting - Churn Analysis
# short_title: Reporting
# date: 2025-12-17
#
# affiliations:
#   - id: "ucb"
#     name: "University of California, Berkeley"
#
# authors:
#   - name: Jocelyn Perez
#     affiliations: ["ucb"]
#     email: jocelyneperez@berkeley.edu
#     orcid: 0009-0009-0231-9254
#
#   - name: Claire Kaoru Shimazaki
#     affiliations: ["ucb"]
#     email: ckshimazaki@berkeley.edu
#     orcid: 0009-0001-0828-3370
#
#   - name: Colby Zhang
#     affiliations: ["ucb"]
#     email: colbyzhang@berkeley.edu
#     orcid: 0009-0005-4786-6922
#
#   - name: Olorundamilola Kazeem
#     affiliations: ["ucb"]
#     email: dami@berkeley.edu
#     orcid: 0000-0003-2118-2221
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
#     output: ../pdf_builds/main/main_ipynb_to.pdf
#     line_numbers: true
#
# license: CC-BY-4.0
#
# keywords: main, churn, reprting, spotify
#
# abstract: Reporting...
# ---
#

# %% [markdown]
# # Main: Reporting

# %%
import src.step00_utils as step00_utils


# %%
import pandas as pd
from pathlib import Path
from IPython.display import Image, display



# %% [markdown]
# # Predicting User Churn from Listening Behavior

# %% [markdown]
# ## Introduction
# User churn is a critical challenge for subscription-based platforms such as Spotify, where long-term success depends on sustained user engagement. Understanding which behavioral patterns and user characteristics are associated with churn can help platforms identify at-risk users and design more effective retention strategies.
# In this project, we analyze a synthetic Spotify churn dataset to answer the following questions:
# What behavioral and demographic factors are associated with user churn?
# How well can churn be predicted using machine learning models?
# Which features most strongly drive churn predictions, and how do they influence model decisions?
# Our analysis follows a structured, reproducible workflow, progressing from data understanding and exploratory analysis to feature engineering, modeling, and interpretability.

# %% [markdown]
# ## Data Description and Assumptions
# The dataset consists of 8,000 synthetic Spotify users generated using GPT to simulate realistic listening behavior, subscription types, device usage, and churn outcomes. Below we list the features of the dataset. 
# 1. `user_id (Numeric, UUID)`: User's universal unique indentifer: 123 (from 1 to 8000).
#
# 2. `gender (Categorical, String)`: User's gender, options are: Male / Female / Other. Example: Female.
#
# 3. `age (Numeric, Integer)`: User's age in ### format. Example: 54.
#
# 4. `country (Categorical, String)`: User's location in @@ format. Example: US.
#
# 5. `subscription_type (Categorical, String)`: User's subscription type, options are Family / Free / Premium / Student. Example: Free.
#
# 6. `listening_type (Numeric, Integer)`: User's listening time in minutes per day in #### format. Example: 789.
#
# 7. `songs_played_per_day (Numeric, Integer)`: User's number of songs played per day in ### format. Exmaple: 19.
#
# 8. `skip_rate (Numeric, Float)`: User's percetange of songs played per day in #.## format. Example: 0.04.
#
# 9. `device_type (Categorical, String)`: User's device type, optiona are Desktop / Mobile / Web. Example: Mobile. 
#
# 10. `ads_listened_per_week (Numeric, Integer)`: User's number of ads heard per week in ### format. Example: 31.
#
# 11. `offline_listening (Numeric, Boolean)`: User's offline usage mode. Example: 0 = Not Active Offline, 1 Active Offline.
#
# 12. `is_chruned (Numeric, Boolean)`: User's churn status. The target variable. Example: 0 = Active, 1 = Churned
#
#
# The target variable is a binary indicator of whether a user churned.
# Because the dataset is synthetically generated rather than collected from real users, this analysis should be interpreted as exploratory rather than causal. We assume that the simulated relationships reasonably approximate real-world churn behavior, but we cannot verify the underlying data-generating process. As a result, all findings describe associations and predictive patterns, not causal effects.
#
# Below is a preview of the first few rows of our dataset to illustrate its structure. It was sourced from Kaggle, [linked here](https://www.kaggle.com/datasets/nabihazahid/spotify-dataset-for-churn-analysis)

# %%
raw_dir = Path.cwd().parent / "data" / "00_raw"
csv_path = next(raw_dir.glob("*.csv")) 

df = pd.read_csv(csv_path)
print("Loaded:", csv_path.name)

df.head()

# %% [markdown]
# ## Exploratory Data Analysis 
# We conduct exploratory data analysis to understand patterns associated with user churn and to motivate feature selection for downstream modeling.

# %%
img_path = Path.cwd().parent / "fig_builds" / "step02_eda" / "churn_distribution.png"
display(Image(filename=str(img_path)))

# %% [markdown]
# In this first plot, we see that approximately 74% of users did not churn, while 26% churned, which indicates a moderate class imbalance typical of churn prediction problems. This imbalance motivates the use of appropriate evaluation metrics and careful interpretation of model performance.

# %%
img_path_two = Path.cwd().parent / "fig_builds" / "step02_eda" / "churn_rate_by_subscription_type.png"
display(Image(filename=str(img_path_two)))

# %% [markdown]
# Here, we see that among all subscription types, the Family plan exhibits the highest churn rate at approximately 27%, indicating that users on family subscriptions are more likely to churn compared to users on other plans in this dataset.

# %%
img_path_th = Path.cwd().parent / "fig_builds" / "step02_eda" / "churn_rate_by_offline_listening.png"
display(Image(filename=str(img_path_th)))

# %% [markdown]
# Here, we see that users who utilize offline listening features exhibit substantially lower churn rates compared to users who do not. This suggests that offline listening may reflect higher platform dependence and stronger user engagement.

# %% [markdown]
# Overall, the EDA showed that churn is more strongly associated with behavioral engagement and subscription characteristics than it is with static demographic features. 

# %% [markdown]
# ## Feature Engineering and Preprocessing
# Raw usage logs capture what users did, but not how they experienced the platform. To better represent user engagement and frustration, we engineer interpretable behavioral features such as average song length and ads per song, which proxy engagement intensity and ad tolerance, respectively.
# To prevent data leakage and ensure reproducibility, we construct a preprocessing pipeline using scikit-learn. Numerical features are imputed and standardized, categorical features are one-hot encoded, and the dataset is split using stratified sampling to preserve the churn rate in both training and test sets. This pipeline produces consistent, vectorized inputs for all downstream models.

# %% [markdown]
# ## Model Building and Evaluation
# We first establish a baseline using Logistic Regression with class weighting to account for imbalance. While interpretable, this linear model achieves limited performance, reflecting the complexity of churn behavior.
# We then train a Random Forest classifier to capture non-linear relationships and feature interactions. Hyperparameters are tuned using cross-validation with F1-score as the primary metric. The Random Forest outperforms the baseline model, confirming that churn depends on interacting behavioral factors rather than simple linear effects.
# However, despite improved performance, the model’s recall for churned users remains modest. Many churners are misclassified as retained users, highlighting the inherent difficulty of predicting churn and the presence of unobserved factors beyond behavioral data.

# %% [markdown]
# ## Results and Interpretation
# To understand why the Random Forest makes its predictions, we apply model interpretability techniques.
# Global SHAP analysis shows that engagement-related features dominate churn predictions. Average song length, listening time, skip rate, and songs played per day are the most influential variables, while age plays a secondary role. Device type, country, and gender contribute relatively little to overall predictions.
# Local SHAP explanations reveal that individual churn predictions arise from the combined effect of many small signals rather than a single decisive feature. For example, a churned user may be predicted to churn due to slightly reduced listening time, higher skip rate, and lower engagement simultaneously.
# Partial dependence plots further illustrate non-linear relationships. Churn risk decreases sharply as engagement increases at low levels, then plateaus, indicating diminishing returns to very high engagement. This suggests that early drops in engagement may be especially informative warning signs.
# Finally, error analysis shows that many missed churners exhibit engagement patterns similar to retained users. This explains the model’s low recall and suggests that churn decisions are often driven by external or unobserved factors such as pricing changes, competitor offers, or personal circumstances.

# %% [markdown]
# ## Limitations and Conclusion
# This analysis is subject to several limitations. First, the dataset is synthetic and observational, limiting external validity and precluding causal interpretation. Second, behavioral data alone cannot capture all drivers of churn, placing an upper bound on predictive performance. Finally, class imbalance and overlapping feature distributions make churn inherently difficult to predict.
#
#

# %% [markdown]
# ## Author Contributions

# %%
