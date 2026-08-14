# Technical Interview Questions & Answers

This document contains 8 technical questions and detailed answers derived exclusively from the concepts and implementations present in this repository.

---

### Q1: How do Python lists differ from tuples regarding mutability, memory allocation, and performance?
**Answer:**
- **Mutability**: Lists are mutable sequences (elements can be modified via `list[0] = val`, appended via `.append()`, or removed via `.pop()`), whereas tuples are immutable once instantiated.
- **Memory Allocation**: Lists are over-allocated to achieve amortized $O(1)$ append operations, resulting in higher memory overhead. Tuples have a fixed size and are allocated with exact memory requirements in a single contiguous memory block.
- **Use Cases**: Use tuples for fixed data structures, write-protection, and as dictionary keys (since immutable types are hashable). Use lists when dynamic resizing or element alteration is required.

---

### Q2: What is the operational difference between `dict[key]` and `dict.get(key)` in Python?
**Answer:**
- Direct bracket access (`dict[key]`) searches for `key` and raises a `KeyError` if the key does not exist in the dictionary.
- The `.get(key, default=None)` method safely queries the dictionary. If `key` is present, it returns the value; if absent, it returns `None` (or the custom default provided) without raising an exception.
- As demonstrated in `py4.ipynb`, `dict.get("learning2")` returns `None`, allowing continuous script execution without unhandled exceptions.

---

### Q3: How does negative indexing and slicing work in Python strings?
**Answer:**
- Python supports negative indexing where `-1` represents the last element, `-2` the second to last, down to `-len(seq)`.
- In slicing syntax `sequence[start:stop:step]`, negative indices are evaluated as `len(sequence) + index`.
- In `py2.ipynb`, the slice `str1[-6:-1]` on `"kushagra"` (length 8) resolves indices from $8 - 6 = 2$ up to $8 - 1 = 7$ (exclusive), yielding the substring `"shagr"`.

---

### Q4: Explain the distinction between implicit type conversion and explicit type casting in Python.
**Answer:**
- **Implicit Type Conversion (Coercion)**: Python automatically promotes operands to a wider type to prevent data loss. For example, adding an `int` (e.g., `2`) and a `float` (e.g., `4.23`) automatically converts the integer to a float, returning `6.23` (`float`).
- **Explicit Type Casting**: Explicitly calling constructor functions like `int()`, `float()`, or `str()` to convert data across types. For example, `int("2")` or `float("4")`.

---

### Q5: What is the time and space complexity of the interval merging algorithm `solution(windows)` in `py3.ipynb`?
**Answer:**
- **Algorithm Mechanism**: The input list `windows` is sorted by start coordinate (`x[0]`). It then iterates through the sorted intervals once, comparing each interval's start time with the end time of the last merged interval (`merged[-1][1]`). If overlapping (`start <= merged[-1][1]`), it expands the boundary using `max(merged[-1][1], end)`; otherwise, it appends a new interval.
- **Time Complexity**: $O(N \log N)$ where $N$ is the number of intervals, dominated by the `windows.sort(key=lambda x: x[0])` step. The single merge pass takes linear $O(N)$ time.
- **Space Complexity**: $O(N)$ to store the resulting `merged` list of intervals.

---

### Q6: How does short-circuit evaluation function in Python's logical `and` / `or` operators?
**Answer:**
- Python evaluates logical expressions from left to right and stops evaluation as soon as the outcome is determined:
  - For `expr1 and expr2`: If `expr1` is falsy, Python returns `expr1` immediately without evaluating `expr2`.
  - For `expr1 or expr2`: If `expr1` is truthy, Python returns `expr1` immediately without evaluating `expr2`.
- As shown in `py1.ipynb`, boolean operators adhere to standard truth table definitions where `True and False` evaluates to `False`, and `True or False` evaluates to `True`.

---

### Q7: Compare the two-pointer approach vs. list copying for palindrome verification.
**Answer:**
- **Two-Pointer Approach (`l < r`)**: Compares symmetric elements from opposite ends moving inward (`arr[l] == arr[r]`). It terminates early on the first mismatch, running in $O(N)$ time and $O(1)$ auxiliary space.
- **Copy and Reverse Approach (`copy() + reverse()`)**: Creates a shallow copy of the list, reverses the copy in-place, and compares equality with the original. While still $O(N)$ time, it requires $O(N)$ additional memory for the duplicated list.

---

### Q8: How does Python's `if-elif-else` control ladder execute compared to multiple standalone `if` statements?
**Answer:**
- In an `if-elif-else` ladder, conditions are tested sequentially until the first truthy condition is encountered. Once that block executes, the remaining `elif` and `else` blocks are skipped entirely.
- With multiple consecutive `if` statements, every single conditional expression is evaluated independently regardless of preceding outcomes, potentially executing multiple blocks.
- In `py2.ipynb`, the student grade categorization utilizes `elif` to ensure that marks $\ge 90$ execute only Grade A and terminate the ladder.
