# 27 — Testing Basics

## Concept

Every `exercise.py` in this course has ended with a `_check()` function
full of `assert` statements — that's already been testing, informally.
This module formalizes it with **pytest**, the most widely used Python
testing tool, and shifts the exercise itself: instead of implementing
code and having tests already written for you, this time **you write the
tests**, against code that's already implemented.

### Why bother with a real test framework?

Manually running a script and eyeballing the output doesn't scale once a
project has more than a few functions — you'd have to remember to
re-check everything by hand after every change. A test suite runs every
check automatically, tells you exactly which one failed and why, and can
be re-run in seconds any time you touch the code.

### Installing pytest

pytest isn't part of the standard library — it needs installing, which
is exactly what module [26](../26-virtual-envs-and-pip/README.md) was
for:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

(If you're working through this course inside a repo that already has a
`.venv` with pytest installed, just activate it: `source .venv/bin/activate`.)

### Writing a test

- Test files are named `test_*.py`.
- Test functions are named `test_*`.
- A test **passes** if it runs without raising anything; it **fails** if
  an `assert` inside it is `False` (or any other exception happens).

```python
# my_math.py
def square(n):
    return n * n
```

```python
# test_my_math.py
from my_math import square

def test_square_of_positive_number():
    assert square(4) == 16

def test_square_of_negative_number():
    assert square(-3) == 9
```

Run with:

```bash
python3 -m pytest -v
```

`-v` (verbose) lists every test by name with PASS/FAIL, instead of just a
summary count. pytest automatically discovers every `test_*.py` file and
every `test_*` function inside it — no manual registration needed.

### Why pytest's `assert` is nicer than what you've been doing

pytest rewrites plain `assert` statements at test-collection time to
show you a detailed failure diff — `assert result == expected` on
failure shows you *both* values and where they differ, not just a bare
`AssertionError`. This is why pytest tests use plain `assert` rather than
special methods like `assertEqual(...)` that some older frameworks
require.

### Fixtures — reusable setup

A **fixture** is a function decorated with `@pytest.fixture` that
provides ready-made data or objects to your tests. Any test function
that takes a parameter with the same name as a fixture automatically
receives what that fixture returns:

```python
import pytest

@pytest.fixture
def empty_cart():
    return ShoppingCart()

def test_new_cart_has_zero_items(empty_cart):
    assert empty_cart.total_items() == 0
```

pytest sees the `empty_cart` parameter, matches it to the fixture of the
same name, calls the fixture, and passes the result in — this is called
**dependency injection**, and it means shared setup lives in one place
instead of being copy-pasted into every test.

### Testing that an error is raised

```python
import pytest

def test_dividing_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

`with pytest.raises(SomeError):` asserts that the indented block raises
`SomeError` — the test **fails** if the block does *not* raise it. This
is how you test the error-handling code you wrote in module 16.

### Running the same test against multiple inputs

```python
import pytest

@pytest.mark.parametrize("n,expected", [(2, 4), (3, 9), (0, 0), (-3, 9)])
def test_square(n, expected):
    assert square(n) == expected
```

`@pytest.mark.parametrize("names", [values])` runs the test body once per
tuple in the list — 4 test cases from one function body here, each shown
individually in `-v` output, instead of 4 near-duplicate test functions.

## Common beginner mistakes

- **Naming the file or function wrong.** pytest only auto-discovers
  `test_*.py` files and `test_*` functions — `check_square.py` or
  `def testing_square():` (missing the underscore) won't be found or
  run.
- **Forgetting `with` before `pytest.raises(...)`** — it's a context
  manager (module 18 introduced the concept with `with open(...)`), used
  the same way here.
- **Testing implementation details instead of behavior.** A good test
  checks *what a function returns/does* for given inputs, not *how* it's
  written internally — that way your tests keep passing even if you
  later rewrite the function's internals without changing its behavior.

## Exercise

There's a small, already-implemented `ShoppingCart` class in
[`cart.py`](cart.py) (this module is about *writing tests*, not
implementing the thing under test).

In [`test_cart.py`](test_cart.py), write:

1. A fixture `sample_cart()` returning a `ShoppingCart` that already has
   2 `"apple"` and 1 `"banana"` added to it.
2. `test_add_increases_total_items(sample_cart)` — asserts that calling
   `.add("kiwi")` on `sample_cart` increases `.total_items()` by exactly
   1.
3. `test_remove_missing_item_raises()` — asserts that calling
   `.remove("kiwi")` on a **new, empty** `ShoppingCart()` raises
   `KeyError`.
4. A parametrized `test_contains(...)` covering at least 3 cases of
   checking whether an item is `in` `sample_cart` (both items that were
   added, and at least one that wasn't).

Run it with:

```bash
cd python-for-beginner/27-testing-basics && python3 -m pytest -v
```
