# Usage Guide

This repository contains a structured progression through Python fundamentals, core built-in data structures, and algorithmic problem solving.

## Repository Overview

- **`py1.ipynb`**: Primitive types (`int`, `float`, `str`, `bool`, `NoneType`), dynamic type casting, input handling, and arithmetic/logical operators.
- **`py2.ipynb`**: String slicing, string utility methods (`.capitalize()`, `.replace()`, `.find()`, `.count()`), and conditional branching logic (`if`, `elif`, `else`).
- **`py3.ipynb`**: Lists, tuples, mutability, palindrome checks, and interval merging algorithm (`solution`).
- **`py4.ipynb`**: Dictionaries, nested dictionary access, safe retrieval with `.get()`, and sets (uniqueness, union, intersection).
- **`py5.ipynb`**: While loops, for loops, sequence traversal, loop control statements (`break`, `continue`), and linear search.
- **`py6.ipynb`**: Functions, function definitions (`def`), parameters, arguments, and sum computation (`calSum`).

## Running the Notebooks

### 1. Interactive Execution
Open any notebook (`py1.ipynb` through `py6.ipynb`) using VS Code, JupyterLab, or Antigravity with a Python 3.8+ kernel.

### 2. Executing Interval Merging Algorithm
The interval merging function is located in `py3.ipynb`:

```python
def solution(windows):
    if not windows:
        return []

    windows.sort(key=lambda x: x[0])
    merged = [[windows[0][0], windows[0][1]]]

    for start, end in windows[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged
```

Example execution:
```python
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = solution(intervals)
print(result)
# Output: [[1, 6], [8, 10], [15, 18]]
```

## Running Automated Tests

Run the full pytest suite from the repository root:
```bash
pytest -v
```
