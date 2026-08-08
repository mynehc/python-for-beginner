"""Reference solution for Exercise 02: Variables & Data Types."""


def type_name(value):
    return type(value).__name__


def is_none(value):
    return value is None


def swap(a, b):
    return b, a


def describe_person(name, age):
    return f"{name} is {age} years old."


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
