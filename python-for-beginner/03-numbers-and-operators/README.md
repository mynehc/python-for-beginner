# 03 — Numbers & Operators

## Concept

### Two kinds of numbers

- `int` — whole numbers, positive or negative, no size limit:
  `42`, `-7`, `1000000000000` all work fine.
- `float` — numbers with a decimal point: `3.14`, `-0.5`, `2.0`.

Writing a decimal point makes it a float, even `2.0` — `2` is an `int`,
`2.0` is a `float`.

### Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | addition | `2 + 3` | `5` |
| `-` | subtraction | `5 - 3` | `2` |
| `*` | multiplication | `4 * 3` | `12` |
| `/` | division (**always** returns a float) | `7 / 2` | `3.5` |
| `//` | floor division (divide, then round **down**) | `7 // 2` | `3` |
| `%` | modulo (the remainder after division) | `7 % 2` | `1` |
| `**` | exponent (power) | `2 ** 3` | `8` |

The two that surprise beginners most:

- `/` **always** gives a float, even when it divides evenly:
  `10 / 2` is `5.0`, not `5`.
- `//` rounds toward **negative infinity**, not just "chops off the
  decimal": `-7 // 2` is `-4`, not `-3`. Regular division would give
  `-3.5`; floor division rounds that *down* to `-4`.

`%` (modulo) is the operator you reach for to check "is this number
divisible by that one" or "what's left over" — e.g. `n % 2 == 0` means `n`
is even (you'll use `==` starting next module).

### Order of operations

Python follows standard math precedence (PEMDAS): parentheses first, then
`**`, then `*` `/` `//` `%` (left to right), then `+` `-` (left to right).

```python
2 + 3 * 4     # 14, not 20 — multiplication happens first
(2 + 3) * 4   # 20 — parentheses force addition first
```

When in doubt, add parentheses — it costs nothing and removes all
ambiguity, for you and for anyone reading your code later.

### Augmented assignment

`x = x + 1` is common enough that Python has a shorthand:

```python
x = 5
x += 1   # same as x = x + 1  ->  x is now 6
x -= 2   # same as x = x - 2  ->  x is now 4
x *= 3   # same as x = x * 3  ->  x is now 12
x /= 4   # same as x = x / 4  ->  x is now 3.0
```

Works with every arithmetic operator: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`,
`**=`.

### Handy built-in functions

```python
abs(-5)          # 5   — absolute value
round(3.14159, 2) # 3.14 — round to 2 decimal places
round(2.5)        # 2   — "round half to even," see gotcha below
min(4, 9, 1)      # 1
max(4, 9, 1)      # 9
sum([1, 2, 3])    # 6   — total of a list (lists: module 08)
```

## Common beginner mistakes

- **Expecting `/` to give a whole number.** `10 / 2 == 5.0`. If you need a
  whole-number result, use `//`.
- **Floating point imprecision.** `0.1 + 0.2` prints `0.30000000000000004`,
  not `0.3`. This isn't a Python bug — it's how *every* language stores
  decimal numbers in binary (float representation can't exactly represent
  most decimals). Never compare floats with `==` for "did this calculation
  work" — round first, or use a small tolerance.
- **`round()`'s "banker's rounding."** `round(0.5)` is `0`, and
  `round(2.5)` is `2`, not the "always round .5 up" you might expect from
  school math. Python rounds half-way values to the nearest *even* number
  to avoid statistical bias. Rare to matter, but confusing the first time
  you hit it.
- **Mixing up `//` and `/`.** `7 // 2` is `3` (an int-like result), `7 / 2`
  is `3.5` (always float). Pick based on whether you want the fractional
  part.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `average(a, b, c)` — return the average of three numbers as a float.
2. `remainder(a, b)` — return `a` modulo `b`.
3. `power(base, exponent)` — return `base` raised to `exponent`.
4. `floor_divide(a, b)` — return the floored integer division of `a` by
   `b`.
5. `round_to(number, digits)` — return `number` rounded to `digits`
   decimal places.

Run it to check yourself:

```bash
python3 python-for-beginner/03-numbers-and-operators/exercise.py
```
