# 21 — Lambda & Functional Tools

## Concept

### Functions are values

In Python, a function is a regular value like any other — you can store
it in a variable, put it in a list, pass it into another function as an
argument, or return it from one. This might feel strange at first coming
from thinking of functions purely as "things you call," but it's the
basis of everything in this module:

```python
def shout(text):
    return text.upper() + "!"

my_function = shout        # no parentheses — this stores the function itself, doesn't call it
my_function("hi")           # "HI!" — calling it through the new name works fine
```

### `lambda` — small, throwaway, unnamed functions

A `lambda` is a one-expression function written inline, with no `def`
and no name:

```python
square = lambda x: x ** 2
square(5)    # 25

# equivalent to:
def square(x):
    return x ** 2
```

`lambda <parameters>: <expression>` — the expression's result is
automatically returned; there's no `return` keyword, and a lambda can
only contain a single expression, not multiple statements. Lambdas are
almost always used **inline**, passed directly into another function,
rather than assigned to a name like above (if you're naming it, a regular
`def` is usually clearer anyway).

### `map()` — transform every item

```python
numbers = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, numbers)
list(doubled)   # [2, 4, 6, 8]
```

`map(function, iterable)` applies `function` to every item and gives
back a lazy `map` object — wrap it in `list(...)` to see the results (the
"lazy" part is explained properly in module
[22](../22-iterators-and-generators/README.md)). This is the same job a
list comprehension does — `[x * 2 for x in numbers]` — and in modern
Python, a comprehension is usually considered more readable. Recognize
`map()` when you see it in others' code; reach for a comprehension in
your own.

### `filter()` — keep only matching items

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
list(evens)   # [2, 4, 6]
```

Same story as `map()` — `[x for x in numbers if x % 2 == 0]` does the
same thing and is generally preferred.

### `sorted()` with a `key` — the one that's genuinely essential

```python
words = ["banana", "kiwi", "apple"]
sorted(words)                          # ["apple", "banana", "kiwi"] — default: alphabetical
sorted(words, key=len)                  # ["kiwi", "apple", "banana"] — sorted by length instead
sorted(words, key=lambda w: w[-1])      # sorted by each word's LAST letter
```

`key=` takes a function; `sorted()` calls it on every item to decide
ordering, without changing the items themselves. This is the one place
`lambda` genuinely earns its keep over a comprehension — there's no
comprehension equivalent for "sort by a computed value." Same `key=`
argument works on `min()`, `max()`, and `list.sort()`.

### `functools.reduce()` — combine everything into one value

```python
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda acc, x: acc + x, numbers, 0)
# 0 is the starting value ("acc"umulator); each step: acc = acc + x
# ((((0+1)+2)+3)+4) = 10
```

`reduce(function, iterable, start)` repeatedly applies `function(acc,
item)`, carrying the running result forward. It's powerful but often
less readable than a plain loop or the built-in `sum()`/`max()` for
simple cases — reach for it when you truly need a custom running
combination, not as a first choice for addition (`sum()` exists for a
reason).

### A function that returns a function (closures, briefly)

```python
def make_adder(n):
    def add(x):
        return x + n
    return add

add5 = make_adder(5)
add5(10)   # 15
```

`add` "remembers" `n` from `make_adder`'s scope even after `make_adder`
has finished running — this is called a **closure**. You don't need to
master the theory here, just recognize the pattern: a function defined
inside another function, returned, that still has access to the outer
function's variables.

## Common beginner mistakes

- **Cramming too much into a lambda.** If you need an `if`/`else` or
  multiple steps, use `def` — lambdas are for simple, single-expression
  cases only, and Python's `lambda` can't contain statements (no `if`
  blocks, no loops, no assignment).
- **Forgetting `map()`/`filter()` are lazy.** `map(f, items)` alone
  doesn't run anything yet, and doesn't print as a list — you need
  `list(...)` around it to see results (or loop over it directly).
- **Using `reduce()` where `sum()`, `max()`, `min()`, or a comprehension
  would be clearer.** `reduce()` is genuinely necessary sometimes, but
  it's frequently overused where a simpler built-in already does the job.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `make_multiplier(n)` — return a function (closure) that multiplies its
   argument by `n`.
2. `square_all(numbers)` — return a list of every number in `numbers`
   squared, using `map()` and a `lambda`.
3. `filter_evens(numbers)` — return a list of just the even numbers in
   `numbers`, using `filter()` and a `lambda`.
4. `sort_by_length(words)` — return `words` sorted from shortest to
   longest, using `sorted()` with `key=`.
5. `total_with_reduce(numbers)` — return the sum of `numbers` using
   `functools.reduce`.

Run it to check yourself:

```bash
python3 python-for-beginner/21-lambda-and-functional-tools/exercise.py
```
