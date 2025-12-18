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
# title: Step 01 - Raw Data
# subject: Churn Analysis
# subtitle: Step 01 - Raw Data - Churn Analysis
# short_title: Raw Data
# date: 2025-12-17
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
#
#   - name: Claire Kaoru Shimazaki
#     email: ckshimazaki@berkeley.edu
#     orcid: 0009-0001-0828-3370
#     affiliations: ["ucb"]
#
#
#   - name: Colby Zhang
#     email: colbyzhang@berkeley.edu
#     orcid: 0009-0005-4786-6922
#     affiliations: ["ucb"]
#
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
#     output: ../pdf_builds/step01_data/step01_data_ipynb_to.pdf
#     line_numbers: true
#
# license: BSD-3-Clause
#
# keywords: data, raw data, churn, spotify
#
# abstract: What is the data? metadata?
# ---

# %% [markdown]
# # Step 01: Data

# %% [markdown]
# The churn analysis dataset can be found here, {cite}`spotify-churn-kaggle`. 
#

# %%
import src.step00_utils as step00_utils
import pandas as pd
import missingno as msno

# %% [markdown]
# **Q: What data are we investigating?**
# - A: [Spotify Dataset for Churn Analysis](https://www.kaggle.com/datasets/nabihazahid/spotify-dataset-for-churn-analysis). 
#
# **Sources**
#
# The dataset is artificially created using GPT, not collected from real users, and is intended for practice, experimentation, and modeling purposes only.
#
# **Collection Methodlogy**
#
# The dataset was synthetically generated using GPT to simulate Spotify user behavior. It includes demographic details, listening habits, subscription types, device usage, and engagement metrics. Churn labels were also generated to mimic real-world distribution (active vs churned users).
#
# **Q: What are the data and metadata details?**
#
# - A: Describe the data, metadata, datatypes, features, labels, number of samples, etc.
#
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
#
# **Q: Is this data publicly available? How is it accessed?**
# - A: Downloaded to local directory - ./data/00_raw/spotify_churn_dataset.csv
#
#
# **Data Example**

# %%
data_raw = pd.read_csv(step00_utils.DIR_DATA_00_RAW / step00_utils.FILE_SPOTIFY_CHURN_DATASET_CSV)
data_raw.head()

# %% [markdown]
# **No Missing Values**

# %%
# # %matplotlib inline
# msno.matrix(data_raw);
msno.bar(data_raw);
