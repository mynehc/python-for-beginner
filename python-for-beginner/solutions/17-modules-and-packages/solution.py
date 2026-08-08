"""Reference solution for Exercise 17: Modules & Packages."""

import math
import random

import mymath


def circle_area(radius):
    return math.pi * radius ** 2


def square_root(n):
    return math.sqrt(n)


def random_in_range(low, high):
    return random.randint(low, high)


def square_and_cube(n):
    return mymath.square(n), mymath.cube(n)


def _check():
    assert round(circle_area(2), 2) == 12.57
    assert round(circle_area(1), 2) == 3.14

    assert square_root(16) == 4.0
    assert square_root(9) == 3.0

    for _ in range(20):
        n = random_in_range(1, 6)
        assert 1 <= n <= 6

    assert square_and_cube(3) == (9, 27)
    assert square_and_cube(2) == (4, 8)

    assert mymath.is_even(4) is True
    assert mymath.is_even(5) is False

    print("All checks passed!")


if __name__ == "__main__":
    _check()
