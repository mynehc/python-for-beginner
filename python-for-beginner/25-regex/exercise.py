"""
Exercise 25: Regular Expressions

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""

import re


def contains_digit(text):
    """Return whether text contains at least one digit."""
    # TODO: implement
    raise NotImplementedError


def extract_numbers(text):
    """Return a list of every run of digits in text, as strings."""
    # TODO: implement
    raise NotImplementedError


def mask_digits(text):
    """Return text with every run of digits replaced by "#"."""
    # TODO: implement
    raise NotImplementedError


def is_valid_hex_color(text):
    """Return whether text is "#" followed by exactly 6 hex digits."""
    # TODO: implement (anchor with ^ and $)
    raise NotImplementedError


def extract_date_parts(text):
    """Find a YYYY-MM-DD date in text; return (year, month, day) strings, or None."""
    # TODO: implement using capture groups
    raise NotImplementedError


def _check():
    assert contains_digit("order #42") is True
    assert contains_digit("no numbers here") is False

    assert extract_numbers("a1 b22 c333") == ["1", "22", "333"]
    assert extract_numbers("no numbers") == []

    assert mask_digits("a1 b22 c333") == "a# b# c#"
    assert mask_digits("clean") == "clean"

    assert is_valid_hex_color("#1A2b3C") is True
    assert is_valid_hex_color("#ffffff") is True
    assert is_valid_hex_color("1A2b3C") is False
    assert is_valid_hex_color("#12") is False
    assert is_valid_hex_color("#1A2b3CZZ") is False

    assert extract_date_parts("Date: 2026-01-15 confirmed") == ("2026", "01", "15")
    assert extract_date_parts("no date here") is None

    print("All checks passed!")


if __name__ == "__main__":
    _check()
