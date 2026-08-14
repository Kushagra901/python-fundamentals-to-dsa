# Python Fundamentals to DSA

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Tests: pytest](https://img.shields.io/badge/Tests-pytest-green.svg)](https://docs.pytest.org/)

A comprehensive, structured collection of Python programming fundamentals, built-in data structures (strings, lists, tuples, dictionaries), and algorithmic problem-solving implementations across 4 curated modules.

---

## Table of Contents
- [Overview](#overview)
- [Module Breakdown & Topics](#module-breakdown--topics)
- [Code Examples by Topic](#code-examples-by-topic)
  - [1. Basics, Types & Operators (`py1.ipynb`)](#1-basics-types--operators-py1ipynb)
  - [2. String Mechanics & Control Flow (`py2.ipynb`)](#2-string-mechanics--control-flow-py2ipynb)
  - [3. Sequence Types & Interval Merging (`py3.ipynb`)](#3-sequence-types--interval-merging-py3ipynb)
  - [4. Dictionaries & Key-Value Lookups (`py4.ipynb`)](#4-dictionaries--key-value-lookups-py4ipynb)
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
4. **Module 4 (`py4.ipynb`)**: Hash maps/dictionaries, nested mappings, and safe retrieval with `.get()`.

---

## Module Breakdown & Topics

```text
.
├── py1.ipynb          # Python Basics, Dynamic Types, Operators, Input/Output
├── py2.ipynb          # String Slicing, String Methods, Conditional Logic
├── py3.ipynb          # Lists, Tuples, Palindromes, Interval Merging Algorithm
├── py4.ipynb          # Dictionaries, Nested Dictionaries, Safe Key Queries
├── docs/
│   └── usage.md       # Detailed usage guide and execution flow
├── tests/
│   ├── test_notebooks.py # Structural and JSON validity tests
│   └── test_solution.py  # Unit tests for interval merging algorithm
├── INTERVIEW.md       # 8 curated technical interview Q&As
├── pyproject.toml     # Packaging metadata and tool configurations
├── requirements.txt   # Runtime & test dependencies
└── LICENSE            # MIT License
```

---

## Code Examples by Topic

### 1. Basics, Types & Operators (`py1.ipynb`)

```python
# Variables and Type Inspection
name = "kush"
age = 23
price = 25.99
is_active = True
empty_val = None

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(price))      # <class 'float'>
print(type(is_active))  # <class 'bool'>
print(type(empty_val))  # <class 'NoneType'>

# Explicit Type Casting & Arithmetic
a = float("4")
b = 4.25
print(a + b)            # Output: 8.25

# Practical Calculations: Area & Average
side = 6.7
area = side * side
print(f"Area of square: {area}")

num1 = 2.0
num2 = 4.0
avg = (num1 + num2) / 2
print(f"Average: {avg}") # Output: 3.0
```

---

### 2. String Mechanics & Control Flow (`py2.ipynb`)

```python
# String Methods & Slicing
text = "i am studying python"

print(text.endswith("on"))             # True
print(text.capitalize())               # "I am studying python"
print(text.replace("python", "java"))  # "i am studying java"
print(text.find("o"))                  # Returns first index of 'o'
print(text.count("am"))                # Counts occurrences of substring

# Slicing Examples
word = "kushagra"
print(word[1:6])                       # 'ushag'
print(word[-6:-1])                     # 'shagr' (negative slicing)

# Conditional Grading Ladder
marks = 85
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"
print(f"Assigned Grade: {grade}")      # Output: B

# Parity Check
num = 49
if num % 7 == 0:
    print(f"{num} is a multiple of 7")
```

---

### 3. Sequence Types & Interval Merging (`py3.ipynb`)

```python
# List Mutation
numbers = [4, 2, 8, 5, 1]
numbers.append(9)                      # [4, 2, 8, 5, 1, 9]
numbers.sort()                         # [1, 2, 4, 5, 8, 9]
numbers.pop(2)                         # Removes element at index 2

# Palindrome Checker (Two-Pointer Inward Scan)
def is_palindrome(seq):
    l, r = 0, len(seq) - 1
    while l < r:
        if seq[l] != seq[r]:
            return False
        l += 1
        r -= 1
    return True

print(is_palindrome([1, 2, 3, 2, 1]))  # True

# Interval Merging Algorithm
def solution(windows):
    """
    Merges overlapping interval pairs.
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
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

# Example:
windows = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solution(windows))  # Output: [[1, 6], [8, 10], [15, 18]]
```

---

### 4. Dictionaries & Key-Value Lookups (`py4.ipynb`)

```python
# Dictionary Creation & Query Methods
info = {
    "key": "value",
    "name": "apnacollege",
    "learning": "python",
    "age": 35,
    "is_adult": True,
    "subject": ["python", "c++"]
}

print(list(info.keys()))     # ['key', 'name', 'learning', 'age', 'is_adult', 'subject']
print(list(info.values()))   # ['value', 'apnacollege', 'python', 35, True, ['python', 'c++']]
print(list(info.items()))    # [('key', 'value'), ...]

# Safe Access: .get() vs Bracket Notation
print(info["learning"])      # Output: 'python'
print(info.get("city"))      # Output: None (safe, avoids KeyError)

# Dictionary Update
info.update({"city": "varanasi"})
print(info["city"])          # Output: 'varanasi'
```

---

## Public API Surface

| Component | Location | Description |
| :--- | :--- | :--- |
| `solution(windows: list[list[int]]) -> list[list[int]]` | `py3.ipynb` | Merges overlapping interval windows after sorting by start coordinate in $O(N \log N)$ time. |
| **String Utilities** | `py2.ipynb` | Methods: `.endswith()`, `.capitalize()`, `.replace()`, `.find()`, `.count()`. |
| **Dictionary Utilities** | `py4.ipynb` | Methods: `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`. |

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

See [INTERVIEW.md](INTERVIEW.md) for 8 in-depth technical interview questions covering topics from this repository (mutability, slicing internals, dictionary hashing, short-circuit evaluation, interval merging complexity).

---

## License

This project is licensed under the [MIT License](LICENSE).
