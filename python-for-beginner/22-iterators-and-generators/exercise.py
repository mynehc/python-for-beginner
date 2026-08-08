"""
Exercise 22: Iterators & Generators

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def count_up_to(n):
    """Generator function: yield 1, 2, ..., n in order."""
    # TODO: implement (use yield, not return). Delete the two lines below
    # once you do -- they only exist so this stays a generator function
    # (the mere presence of `yield` in a function makes it one) until you
    # write your own yield statement(s).
    raise NotImplementedError
    yield


def even_numbers_up_to(n):
    """Generator function: yield only the even numbers from 1 to n inclusive."""
    # TODO: implement (use yield, not return). Same note as above.
    raise NotImplementedError
    yield


def first_two(iterable):
    """Return a tuple of the first two items of `iterable`, using iter()/next()."""
    # TODO: implement
    raise NotImplementedError


def squares_generator_expr(n):
    """Return a generator expression computing the squares of 0 through n - 1."""
    # TODO: implement
    raise NotImplementedError


def _check():
    assert list(count_up_to(5)) == [1, 2, 3, 4, 5]
    assert list(count_up_to(1)) == [1]

    assert list(even_numbers_up_to(10)) == [2, 4, 6, 8, 10]
    assert list(even_numbers_up_to(1)) == []

    assert first_two([10, 20, 30]) == (10, 20)
    assert first_two("abcdef") == ("a", "b")
    assert first_two(count_up_to(5)) == (1, 2)  # works on a generator too, not just a list

    gen = squares_generator_expr(5)
    assert list(gen) == [0, 1, 4, 9, 16]

    print("All checks passed!")


if __name__ == "__main__":
    _check()
