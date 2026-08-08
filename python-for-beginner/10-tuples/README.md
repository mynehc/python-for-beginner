# 10 — Tuples

## Concept

A **tuple** is an ordered collection, just like a list — but written with
parentheses (or often nothing at all) instead of square brackets, and
**immutable**: once created, it can't be changed.

```python
point = (3, 4)
also_a_tuple = 3, 4        # parentheses are optional in many contexts
single = (5,)               # note the trailing comma — (5) alone is just the int 5 in parens!
empty = ()
```

That trailing comma on a one-item tuple is a real gotcha: `(5,)` is a
tuple containing `5`; `(5)` is just the number `5` with redundant
parentheses around it, because parentheses alone don't make a tuple —
the comma does.

### Indexing, slicing, `len()` — same as lists

```python
point = (3, 4)
point[0]     # 3
point[-1]    # 4
len(point)   # 2
```

### Immutable — no changing after creation

```python
point[0] = 10   # TypeError: 'tuple' object does not support item assignment
```

If you need to "change" a tuple, you build a new one — same idea as
strings being immutable (module 04).

### Why use a tuple instead of a list?

- **Meaning**: a tuple often represents a fixed-shape, related bundle of
  values — a coordinate `(x, y)`, an RGB color `(255, 0, 0)`, a
  `(name, age)` pair — where the *position* of each value has a fixed
  meaning. A list usually represents a variable-length collection of
  similar items (a list of usernames, a list of scores).
- **Safety**: immutability means a tuple you pass to a function or store
  somewhere can't be accidentally modified later.
- Tuples are also the type Python uses internally for a **function
  returning multiple values** — covered fully in module
  [13](../13-functions/README.md) — because `return a, b` is really
  returning one tuple `(a, b)`.

### Unpacking

You met this briefly in module 02's `swap`. It works for any tuple (or
any iterable, really) of a known length:

```python
point = (3, 4)
x, y = point
print(x, y)   # 3 4
```

The number of variables on the left must match the number of items,
or Python raises `ValueError: too many values to unpack` (or "not enough
values").

### Tuple methods

Only two — since tuples can't change, there's much less you can do to one
than a list:

```python
t = (1, 2, 2, 3)
t.count(2)    # 2  — how many times 2 appears
t.index(3)    # 3  — position of the first 3
```

### Combining tuples

```python
(1, 2) + (3, 4)   # (1, 2, 3, 4) — like list concatenation, makes a new tuple
(0,) * 3          # (0, 0, 0)
```

## Common beginner mistakes

- **Forgetting the comma on a single-item tuple**: `(5)` is just `5`, not
  a tuple. You need `(5,)`.
- **Trying to mutate a tuple** — `TypeError`. If you find yourself wanting
  to `.append()` to something, you probably want a list, not a tuple.
- **Assuming tuple unpacking always works.** Unpacking `(1, 2, 3)` into
  `a, b = ...` (only two names for three values) raises `ValueError`.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `make_point(x, y)` — return the tuple `(x, y)`.
2. `sum_point(point)` — `point` is an `(x, y)` tuple; unpack it and
   return `x + y`.
3. `first_two(t)` — return a tuple of the first two elements of `t`,
   using indexing (not slicing).
4. `count_occurrences(t, value)` — return how many times `value` appears
   in tuple `t`.
5. `combine(a, b)` — return the concatenation of tuples `a` and `b`.

Run it to check yourself:

```bash
python3 python-for-beginner/10-tuples/exercise.py
```
