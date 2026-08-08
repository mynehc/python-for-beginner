# 20 — Inheritance & Dunder Methods

## Concept

### Inheritance

**Inheritance** lets a class reuse and extend another class's behavior,
modeling an "is-a" relationship: a `Dog` **is an** `Animal`, a `Cat`
**is an** `Animal`.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."   # generic default, subclasses will override this

class Dog(Animal):          # Dog inherits from Animal
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

`class Dog(Animal):` — the parenthesized name is the **parent class**
(also called the **base class** or **superclass**). `Dog` automatically
gets everything `Animal` has (like `__init__`, and therefore
`self.name`), and can **override** any method by defining one with the
same name — that's what `speak` does here.

```python
rex = Dog("Rex")
rex.name      # "Rex" — inherited from Animal's __init__, Dog didn't need its own
rex.speak()   # "Rex says Woof!" — Dog's own version, not Animal's
```

### `isinstance()` respects inheritance

```python
isinstance(rex, Dog)      # True
isinstance(rex, Animal)   # True — rex IS an Animal too, through inheritance
isinstance(rex, Cat)      # False
```

This is why `isinstance()` (not `type(x) ==`) is the right way to check
"is this a kind of X" — it correctly accounts for subclasses.

### Extending `__init__` with `super()`

If a subclass needs its **own** extra attributes, on top of what the
parent already sets up, call the parent's `__init__` explicitly with
`super().__init__(...)` instead of duplicating its logic:

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # let Animal.__init__ handle `name`
        self.breed = breed        # Dog adds its own attribute

rex = Dog("Rex", "Labrador")
rex.name    # "Rex"       — set by Animal.__init__
rex.breed   # "Labrador"  — set by Dog.__init__
```

`super()` gives you access to the parent class from inside the child, so
you extend behavior instead of copy-pasting it.

## Dunder methods

"Dunder" = **d**ouble **under**score — methods named like `__init__`,
`__str__`, `__eq__`. You've used `__init__` since module 19; these are
the same idea: Python calls them automatically at specific moments, and
implementing one lets your objects hook into built-in language behavior.

### `__str__` — how an object prints

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} the {type(self).__name__}"

rex = Dog("Rex")
print(rex)        # Rex the Dog       — uses __str__ automatically
str(rex)           # "Rex the Dog"
```

Without `__str__`, `print(rex)` would show something unhelpful like
`<__main__.Dog object at 0x1044b2a10>` — the default, memory-address-based
description every object gets unless you customize it.

`type(self).__name__` gives the **actual** class name of the instance
(`"Dog"` for a `Dog`, `"Cat"` for a `Cat`) even though this code is
written once, in the shared parent — because `self` is always the real
instance, not the class the method happens to be defined on.

### `__eq__` — how `==` compares your objects

Recall from module 19: objects don't compare equal by content by
default. `__eq__` fixes that:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name

Dog("Rex") == Dog("Rex")   # True now — same class, same name
Dog("Rex") == Cat("Rex")   # False — different class
```

### Other common dunders (good to recognize, not required here)

| Dunder | Hooks into |
|---|---|
| `__repr__` | the developer-facing representation, shown in the REPL / inside a list |
| `__len__` | `len(obj)` |
| `__lt__` | `obj1 < obj2` |
| `__getitem__` | `obj[index]` |

You'll meet more of these if you continue past this course — they're how
Python lets custom classes behave like built-in types.

## Common beginner mistakes

- **Forgetting `super().__init__(...)`** when a subclass defines its own
  `__init__` — the parent's setup (like `self.name = name`) never runs,
  and accessing `self.name` later raises `AttributeError`.
- **Confusing `__str__` with `return` inside a normal method.** `__str__`
  must return a `str` — Python calls it for you on `print()`/`str()`;
  you never call `obj.__str__()` directly in normal code.
- **Comparing with `==` before defining `__eq__`** and being surprised
  it's `False` for "obviously equal" objects — covered in module 19,
  worth repeating since it comes up again here.

## Exercise

Open [`exercise.py`](exercise.py) — it has an `Animal` base class and
`Dog`/`Cat` subclasses. Implement:

1. `Animal.__str__(self)` — return `"<name> the <ClassName>"`, e.g.
   `"Rex the Dog"`. Use `type(self).__name__` for the class name.
2. `Animal.__eq__(self, other)` — return `True` if `other` is the exact
   same class as `self` **and** has the same `name`.
3. `Dog.speak(self)` — return `"<name> says Woof!"`.
4. `Cat.speak(self)` — return `"<name> says Meow!"`.

Run it to check yourself:

```bash
python3 python-for-beginner/20-oop-inheritance/exercise.py
```
