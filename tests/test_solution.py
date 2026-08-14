"""Unit tests for the interval merging solution in py3.ipynb."""
import json
import os
import pytest


def load_solution_from_notebook():
    """Extracts and executes the solution function definition from py3.ipynb."""
    notebook_path = os.path.join(os.path.dirname(__file__), "..", "py3.ipynb")
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    solution_code = None
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            source = "".join(cell.get("source", []))
            if "def solution(" in source:
                solution_code = source
                break

    if not solution_code:
        raise RuntimeError("Could not find 'solution' function in py3.ipynb")

    namespace = {}
    exec(solution_code, namespace)
    return namespace["solution"]


@pytest.fixture(scope="module")
def solution():
    return load_solution_from_notebook()


def test_empty_windows(solution):
    assert solution([]) == []


def test_single_window(solution):
    assert solution([[1, 5]]) == [[1, 5]]


def test_overlapping_windows(solution):
    windows = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]
    assert solution(windows) == expected


def test_nested_windows(solution):
    windows = [[1, 10], [2, 5], [3, 7]]
    expected = [[1, 10]]
    assert solution(windows) == expected


def test_non_overlapping_windows(solution):
    windows = [[1, 2], [3, 4], [5, 6]]
    expected = [[1, 2], [3, 4], [5, 6]]
    assert solution(windows) == expected


def test_unsorted_windows(solution):
    windows = [[8, 10], [1, 3], [2, 6], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]
    assert solution(windows) == expected


def test_touching_boundaries(solution):
    windows = [[1, 4], [4, 8]]
    expected = [[1, 8]]
    assert solution(windows) == expected
