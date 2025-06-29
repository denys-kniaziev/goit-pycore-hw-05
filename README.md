# Woolf University. Python Programing Course. Homework – Functional Programming and Python Built-ins

## Overview

This assignment covers:

1. A closure-based caching Fibonacci function.
2. A number-extraction generator and sum function.
3. A log-file analysis script with filtering and summaries.
4. Extending a CLI assistant with error-handling decorators.

---

## Task 1: Caching Fibonacci

**Objective:** Implement an efficient Fibonacci calculator using closures and caching.

**Requirements:**

* `caching_fibonacci() -> Callable[[int], int]` returns `fibonacci(n)`.
* Inner `fibonacci(n: int) -> int`:

  * Returns 0 if `n <= 0`, 1 if `n == 1`.
  * Uses a `cache: dict[int, int]` to store computed values.
  * On cache miss, computes `fibonacci(n-1) + fibonacci(n-2)`, stores, and returns.

**Evaluation:**

* Correct Fibonacci values.
* Recursive caching avoids redundant calls.
* Clean, documented code.

**Example:**

```python
fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610
```

---

## Task 2: Generator and Summation of Numbers in Text

**Objective:** Extract real numbers from text and sum them.

**Requirements:**

1. `generator_numbers(text: str) -> Generator[float, None, None]`:

   * Yields all real numbers found, using regex `r"\b\d+\.\d+\b"`.
2. `sum_profit(text: str, func: Callable) -> float`:

   * Uses `generator_numbers` to compute total.

**Evaluation:**

* Correct extraction and summation.
* Proper generator usage.
* PEP8-compliant, commented code.

**Example:**

```python
text = "Parts: 1000.01 base, + 27.45 bonus, + 324.00 extra."
print(sum_profit(text, generator_numbers))  # 1351.46
```

---

## Task 3: Log File Analyzer

**Objective:** CLI script to analyze log files, count levels, and filter entries.

**Requirements:**

* Accepts `logfile_path` and optional `level` from `sys.argv`.
* Functions:

  1. `parse_log_line(line: str) -> dict` ({date, time, level, message}).
  2. `load_logs(path: str) -> list[dict]`.
  3. `filter_logs_by_level(logs: list, level: str) -> list[dict]`.
  4. `count_logs_by_level(logs: list) -> dict[str, int]`.
  5. `display_log_counts(counts: dict) -> None`.
* Include a functional element: lambda, list comprehension or `filter`.
* Handle file-not-found errors gracefully.

**Evaluation:**

* Accurate parsing and counts.
* Functional programming usage.
* Robust error handling.
* Modular code structure.

**Example CLI Usage:**

```bash
python main.py /path/to/log.log error
```

Output:

```
Level   | Count
--------|------
INFO    | 4
DEBUG   | 3
ERROR   | 2
WARNING | 1

Details for ERROR:
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

---

## Task 4: Enhanced CLI Assistant with Decorators

**Objective:** Extend the previous assistant bot by adding input-error handling via a decorator.

**Requirements:**

* Implement `@input_error` decorator:

  * Catches `KeyError`, `ValueError`, `IndexError` in handlers.
  * Returns friendly messages (e.g., "No such contact.").
* Decorate all command handler functions (`add_contact`, `change_contact`, etc.).
* The bot’s REPL must continue running after errors.

**Evaluation:**

* Correct decorator behavior.
* Handlers remain concise; I/O in `main()` only.
* Bot resilience to invalid inputs.

**Decorator Example:**

```python
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact."
        except ValueError:
            return "Please provide name and phone."
        except IndexError:
            return "Insufficient arguments."
    return wrapper
```

Apply to:

```python
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
```

---
