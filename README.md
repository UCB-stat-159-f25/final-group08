# Final Project for Group 08 aka Da' Wrecking Crew

<!-- [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group08/main?urlpath=%2Fdoc%2Ftree%2Fnotebooks) -->

## Group Members

**Jocelyn Perez** • **Claire Kaoru Shimazaki** • **Colby Zhang** • **Olorundamilola Kazeem**

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group08/main)    *    [![DOI](https://zenodo.org/badge/1110891217.svg)](https://doi.org/10.5281/zenodo.17972478)

---

## Table of Contents

- [About the Project](#about-the-project)
  - [Background](#background)
  - [01. The Raw Dataset](#01-the-dataset)
  - [02. The Exploratory Data Analysis](#02-the-exploratory-data-analysis)
  - [03. The Features i.e. Data Transformation and Vectorization](#03-the-features-ie-data-transformation-and-vectorization)
  - [04. The Modeling i.e. Analysis and Modeling](#04-the-modeling-ie-analysis-and-modeling)
  - [05. The Reporting i.e. Consolidation](#05-the-reporting-ie-consolidation)
- [The Project Structure](#the-project-structure)
  - [01. How to Run the Project](#how-to-run-the-project)
  - [02. How to Test the Project](#how-to-test-the-project)
  - [03. How to Generate PDFs of the Project](#how-to-generate-pdfs-of-the-project)
  - [04. How to Get Help for the Project](#04-how-to-get-help-for-the-project)

---

## About the Project

User churn is a critical challenge for subscription-based platforms such as Spotify, where long-term success depends on sustained user engagement. Understanding which behavioral patterns and user characteristics are associated with churn can help platforms identify at-risk users and design more effective retention strategies.

In this project, we analyze a synthetic Spotify churn dataset to answer the following questions:
- What behavioral and demographic factors are associated with user churn?
- How well can churn be predicted using machine learning models?
- Which features most strongly drive churn predictions, and how do they influence model decisions?

Our analysis follows a structured, reproducible workflow, progressing from data understanding and exploratory analysis to feature engineering, modeling, and interpretability.

## What's Inside?

### 00. The Main Report

```bash
❯ notebooks/main.ipynb 
```

### 01. The Raw Dataset

```bash
❯ notebooks/step01_data.ipynb 
```

### 02. The Exploratory Data Analysis (EDA)

```bash
❯ notebooks/step02_eda.ipynb
```

### 03. The Featurization i.e. Data Transformation and Vectorization

```bash
❯ notebooks/step03_features.ipynb 
```

### 04. The Modeling i.e. Analysis and Modeling 

```bash
❯ notebooks/step04_modeling.ipynb
```

### 05. The Explanability i.e. Interpretability Analysis

```bash
❯ notebooks/step05_interpret.ipynb
```

## The Project Structure

```bash
❯ tree -f -L 2 .
.
├── ./ai_documentation.txt
├── ./_build
│   ├── ./_build/cache
│   ├── ./_build/html
│   ├── ./_build/logs
│   ├── ./_build/site
│   ├── ./_build/temp
│   └── ./_build/templates
├── ./CITATION.cff
├── ./contribution_statement.md
├── ./data
│   ├── ./data/00_raw
│   ├── ./data/01_processed
│   └── ./data/02_vectorized
├── ./docs
│   └── ./docs/__init__.py
├── ./environment.yml
├── ./fig_builds
│   ├── ./fig_builds/main
│   ├── ./fig_builds/step00_utils
│   ├── ./fig_builds/step01_data
│   ├── ./fig_builds/step02_eda
│   ├── ./fig_builds/step03_features
│   ├── ./fig_builds/step04_modeling
│   └── ./fig_builds/step05_interpret
├── ./final_group08.egg-info
│   ├── ./final_group08.egg-info/dependency_links.txt
│   ├── ./final_group08.egg-info/PKG-INFO
│   ├── ./final_group08.egg-info/requires.txt
│   ├── ./final_group08.egg-info/SOURCES.txt
│   └── ./final_group08.egg-info/top_level.txt
├── ./LICENSE
├── ./Makefile
├── ./misc
│   ├── ./misc/environment-BASIC-01.yml
│   ├── ./misc/environment-BASIC.yml
│   ├── ./misc/__init__.py
│   ├── ./misc/Makefile-BACKUP
│   ├── ./misc/Makefile-BACKUP-01
│   └── ./misc/README-FYEO.md
├── ./myst.datasets.bib
├── ./myst.doi.bib
├── ./myst.references.bib
├── ./myst.yml
├── ./notebooks
│   ├── ./notebooks/__init__.py
│   ├── ./notebooks/main.ipynb
│   ├── ./notebooks/main.py
│   ├── ./notebooks/step00_utils.ipynb
│   ├── ./notebooks/step00_utils.py
│   ├── ./notebooks/step01_data.ipynb
│   ├── ./notebooks/step01_data.py
│   ├── ./notebooks/step02_eda.ipynb
│   ├── ./notebooks/step02_eda.py
│   ├── ./notebooks/step03_features.ipynb
│   ├── ./notebooks/step03_features.py
│   ├── ./notebooks/step04_modeling.ipynb
│   ├── ./notebooks/step04_modeling.py
│   ├── ./notebooks/step05_interpret.ipynb
│   └── ./notebooks/step05_interpret.py
├── ./pdf_builds
│   ├── ./pdf_builds/main
│   ├── ./pdf_builds/step00_utils
│   ├── ./pdf_builds/step01_data
│   ├── ./pdf_builds/step02_eda
│   ├── ./pdf_builds/step03_features
│   ├── ./pdf_builds/step04_modeling
│   ├── ./pdf_builds/step05_interpret
│   └── ./pdf_builds/step05_main
├── ./postBuild
├── ./preBuild
├── ./project-description.md
├── ./pyproject.toml
├── ./README.md
├── ./src
│   ├── ./src/__init__.py
│   ├── ./src/main.py
│   ├── ./src/__pycache__
│   ├── ./src/step00_utils.py
│   ├── ./src/step01_data.py
│   ├── ./src/step02_eda.py
│   ├── ./src/step03_features.py
│   ├── ./src/step04_modeling.py
│   └── ./src/step05_interpret.py
└── ./tests
    ├── ./tests/__init__.py
    ├── ./tests/test_main.py
    ├── ./tests/test_step00_utils.py
    ├── ./tests/test_step01_data.py
    ├── ./tests/test_step02_eda.py
    ├── ./tests/test_step03_features.py
    ├── ./tests/test_step04_modeling.py
    └── ./tests/test_step05_interpret.py

36 directories, 58 files
```

## 01. How to Run the Project

- To create and activate the project's environment

```bash
❯ make env && conda activate final-group08
```

- To add/remove and update the project's environment
  - Open the `environment.yml` file
  - Find the category of the package
  - Add/remove the pacakge and save

```yaml
  # ---------------------------------------------------------------------------
  # 03. EDA / Visualization - BEFORE
  # ---------------------------------------------------------------------------
  - matplotlib
  - seaborn
  - missingno


  # ---------------------------------------------------------------------------
  # 03. EDA / Visualization - AFTER
  # ---------------------------------------------------------------------------
  - matplotlib
  - seaborn
  - missingno
  - plotly 
```

- Update the project's enviroment

```bash
make env || make env && conda activate final-group08
```

## 02. How to Test the Project

- To test run the following command

```bash
❯ make test
```

## 03. How to Generate PDFs of the Project

- To create pdf files from the notebooks

```bash
❯ make all
```

## 04. How to Get Help for the Project

```bash
❯ make help             

USAGE:
  make <target>

00. Defaults / End-to-end:
  help                                  - Show this help message
  all                                   - Build all PDFs via nbconvert (end-to-end)
  env                                   - Create/update env from environment.yml (end-to-end)
  test                                  - TODO placeholder

01. Conda environment (primitives):
  ...
  env-list                              - List conda envs
  env-list-packages                     - List packages in current
  env-update                            - Update environment with new packages 
  ...

02. Conda environment (composites):
  ...

03. Jupyter kernel:
  ...
  ker-list                              - List Jupyter kernels
  ...

04. Project directories:
  ...

05. Jupytext pairing:
  ...

06. Docs / site / exports:
  ...

07. PDF builds (nbconvert):
  ...
```


