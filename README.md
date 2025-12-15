# Final Project for Group 08 aka Da' Wrecking Crew

<!-- [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group08/main?urlpath=%2Fdoc%2Ftree%2Fnotebooks) -->

## Group Members

**Jocelyn Perez** • **Claire Kaoru Shimazaki** • **Colby Zhang** • **Olorundamilola Kazeem**

[Group Resources - Internal Use Only](https://drive.google.com/drive/folders/1Za-QzHQQBWf5ob-vrTWZSwD2isSU4_oy?usp=sharing)

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
- [Misc.](#misc)

---

## About the Project
...

### Background

```bash
Write a short self-contained description of the project, including the motivation behind your project and the analysis you conducted. 

Include all relevant information about how to run the analysis, including installation steps (for any packages, environments, etc.), testing, and automation. 

A good README should be short but also provide all the useful information to help the user to start running the analysis.
```

### 01. The Raw Dataset

```bash

```

### 02. The Exploratory Data Analysis 

```bash

```

### 03. The Features i.e. Data Transformation and Vectorization

```bash

```

### 04. The Modeling i.e. Analysis and Modeling 

```bash

```

### 05. The Reporting i.e. Consolidation


...

```bash

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
│   ├── ./fig_builds/step00_utils
│   ├── ./fig_builds/step01_data
│   ├── ./fig_builds/step02_eda
│   ├── ./fig_builds/step03_features
│   ├── ./fig_builds/step04_modeling
│   └── ./fig_builds/step05_main
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
│   ├── ./notebooks/step05_main.ipynb
│   └── ./notebooks/step05_main.py
├── ./pdf_builds
│   ├── ./pdf_builds/step00_utils
│   ├── ./pdf_builds/step01_data
│   ├── ./pdf_builds/step02_eda
│   ├── ./pdf_builds/step03_features
│   ├── ./pdf_builds/step04_modeling
│   └── ./pdf_builds/step05_main
├── ./postBuild
├── ./preBuild
├── ./project-description.md
├── ./pyproject.toml
├── ./README.md
├── ./src
│   ├── ./src/__init__.py
│   ├── ./src/__pycache__
│   ├── ./src/step00_utils.py
│   ├── ./src/step01_data.py
│   ├── ./src/step02_eda.py
│   ├── ./src/step03_features.py
│   ├── ./src/step04_modeling.py
│   └── ./src/step05_main.py
└── ./tests
    ├── ./tests/__init__.py
    ├── ./tests/test_step00_utils.py
    ├── ./tests/test_step01_data.py
    ├── ./tests/test_step02_eda.py
    ├── ./tests/test_step03_features.py
    ├── ./tests/test_step04_modeling.py
    └── ./tests/test_step05_main.py

32 directories, 54 files
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

- To be added/implemented

```bash
❯ make test
```

## 03. How to Generate PDFs of the Project

- To create pdf files from the notebooks

```bash
❯ make all
```

## Misc.

```bash

```


