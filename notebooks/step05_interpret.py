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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ---
# title: Step 05- Interpret
# subject: Churn Analysis
# subtitle: Step 05 - Interpret - Churn Analysis
# short_title: Explanations and Interpretations
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
#     output: ../pdf_builds/step05_interpret/step05_interpret_ipynb_to.pdf
#     line_numbers: true
#
# license: CC-BY-4.0
#
# keywords: interpret, churn, spotify
#
# abstract: What are the explanations? intrepretations?
# ---
#

# %%
import sys
from pathlib import Path

PROJECT_ROOT = Path.cwd().parent
sys.path.insert(0, str(PROJECT_ROOT))

import joblib

DATA_DIR = PROJECT_ROOT / "data" / "02_vectorized"
train = joblib.load(DATA_DIR / "train.joblib")
test  = joblib.load(DATA_DIR / "test.joblib")

X_train = train["X"]
X_test  = test["X"]
y_test  = test["y"]

X_test.shape


# %%
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

rf = RandomForestClassifier(
    random_state=0,
    class_weight="balanced"
)

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [10, None],
    "min_samples_split": [2, 5],
}

grid = GridSearchCV(
    rf,
    param_grid=param_grid,
    cv=5,
    n_jobs=-1,
    scoring="f1"
)

grid.fit(X_train, train["y"])
final_model = grid.best_estimator_

print("Best params:", grid.best_params_)
print(classification_report(y_test, final_model.predict(X_test)))


# %%
import shap
import matplotlib.pyplot as plt

explainer = shap.TreeExplainer(final_model)
shap_values = explainer.shap_values(X_test)


# %%
