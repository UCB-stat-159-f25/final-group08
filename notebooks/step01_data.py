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
# title: Step 01 - Data
# subject: Churn Analysis
# subtitle: Step 00 - Data - Churn Analysis
# short_title: Raw Data
# date: 2025-12-17
#
# affiliations:
#   - id: "ucb"
#     name: "University of California, Berkeley"
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
#     output: ../pdf_builds/step01_data/step01_data_ipynb_to.pdf
#     line_numbers: true
#
# license: CC-BY-4.0
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

# %%
import src.step00_utils as step00_utils

import typing as typ

import pandas as pd
import pandera as pdr
import pathlib as pl

import missingno as msno

# %%
step00_utils.DIR_PROJECT_CURRENT

# %%
step00_utils.DIR_PROJECT_HOME

# %%
step00_utils.DIR_DATA

# %% [markdown]
# Q: What data are we investigating? 
# - A: [Spotify Dataset for Churn Analysis](https://www.kaggle.com/datasets/nabihazahid/spotify-dataset-for-churn-analysis)
#
# Q: What are the data and metadata details?
# - A: Describe the data, metadata, datatypes, features, labels, number of samples, etc.
#
# Q: Is this data publicly available? How is it accessed?
# - A: Downloaded to local directory - ./data/00_raw/spotify_churn_dataset.csv
#

# %%
data_raw = pd.read_csv(step00_utils.DIR_DATA_00_RAW / step00_utils.FILE_SPOTIFY_CHURN_DATASET_CSV)
data_raw

# %%
# # %matplotlib inline
# msno.matrix(data_raw.sample(250))
msno.matrix(data_raw);

# %%
# msno.bar(data_raw.sample(250))
msno.bar(data_raw);

# %%
