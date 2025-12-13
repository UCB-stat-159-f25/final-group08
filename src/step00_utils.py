#!/usr/bin/env python3

###
# Imports
###
import pathlib as pl


###
# Filepaths
###
# DIR_PROJECT_HOME                   = pl.Path("..")
DIR_PROJECT_HOME                   = pl.Path(".").resolve().parent
DIR_PROJECT_CURRENT                = pl.Path(".").resolve()

DIR_DATA                           = DIR_PROJECT_HOME / "data"
DIR_DATA_00_RAW                    = DIR_DATA / "00_raw" 
DIR_DATA_01_PROCESSED              = DIR_DATA / "01_processed"
DIR_DATA_02_VECTORIZED             = DIR_DATA / "02_vectorized"

DIR_NOTEBOOKS                      = DIR_PROJECT_HOME / "notebooks"

DIR_OUTPUTS_FIG_BUILDS             = DIR_PROJECT_HOME / "fig_builds"
DIR_OUTPUTS_FIG_BUILDS_00_UTILS    = DIR_OUTPUTS_FIG_BUILDS / "step00_utils"
DIR_OUTPUTS_FIG_BUILDS_01_DATA     = DIR_OUTPUTS_FIG_BUILDS / "step01_data"
DIR_OUTPUTS_FIG_BUILDS_02_EDA      = DIR_OUTPUTS_FIG_BUILDS / "step02_eda"
DIR_OUTPUTS_FIG_BUILDS_03_FEATURES = DIR_OUTPUTS_FIG_BUILDS / "step03_features"
DIR_OUTPUTS_FIG_BUILDS_04_MODELING = DIR_OUTPUTS_FIG_BUILDS / "step04_modeling"
DIR_OUTPUTS_FIG_BUILDS_05_MAIN     = DIR_OUTPUTS_FIG_BUILDS / "step05_main"

DIR_OUTPUTS_PDF_BUILDS             = DIR_PROJECT_HOME / "pdf_builds"
DIR_OUTPUTS_PDF_BUILDS_00_UTILS    = DIR_OUTPUTS_PDF_BUILDS / "step00_utils"
DIR_OUTPUTS_PDF_BUILDS_01_DATA     = DIR_OUTPUTS_PDF_BUILDS / "step01_data"
DIR_OUTPUTS_PDF_BUILDS_02_EDA      = DIR_OUTPUTS_PDF_BUILDS / "step02_eda"
DIR_OUTPUTS_PDF_BUILDS_03_FEATURES = DIR_OUTPUTS_PDF_BUILDS / "step03_features"
DIR_OUTPUTS_PDF_BUILDS_04_MODELING = DIR_OUTPUTS_PDF_BUILDS / "step04_modeling"
DIR_OUTPUTS_PDF_BUILDS_05_MAIN     = DIR_OUTPUTS_PDF_BUILDS / "step05_main"


##########
# TBDs
##########



###
# Random Seeds
###


###
# Figures, Plots, and Visualizations
###


###
# ...
###