# 19 — OOP Basics (Classes & Objects)

## Concept

Everything so far has been either data (numbers, strings, lists, dicts)
or standalone functions that operate on that data separately. **Object-
oriented programming (OOP)** bundles data and the functions that work on
it together into one thing, called an **object**.

### Defining a class

A **class** is a blueprint for creating objects. An individual object
built from a class is called an **instance**.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
```

- `class Dog:` — starts the definition, `Dog` is the class name
  (convention: `CapWords`, unlike the `snake_case` used for variables
  and functions).
- `__init__` — a special method (Python calls these **dunder methods**,
  short for "double underscore," covered more in module
  [20](../20-oop-inheritance/README.md)) that runs automatically when you
  create a new instance. It's the **constructor** — where you set up the
  object's initial data.
- `self` — the instance itself. It's always the **first parameter** of
  every method, and Python passes it automatically — you never pass it
  explicitly when calling. Inside a method, `self.name` means "*this
  particular dog's* name."

### Creating instances

```python
rex = Dog("Rex", 3)
fido = Dog("Fido", 5)

rex.name    # "Rex"
fido.name   # "Fido"
rex.bark()  # "Rex says Woof!"
```

`Dog("Rex", 3)` calls `__init__` behind the scenes with `self` bound to
the new object, `name="Rex"`, `age=3`. Each instance has its **own**
independent copy of the attributes set in `__init__` — changing `rex.age`
doesn't touch `fido.age`.

```python
rex.age = 4
rex.age    # 4
fido.age   # 5 — unaffected, separate object
```

### Instance attributes vs. methods

- **Attributes** — data stored on the object (`self.name`, `self.age`).
  Accessed with `.` and no parentheses: `rex.name`.
- **Methods** — functions defined inside the class, called on an
  instance with `.` and parentheses: `rex.bark()`. Every method
  automatically receives `self` as its first parameter, referring to the
  instance it was called on.

### Class attributes (shared across all instances)

Attributes defined **inside the class but outside any method** belong to
the class itself, shared by every instance unless an instance overrides
its own copy:

```python
class Dog:
    species = "Canis familiaris"   # class attribute — same for every Dog

    def __init__(self, name):
        self.name = name            # instance attribute — unique per Dog

rex = Dog("Rex")
fido = Dog("Fido")
rex.species    # "Canis familiaris"
fido.species   # "Canis familiaris" — same value, shared
```

Use class attributes for things genuinely constant across every instance
(a species name, a default configuration value); use instance attributes
(set in `__init__`) for anything that varies per object — which is most
things.

### Methods that change state

A method can read and modify `self`'s attributes, which is most of what
makes OOP useful — grouping "the data" with "the operations that are
valid on that data" in one place:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount("Ava", 100)
account.deposit(50)
account.balance    # 150
```

### Objects don't compare equal by default

```python
Dog("Rex", 3) == Dog("Rex", 3)   # False!
```

By default, `==` checks whether two variables point to the **exact same
object** in memory (like `is`), not whether their contents look the
same. Teaching a class to compare by *content* requires defining a
special method (`__eq__`) — covered in module
[20](../20-oop-inheritance/README.md).

## Common beginner mistakes

- **Forgetting `self`** as the first parameter of every method —
  `TypeError: bark() takes 0 positional arguments but 1 was given` (the
  instance itself is the "1" being passed automatically, with no
  parameter to catch it).
- **Forgetting `self.` when reading/writing an attribute inside a
  method** — `name = name` inside a method creates/reads a plain local
  variable, not the instance's attribute; you need `self.name = name`.
- **Confusing the class with an instance.** `Dog` is the blueprint;
  `rex = Dog("Rex", 3)` is an actual dog. `Dog.bark()` (calling on the
  class itself, no instance) fails — methods need an instance to operate
  on (or need to be explicitly declared not to, which is beyond this
  module).

## Exercise

Open [`exercise.py`](exercise.py) — it has a `BankAccount` class skeleton.
Implement:

1. `__init__(self, owner, balance=0)` — store `owner` and `balance` as
   instance attributes.
2. `deposit(self, amount)` — add `amount` to `self.balance`.
3. `withdraw(self, amount)` — subtract `amount` from `self.balance`, but
   `raise ValueError("insufficient funds")` first if `amount` is greater
   than the current balance (don't change the balance in that case).
4. `get_balance(self)` — return the current balance.

Run it to check yourself:

```bash
python3 python-for-beginner/19-oop-basics/exercise.py
```
