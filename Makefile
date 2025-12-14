###
# 00. Reference
# - https://stat159.berkeley.edu/fall-2025/lectures/automation/make/#make-for-creating-a-new-environment
# - https://github.com/hackalog/make_better_defaults
###

.ONESHELL:
SHELL = /bin/bash



############
# 00. Configuration
############

ENV_NAME         := final-group08
PYTHON_VERSION   := 3.12
CONDA_BASE       ?= /srv/conda
# Datahub default; change/remove if needed - source /srv/conda/etc/profile.d/conda.sh
# CONDA_INIT     := source $(CONDA_BASE)/etc/profile.d/conda.sh || true
CONDA_INIT       := source $(CONDA_BASE)/etc/profile.d/conda.sh 
CONDA_ACTIVATE 	 := $(CONDA_INIT) && conda activate $(ENV_NAME)
CONDA_DEACTIVATE := $(CONDA_INIT) && conda deactivate


############
# 01. Environment Management - Primitives
############

.PHONY: env-source-conda env-create-from-scratch env-create-from-yml \
        env-activate env-install-basics env-export-from-history \
        env-deactivate env-list env-list-packages env-remove

env-source-conda:
	$(CONDA_INIT)

# env-create-from-scratch: env-source-conda
env-create-from-scratch:
	conda create -n $(ENV_NAME) python=$(PYTHON_VERSION) -y

# env-create-from-yml: env-source-conda
env-create-from-yml:
	conda env create -f environment.yml

# env-activate: env-source-conda
env-activate:
	@echo "Run the following command manually to TURN ON the environment:"
	@echo "    conda activate $(ENV_NAME)"
	@echo "    pip install -e ."
# 	conda activate $(ENV_NAME)
# 	$(CONDA_ACTIVATE)
# 	pip install -e .
	$(CONDA_ACTIVATE) && pip install -e .

# env-install-basics: env-source-conda
env-install-basics:
# 	conda activate $(ENV_NAME)
	conda install -y \
	ipykernel \
	jupyterlab \
	jupyter-ai \
	jupytext \
	nbconvert \
	pandoc \
	texlive-core \
	playwright \
	numpy \
	pandas \
	scikit-learn \
	matplotlib \
	seaborn \
	scipy \
	mlcroissant \

# env-export-from-history: env-source-conda
env-export-from-history:
# 	conda activate $(ENV_NAME)
#   For clean, minimal, maintainable environment.yml (best for repos)
	conda env export --from-history > environment.yml
#   For strict reproducibility inside the same platform (rare)
# 	conda env export --no-builds > environment.yml

# env-deactivate: env-source-conda
env-deactivate:
# 	conda deactivate || true
	@echo "Run the following command manually to TURN OFF the environment:"
	@echo "    conda deactivate"
#	conda deactivate
	$(CONDA_DEACTIVATE)

# env-list: env-source-conda
env-list:
	conda env list

env-list-packages:
	conda list

# env-remove: env-source-conda
env-remove:
	conda remove -n $(ENV_NAME) -y --all

############
# 02. Environment Managenent - Kernel Primitives
############

.PHONY: ker-create ker-list ker-remove

KERNEL := $(ENV_NAME)

ker-create:
	python -m ipykernel install --user --name $(KERNEL) --display-name "IPython - $(KERNEL)"

ker-list:
	jupyter kernelspec list

ker-remove:
	jupyter kernelspec uninstall -y $(KERNEL)

############
# 03. Environment Management - Composites - All Directives
############

.PHONY: all-env-create-from-scratch-once all-env-create-from-yml

# all-env-create-from-scratch-once: env-source-conda env-create-from-scratch env-activate env-install-basics env-export-from-history ker-create 
# # env-deactivate env-remove
# 	@echo "One-time bootstrap complete. environment.yml written."
# 	@echo "Commit it and use 'make all-env-create-from-yml' next time."

all-env-create-from-scratch-once:
	$(CONDA_INIT); \
	conda create -n $(ENV_NAME) python=$(PYTHON_VERSION) -y; \
	conda activate $(ENV_NAME); \
	conda install -y \
		ipykernel \
		jupyterlab \
		jupyter-ai \
		jupytext \
		nbconvert \
		pandoc \
		texlive-core \
		playwright \
		numpy \
		pandas \
		scikit-learn \
		matplotlib \
		seaborn \
		scipy \
		mlcroissant; \
	conda env export --from-history > environment.yml; \
	python -m ipykernel install --user --name $(ENV_NAME) --display-name "IPython - $(ENV_NAME)"; \
	conda deactivate; \
	conda remove -n $(ENV_NAME) --all -y; \	
	@echo "One-time bootstrap complete. environment.yml written."
	@echo "Commit it and use 'make all-env-create-from-yml' next time."

