"""Reference solution for Exercise 03: Numbers & Operators."""


def average(a, b, c):
    return (a + b + c) / 3


def remainder(a, b):
    return a % b


def power(base, exponent):
    return base ** exponent


def floor_divide(a, b):
    return a // b


def round_to(number, digits):
    return round(number, digits)


def _check():
    assert average(1, 2, 3) == 2.0
    assert average(2, 2, 2) == 2.0
    assert isinstance(average(1, 2, 3), float)

    assert remainder(7, 2) == 1
    assert remainder(10, 5) == 0

    assert power(2, 3) == 8
    assert power(5, 0) == 1

    assert floor_divide(7, 2) == 3
    assert floor_divide(-7, 2) == -4

    assert round_to(3.14159, 2) == 3.14
    assert round_to(2.005, 1) == 2.0

    print("All checks passed!")


if __name__ == "__main__":
    _check()
