# 02 — Variables & Data Types

## Concept

### What is a variable?

A **variable** is a name that points to a value stored in memory. Instead
of writing `"Ava"` every time you need that text, you give it a name once
and reuse the name:

```python
name = "Ava"
print(name)        # Ava
print(name + "!")  # Ava!
```

`=` is the **assignment operator** — read `name = "Ava"` as "make the name
`name` point to the value `"Ava"`," not as a math equals sign. This trips
up a lot of beginners: `x = x + 1` is not a false mathematical statement,
it means "compute `x + 1`, then make `x` point to that new result."

### Naming rules

A variable name:
- can contain letters, digits, and underscores (`_`)
- **cannot** start with a digit (`1st_name` is invalid, `first_name` is fine)
- is **case-sensitive** (`age` and `Age` are two different variables)
- cannot be a reserved word (`if`, `for`, `class`, etc.)

Convention: use `snake_case` (lowercase words separated by underscores) for
variable and function names — `first_name`, not `firstName` or
`FirstName`. This is a strong community convention (part of a style guide
called **PEP 8**), not a rule Python enforces, but following it makes your
code look like everyone else's Python code.

For values that shouldn't change, convention is `ALL_CAPS`:
`MAX_ATTEMPTS = 3`. Python doesn't actually stop you reassigning it —
there's no real `const` — the capitals are a signal to readers ("treat
this as fixed"), not an enforced rule.

### Reassignment

A variable can point to a new value at any time, even a different **type**
of value:

```python
x = 5
x = "now I'm text"   # totally legal, if a bit confusing to do on purpose
```

### Core built-in types

| Type | Example | Meaning |
|---|---|---|
| `int` | `42`, `-7` | whole numbers |
| `float` | `3.14`, `-0.5` | decimal numbers |
| `str` | `"hello"` | text |
| `bool` | `True`, `False` | yes/no, covered fully in [06](../06-booleans-and-comparisons/README.md) |
| `NoneType` | `None` | "no value" — Python's version of "nothing here" |

Python decides a value's type automatically from how you write it — you
never declare a type yourself (no `int x = 5` like some languages). This is
called **dynamic typing**. Use the built-in `type()` function to ask Python
what type something is:

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("hi")      # <class 'str'>
type(None)      # <class 'NoneType'>
```

`type(x).__name__` gives you just the name as a plain string (`"int"`)
instead of the full `<class 'int'>` display — handy when you want to
print or compare it.

### `None`

`None` is a special, singular value meaning "no value here." It's not the
same as `0`, `""`, or `False` — it's its own thing. Use `is` (not `==`) to
check for it: `value is None`. You'll see `is` again for exactly this kind
of identity check; everyday value comparisons (`5 == 5`) use `==`, covered
in module [06](../06-booleans-and-comparisons/README.md).

### Multiple assignment

Python lets you assign several variables in one line:

```python
a, b = 1, 2
print(a, b)   # 1 2
```

This also gives you a clean way to **swap** two variables without a
temporary holding variable (something most languages need one for):

```python
a, b = 1, 2
a, b = b, a
print(a, b)   # 2 1
```

### f-strings — combining variables into text

To build a string that includes variable values, prefix the string with
`f` and put variables in `{ }`:

```python
name = "Ava"
age = 30
print(f"{name} is {age} years old.")   # Ava is 30 years old.
```

This is called an **f-string** (formatted string literal) — you'll use it
constantly. Full string details are in module
[04](../04-strings/README.md); this is just enough to use it now.

## Common beginner mistakes

- Using `=` when you mean "check if equal" — that's `==`, covered in
  module 06. `if x = 5:` is a `SyntaxError` in Python (it won't even let
  you make this mistake, unlike some languages).
- Forgetting quotes: `x = hello` looks for a *variable* named `hello` and
  fails with `NameError: name 'hello' is not defined`. You wanted
  `x = "hello"`.
- Assuming a variable "remembers" its old type. `x = 5` then later
  `x = "5"` — `x` is now a string, and `x + 1` will raise a `TypeError`
  because you can't add a string and an int directly.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `type_name(value)` — return the name of `value`'s type as a string,
   e.g. `type_name(42) == "int"`.
2. `is_none(value)` — return `True` if `value` is `None`, `False`
   otherwise. Use `is`, not `==`.
3. `swap(a, b)` — return `(b, a)` using multiple assignment, no temporary
   variable.
4. `describe_person(name, age)` — return an f-string in the shape
   `"<name> is <age> years old."`.

Run it to check yourself:

```bash
python3 python-for-beginner/02-variables-and-data-types/exercise.py
```