# all-env-create-from-yml: env-source-conda env-create-from-yml env-activate ker-create
# # all-env-create-from-yml: $(CONDA_INIT) env-create-from-yml env-activate ker-create
# 	@echo "Environment created from environment.yml and kernel installed."

###
# GOTO - Appendix below: rename from all-env-create-from-yml to env, as required
###
all-env-create-from-yml:
# 	$(CONDA_INIT); \
	conda env create -f environment.yml; \
	conda activate $(ENV_NAME); \

	$(CONDA_INIT); \
	conda env create -f environment.yml -n $(ENV_NAME) || conda env update -f environment.yml -n $(ENV_NAME); \
	conda activate $(ENV_NAME); \
	
	pip install -e .
	python -m ipykernel install --user --name $(ENV_NAME) --display-name "IPython - $(ENV_NAME)"
	
	@echo "Environment created from environment.yml and kernel installed."

############
# 04. Project, Directory, and File Structure
############

.PHONY: dir-create-binder dir-delete-binder \
	dir-create-data dir-delete-data \
	dir-create-docs dir-delete-docs \
	dir-create-misc dir-delete-misc \
	dir-create-notebooks dir-delete-notebooks \
	dir-create-pdf-builds dir-delete-pdf-builds \
	dir-create-src dir-delete-src \
	dir-create-tests dir-delete-tests \

dir-create-binder:
	mkdir -p binder

	touch binder/.gitkeep \
		binder/preBuild \
		binder/environment.yml
		binder/postBuild

	@echo "Created the binder directory and files."

dir-delete-binder:
	rm -rf binder

	@echo "Deleted the binder directory and files."

dir-create-data:
	mkdir -p data/00_raw \
		data/01_processed \
		data/02_vectorized

	touch data/.gitkeep \
		data/00_raw/.gitkeep \
		data/01_processed/.gitkeep \
		data/02_vectorized/.gitkeep

	@echo "Created the data directory and files."

dir-delete-data:
# 	rm -rf data/00_raw \
		data/01_processed \
		data/02_vectorized
	rm -rf \
		data/01_processed \
		data/02_vectorized

	@echo "Deleted the data directory and files."

dir-create-docs:
	mkdir -p docs

	touch docs/.gitkeep docs/__init__.py

	@echo "Created the docs directory and files."

dir-delete-docs:
	rm -rf docs

	@echo "Deleted the docs directory and files."

dir-create-misc:
	mkdir -p misc

	touch misc/.gitkeep misc/__init__.py

	@echo "Created the misc directory and files."

dir-delete-misc:
	rm -rf misc

	@echo "Deleted the misc directory and files."

dir-create-notebooks:
	mkdir -p notebooks

	touch notebooks/.gitkeep notebooks/__init__.py \
		notebooks/step00_utils.ipynb \
		notebooks/step01_data.ipynb \
		notebooks/step02_eda.ipynb \
		notebooks/step03_features.ipynb \
		notebooks/step04_modeling.ipynb \
		notebooks/step05_main.ipynb

	@echo "Created the notebooks directory and files."

dir-delete-notebooks:
	rm -rf notebooks

	@echo "Deleted the notebooks directory and files."


dir-create-fig-builds:
	mkdir -p fig_builds \
		fig_builds/step00_utils \
		fig_builds/step01_data \
		fig_builds/step02_eda \
		fig_builds/step03_features \
		fig_builds/step04_modeling \
		fig_builds/step05_main

	touch fig_builds/.gitkeep \
		fig_builds/step00_utils/.gitkeep \
		fig_builds/step01_data/.gitkeep \
		fig_builds/step02_eda/.gitkeep \
		fig_builds/step03_features/.gitkeep \
		fig_builds/step04_modeling/.gitkeep \
		fig_builds/step05_main/.gitkeep

		@echo "Deleted the fig_builds directory and files."

dir-delete-fig-builds:
	rm -rf fig_builds

	@echo "Deleted the fig_builds directory and files."

dir-create-pdf-builds:
	mkdir -p pdf_builds \
		pdf_builds/step00_utils \
		pdf_builds/step01_data \
		pdf_builds/step02_eda \
		pdf_builds/step03_features \
		pdf_builds/step04_modeling \
		pdf_builds/step05_main

	touch pdf_builds/.gitkeep \
		pdf_builds/step00_utils/.gitkeep \
		pdf_builds/step01_data/.gitkeep \
		pdf_builds/step02_eda/.gitkeep \
		pdf_builds/step03_features/.gitkeep \
		pdf_builds/step04_modeling/.gitkeep \
		pdf_builds/step05_main/.gitkeep

	@echo "Created the pdf_builds directory and files."

dir-delete-pdf-builds:
	rm -rf pdf_builds

	@echo "Deleted the pdf_builds directory and files."

