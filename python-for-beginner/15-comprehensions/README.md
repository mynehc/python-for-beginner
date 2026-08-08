# 15 — Comprehensions

## Concept

A **comprehension** is a compact, one-line way to build a list, dict, or
set from another iterable — a shorthand for a very common loop pattern:
"for each item, transform it (and maybe filter it), and collect the
results."

### The loop you already know

```python
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
# squares == [1, 4, 9, 16, 25]
```

### The same thing as a list comprehension

```python
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
# squares == [1, 4, 9, 16, 25]
```

Read it left to right as "build a list of `n ** 2`, for each `n` in
`numbers`." The shape is always:

```
[ <expression> for <item> in <iterable> ]
```

### Adding a filter with `if`

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
# evens == [2, 4, 6]
```

The `if` at the end filters which items get included — only items where
the condition is `True` make it into the result. This is equivalent to:

```python
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
```

### Dict comprehensions

Same idea, building a dict — note the `{key: value for ...}` shape:

```python
words = ["hi", "hello", "hey"]
lengths = {word: len(word) for word in words}
# lengths == {"hi": 2, "hello": 5, "hey": 3}
```

### Set comprehensions

```python
words = ["hi", "hello", "hey", "yo"]
unique_lengths = {len(word) for word in words}
# unique_lengths == {2, 5, 3}
```

### When to use a comprehension vs a regular loop

Comprehensions are idiomatic Python and you'll see them constantly in
real code — use one when the whole operation is a simple
transform-and/or-filter that fits comfortably on one line (or a short
wrapped one). Once the logic needs multiple steps, multiple conditions
with different results, or has side effects (printing, saving, updating
several things), a regular `for` loop is more readable — don't force
something complex into a comprehension just because you can.

## Common beginner mistakes

- **Forgetting the brackets/braces change the result type.** `[ ]` makes
  a list, `{ }` with `key: value` makes a dict, `{ }` with just a value
  makes a set. Using the wrong one gives you the wrong kind of collection,
  silently — no error, just not what you meant.
- **Putting the `if` in the wrong place.** A filter `if` goes at the
  **end**: `[x for x in items if cond]`. An `if`/`else` that picks
  between two *values* (not filtering) goes in the **expression** part,
  before the `for`: `[x if cond else y for x in items]` — this variant
  keeps every item, just changing what it becomes.
- **Overcomplicating a comprehension** until it's harder to read than the
  loop it replaced — a sign to switch back to a plain `for` loop.

## Exercise

Open [`exercise.py`](exercise.py) and implement each using a
comprehension (not a manual `for`-loop-with-`.append()`):

1. `squares_up_to(n)` — return a list of the squares of `1` through `n`
   inclusive, e.g. `squares_up_to(4) == [1, 4, 9, 16]`.
2. `evens_only(numbers)` — return a list of just the even numbers from
   `numbers`, preserving order.
3. `upper_words(words)` — return a new list with every word in `words`
   uppercased.
4. `length_map(words)` — return a dict mapping each word in `words` to
   its length.
5. `unique_lengths(words)` — return a set of the distinct word lengths
   present in `words`.

Run it to check yourself:

```bash
python3 python-for-beginner/15-comprehensions/exercise.py
```
