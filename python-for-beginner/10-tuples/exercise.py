"""
Exercise 10: Tuples

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def make_point(x, y):
    """Return the tuple (x, y)."""
    # TODO: implement
    raise NotImplementedError


def sum_point(point):
    """point is an (x, y) tuple. Unpack it and return x + y."""
    # TODO: implement
    raise NotImplementedError


def first_two(t):
    """Return a tuple of the first two elements of t, using indexing."""
    # TODO: implement
    raise NotImplementedError


def count_occurrences(t, value):
    """Return how many times value appears in tuple t."""
    # TODO: implement
    raise NotImplementedError


def combine(a, b):
    """Return the concatenation of tuples a and b."""
    # TODO: implement
    raise NotImplementedError


def _check():
    assert make_point(3, 4) == (3, 4)

    assert sum_point((3, 4)) == 7
    assert sum_point((0, 0)) == 0

    assert first_two((1, 2, 3, 4)) == (1, 2)
    assert first_two(("a", "b")) == ("a", "b")

    assert count_occurrences((1, 2, 2, 3, 2), 2) == 3
    assert count_occurrences((1, 2, 3), 9) == 0

    assert combine((1, 2), (3, 4)) == (1, 2, 3, 4)
    assert combine((), (1,)) == (1,)

    print("All checks passed!")


if __name__ == "__main__":
    _check()
