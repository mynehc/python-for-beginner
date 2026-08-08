# 14 — Scope & Recursion

## Concept

### What is scope?

**Scope** is where a variable is visible/usable from. A variable created
**inside** a function is **local** to it — it doesn't exist outside:

```python
def greet():
    message = "Hello!"   # local to greet()
    print(message)

greet()        # Hello!
print(message) # NameError: name 'message' is not defined
```

A variable created at the top level of your file (not inside any
function) is **global** — visible everywhere, including inside functions:

```python
app_name = "MyApp"   # global

def show_name():
    print(app_name)   # reading a global from inside a function works fine

show_name()   # MyApp
```

### Reading a global is fine; assigning to one is not (by default)

Here's the part that surprises people. **Reading** a global variable from
inside a function works with no special syntax. But if you try to
**assign** to a variable with the same name inside a function, Python
assumes you mean a brand-new *local* variable, shadowing the global one:

```python
counter = 0

def increment():
    counter = counter + 1   # UnboundLocalError!

increment()
```

This fails because the moment Python sees `counter = ...` inside
`increment()`, it decides `counter` is local to that function for its
*entire* body — including the right-hand side, before it's been given a
value. To actually modify the global, say so explicitly with `global`:

```python
counter = 0

def increment():
    global counter
    counter = counter + 1   # now this refers to the global counter

increment()
print(counter)   # 1
```

In practice, reaching for `global` a lot is usually a sign to restructure
your code (pass values in as parameters, return results, or move to a
class — module 19) — but you'll see it, and this module's exercise has
you use it once so you recognize the pattern when you meet it.

### The LEGB rule (just the name — useful to have heard it)

When Python looks up a name, it checks, in order: **L**ocal (inside the
current function) → **E**nclosing (an outer function, if this one is
nested inside another) → **G**lobal (top of the file) → **B**uilt-in
(`print`, `len`, etc., always available). You don't need to memorize this
today — just know the term "LEGB" if you see it in error messages or
docs later.

## Recursion

A **recursive** function is one that calls itself, working on a smaller
version of the same problem each time, until it reaches a **base case**
simple enough to answer directly without recursing further.

Classic example — factorial (`n! = n × (n-1) × (n-2) × ... × 1`):

```python
def factorial(n):
    if n <= 1:
        return 1          # base case — stops the recursion
    return n * factorial(n - 1)   # recursive case — smaller problem

factorial(5)   # 5 * factorial(4) * ... = 120
```

Trace it: `factorial(5)` calls `factorial(4)`, which calls `factorial(3)`,
... down to `factorial(1)`, which returns `1` without recursing further.
Then each call multiplies its `n` by what it got back, unwinding back up:
`1 → 1 → 2 → 6 → 24 → 120`.

**Every recursive function needs a base case**, or it recurses forever
(well — until Python hits its recursion limit and raises
`RecursionError: maximum recursion depth exceeded`, which is Python's
version of a stack overflow). Forgetting the base case, or writing one
that's never actually reached, is the #1 recursion bug.

### When to use recursion vs a loop

Anything recursion can do, a loop can also do (and often faster, since
each recursive call has some overhead). Recursion tends to read more
naturally for problems that are naturally defined in terms of themselves
— tree/nested-structure traversal, "divide and conquer" algorithms,
math sequences like Fibonacci. For straightforward repetition, a loop
(module 09) is usually the more direct and more common choice in everyday
code.

## Common beginner mistakes

- **`UnboundLocalError`** from assigning to a name that's also a global,
  without `global` — covered above. The error message
  `local variable 'x' referenced before assignment` is the tell.
- **Missing or unreachable base case** — infinite recursion,
  `RecursionError`.
- **Recursing on the wrong thing.** `factorial(n)` must call
  `factorial(n - 1)` (smaller), not `factorial(n)` again (same size,
  never shrinks, never terminates).

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `increment_counter()` — increment the module-level `counter` variable
   (defined near the top of `exercise.py`) by 1, using the `global`
   keyword. No return value needed.
2. `factorial(n)` — return `n!` recursively. `factorial(0)` and
   `factorial(1)` are both `1` (base case).
3. `fibonacci(n)` — return the `n`th Fibonacci number recursively, where
   `fibonacci(0) == 0` and `fibonacci(1) == 1` (both base cases), and
   every later number is the sum of the two before it.
4. `sum_recursive(numbers)` — return the sum of a list of numbers,
   recursively (no `sum()`, no loop) — base case: an empty list sums to
   `0`.

Run it to check yourself:

```bash
python3 python-for-beginner/14-scope-and-recursion/exercise.py
```
