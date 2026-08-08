"""
Exercise 03: Numbers & Operators

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def average(a, b, c):
    """Return the average of three numbers as a float."""
    # TODO: implement
    raise NotImplementedError


def remainder(a, b):
    """Return a modulo b (the remainder of a / b)."""
    # TODO: implement
    raise NotImplementedError


def power(base, exponent):
    """Return base raised to exponent."""
    # TODO: implement
    raise NotImplementedError


def floor_divide(a, b):
    """Return the floored (rounded down) integer division of a by b."""
    # TODO: implement
    raise NotImplementedError


def round_to(number, digits):
    """Return number rounded to `digits` decimal places."""
    # TODO: implement
    raise NotImplementedError


def _check():
    assert average(1, 2, 3) == 2.0
    assert average(2, 2, 2) == 2.0
    assert isinstance(average(1, 2, 3), float)

    assert remainder(7, 2) == 1
    assert remainder(10, 5) == 0

    assert power(2, 3) == 8
    assert power(5, 0) == 1

    assert floor_divide(7, 2) == 3
    assert floor_divide(-7, 2) == -4

    assert round_to(3.14159, 2) == 3.14
    assert round_to(2.005, 1) == 2.0

    print("All checks passed!")


if __name__ == "__main__":
    _check()
