"""Reference solution for Exercise 21: Lambda & Functional Tools."""

from functools import reduce


def make_multiplier(n):
    return lambda x: x * n


def square_all(numbers):
    return list(map(lambda x: x ** 2, numbers))


def filter_evens(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def sort_by_length(words):
    return sorted(words, key=len)


def total_with_reduce(numbers):
    return reduce(lambda acc, x: acc + x, numbers, 0)


def _check():
    double = make_multiplier(2)
    assert double(5) == 10
    triple = make_multiplier(3)
    assert triple(5) == 15
    assert double(4) == 8

    assert square_all([1, 2, 3]) == [1, 4, 9]

    assert filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    assert sort_by_length(["banana", "kiwi", "fig"]) == ["fig", "kiwi", "banana"]

    assert total_with_reduce([1, 2, 3, 4]) == 10
    assert total_with_reduce([]) == 0

    print("All checks passed!")


if __name__ == "__main__":
    _check()
