"""
Exercise 07: Conditionals (if / elif / else)

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def classify_number(n):
    """Return "negative", "zero", or "positive" depending on n."""
    # TODO: implement
    raise NotImplementedError


def letter_grade(score):
    """Return a letter grade: 90+ A, 80-89 B, 70-79 C, 60-69 D, below 60 F."""
    # TODO: implement
    raise NotImplementedError


def largest_of_three(a, b, c):
    """Return the largest of a, b, c using if/elif/else (not max())."""
    # TODO: implement
    raise NotImplementedError


def describe_temperature(celsius):
    """Return "freezing" (<=0), "cold" (<=15), "warm" (<=25), else "hot"."""
    # TODO: implement
    raise NotImplementedError


def abs_value(n):
    """Return the absolute value of n using a one-line conditional expression."""
    # TODO: implement
    raise NotImplementedError


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