dir-create-src:
	mkdir -p src

	touch src/.gitkeep src/__init__.py \
		src/step00_utils.py \
		src/step01_data.py \
		src/step02_eda.py \
		src/step03_features.py \
		src/step04_modeling.py \
		src/step05_main.py

	@echo "Created the src directory and files."

dir-delete-src:
	rm -rf src

	@echo "Deleted the src directory and files."

dir-create-tests:
	mkdir -p tests

	touch tests/.gitkeep tests/__init__.py \
		tests/test_step00_utils.py \
		tests/test_step01_data.py \
		tests/test_step02_eda.py \
		tests/test_step03_features.py \
		tests/test_step04_modeling.py \
		tests/test_step05_main.py

dir-delete-tests:
	rm -rf tests

all-dir-create: dir-create-data dir-create-docs dir-create-misc dir-create-notebooks dir-create-fig-builds dir-create-pdf-builds dir-create-src dir-create-tests
	@echo "Created all of the required project directories."

all-dir-remove: dir-delete-data dir-delete-docs dir-delete-misc dir-delete-notebooks dir-delete-fig-builds dir-delete-pdf-builds dir-delete-src dir-delete-tests
	@echo "Removed all of the required project directories."

############
# 05. Notebook Management with JupyText
############

.PHONY:  nb-pair-step00-py nb-pair-step00-ipynb \
	nb-pair-step01-py nb-pair-step01-ipynb \
	nb-pair-step02-py nb-pair-step02-ipynb \
	nb-pair-step03-py nb-pair-step03-ipynb \
	nb-pair-step04-py nb-pair-step04-ipynb \
	nb-pair-step05-py nb-pair-step05-ipynb \
	nb-pair-all-py nb-pair-all-ipynb 

DIR_NOTEBOOKS = notebooks

nb-pair-step00-py:
	jupytext --set-formats py:percent,ipynb $(DIR_NOTEBOOKS)/step00_utils.py

nb-pair-step00-ipynb:
	jupytext --set-formats ipynb:percent,py $(DIR_NOTEBOOKS)/step00_utils.ipynb

nb-pair-step01-py:
	jupytext --set-formats py:percent,ipynb $(DIR_NOTEBOOKS)/step01_data.py

nb-pair-step01-ipynb:
	jupytext --set-formats ipynb:percent,py $(DIR_NOTEBOOKS)/step01_data.ipynb

nb-pair-step02-py:
	jupytext --set-formats py:percent,ipynb $(DIR_NOTEBOOKS)/step02_eda.py

nb-pair-step02-ipynb:
	jupytext --set-formats ipynb:percent,py $(DIR_NOTEBOOKS)/step02_eda.ipynb

nb-pair-step03-py:
	jupytext --set-formats py:percent,ipynb $(DIR_NOTEBOOKS)/step03_features.py

nb-pair-step03-ipynb:
	jupytext --set-formats ipynb:percent,py $(DIR_NOTEBOOKS)/step03_features.ipynb

nb-pair-step04-py:
	jupytext --set-formats py:percent,ipynb $(DIR_NOTEBOOKS)/step04_modeling.py

nb-pair-step04-ipynb:
	jupytext --set-formats ipynb:percent,py $(DIR_NOTEBOOKS)/step04_modeling.ipynb

nb-pair-step05-py:
	jupytext --set-formats py:percent,ipynb $(DIR_NOTEBOOKS)/step05_main.py

nb-pair-step05-ipynb:
	jupytext --set-formats ipynb:percent,py $(DIR_NOTEBOOKS)/step05_main.ipynb

nb-pair-all-py: nb-pair-step00-py \
	nb-pair-step01-py \
	nb-pair-step02-py \
	nb-pair-step03-py \
	nb-pair-step04-py \
	nb-pair-step05-py
# 	jupytext --set-formats py:percent,ipynb $(DIR_NOTEBOOKS)/step0{0..5}_*.py

nb-pair-all-ipynb: nb-pair-step00-ipynb \
	nb-pair-step01-ipynb \
	nb-pair-step02-ipynb \
	nb-pair-step03-ipynb \
	nb-pair-step04-ipynb \
	nb-pair-step05-ipynb
# 	jupytext --set-formats ipynb:percent,py $(DIR_NOTEBOOKS)/step0{0..5}_*.ipynb


############
# 06. Project Documents and Documentation
############

.PHONY: doc-ai-documentation doc-contribution-statement \
	doc-license \
	doc-myst-site-init doc-myst-site-init-toc doc-myst-site-init-ghpages \
	doc-nbconvert

