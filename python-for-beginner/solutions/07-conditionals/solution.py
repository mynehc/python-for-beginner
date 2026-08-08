"""Reference solution for Exercise 07: Conditionals (if / elif / else)."""


def classify_number(n):
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"


def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def describe_temperature(celsius):
    if celsius <= 0:
        return "freezing"
    elif celsius <= 15:
        return "cold"
    elif celsius <= 25:
        return "warm"
    else:
        return "hot"


def abs_value(n):
    return n if n >= 0 else -n


def _check():
    assert classify_number(-5) == "negative"
    assert classify_number(0) == "zero"
    assert classify_number(5) == "positive"

    assert letter_grade(95) == "A"
    assert letter_grade(82) == "B"
    assert letter_grade(71) == "C"
    assert letter_grade(65) == "D"
    assert letter_grade(40) == "F"

    assert largest_of_three(1, 2, 3) == 3
    assert largest_of_three(3, 2, 1) == 3
    assert largest_of_three(1, 3, 2) == 3
    assert largest_of_three(5, 5, 5) == 5

    assert describe_temperature(-5) == "freezing"
    assert describe_temperature(10) == "cold"
    assert describe_temperature(20) == "warm"
    assert describe_temperature(30) == "hot"

    assert abs_value(-5) == 5
    assert abs_value(5) == 5
    assert abs_value(0) == 0

    print("All checks passed!")


if __name__ == "__main__":
    _check()
