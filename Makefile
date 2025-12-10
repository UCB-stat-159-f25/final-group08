###
# 00. Reference
# - https://stat159.berkeley.edu/fall-2025/lectures/automation/make/#make-for-creating-a-new-environment
# - https://github.com/hackalog/make_better_defaults
###

.ONESHELL:
SHELL = /bin/bash


###
# 01. Configuration
###
ENV_NAME       := final-group08
PYTHON_VERSION := 3.12
CONDA_BASE     ?= /srv/conda
# Datahub default; change/remove if needed - source /srv/conda/etc/profile.d/conda.sh
CONDA_INIT     := source $(CONDA_BASE)/etc/profile.d/conda.sh || true


###
# 01. Environment Management
###

env-create-from-scratch-once:
	$(CONDA_INIT); \
	conda create -n $(ENV_NAME) python=$(PYTHON_VERSION) -y; \
	conda activate $(ENV_NAME); \
	conda install -y ipykernel jupyterlab jupyter-ai numpy pandas scikit-learn matplotlib seaborn scipy mlcroissant; \
	conda env export --from-history > environment.yml; \
	python -m ipykernel install --user --name $(ENV_NAME) --display-name "Python ($(ENV_NAME))"; \
	conda deactivate; \
	conda remove -n $(ENV_NAME) --all -y; \
	echo "One-time bootstrap complete. environment.yml written. Commit it and use 'make env-create-from-yml' next time."


env-create-from-yml:
	$(CONDA_INIT); \
	conda env create -f environment.yml; \
	conda activate $(ENV_NAME); \
	python -m ipykernel install --user --name $(ENV_NAME) --display-name "IPython - ($(ENV_NAME))"

env-activate:
	$(CONDA_INIT); \
	conda activate $(ENV_NAME); \

env-deactivate:
	$(CONDA_INIT); \
	conda deactivate; \

env-remove:
	$(CONDA_INIT); \
	conda remove -n $(ENV_NAME) --all; \

.PHONY: env-create-from-scratch-once env-create-from-yml env-activate env-deactivate env-remove


###
# 02. Kernel Management
###

KERNEL = $(ENV_NAME)

ker-create:
	python -m ipykernel install --user --name $(KERNEL) --display-name "IPython - ($(KERNEL))"

ker-list:
	jupyter kernelspec list

ker-remove:
	jupyter kernelspec uninstall -y $(KERNEL)

.PHONY: ker-create ker-list ker-remove


###
# 03. Project, Directory, and File Structure
###
# (Intentionally empty for future additions)


###
# 04. Notebook Management with JupyText
###
# TODO — Consolidate this section


###
# 05. Project Documents and Documentation
###
# (Intentionally empty for future additions)


###
# Appendix Aa. General E2E - Phony and Default Target
###

all:
	@echo "TODO - Create an end-to-end pipeline — All tasks complete!"

.PHONY: all


###
# Appendix Zz. Help
###

help:
	@echo "01. Environment targets:"
	@echo "  env-create-from-scratch-once - Create the environment from scratch"
	@echo "  env-create-from-yml          - Create the environment from environment.yml"
	@echo "  env-remove                   - Remove the 'final-group08' environment"
	@echo "  env-update                   - Update, install, and clean up packages INTO the environment"
	@echo "  env-update-environment-yml   - Update and save the environment packages INTO environment.yml"
	@echo "  env-run-jupyterlab           - Launch JupyterLab using the environment"
	@echo "  env-list                     - List all conda environments"
	@echo "  env-package-install          - Install a package into an environment"
	@echo "  env-package-check            - Check if a package is installed in an environment"
	@echo "  env-activate                 - Activate the 'final-group08' environment"
	@echo "  env-deactivate               - Deactivate the current environment"
	@echo ""
	@echo "02. Kernel targets:"
	@echo "  ker-create                   - Create the IPython kernel"
	@echo "  ker-list                     - List all Jupyter kernels"
	@echo "  ker-remove                   - Remove the IPython kernel"
	@echo ""
	@echo "03. Directory targets:"
	@echo "  dir-code-create              - Create the code/ directory and subdirectories"
	@echo "  dir-code-delete              - Delete the code/ directory"
	@echo "  dir-data-create              - Create the data/ directory and subdirectories"
	@echo "  dir-data-delete              - Delete the data/ directory and subdirectories"
	@echo "  dir-docs-create              - Create the docs/ directory"
	@echo "  dir-docs-delete              - Delete the docs/ directory"
	@echo "  dir-misc-create              - Create the misc/ directory"
	@echo "  dir-misc-delete              - Delete the misc/ directory"
	@echo "  dir-notebooks-create         - Create the notebooks/ directory"
	@echo "  dir-notebooks-delete         - Delete the notebooks/ directory"
	@echo "  dir-tests-create             - Create the tests/ directory"
	@echo "  dir-tests-delete             - Delete the tests/ directory"
	@echo ""
	@echo "04. Jupytext targets:"
	@echo "  nb-pair-all-py             - Pair all from .py to .ipynb"
	@echo "  nb-pair-all-ipynb          - Pair all from .ipynb to .py"
	@echo "  nb-pair-p01-py             - Pair P01 .py -> .ipynb"
	@echo "  nb-pair-p01-ipynb          - Pair P01 .ipynb -> .py"
	@echo "  nb-pair-p02-py             - Pair P02 .py -> .ipynb"
	@echo "  nb-pair-p02-ipynb          - Pair P02 .ipynb -> .py"
	@echo "  nb-pair-p03-py             - Pair P03 .py -> .ipynb"
	@echo "  nb-pair-p03-ipynb          - Pair P03 .ipynb -> .py"
	@echo "  nb-pair-p04-py             - Pair P04 .py -> .ipynb"
	@echo "  nb-pair-p04-ipynb          - Pair P04 .ipynb -> .py"
	@echo ""
	@echo "05. Documentation targets:"
	@echo "  doc-ai-documentation       - Generate ai_documentation.txt from template"
	@echo "  doc-contribution-statement - Generate contribution_statement.md from template"
	@echo "  doc-myst-site-init         - Initialize a MyST site"
	@echo "  doc-myst-site-init-toc     - Initialize MyST site with Table of Contents"
	@echo "  doc-myst-site-init-ghpages - Initialize MyST site for GitHub Pages"
	@echo ""
	@echo "Appendix Aa. General E2E targets:"
	@echo "  all                        - Run all tasks"

.PHONY: help
