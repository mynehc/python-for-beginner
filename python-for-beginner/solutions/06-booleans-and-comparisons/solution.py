"""Reference solution for Exercise 06: Booleans & Comparisons."""


def is_falsy(value):
    return not value


def in_range(n, low, high):
    return low <= n <= high


def both_positive(a, b):
    return a > 0 and b > 0


def at_least_one_true(a, b, c):
    return a or b or c


def flip(value):
    return not value


def _check():
    assert is_falsy(0) is True
    assert is_falsy("") is True
    assert is_falsy([]) is True
    assert is_falsy(None) is True
    assert is_falsy(False) is True
    assert is_falsy(1) is False
    assert is_falsy("a") is False
    assert is_falsy([0]) is False

    assert in_range(5, 1, 10) is True
    assert in_range(1, 1, 10) is True
    assert in_range(10, 1, 10) is True
    assert in_range(11, 1, 10) is False
    assert in_range(0, 1, 10) is False

    assert both_positive(1, 2) is True
    assert both_positive(-1, 2) is False
    assert both_positive(0, 2) is False

    assert at_least_one_true(False, False, True) is True
    assert at_least_one_true(False, False, False) is False
    assert at_least_one_true(True, True, True) is True

    assert flip(True) is False
    assert flip(False) is True

    print("All checks passed!")


if __name__ == "__main__":
    _check()
