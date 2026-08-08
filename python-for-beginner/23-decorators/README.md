# 23 — Decorators

## Concept

A **decorator** wraps a function with extra behavior, without changing
the function's own code. This builds directly on module 21's "functions
are values" idea — a decorator is a function that takes a function in and
returns a (usually enhanced) function out.

### Building up to `@` from scratch

```python
def shout(text):
    return text + "!"

def loud(func):
    def wrapper(text):
        result = func(text)
        return result.upper()
    return wrapper

shout = loud(shout)   # replace shout with the wrapped version
shout("hello")          # "HELLO!"
```

`loud` takes a function (`func`), defines a new function (`wrapper`) that
calls `func` and does something extra with the result, and returns
`wrapper`. Reassigning `shout = loud(shout)` is exactly what a decorator
automates.

### The `@` syntax

```python
def loud(func):
    def wrapper(text):
        result = func(text)
        return result.upper()
    return wrapper

@loud
def shout(text):
    return text + "!"

shout("hello")   # "HELLO!"
```

`@loud` directly above `def shout(...)` is exactly equivalent to writing
`shout = loud(shout)` right after defining it — just cleaner and impossible
to forget to apply. Read `@loud` as "wrap the function below with `loud`."

### Handling arguments generically with `*args`/`**kwargs`

The `wrapper` above only works for functions that take exactly one
argument named the same thing. A decorator meant to wrap *any* function
needs to accept and forward arbitrary arguments (module 13's `*args`/
`**kwargs`):

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logged
def add(a, b):
    return a + b

add(2, 3)
# Calling add
# add returned 5
```

`wrapper(*args, **kwargs)` accepts anything; `func(*args, **kwargs)`
forwards it all straight through to the wrapped function unchanged. This
is the standard shape of a general-purpose decorator.

### A decorator that tracks state

A decorator can attach extra data to the wrapper, useful for things like
counting calls:

```python
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def greet(name):
    return f"Hi, {name}"

greet("Ava")
greet("Sam")
greet.calls   # 2
```

Functions can have arbitrary attributes attached to them (`wrapper.calls
= 0` just sets an attribute on the function object, same idea as
`self.attribute` on an instance in module 19) — this is how the decorator
keeps a running count across calls.

### What decorators are used for in real code

You'll meet built-in and framework decorators constantly once you go
further: `@staticmethod`/`@classmethod` on class methods, `@app.route(...)`
in web frameworks like Flask, `@pytest.fixture` in testing (module 27).
They're all the same underlying mechanism you just built by hand.

## Common beginner mistakes

- **Forgetting to `return wrapper`** from the decorator — the decorated
  function then becomes `None` (whatever the outer function returns by
  default), and calling it raises `TypeError: 'NoneType' object is not
  callable`.
- **Forgetting `*args, **kwargs`** in `wrapper`'s signature when the
  decorator needs to work on functions with different parameter shapes —
  it'll work for the first function you tried it on, then break on the
  next one with a different number of arguments.
- **Forgetting to call `func(...)` inside `wrapper`** — easy to write a
  wrapper that does the "extra" behavior but never actually runs the
  original function.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `uppercase_result(func)` — a decorator: the wrapped function should
   call `func(*args, **kwargs)`, then return its result converted to
   uppercase with `.upper()`.
2. `count_calls(func)` — a decorator: the wrapped function should track
   how many times it's been called on a `.calls` attribute of the
   wrapper (starting at `0`), incrementing it on every call, while still
   calling and returning `func`'s normal result.

`exercise.py` also defines two ordinary functions, `shout` and `greet`,
decorated with `@uppercase_result` and `@count_calls` respectively — once
your decorators are implemented, those functions should behave as
described in the checks.

Run it to check yourself:

```bash
python3 python-for-beginner/23-decorators/exercise.py
```
