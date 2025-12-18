#!/usr/bin/env python3

###
# Imports
###
import pytest

from pathlib import Path
from src.step00_utils import get_project_root, is_csv_file

###
# ...
###

def test_get_project_root_returns_path(tmp_path):
    root = get_project_root(tmp_path)

    assert isinstance(root, Path)
    assert root == tmp_path.resolve()

def test_is_csv_file():
    assert is_csv_file("data.csv") is True
    assert is_csv_file("data.txt") is False
