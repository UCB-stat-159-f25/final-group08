#!/usr/bin/env python3

# imports
from __future__ import annotations

import src.step00_utils as step00_utils
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# filepaths
DIR_DATA = step00_utils.DIR_DATA

# RAW_DATA_PATH = DIR_DATA / "00_raw" / "spotify_churn_dataset.csv"
# PROCESSED_DATA_DIR = DIR_DATA / "01_processed"
# VECTORIZED_DATA_DIR = DIR_DATA / "02_vectorized"

RAW_DATA_PATH = step00_utils.DIR_DATA_00_RAW / step00_utils.FILE_SPOTIFY_CHURN_DATASET_CSV
PROCESSED_DATA_DIR = step00_utils.DIR_DATA_01_PROCESSED
VECTORIZED_DATA_DIR = step00_utils.DIR_DATA_02_VECTORIZED

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
VECTORIZED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# features
NUMERIC_FEATURES = [
    "age",
    "listening_time",
    "songs_played_per_day",
    "skip_rate",
    "ads_listened_per_week",
    # new features (derived from EDA)
    "ads_per_song",
    "avg_song_length", 
]

CATEGORICAL_FEATURES = [
    "gender",
    "country",
    "subscription_type",
    "device_type",
]

BINARY_FEATURES = [
    "offline_listening",
]

TARGET_COL = "is_churned"
ID_COL = "user_id"

# feature engineering
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform light feature cleaning and create interaction features.
    """
    df = df.copy()

    # type enforcement
    df[BINARY_FEATURES] = df[BINARY_FEATURES].astype(int)
    df[TARGET_COL] = df[TARGET_COL].astype(int)

    # new features
    # +1 to denominators to avoid division by zero errors.
    # ratio: how much ad spam are they tolerating per song?
    # ratio: are they listening to full songs or skipping fast?
    est_songs_per_week = (df["songs_played_per_day"] * 7) + 1
    df["ads_per_song"] = df["ads_listened_per_week"] / est_songs_per_week
    df["avg_song_length"] = df["listening_time"] / (df["songs_played_per_day"] + 1)

    return df


# X/y split function
def make_X_y(df: pd.DataFrame):
    y = df[TARGET_COL]
    X = df.drop(columns=[TARGET_COL, ID_COL])
    return X, y


# preprocessor
def build_preprocessor() -> ColumnTransformer:
    numeric_transformer = StandardScaler()

    categorical_transformer = OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, NUMERIC_FEATURES),
            ("cat", categorical_transformer, CATEGORICAL_FEATURES),
            ("bin", "passthrough", BINARY_FEATURES),
        ]
    )

    return preprocessor