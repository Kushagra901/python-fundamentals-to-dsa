# Python Fundamentals to DSA

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Tests: pytest](https://img.shields.io/badge/Tests-pytest-green.svg)](https://docs.pytest.org/)

A comprehensive, structured collection of Python programming fundamentals, built-in data structures (strings, lists, tuples, dictionaries, sets), iteration controls, and modular functions across 6 curated modules.

---

## Table of Contents
- [Overview](#overview)
- [Module Breakdown & Topics](#module-breakdown--topics)
- [Public API Surface](#public-api-surface)
- [Installation & Setup](#installation--setup)
- [Running the Code](#running-the-code)
- [Running Tests](#running-tests)
- [Interview Reference](#interview-reference)
- [License](#license)

---

## Overview

This repository provides clear reference implementations covering essential Python concepts:
1. **Module 1 (`py1.ipynb`)**: Primitive types, type inspection (`type()`), explicit/implicit type conversion, and arithmetic/relational/logical operators.
2. **Module 2 (`py2.ipynb`)**: String indexing and slicing (including negative slices), string methods, and conditional branching (`if`/`elif`/`else`).
3. **Module 3 (`py3.ipynb`)**: Sequence manipulation (lists vs. tuples, mutability), palindrome detection, and interval merging algorithm (`solution`).
4. **Module 4 (`py4.ipynb`)**: Hash maps/dictionaries, nested mappings, safe retrieval with `.get()`, and sets (uniqueness, union, intersection).
5. **Module 5 (`py5.ipynb`)**: Loops and iteration (`while`, `for`, `range()`, `break`, `continue`, sequence traversal, linear search).
6. **Module 6 (`py6.ipynb`)**: Functions, parameter definitions, and argument handling (`def`, `calSum`).

---

## Module Breakdown & Topics

```text
.
├── py1.ipynb          # Python Basics, Dynamic Types, Operators, Input/Output
├── py2.ipynb          # String Slicing, String Methods, Conditional Logic
├── py3.ipynb          # Lists, Tuples, Palindromes, Interval Merging Algorithm
├── py4.ipynb          # Dictionaries, Nested Dictionaries, Sets & Set Operations
├── py5.ipynb          # While Loops, For Loops, Iteration Control, Linear Search
├── py6.ipynb          # Functions, Parameters, Arguments, calSum Implementation
├── docs/
│   └── usage.md       # Detailed usage guide and execution flow
├── tests/
│   ├── test_notebooks.py # Structural and JSON validity tests
│   └── test_solution.py  # Unit tests for interval merging algorithm
├── INTERVIEW.md       # 13 curated technical interview Q&As
├── pyproject.toml     # Packaging metadata and tool configurations
├── requirements.txt   # Runtime & test dependencies
└── LICENSE            # MIT License
```

---

## Public API Surface

| Component | Location | Description |
| :--- | :--- | :--- |
| `solution(windows: list[list[int]]) -> list[list[int]]` | `py3.ipynb` | Merges overlapping interval windows after sorting by start coordinate in $O(N \log N)$ time. |
| `calSum(a: int | float, b: int | float) -> None` | `py6.ipynb` | Computes and prints the sum of two parameters $a$ and $b$. |
| **String Utilities** | `py2.ipynb` | Methods: `.endswith()`, `.capitalize()`, `.replace()`, `.find()`, `.count()`. |
| **Dictionary Utilities** | `py4.ipynb` | Methods: `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`. |
| **Set Utilities** | `py4.ipynb` | Methods: `.add()`, `.remove()`, `.clear()`, `.pop()`, `.union()`, `.intersection()`. |
| **Iteration Utilities** | `py5.ipynb` | Flow control: `while`, `for`, `range()`, `break`, `continue`, `while-else`. |

---

## Installation & Setup

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Kushagra901/python-fundamentals-to-dsa.git
cd python-fundamentals-to-dsa
python -m venv .venv

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# On Linux / macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Running the Code

### Jupyter Notebooks
Launch JupyterLab or VS Code to run interactive notebook cells:
```bash
jupyter lab
```

---

## Running Tests

Run the automated test suite with `pytest`:

```bash
pytest -v
```

---

## Interview Reference

See [INTERVIEW.md](INTERVIEW.md) for 13 in-depth technical interview questions covering topics from this repository (mutability, slicing internals, dictionary hashing, set deduplication, loop control flow, short-circuit evaluation, functions, interval merging complexity).

---

## License

This project is licensed under the [MIT License](LICENSE).

