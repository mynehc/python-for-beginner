# 05 — Input, Output & Type Conversion

## Concept

### Getting input from the user

`input()` pauses your program, waits for the person running it to type
something and press Enter, then returns what they typed:

```python
name = input("What's your name? ")
print("Hello, " + name)
```

Running this shows the prompt `What's your name? `, waits for you to type
`Ava` and press Enter, then prints `Hello, Ava`.

**Critical fact: `input()` always returns a `str`, no matter what the
user typed.** If you ask for their age and they type `25`, you get back
the *string* `"25"`, not the number `25`. This catches every beginner at
least once:

```python
age = input("Age? ")     # user types 25
age + 1                  # TypeError! age is "25" (a string), not 25 (an int)
```

### Converting types

To fix that, convert the string to a number using `int()` or `float()`:

```python
age = input("Age? ")        # "25" (str)
age = int(age)               # 25   (int)
age + 1                      # 26 — works now
```

The conversion functions you'll use constantly:

```python
int("25")      # 25      — str to int
int("25.9")    # ValueError! int() can't parse a decimal point directly
float("25.9")  # 25.9    — str to float
float("25")    # 25.0    — works, ints-as-strings parse fine as float too
str(25)        # "25"    — number to str (needed to concatenate with +)
str(25.9)      # "25.9"
bool(1)        # True    — see module 06 for the full falsy/truthy rules
```

`int()` and `float()` raise a `ValueError` if the string isn't actually a
valid number (e.g. `int("abc")`). Handling that gracefully instead of
crashing is covered in module [16](../16-error-handling/README.md) — for
now, just know the error exists and why: `int()` is unfamiliar with "abc"
and refuses to guess.

### `print()` in more detail

You've used `print()` since module 01. It has two useful keyword
arguments:

```python
print("a", "b", "c")                 # a b c        (default separator: space)
print("a", "b", "c", sep=", ")       # a, b, c      (custom separator)
print("Loading", end="")             # no newline after — next print continues same line
print("...")                         # Loading...   (both prints joined on one line)
```

`sep` controls what goes **between** the arguments you pass to `print()`;
`end` controls what's printed **after** everything (default is `"\n"`, a
newline — that's why every `print()` normally starts a new line).

### Putting it together: a typical input/convert/output flow

```python
name = input("Name: ")
age_text = input("Age: ")
age = int(age_text)
print(f"{name} will turn {age + 1} next year.")
```

This three-step shape — **read a string, convert it, use the converted
value** — is the pattern behind almost every interactive terminal program,
including the capstone projects at the end of this course.

## Common beginner mistakes

- **Forgetting to convert `input()` before doing math with it.**
  `input()` result + a number raises `TypeError: can only concatenate str
  (not "int") to str` (if you used `+`) or a similar error for other
  operators.
- **Using `int()` on decimal text.** `int("3.5")` raises `ValueError` —
  `int()` won't drop the decimal for you. Go through `float()` first if
  you need to handle decimals, or use `int(float("3.5"))` if you
  specifically want to truncate.
- **Printing a number with `+`.** `print("Age: " + age)` where `age` is
  an `int` raises `TypeError`. Either convert with `str(age)`, or — much
  more common in practice — just pass multiple arguments to `print`:
  `print("Age:", age)`, or use an f-string: `print(f"Age: {age}")`.

## Exercise

Open [`exercise.py`](exercise.py) and implement (note: none of these call
the real `input()` — they take strings as parameters instead, so the
exercise can be checked automatically, but the conversion logic is
identical to what you'd do with real user input):

1. `sum_from_text(a_text, b_text)` — `a_text` and `b_text` are strings
   like `"3"` and `"4"` (as if read from `input()`). Convert both to `int`
   and return their sum as an `int`.
2. `average_from_text(a_text, b_text, c_text)` — three number-strings like
   `"1"`, `"2"`, `"3"` (as if read from three separate `input()` calls).
   Convert each to `float` and return their average as a `float`.
3. `parse_yes_no(text)` — `text` is `"yes"`, `"no"`, `"Yes"`, etc.
   (case can vary). Return `True` if it means yes, `False` if no. Hint:
   normalize with `.strip().lower()` first.
4. `format_line(label, value)` — return a string built the way
   `print(label, value, sep=": ")` would produce it, **without** using
   `print` — i.e. return `f"{label}: {value}"`.

Run it to check yourself:

```bash
python3 python-for-beginner/05-input-output-and-conversion/exercise.py
```
