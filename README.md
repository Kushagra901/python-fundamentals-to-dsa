# Python Fundamentals to DSA

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Tests: pytest](https://img.shields.io/badge/Tests-pytest-green.svg)](https://docs.pytest.org/)

A comprehensive, structured collection of Python programming fundamentals, built-in data structures (strings, lists, tuples, dictionaries, sets), iteration controls, modular functions & recursion, File I/O, and Object-Oriented Programming (OOP) across 9 curated modules.

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
6. **Module 6 (`py6.ipynb`)**: Functions, parameter definitions, argument handling, default arguments, and recursion (`cal_sum`, `cal_fact`, `converter`, `sum_natural`, `fact`).
7. **Module 7 (`py7.ipynb`)**: File Input/Output (I/O) modes (`'r'`, `'w'`, `'a'`, `'r+'`, `'w+'`), context managers (`with`), file manipulation (`os.remove()`), word search, and text stream parsing.
8. **Module 8 (`py8.ipynb`)**: Object-Oriented Programming (OOP) fundamentals: classes, objects, `__init__` constructor, `self` parameter, class vs. instance attributes, methods, static methods (`@staticmethod`), and abstraction.
9. **Module 9 (`py9.ipynb`)**: Advanced Object-Oriented Programming: `del` keyword, public vs. private attributes & methods (name mangling), and inheritance patterns (single, multi-level, multiple) with MRO.

---

## Module Breakdown & Topics

```text
.
├── py1.ipynb          # Python Basics, Dynamic Types, Operators, Input/Output
├── py2.ipynb          # String Slicing, String Methods, Conditional Logic
├── py3.ipynb          # Lists, Tuples, Palindromes, Interval Merging Algorithm
├── py4.ipynb          # Dictionaries, Nested Dictionaries, Sets & Set Operations
├── py5.ipynb          # While Loops, For Loops, Iteration Control, Linear Search
├── py6.ipynb          # Functions, Parameters, Arguments, Recursion Fundamentals
├── py7.ipynb          # File I/O, Reading/Writing, Context Managers, OS Operations
├── py8.ipynb          # OOP Fundamentals, Classes, Objects, Constructors, Methods, Abstraction
├── py9.ipynb          # Advanced OOP, del Keyword, Name Mangling, Inheritance (Single, Multi, Multiple)
├── practice.txt       # Sample file dataset for file parsing exercises
├── docs/
│   └── usage.md       # Detailed usage guide and execution flow
├── tests/
│   ├── test_notebooks.py # Structural and JSON validity tests
│   └── test_solution.py  # Unit tests for interval merging algorithm
├── INTERVIEW.md       # 24 curated technical interview Q&As
├── pyproject.toml     # Packaging metadata and tool configurations
├── requirements.txt   # Runtime & test dependencies
└── LICENSE            # MIT License
```

---

## Public API Surface

| Component | Location | Description |
| :--- | :--- | :--- |
| `solution(windows: list[list[int]]) -> list[list[int]]` | `py3.ipynb` | Merges overlapping interval windows after sorting by start coordinate in $O(N \log N)$ time. |
| `cal_sum(a, b)` / `avg_sum(a, b, c)` | `py6.ipynb` | Computes sum and average with clean parameter passing and return handling. |
| `cal_fact(n)` / `fact(n)` | `py6.ipynb` | Computes factorial using iterative loop and recursive call stack. |
| `sum_natural(n)` | `py6.ipynb` | Computes sum of first $n$ natural numbers recursively with base case $n=0$. |
| `check_for_word(word, filename)` | `py7.ipynb` | Searches for keyword existence in disk files using safe context managers. |
| `check_for_line(word, filename)` | `py7.ipynb` | Streams file lines sequentially to locate 1-indexed occurrence of a target word. |
| **String Utilities** | `py2.ipynb` | Methods: `.endswith()`, `.capitalize()`, `.replace()`, `.find()`, `.count()`. |
| **Dictionary Utilities** | `py4.ipynb` | Methods: `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`. |
| **Set Utilities** | `py4.ipynb` | Methods: `.add()`, `.remove()`, `.clear()`, `.pop()`, `.union()`, `.intersection()`. |
| **Iteration Utilities** | `py5.ipynb` | Flow control: `while`, `for`, `range()`, `break`, `continue`, `while-else`. |
| **File I/O Utilities** | `py7.ipynb` | Modes (`'r'`, `'w'`, `'a'`, `'r+'`, `'w+'`), `read()`, `readline()`, `with`, `os.remove()`. |

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

See [INTERVIEW.md](INTERVIEW.md) for 18 in-depth technical interview questions covering topics from this repository (mutability, slicing internals, dictionary hashing, set deduplication, loop control flow, recursion call stack, context managers, file modes `'r+'` vs `'w+'`, memory streaming).

---

## License

This project is licensed under the [MIT License](LICENSE).
