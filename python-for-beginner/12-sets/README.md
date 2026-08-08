# 12 — Sets

## Concept

A **set** is an unordered collection of **unique** values — duplicates
are automatically dropped, and there's no indexing (no "first item,"
since sets have no order).

```python
numbers = {1, 2, 3, 2, 1}
numbers          # {1, 2, 3} — duplicates gone
```

### The empty set trap

`{}` is an empty **dict**, not an empty set — a quirk of Python's syntax
history. For an empty set, you must call `set()`:

```python
empty_dict = {}       # dict!
empty_set = set()     # set
```

### Creating a set from a list (deduplicating)

The most common practical use of sets — remove duplicates from a list:

```python
names = ["ava", "sam", "ava", "kim", "sam"]
set(names)     # {"ava", "sam", "kim"} (order not guaranteed)
```

### Adding, removing, membership

```python
s = {1, 2, 3}
s.add(4)          # {1, 2, 3, 4}
s.remove(2)        # {1, 3, 4}  — KeyError if 2 isn't present
s.discard(99)       # does nothing, no error, even though 99 isn't in s
2 in s              # membership check — very fast, this is what sets are best at
```

### Set math: union, intersection, difference

This is where sets earn their keep — the same operations from math class:

```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b    # {1, 2, 3, 4}   — union: everything in either
a & b    # {2, 3}         — intersection: only what's in both
a - b    # {1}            — difference: in a but NOT in b
a ^ b    # {1, 4}         — symmetric difference: in exactly one, not both
```

Or the equivalent method names, if you prefer words to symbols:
`a.union(b)`, `a.intersection(b)`, `a.difference(b)`,
`a.symmetric_difference(b)` — identical results, just spelled out.

### Subset / superset checks

```python
{1, 2} <= {1, 2, 3}          # True  — is {1,2} a subset of {1,2,3}?
{1, 2, 3}.issuperset({1, 2}) # True  — same idea, other direction
```

### Why use a set instead of a list?

- **Uniqueness is automatic** — no manual "have I seen this before"
  checking.
- **Membership checks (`in`) are much faster** on large sets than on
  lists — this matters once your collections get big, though for the
  small collections in this course you won't notice a speed difference.
- You lose **order** and **duplicates** — if you need either, use a list.

## Common beginner mistakes

- **`{}` for an empty set.** It's a dict. Use `set()`.
- **Expecting order.** `for item in my_set:` may iterate in a different
  order than you added items — never rely on set order. Use a list if
  order matters.
- **Trying to index a set.** `my_set[0]` raises `TypeError` — sets aren't
  sequences, there's no "first item."
- **Putting a mutable value in a set.** `{[1, 2]}` raises
  `TypeError: unhashable type: 'list'` — same rule as dict keys (module
  11): set members must be immutable. A tuple works, a list doesn't.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `unique_items(items)` — return the set of unique items in the list
   `items`.
2. `common_elements(a, b)` — return the set of elements present in both
   list `a` and list `b`, using set intersection.
3. `only_in_first(a, b)` — return the set of elements in list `a` that
   are **not** in list `b`, using set difference.
4. `add_item(s, item)` — add `item` to set `s` (mutate it) and return
   `s`.
5. `is_subset(a, b)` — return whether every element of set `a` is also in
   set `b`.

Run it to check yourself:

```bash
python3 python-for-beginner/12-sets/exercise.py
```
