"""Smoke and structure validation tests for repository notebooks."""
import json
import os
import pytest

NOTEBOOK_FILES = ["py1.ipynb", "py2.ipynb", "py3.ipynb", "py4.ipynb", "py5.ipynb"]


@pytest.mark.parametrize("nb_file", NOTEBOOK_FILES)
def test_notebook_json_validity(nb_file):
    root_dir = os.path.join(os.path.dirname(__file__), "..")
    path = os.path.join(root_dir, nb_file)
    assert os.path.exists(path), f"Missing notebook: {nb_file}"

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert "cells" in data, f"Notebook {nb_file} missing 'cells'"
    assert "metadata" in data, f"Notebook {nb_file} missing 'metadata'"
    assert isinstance(data["cells"], list)
    assert len(data["cells"]) > 0, f"Notebook {nb_file} has no cells"


def test_notebook_topics_present():
    root_dir = os.path.join(os.path.dirname(__file__), "..")

    # py1: check for operator and type topics
    with open(os.path.join(root_dir, "py1.ipynb"), "r", encoding="utf-8") as f:
        py1_text = f.read()
        assert "type(" in py1_text
        assert "print(" in py1_text

    # py2: check for string and conditional topics
    with open(os.path.join(root_dir, "py2.ipynb"), "r", encoding="utf-8") as f:
        py2_text = f.read()
        assert "elif" in py2_text or "if(" in py2_text or "if " in py2_text

    # py3: check for list and tuple topics
    with open(os.path.join(root_dir, "py3.ipynb"), "r", encoding="utf-8") as f:
        py3_text = f.read()
        assert "solution" in py3_text
        assert "append" in py3_text

    # py4: check for dictionary and set topics
    with open(os.path.join(root_dir, "py4.ipynb"), "r", encoding="utf-8") as f:
        py4_text = f.read()
        assert "keys()" in py4_text
        assert "values()" in py4_text
        assert "set(" in py4_text or "union(" in py4_text

    # py5: check for loop topics
    with open(os.path.join(root_dir, "py5.ipynb"), "r", encoding="utf-8") as f:
        py5_text = f.read()
        assert "while" in py5_text
        assert "break" in py5_text or "range(" in py5_text
