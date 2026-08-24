# Technical Interview Questions & Answers

This document contains 18 technical questions and detailed answers derived exclusively from the concepts and implementations present in this repository.

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

---

### Q9: How do Python sets guarantee uniqueness and how does their membership lookup compare to lists?
**Answer:**
- **Hash Table Implementation**: Sets are implemented as hash tables containing only keys (no values).
- **Lookup Complexity**: Checking element existence (`x in my_set`) operates in amortized **$O(1)$ time** because Python computes `hash(x)` and directly accesses the corresponding hash bucket.
- **Comparison to Lists**: In contrast, list membership lookup (`x in my_list`) performs a sequential linear scan running in **$O(N)$ time**.

---

### Q10: Why does `{9, 9.0}` evaluate to `{9}` in Python sets, and how can they be stored distinctly?
**Answer:**
- In Python, integer `9` and float `9.0` evaluate to equal values (`9 == 9.0`) and have identical hash codes (`hash(9) == hash(9.0) == 9`).
- When a set processes `9.0` after inserting `9`, it detects a hash collision and an equality match, causing Python to treat `9.0` as duplicate and ignore it.
- **Workarounds**: To preserve both values distinctly, use string casting `{9, "9.0"}` or typed tuple identifiers `{("int", 9), ("float", 9.0)}`.

---

### Q11: What is the fundamental difference between `while` and `for` loops, and how does the `else` clause operate?
**Answer:**
- **Condition vs Sequence**: A `while` loop is condition-controlled (repeats until its condition is `False`), making it ideal when the iteration count is undetermined. A `for` loop is iterator-controlled (traverses sequences/ranges of known bounds).
- **Loop `else` Clause**: The `else` clause attached to a `while` or `for` loop executes only when the loop completes all iterations naturally without encountering a `break` statement.

---

### Q12: How do `break`, `continue`, and `pass` differ in Python loop control flow?
**Answer:**
- `break`: Immediately terminates loop execution and jumps to the first statement following the loop.
- `continue`: Skips the remainder of the current iteration and jumps directly to the loop condition evaluation / next item.
- `pass`: A null operation used as a syntactical placeholder where a statement is required but no action is to be performed.

---

### Q13: What is the semantic difference between parameters and arguments in Python functions?
**Answer:**
- **Parameters**: The variable identifiers defined in a function signature (e.g. `a` and `b` in `def cal_sum(a, b):`). They serve as placeholders that receive values.
- **Arguments**: The actual concrete values, literals, or expressions passed to the function upon invocation (e.g. `1` and `2` in `cal_sum(1, 2)`).
- Functions provide modularity and reusability by allowing the same logic block to execute against different input arguments.

---

### Q14: How does Python evaluate default parameter values, and why are mutable default arguments problematic?
**Answer:**
- Default parameters provide fallback values if arguments are omitted upon invocation (e.g. `def converter(usd_val, rate=83):`).
- Non-default parameters must always appear before default parameters; otherwise, Python raises a `SyntaxError`.
- Default parameter values are evaluated **once when the function definition is executed**, not each time the function is called.
- If a mutable object (like a `list` or `dict`) is used as a default parameter (`def append_item(x, lst=[]):`), that single list instance is shared across all function invocations, creating unintended side effects. The idiomatic pattern is using `lst=None` and initializing inside the function (`if lst is None: lst = []`).

---

### Q15: How does recursion utilize the call stack, and what causes a `RecursionError`?
**Answer:**
- Each recursive call creates a new **stack frame** containing the function's local variables, parameters, and return address on the process call stack.
- A **base case** is strictly required to halt further recursive invocations and begin unwinding the stack.
- Without a valid base case, calls accumulate until reaching Python's recursion limit (accessible via `sys.getrecursionlimit()`, default 1000), raising `RecursionError: maximum recursion depth exceeded`.
- **Complexity**: In recursive factorial `fact(n)`, $N$ nested stack frames consume $O(N)$ auxiliary stack space.

---

### Q16: Why is the `with` statement (context manager) preferred for File I/O over manual `open()` and `close()`?
**Answer:**
- The `with` statement utilizes Python's context management protocol (`__enter__` and `__exit__`).
- It guarantees deterministic resource cleanup: the file descriptor is flushed and closed immediately when the code exits the `with` block, even if an exception is thrown or an early `return`/`break` occurs.
- Manual `f.close()` risks remaining unexecuted if an exception occurs prior to reaching the `close()` call, leading to memory leaks and locked file handles.

---

### Q17: Compare file access modes `'r+'`, `'w+'`, and `'a+'` in Python.
**Answer:**
| Mode | Purpose | File Pointer Start Position | Truncates Existing Content? |
| :--- | :--- | :--- | :--- |
| `'r+'` | Read + Write | Beginning (byte 0) | **No** (overwrites byte-by-byte from pointer) |
| `'w+'` | Write + Read | Beginning (byte 0) | **Yes** (truncates file to 0 bytes on open) |
| `'a+'` | Append + Read | End of file | **No** (all writes append to end) |

- In `'r+'`, attempting to open a non-existent file raises `FileNotFoundError`, whereas `'w+'` and `'a+'` create a new file if it does not exist.

---

### Q18: What is the most memory-efficient technique to process large (multi-GB) text files in Python?
**Answer:**
- Avoid `f.read()` and `f.readlines()`, which load the entire file into RAM simultaneously, resulting in $O(\\text{file\\_size})$ memory overhead.
- Instead, iterate directly over the file object (`with open("huge.txt", "r") as f: for line in f:`).
- Python's file iterator streams data line-by-line using an internal buffer generator, consuming only $O(\\text{max\\_line\\_length})$ memory regardless of how large the file is.


