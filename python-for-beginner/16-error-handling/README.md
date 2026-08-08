# 16 — Error Handling (try / except)

## Concept

You've seen plenty of errors already — `ValueError`, `TypeError`,
`IndexError`, `KeyError`. By default, an error (Python calls these
**exceptions**) stops your program immediately and prints a **traceback**
(the red-looking error report showing where things went wrong). Often
that's exactly what you want during development — a loud, obvious
failure. But a finished program usually needs to handle *expected*
failure cases gracefully instead of crashing — a user typing letters
where you expected a number, a file that doesn't exist, and so on.

### `try` / `except`

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("That's not a valid number.")
    age = 0
```

Python runs the `try` block. If a `ValueError` happens anywhere inside
it, execution jumps straight to the matching `except` block instead of
crashing the program, and continues normally after it.

### Catching specific exceptions

Name the exact exception type you expect, so you don't accidentally hide
unrelated bugs:

```python
try:
    result = 10 / user_input
except ZeroDivisionError:
    print("Can't divide by zero.")
except ValueError:
    print("Not a valid number.")
```

Multiple `except` blocks let you handle different failure types
differently. Python checks them top to bottom and runs the first
matching one.

### Catching "anything" — use sparingly

```python
try:
    risky_operation()
except Exception as e:
    print(f"Something went wrong: {e}")
```

`except Exception:` catches nearly any error. It's tempting to reach for
this everywhere, but it also silently swallows bugs you didn't anticipate
(a typo causing a `NameError`, for instance) — prefer naming the specific
exception(s) you actually expect, and only fall back to broad `Exception`
catching at a genuine "don't crash the whole program" boundary, like the
top-level loop of a CLI app (which is exactly where you'll use it in this
course's capstone projects).

`as e` binds the exception object to a name so you can inspect it —
`str(e)` gives you its message.

### `else` and `finally`

```python
try:
    value = int(text)
except ValueError:
    print("invalid")
else:
    print("conversion succeeded:", value)   # runs only if NO exception happened
finally:
    print("done trying")                     # ALWAYS runs, error or not
```

`else` is for code that should only run when the `try` block succeeded
cleanly; `finally` is for cleanup that must happen either way (closing a
file, releasing a resource — you'll see this again with context managers
in the advanced modules). Both are optional and used far less often than
plain `try`/`except`.

### Raising your own errors with `raise`

Sometimes *your* code should be the one to signal "this input is
invalid," rather than waiting for Python to fail on its own:

```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

Calling `set_age(-5)` now raises `ValueError: age cannot be negative`
immediately — the caller can catch it with `try`/`except ValueError`
just like a built-in error. Raising an existing, sensible built-in
exception type (`ValueError`, `TypeError`, etc.) with a clear message is
usually enough; writing your own custom exception classes is a small
extra step you'll see if you continue past this course.

### Common built-in exceptions, at a glance

| Exception | Typical cause |
|---|---|
| `ValueError` | Right type, wrong value — `int("abc")` |
| `TypeError` | Wrong type entirely — `"5" + 5` |
| `IndexError` | List/tuple index out of range |
| `KeyError` | Dict key doesn't exist |
| `ZeroDivisionError` | Dividing by zero |
| `FileNotFoundError` | Opening a file that doesn't exist (module 18) |
| `AttributeError` | Calling a method/attribute that doesn't exist on a value |

## Common beginner mistakes

- **Catching too broadly, too early.** `except:` (with no type at all,
  not even `Exception`) catches *everything*, including things like
  Ctrl+C — almost never what you want. Always name a type.
- **Swallowing errors silently.** `except Exception: pass` hides bugs
  instead of fixing them — at minimum, print or log what happened.
- **Using `try`/`except` for normal control flow** where a simple `if`
  would do — e.g. checking a dict key with `try: d[key] / except
  KeyError` when `d.get(key)` (module 11) is clearer for that specific
  case. `try`/`except` shines for things you *can't* easily check in
  advance (like "will this string parse as a number").

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `safe_int(text)` — try to convert `text` to `int`; return the number
   on success, or `None` if it raises `ValueError`.
2. `safe_divide(a, b)` — return `a / b`, or `None` if it raises
   `ZeroDivisionError`.
3. `safe_get_item(items, index)` — return `items[index]`, or `None` if it
   raises `IndexError`.
4. `safe_get_value(d, key)` — return `d[key]`, or `"not found"` if it
   raises `KeyError`.
5. `validate_age(age)` — return `age` if `age >= 0`; otherwise `raise
   ValueError("age cannot be negative")`.

Run it to check yourself:

```bash
python3 python-for-beginner/16-error-handling/exercise.py
```
