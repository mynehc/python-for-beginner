"""Reference solution for Exercise 01: Hello, World & Comments."""


def hello_world():
    return "Hello, World!"


def say_hello(name):
    # Concatenation: gluing strings together with +.
    return "Hello, " + name + "!"


def two_lines():
    return "First line\nSecond line"


def _check():
    assert hello_world() == "Hello, World!"

    assert say_hello("Ava") == "Hello, Ava!"
    assert say_hello("Sam") == "Hello, Sam!"

    assert two_lines() == "First line\nSecond line"
    assert two_lines().count("\n") == 1

    print("All checks passed!")


if __name__ == "__main__":
    _check()
