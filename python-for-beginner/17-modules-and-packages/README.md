# 17 — Modules & Packages

## Concept

A **module** is just a `.py` file. A **package** is a folder of modules
(with a bit of extra setup, below). So far every exercise has been a
single file — real programs are usually split across many, and `import`
is how one file uses code from another.

### Importing from the standard library

Python ships with a huge collection of built-in modules — the **standard
library** — ready to use with no installation. You've been using pieces
of it indirectly; now you `import` it explicitly:

```python
import math

math.pi          # 3.141592653589793
math.sqrt(16)    # 4.0
math.floor(3.7)  # 3
```

`math.pi` — read the dot as "look inside the `math` module for something
named `pi`." Same pattern as `d.get(...)` from module 11: dot access into
something that holds multiple things.

### `from ... import ...`

Pull specific names out of a module so you can use them directly, without
the module prefix:

```python
from math import pi, sqrt

pi          # 3.141592653589793 — no "math." needed now
sqrt(16)    # 4.0
```

Trade-off: `import math` then `math.sqrt(...)` is more typing but always
clear where `sqrt` came from; `from math import sqrt` is shorter but can
cause name clashes if two modules both define something called `sqrt`.
Either is fine — `import module_name` (and using the prefix) is the
safer default for beginners; reach for `from ... import ...` once you're
sure there's no ambiguity.

### Aliasing with `as`

```python
import random as rnd
rnd.randint(1, 6)
```

Common for long names — you'll see `import numpy as np` and
`import pandas as pd` constantly if you ever do data work in Python;
those aren't standard library, but the `as` syntax is the same.

### `random` — a taste

```python
import random

random.randint(1, 6)         # a random int, 1 through 6 INCLUSIVE (unlike range())
random.choice(["a", "b", "c"]) # a random element from a list
random.shuffle(my_list)       # shuffles my_list IN PLACE (mutates it, returns None)
```

`random.randint(a, b)` includes both endpoints — different from
`range()`, which excludes its stop value. Worth double-checking against
the docs whenever you're unsure about a boundary.

There's a much fuller tour of useful standard library modules in module
[24](../24-stdlib-tour/README.md); this module is about the `import`
mechanics themselves.

### Writing and importing your own module

Any `.py` file can be imported by another file **in the same folder**,
using its filename without `.py`:

```python
# mymath.py
def square(n):
    return n * n
```

```python
# exercise.py, same folder
import mymath

mymath.square(4)   # 16
```

This course's [`mymath.py`](mymath.py) (sitting right next to this
README) is exactly this pattern — open it, it's short.

### The `if __name__ == "__main__":` guard, revisited

You first saw this in [00-setup](../00-setup/README.md). Now that you can
import files into each other, here's why it matters: when Python
**imports** a module, it runs the whole file top to bottom — including
any bare `print()` calls or other code sitting outside a function.
Wrapping "only run this when the file is executed directly" code in that
guard prevents it from firing just because someone else imported your
file:

```python
def main():
    print("Running as a script")

if __name__ == "__main__":
    main()
```

`__name__` is a special variable Python sets automatically: it's
`"__main__"` when the file is run directly, but the module's own name
(e.g. `"mymath"`) when it's imported by something else. Every
`exercise.py` in this course uses this guard around its `_check()` call,
which is exactly why importing `mymath` at the top of this module's
exercise doesn't also run mymath's own code (it has none outside
functions, but the principle is the same).

### Packages (the short version)

A **package** is a folder containing an `__init__.py` file (which can be
empty) plus other modules — it lets you group related modules under one
importable name, e.g. `import mypackage.utils`. You won't need to build
one for this course, but recognize the shape if you see it in a real
project's folder structure: a folder with `__init__.py` in it is a
package, not just a folder.

### Third-party packages (preview)

`math` and `random` ship with Python. Most real projects also use
packages that **don't** ship with Python and need installing first (like
`requests` for making web calls) — that's what `pip` and virtual
environments (module [26](../26-virtual-envs-and-pip/README.md)) are for.
Nothing in this module needs installing anything.

## Common beginner mistakes

- **`ModuleNotFoundError: No module named 'mymath'`** — when you run a
  file directly (`python3 exercise.py`), Python automatically looks for
  same-folder imports next to *that file*, regardless of which directory
  you ran the command from, so this specific exercise should just work.
  This error shows up later once you start importing across folders in a
  larger, multi-file project without proper package setup — the fix
  there is usually running things as a package (`python3 -m folder.file`)
  instead of a bare script path.
- **Circular imports** — module A imports module B, and module B imports
  module A. Causes confusing errors. Not something you'll likely hit yet,
  but the fix, when you do, is usually restructuring so the shared code
  lives in a third module both import.
- **Shadowing a standard library name.** Naming your own file `random.py`
  in a folder where you also `import random` will import *your* file
  instead of the real standard library module — avoid naming your files
  after standard library modules.

## Exercise

Open [`exercise.py`](exercise.py) and implement (it already has
`import math`, `import random`, and `import mymath` at the top — use
them):

1. `circle_area(radius)` — return the area of a circle
   (`math.pi * radius ** 2`).
2. `square_root(n)` — return the square root of `n` using `math.sqrt`.
3. `random_in_range(low, high)` — return a random integer between `low`
   and `high`, inclusive, using `random.randint`.
4. `square_and_cube(n)` — return a tuple `(n squared, n cubed)`, using
   `mymath.square` and `mymath.cube` from the local `mymath` module.

Run it to check yourself:

```bash
python3 python-for-beginner/17-modules-and-packages/exercise.py
```
