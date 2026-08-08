"""
Exercise 16: Error Handling (try / except)

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def safe_int(text):
    """Convert text to int; return None instead of raising ValueError on failure."""
    # TODO: implement
    raise NotImplementedError


def safe_divide(a, b):
    """Return a / b, or None if it raises ZeroDivisionError."""
    # TODO: implement
    raise NotImplementedError


def safe_get_item(items, index):
    """Return items[index], or None if it raises IndexError."""
    # TODO: implement
    raise NotImplementedError


def safe_get_value(d, key):
    """Return d[key], or "not found" if it raises KeyError."""
    # TODO: implement
    raise NotImplementedError


def validate_age(age):
    """Return age if age >= 0; otherwise raise ValueError("age cannot be negative")."""
    # TODO: implement
    raise NotImplementedError


def _check():
    assert safe_int("42") == 42
    assert safe_int("abc") is None

    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None

    assert safe_get_item([1, 2, 3], 1) == 2
    assert safe_get_item([1, 2, 3], 10) is None

    assert safe_get_value({"a": 1}, "a") == 1
    assert safe_get_value({"a": 1}, "z") == "not found"

    assert validate_age(25) == 25
    try:
        validate_age(-5)
        assert False, "expected ValueError"
    except ValueError as e:
        assert str(e) == "age cannot be negative"

    print("All checks passed!")


if __name__ == "__main__":
    _check()
