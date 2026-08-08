"""
Exercise 15: Comprehensions

Implement each function below using a comprehension. Run this file
directly to self-check:
    python3 exercise.py
"""


def squares_up_to(n):
    """Return [1, 4, 9, ...] — squares of 1 through n inclusive."""
    # TODO: implement using a list comprehension
    raise NotImplementedError


def evens_only(numbers):
    """Return a list of just the even numbers from `numbers`, order preserved."""
    # TODO: implement using a list comprehension
    raise NotImplementedError


def upper_words(words):
    """Return a new list with every word in `words` uppercased."""
    # TODO: implement using a list comprehension
    raise NotImplementedError


def length_map(words):
    """Return a dict mapping each word in `words` to its length."""
    # TODO: implement using a dict comprehension
    raise NotImplementedError


def unique_lengths(words):
    """Return a set of the distinct word lengths present in `words`."""
    # TODO: implement using a set comprehension
    raise NotImplementedError


def _check():
    assert squares_up_to(4) == [1, 4, 9, 16]
    assert squares_up_to(1) == [1]

    assert evens_only([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert evens_only([1, 3, 5]) == []

    assert upper_words(["hi", "there"]) == ["HI", "THERE"]

    assert length_map(["hi", "hello", "hey"]) == {"hi": 2, "hello": 5, "hey": 3}

    assert unique_lengths(["hi", "hello", "hey", "yo"]) == {2, 5, 3}

    print("All checks passed!")


if __name__ == "__main__":
    _check()
