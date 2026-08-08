# 11 — Dictionaries

## Concept

A **dictionary** (`dict`) stores **key → value** pairs — instead of
looking things up by position (like a list), you look them up by a
meaningful key:

```python
person = {"name": "Ava", "age": 30, "city": "Boston"}
person["name"]    # "Ava"
person["age"]     # 30
```

Keys are usually strings (or numbers), and must be an **immutable** type
(strings, numbers, tuples — not lists, since keys need to stay constant to
be findable). Values can be absolutely anything, including other lists or
dicts.

### Adding and updating

```python
person["email"] = "ava@example.com"   # adds a new key
person["age"] = 31                    # updates an existing key — same syntax either way
```

### Missing keys

```python
person["phone"]           # KeyError! "phone" doesn't exist
person.get("phone")       # None — .get() returns None instead of crashing
person.get("phone", "N/A") # "N/A" — .get() with a default value
```

`.get()` is the safe way to read a key that might not exist. Prefer it
over `[ ]` whenever you're not certain the key is there.

### Checking membership

```python
"name" in person        # True — checks the KEYS by default
"Ava" in person          # False — "Ava" is a value, not a key
"Ava" in person.values()  # True
```

### Removing keys

```python
del person["city"]              # removes the key (KeyError if missing)
person.pop("city")               # removes AND returns the value (KeyError if missing, unless you give a default)
person.pop("city", None)         # removes and returns, or None if missing — safe version
```

### Looping over a dict

```python
person = {"name": "Ava", "age": 30}

for key in person:                 # loops over keys by default
    print(key)

for key, value in person.items():  # loops over (key, value) pairs — the common one
    print(key, value)

for value in person.values():      # loops over values only
    print(value)
```

`.items()` is what you'll reach for almost every time you need both the
key and value in a loop.

### `keys()`, `values()`, `items()`, `len()`

```python
person.keys()     # dict_keys(['name', 'age'])   — view of just the keys
person.values()   # dict_values(['Ava', 30])     — view of just the values
person.items()    # dict_items([('name', 'Ava'), ('age', 30)])
len(person)       # 2 — number of key/value pairs
```

### Merging dicts

```python
defaults = {"theme": "light", "font_size": 12}
overrides = {"font_size": 16}
{**defaults, **overrides}   # {"theme": "light", "font_size": 16} — overrides wins on conflicts
```

`{**a, **b}` unpacks both dicts into a new one; keys from `b` overwrite
matching keys from `a`. This is a very common pattern for "defaults +
user overrides."

### Nested dicts

Just like nested lists, values can be dicts themselves:

```python
users = {
    "ava": {"age": 30, "city": "Boston"},
    "sam": {"age": 25, "city": "Denver"},
}
users["ava"]["city"]   # "Boston"
```

### Dicts are mutable — same aliasing gotcha as lists

```python
a = {"x": 1}
b = a          # b is the SAME dict, not a copy
b["x"] = 99
a              # {"x": 99} — a changed too!
```

Use `.copy()` for an independent copy, same as lists (module 08).

## Common beginner mistakes

- **`d[key]` on a missing key** — `KeyError`, crashes the program. Use
  `.get()` if the key might not exist.
- **Assuming dicts remember insertion order is unimportant** — since
  Python 3.7, dicts *do* preserve insertion order (the order you added
  keys), and code frequently relies on this. Don't assume it's random.
- **Using a list as a dict key** — `TypeError: unhashable type: 'list'`.
  Keys must be immutable; use a tuple instead if you need a
  multi-part key.
- **Forgetting `.items()` in a loop** when you need both key and value —
  `for pair in person:` only gives you keys, not `(key, value)` pairs.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `get_or_default(d, key, default)` — return `d[key]` if present,
   otherwise `default`. Use `.get()`.
2. `add_or_update(d, key, value)` — set `d[key] = value` (mutating `d`)
   and return `d`.
3. `word_counts(words)` — `words` is a list of strings; return a dict
   mapping each word to how many times it appears. Build it with a `for`
   loop and `.get()`.
4. `merge_with_overrides(defaults, overrides)` — return a new dict:
   `defaults` with `overrides` layered on top.
5. `invert(d)` — return a new dict with `d`'s keys and values swapped
   (assume all of `d`'s values are unique so this is safe).

Run it to check yourself:

```bash
python3 python-for-beginner/11-dictionaries/exercise.py
```
