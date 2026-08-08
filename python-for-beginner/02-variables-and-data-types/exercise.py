"""
Exercise 02: Variables & Data Types

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def type_name(value):
    """Return the name of value's type as a string, e.g. type_name(1) == "int"."""
    # TODO: implement
    raise NotImplementedError


def is_none(value):
    """Return True if value is None, False otherwise. Use `is`, not `==`."""
    # TODO: implement
    raise NotImplementedError


def swap(a, b):
    """Return (b, a) using multiple assignment, not a temp variable."""
    # TODO: implement
    raise NotImplementedError


def describe_person(name, age):
    """Return an f-string: "<name> is <age> years old."."""
    # TODO: implement
    raise NotImplementedError


def _check():
    assert type_name(1) == "int"
    assert type_name(1.5) == "float"
    assert type_name("hi") == "str"
    assert type_name(None) == "NoneType"
    assert type_name(True) == "bool"

    assert is_none(None) is True
    assert is_none(0) is False
    assert is_none("") is False

    assert swap(1, 2) == (2, 1)
    assert swap("a", "b") == ("b", "a")

    assert describe_person("Ava", 30) == "Ava is 30 years old."
    assert describe_person("Sam", 8) == "Sam is 8 years old."

    print("All checks passed!")


if __name__ == "__main__":
    _check()
