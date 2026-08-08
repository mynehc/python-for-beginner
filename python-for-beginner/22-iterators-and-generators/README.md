# 22 — Iterators & Generators

## Concept

### What actually makes `for` work

Every time you write `for item in something:`, Python is doing two things
behind the scenes: getting an **iterator** from `something`, then
repeatedly calling `next()` on it until it runs out. You can do this
manually:

```python
numbers = [10, 20, 30]
it = iter(numbers)     # get an iterator from the list
next(it)                 # 10
next(it)                 # 20
next(it)                 # 30
next(it)                 # StopIteration! no more items
```

- An **iterable** is anything you can call `iter()` on — lists, tuples,
  strings, dicts, sets, files (module 18) all qualify.
- An **iterator** is the object `iter()` gives you back — it remembers
  its position and hands out one item at a time via `next()`, raising
  `StopIteration` when exhausted.

`for` catches that `StopIteration` for you automatically — that's the
whole mechanism, and it's why `for item in "abc":`, `for item in
[1,2,3]:`, and `for line in open("file.txt"):` all work with identical
syntax despite being very different kinds of data underneath.

### Generator functions — `yield` instead of `return`

A **generator function** looks like a regular function but uses `yield`
instead of (or alongside) `return`. Calling it doesn't run the function
body immediately — it returns a generator (an iterator) that runs the
body **lazily**, one step at a time, only as you ask for the next value:

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)
next(gen)   # 1
next(gen)   # 2
next(gen)   # 3
next(gen)   # StopIteration

# more commonly, just loop over it directly:
for n in count_up_to(3):
    print(n)   # 1, 2, 3
```

Each `yield` pauses the function exactly where it is, hands a value back
out, and resumes right there (with all its local variables intact) the
next time a value is requested. This is genuinely different from
`return`, which exits the function entirely and forgets everything.

### Why generators matter: memory

```python
def all_squares_list(n):
    return [i ** 2 for i in range(n)]   # builds the ENTIRE list in memory, all at once

def all_squares_gen(n):
    for i in range(n):
        yield i ** 2                     # produces ONE value at a time, on demand
```

For a huge `n`, the list version has to hold every value simultaneously;
the generator version never holds more than one value at a time. This is
also exactly why `range()` itself doesn't build a giant list — `range(n)`
is lazy the same way, which is why `range(1_000_000_000)` is instant.

### Generator expressions — the comprehension-shaped version

Same idea as a list comprehension, but with `( )` instead of `[ ]`,
producing a lazy generator instead of a full list:

```python
squares = (i ** 2 for i in range(5))   # a generator, nothing computed yet
list(squares)                            # [0, 1, 4, 9, 16] — now it runs
```

Handy when you're about to feed the result straight into `sum()`,
`max()`, or a `for` loop and never actually need the whole list sitting
in memory at once: `sum(i ** 2 for i in range(1000))` (note: no extra
parentheses needed when it's the only argument to a function call).

## Common beginner mistakes

- **Trying to reuse an exhausted generator.** Once a generator has been
  fully consumed (looped over, or `next()`'d until `StopIteration`),
  it's empty — calling the generator *function* again gives you a fresh
  one, but the same generator *object* won't restart.
- **Calling `next()` past the end without handling `StopIteration`** —
  crashes, unless you're the one implementing the low-level iteration
  yourself (rare; usually you just use `for`, which handles this for
  you).
- **Expecting a generator to act like a list** — you can't index it
  (`gen[0]` fails) or check its `len()`. Wrap it in `list(...)` first if
  you need those.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `count_up_to(n)` — a generator function that `yield`s `1, 2, ..., n`
   in order.
2. `even_numbers_up_to(n)` — a generator function that `yield`s only the
   even numbers from `1` to `n` inclusive.
3. `first_two(iterable)` — given any iterable, return a tuple of its
   first two items, using `iter()` and `next()` (not indexing — this
   should work even on things that can't be indexed, like a generator).
4. `squares_generator_expr(n)` — return a **generator expression**
   (not a function) computing the squares of `0` through `n - 1`.

Run it to check yourself:

```bash
python3 python-for-beginner/22-iterators-and-generators/exercise.py
```
