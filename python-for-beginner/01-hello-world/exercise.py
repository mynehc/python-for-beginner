"""
Exercise 01: Hello, World & Comments

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def hello_world():
    """Return the exact string "Hello, World!"."""
    return "Hello, World!"
    # TODO: implement
    raise NotImplementedError


def say_hello(name):
    """Return "Hello, <name>!" built using string concatenation (+)."""
    return "Hello, " + name + "!"
    # TODO: implement
    raise NotImplementedError


def two_lines():
    """Return one string that prints as two lines: "First line" then "Second line"."""
    return "First line\nSecond line"
    # TODO: implement
    raise NotImplementedError


def _check():
    assert hello_world() == "Hello, World!"

    assert say_hello("Ava") == "Hello, Ava!"
    assert say_hello("Sam") == "Hello, Sam!"

    assert two_lines() == "First line\nSecond line"
    assert two_lines().count("\n") == 1

    print("All checks passed!")


if __name__ == "__main__":
    _check()