doc-ai-documentation:
	cat <<'EOF' > ai_documentation.txt
		------------------------------------------------
		[Step 00 for notebooks/step00_utils.ipynb, src/step00_utils.py, and tests/test_step00_utils.py]

		PROMPT:

		OUTPUT:


		------------------------------------------------
		[Step 01 for notebooks/step01_data.ipynb, src/step01_data.py, and tests/test_step01_data.py]

		PROMPT:

		OUTPUT:


		------------------------------------------------
		[Step 02 for notebooks/step02_eda.ipynb, src/step02_eda.py, and tests/test_step02_eda.py]

		PROMPT:

		OUTPUT:


		------------------------------------------------
		[Step 03 for notebooks/step03_features.ipynb, src/step03_features.py, and tests/test_step03_features.py]

		PROMPT:

		OUTPUT:

		------------------------------------------------
		[Step 04 for notebooks/step04_modeling.ipynb, src/step04_modeling.py, and tests/test_step04_modeling.py]

		PROMPT:

		OUTPUT:

		------------------------------------------------
		[Step 05 for notebooks/step05_main.ipynb, src/step05_main.py, and tests/test_step05_main.py]

		PROMPT:

		OUTPUT:
	EOF

doc-contribution-statement:
	cat <<'EOF' > contribution_statement.md
		------------------------------------------------
		[Step 00 for notebooks/step00_utils.ipynb, src/step00_utils.py, and tests/test_step00_utils.py]

		TEAM MEMBER NAME(S) - PERCENT CONTRIBUTION:


		------------------------------------------------
		[Step 01 for notebooks/step01_data.ipynb, src/step01_data.py, and tests/test_step01_data.py]

		TEAM MEMBER NAME(S) - PERCENT CONTRIBUTION:


		------------------------------------------------
		[Step 02 for notebooks/step02_eda.ipynb, src/step02_eda.py, and tests/test_step02_eda.py]

		TEAM MEMBER NAME(S) - PERCENT CONTRIBUTION:


		------------------------------------------------
		[Step 04 for notebooks/step04_modeling.ipynb, src/step04_modeling.py, and tests/test_step04_modeling.py]

		TEAM MEMBER NAME(S) - PERCENT CONTRIBUTION:


		------------------------------------------------
		[Step 05 for notebooks/step05_main.ipynb, src/step05_main.py, and tests/test_step05_main.py]

		TEAM MEMBER NAME(S) - PERCENT CONTRIBUTION:


	EOF

doc-license:
#   choose a license, https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository
	touch LICENSE

doc-myst-site-local-start:
	myst start

doc-myst-site-init:
	myst init

doc-myst-site-init-toc:
	myst init --write-toc

doc-myst-site-init-ghpages:
	myst init --gh-pages

doc-myst-build:
	myst build

doc-myst-build-html:
	myst build --html

doc-myst-build-bibtex:
	myst build --doi-bib

doc-pyproject-toml:
	touch pyproject.toml

doc-nbconvert-step00-utils-to-pdf:
	jupyter nbconvert --to pdf --output-dir pdf_builds/step00_utils notebooks/step00_utils.ipynb

doc-nbconvert-step01-data-to-pdf:
	jupyter nbconvert --to pdf --output-dir pdf_builds/step01_data notebooks/step01_data.ipynb

doc-nbconvert-step02-eda-to-pdf:
	jupyter nbconvert --to pdf --output-dir pdf_builds/step02_eda notebooks/step02_eda.ipynb

doc-nbconvert-step03-features-to-pdf:
	jupyter nbconvert --to pdf --output-dir pdf_builds/step03_features notebooks/step03_features.ipynb

doc-nbconvert-step04-modeling-to-pdf:
	jupyter nbconvert --to pdf --output-dir pdf_builds/step04_modeling notebooks/step04_modeling.ipynb

doc-nbconvert-step05-main-to-pdf:
	jupyter nbconvert --to pdf --output-dir pdf_builds/step05_main notebooks/step05_main.ipynb

###
# TODO rename from doc-nbconvert-all-to-pdfs to all, as required
###
# all:
doc-nbconvert-all-to-pdfs: doc-nbconvert-step00-utils-to-pdf \
	doc-nbconvert-step01-data-to-pdf \
	doc-nbconvert-step02_eda-to-pdf \
	doc-nbconvert-step03-features-to-pdf \
	doc-nbconvert-step04-modeling-to-pdf \
	doc-nbconvert-step05-main-to-pdf


############
# Appendix Aa. General E2E - Phony and Default Target
############

.PHONY: all env test

all: doc-nbconvert-all-to-pdfs
	@echo "Created end-to-end all pdf documents — All tasks complete!"

env: all-env-create-from-yml
	@echo "Created end-to-end environment — All tasks complete!"

test:
	@echo "TODO - Created end-to-end environment — All tasks complete!"


############
# Appendix Zz. Help
############

# TODO: Update!!!!!

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
