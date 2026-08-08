# 07 — Conditionals (if / elif / else)

## Concept

A conditional lets your program **choose** which code to run based on a
`bool` (True/False) condition.

```python
age = 20

if age >= 18:
    print("You're an adult.")
```

The colon `:` and the **indented** line(s) below it are the "block" that
runs only when the condition is `True`. This is the moment indentation
starts to matter for real: everything indented at the same level under
`if` is part of that block; the first line back at the original
indentation ends it.

### `else` — the fallback

```python
age = 15

if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")
```

### `elif` — more branches

`elif` (short for "else if") lets you check additional conditions in
order. Python checks each condition top to bottom and runs the **first**
one that's `True`, then skips the rest — even if a later condition would
also be true:

```python
score = 72

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)   # C
```

You can have as many `elif`s as you need, and `else` is always optional —
skip it if there's genuinely nothing to do when no condition matches.

### Nesting

Conditionals can contain other conditionals, indented one level deeper
each time:

```python
if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Need ID.")
else:
    print("Too young.")
```

Deep nesting (4+ levels) gets hard to read — often a sign you can flip a
condition or use `elif` instead. Not a rule to memorize now, just
something to notice as your programs grow.

### The conditional expression (a compact if/else)

For simple "pick one of two values" cases, Python has a one-line form:

```python
status = "adult" if age >= 18 else "minor"
```

Read it as: `status = (result if condition else other_result)`. This is
equivalent to a full `if`/`else` that just assigns a variable, but in one
expression. Don't overuse it for anything more complex than a single
value choice — a real `if`/`else` block is more readable once logic
grows.

### Comparing to multiple values with `in`

Instead of `x == "a" or x == "b" or x == "c"`, use `in` with a collection
(you'll cover lists properly in module 08):

```python
if grade in ("A", "B"):
    print("Passing with distinction")
```

## Common beginner mistakes

- **Forgetting the colon `:`** after `if`/`elif`/`else` — `SyntaxError`.
- **Inconsistent indentation** — mixing tabs and spaces, or indenting by a
  different amount than the surrounding block, raises `IndentationError`.
  Most editors (including VS Code with the Python extension) auto-indent
  correctly; if you're ever unsure, use 4 spaces per level, which is the
  Python community standard.
- **Using `elif` chains where each condition should be independently
  checked.** If you actually need to check several *unrelated* things
  (not "which one of these categories"), you want separate `if`
  statements, not `elif` — `elif` only runs when everything above it in
  the chain was `False`.
- **Comparing floats for exact equality** inside a condition — see module
  03's note on floating point imprecision; `if result == 0.3:` can
  silently fail even when it "should" be true.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `classify_number(n)` — return `"negative"`, `"zero"`, or `"positive"`
   depending on `n`.
2. `letter_grade(score)` — return a letter grade using this scale:
   `90+` → `"A"`, `80-89` → `"B"`, `70-79` → `"C"`, `60-69` → `"D"`,
   below `60` → `"F"`. Use an `if`/`elif`/`else` chain.
3. `largest_of_three(a, b, c)` — return the largest of the three numbers,
   using only `if`/`elif`/`else` (not the built-in `max()`).
4. `describe_temperature(celsius)` — return `"freezing"` if `celsius <=
   0`, `"cold"` if `celsius <= 15`, `"warm"` if `celsius <= 25`, else
   `"hot"`.
5. `abs_value(n)` — return the absolute value of `n` using a one-line
   conditional expression (not the built-in `abs()`).

Run it to check yourself:

```bash
python3 python-for-beginner/07-conditionals/exercise.py
```
