"""
Exercise 23: Decorators

Implement the two decorators below, then apply them (already done, at
the bottom) to `shout` and `greet`. Run this file directly to self-check:
    python3 exercise.py
"""


def uppercase_result(func):
    """Decorator: call func(*args, **kwargs), return its result uppercased."""
    def wrapper(*args, **kwargs):
        # TODO: implement
        raise NotImplementedError
    return wrapper


def count_calls(func):
    """Decorator: track how many times the wrapped function has been called
    on a `.calls` attribute of the wrapper, starting at 0."""
    def wrapper(*args, **kwargs):
        # TODO: implement
        raise NotImplementedError
    wrapper.calls = 0
    return wrapper


@uppercase_result
def shout(text):
    return text + "!"


@count_calls
def greet(name):
    return f"Hi, {name}"


def _check():
    assert shout("hello") == "HELLO!"
    assert shout("already loud") == "ALREADY LOUD!"

    assert greet.calls == 0
    assert greet("Ava") == "Hi, Ava"
    assert greet.calls == 1
    assert greet("Sam") == "Hi, Sam"
    assert greet.calls == 2

    print("All checks passed!")


if __name__ == "__main__":
    _check()
