"""Reference solution for Exercise 23: Decorators."""


def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
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
