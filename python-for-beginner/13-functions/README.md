# 13 — Functions

## Concept

You've been *calling* functions since module 01 (`print()`, `len()`,
`int()`...). Now you'll *write* your own — a named, reusable block of code
that takes input, does something, and (usually) gives back a result.

```python
def greet(name):
    return f"Hello, {name}!"

greet("Ava")   # "Hello, Ava!"
```

- `def` starts a function definition.
- `greet` is the function's name — same naming rules as variables
  (snake_case by convention).
- `(name)` is the **parameter list** — placeholder names for the values
  the function needs. `name` here is a **parameter**; when you call
  `greet("Ava")`, `"Ava"` is the **argument** — the actual value passed
  in. People often use the two words loosely, but "parameter" = the name
  in the definition, "argument" = the value at the call site.
- `return` sends a value back to whoever called the function, and
  immediately exits the function — any code after `return` inside the
  function doesn't run.

### Functions with no `return`

If a function never hits a `return`, or has bare `return` with nothing
after it, calling it gives back `None`:

```python
def log(message):
    print(message)   # this function's job is the side effect (printing),
                      # not producing a value

result = log("hi")   # prints "hi"
result                # None
```

That's normal and common — not every function needs to hand back a
value; some exist purely for their **side effect** (printing, saving a
file, modifying something).

### Default parameter values

Give a parameter a default so callers can omit it:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ava")             # "Hello, Ava!"          — uses the default
greet("Ava", "Hi")       # "Hi, Ava!"              — overrides it
greet("Ava", greeting="Hey")  # "Hey, Ava!"        — same, named explicitly
```

Calling with `greeting="Hey"` (name=value) is a **keyword argument** — you
can pass arguments by name instead of position, which is especially handy
once a function has several parameters and you want the call site to be
unambiguous about which is which.

### `*args` — accept any number of positional arguments

```python
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

sum_all(1, 2, 3)       # 6 — numbers is the tuple (1, 2, 3) inside the function
sum_all(1, 2, 3, 4, 5) # 15
sum_all()               # 0
```

`*numbers` collects however many positional arguments were passed into a
tuple named `numbers`. The name `numbers` is up to you — `*args` is just
the common convention name when the meaning isn't more specific.

### `**kwargs` — accept any number of keyword arguments

```python
def build_profile(**details):
    return details

build_profile(name="Ava", age=30)   # {"name": "Ava", "age": 30} — collected into a dict
```

`**details` collects any number of `key=value` arguments into a dict
named `details`. `**kwargs` is the common convention name.

### Docstrings

The string literal right under a `def` line, in triple quotes, is a
**docstring** — documentation for the function, shown by `help(func)`
and by most editors when you hover over a call to it:

```python
def greet(name):
    """Return a friendly greeting for name."""
    return f"Hello, {name}!"
```

Every function in this course's `exercise.py` files has one — you've been
reading them as instructions all along.

### Multiple return values

A function can `return` several values separated by commas — really
returning one tuple (module 10):

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)

low, high = min_and_max([3, 1, 4, 1, 5])
print(low, high)   # 1 5
```

## Common beginner mistakes

- **Forgetting `return`.** Writing the result on its own line at the end
  of a function does nothing useful — Python doesn't auto-return the last
  expression like some languages. You must write `return result`.
- **Mutating a default argument that's a list or dict.** `def f(items=[]):`
  is a classic Python trap — that default list is created **once**, when
  the function is defined, and shared across every call that doesn't pass
  its own. Prefer `def f(items=None):` then `if items is None: items = []`
  inside the function.
- **Confusing parameters and arguments in your own head** isn't fatal,
  but knowing the vocabulary helps you read error messages like
  `missing 1 required positional argument` — it's telling you a
  *parameter* had no matching *argument* at the call site.
- **Calling a function without enough arguments.** `TypeError: greet()
  missing 1 required positional argument: 'name'` — parameters without a
  default are required.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `power(base, exponent=2)` — return `base` raised to `exponent`,
   defaulting to squaring when `exponent` isn't given.
2. `full_name(first, last, middle=None)` — return `"first last"`
   normally, or `"first middle last"` if `middle` is given (not `None`).
3. `sum_all(*numbers)` — return the sum of any number of positional
   arguments, using `*args`-style collection.
4. `build_profile(**details)` — return the `details` dict built from
   however many keyword arguments were passed.
5. `safe_divide(a, b)` — return `a / b`, or `None` if `b` is `0` (instead
   of raising an error).

Run it to check yourself:

```bash
python3 python-for-beginner/13-functions/exercise.py
```
