# 08 — Lists

## Concept

A **list** is an ordered collection of values, written with square
brackets:

```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]   # a list can hold mixed types, though usually you keep one kind
empty = []
```

### Indexing and slicing

Same rules as strings (module 04) — 0-based indexing, slices exclude the
`stop`:

```python
fruits[0]     # "apple"
fruits[-1]    # "cherry"  — last item
fruits[0:2]   # ["apple", "banana"]
len(fruits)   # 3
```

### Lists are mutable

Unlike strings, lists **can** be changed in place after creation:

```python
fruits[0] = "avocado"
fruits            # ["avocado", "banana", "cherry"]
```

### Common list methods

```python
fruits = ["apple", "banana"]

fruits.append("cherry")     # ["apple", "banana", "cherry"] — add to the end
fruits.insert(0, "kiwi")    # ["kiwi", "apple", "banana", "cherry"] — insert at index
fruits.remove("banana")     # removes the first "banana" it finds (ValueError if absent)
fruits.pop()                # removes AND returns the last item
fruits.pop(0)                # removes AND returns the item at index 0
fruits.extend(["mango", "fig"])  # appends every item from another list
fruits.sort()                # sorts the list IN PLACE (mutates it, returns None)
fruits.reverse()             # reverses IN PLACE
fruits.index("apple")        # position of the first "apple" (ValueError if absent)
fruits.count("apple")        # how many times "apple" appears
```

`sort()` and `reverse()` mutate the list and return `None` — a very common
beginner bug is `fruits = fruits.sort()`, which throws away the list and
replaces it with `None`. If you want a **new**, sorted list without
touching the original, use the built-in function `sorted(fruits)` instead
— it returns a new list, leaving the original untouched.

### `in` — membership check

```python
"apple" in fruits       # True
"pear" not in fruits    # True
```

### Concatenation and repetition

```python
[1, 2] + [3, 4]   # [1, 2, 3, 4]  — join two lists into a new one
[0] * 3           # [0, 0, 0]     — repeat
```

### Nested lists

A list can contain other lists — useful for grids/tables:

```python
grid = [[1, 2], [3, 4]]
grid[0]       # [1, 2]
grid[0][1]    # 2
```

### The aliasing gotcha

This one catches everyone eventually. Assigning a list to a new variable
does **not** copy it — both names point to the *same* list in memory:

```python
a = [1, 2, 3]
b = a          # b is NOT a copy, it's another name for the same list
b.append(4)
a              # [1, 2, 3, 4] — a changed too!
```

To get an actual independent copy, use `.copy()` or a full slice:

```python
b = a.copy()   # or: b = a[:]
b.append(5)
a              # unaffected
```

You'll see the same behavior with dicts (module 11) — it applies to every
mutable type, not just lists.

### `sum()`, `len()`, `min()`, `max()` on lists

```python
numbers = [4, 1, 7, 3]
sum(numbers)    # 15
len(numbers)    # 4
min(numbers)    # 1
max(numbers)    # 7
```

Repeating an item over and over "manually" (checking each one by hand) is
exactly what loops (module [09](../09-loops/README.md)) exist to automate
— this module focuses on the list itself; you'll combine lists with loops
right after.

## Common beginner mistakes

- **`fruits = fruits.sort()`** — loses the list, since `.sort()` returns
  `None`. Just call `fruits.sort()` on its own line, or use
  `fruits = sorted(fruits)` for a new sorted copy.
- **Indexing past the end.** `fruits[10]` on a 3-item list raises
  `IndexError: list index out of range` — always a runtime error, never
  silently `None` like some languages.
- **Aliasing instead of copying.** Covered above — `b = a` shares the
  same list. This is the single most common "why did my other variable
  change too?!" bug for beginners.
- **`.remove(x)` vs `.pop(i)`.** `.remove()` takes a *value* and deletes
  its first match; `.pop()` takes an *index* (or none, for "last item")
  and returns what it removed. Mixing these up raises a `TypeError` or
  removes the wrong thing.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `first_and_last_items(items)` — return a tuple `(first, last)` of
   `items`, using indexing.
2. `add_to_front(items, item)` — return a **new** list with `item` placed
   at the front, without modifying the original `items` list.
3. `remove_item(items, target)` — remove the first occurrence of `target`
   from `items` (mutate it in place) and return `items`.
4. `total_and_average(numbers)` — return a tuple `(total, average)` using
   `sum()` and `len()`.
5. `sort_descending(numbers)` — return a **new** list of `numbers` sorted
   from largest to smallest, without modifying the original.

Run it to check yourself:

```bash
python3 python-for-beginner/08-lists/exercise.py
```
