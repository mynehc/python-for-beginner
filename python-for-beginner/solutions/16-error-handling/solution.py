"""Reference solution for Exercise 16: Error Handling (try / except)."""


def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def safe_get_item(items, index):
    try:
        return items[index]
    except IndexError:
        return None


def safe_get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "not found"


def validate_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age


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
