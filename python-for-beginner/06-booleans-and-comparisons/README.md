# 06 — Booleans & Comparisons

## Concept

### `bool`, the yes/no type

`bool` has exactly two values: `True` and `False` (capitalized — `true`
and `false` lowercase don't exist in Python and will raise `NameError`).
They're the result of asking a yes/no question about your data.

### Comparison operators

These compare two values and produce a `bool`:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 3` | `True` |
| `<` | less than | `3 < 5` | `True` |
| `>` | greater than | `3 > 5` | `False` |
| `<=` | less than or equal | `5 <= 5` | `True` |
| `>=` | greater than or equal | `4 >= 5` | `False` |

**`==` is comparison, `=` is assignment** — mixing these up is one of the
single most common beginner errors coming from other contexts (and
Python won't even let you write `if x = 5:`, it's a `SyntaxError`, which
is Python protecting you from this exact mistake).

Comparisons work on strings too, alphabetically: `"apple" < "banana"` is
`True`.

### Chained comparisons

Python lets you chain comparisons the way you would in math class — this
is fairly unusual among programming languages and very convenient:

```python
age = 25
18 <= age <= 65   # True — equivalent to (18 <= age) and (age <= 65)
```

### Logical operators: `and`, `or`, `not`

Combine or invert boolean values:

```python
is_adult = True
has_ticket = False

is_adult and has_ticket   # False — both must be True
is_adult or has_ticket    # True  — at least one must be True
not is_adult              # False — flips True to False, or False to True
```

Truth tables:

| `a` | `b` | `a and b` | `a or b` |
|---|---|---|---|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

### Short-circuit evaluation

`and`/`or` stop evaluating as soon as the result is decided:

- `a and b` — if `a` is `False`, Python never even looks at `b` (the
  whole thing must be `False` already).
- `a or b` — if `a` is `True`, Python never looks at `b` (the whole thing
  must be `True` already).

This isn't just an optimization detail — it's commonly used on purpose:

```python
name = ""
display_name = name or "Anonymous"   # "Anonymous" — falls back if name is falsy
```

### Truthy and falsy values

Every value in Python can be used where a `bool` is expected (e.g. in an
`if`), and Python decides whether to treat it as `True`-like ("truthy")
or `False`-like ("falsy"). These are **falsy**:

```
0        0.0        ""        []        {}        set()        None        False
```

Every other value — every non-empty string, every non-zero number, every
non-empty list/dict/set — is **truthy**. This matters a lot once you hit
`if` statements next module: `if my_list:` is a very common, idiomatic way
to check "is this list non-empty," instead of the more verbose
`if len(my_list) > 0:`.

`not value` gives you the boolean for whether something is falsy:
`not []` is `True`, `not "hi"` is `False`.

## Common beginner mistakes

- **`=` vs `==`.** Covered above — Python's `SyntaxError` on
  `if x = 5:` is a safety net most languages don't have; lean on it.
- **Comparing across incompatible types.** `"5" == 5` is `False` — a
  string is never equal to a number, even if they "look the same." Convert
  first (module 05) if you're not sure what type you have.
- **Using `and`/`or` when you meant a comparison.** `if 1 <= x <= 10` is
  correct Python (chained comparison). Beginners coming from languages
  without chaining sometimes overcorrect into
  `if 1 <= x and x <= 10`, which also works but is more to type — either
  is fine, chaining just reads closer to math notation.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `is_falsy(value)` — return `True` if Python would treat `value` as
   falsy in an `if` check, `False` otherwise.
2. `in_range(n, low, high)` — return whether `n` is between `low` and
   `high`, inclusive on both ends. Use a chained comparison.
3. `both_positive(a, b)` — return `True` only if both `a` and `b` are
   greater than 0.
4. `at_least_one_true(a, b, c)` — return `True` if at least one of the
   three booleans is `True`.
5. `flip(value)` — return the boolean opposite of `value`.

Run it to check yourself:

```bash
python3 python-for-beginner/06-booleans-and-comparisons/exercise.py
```
