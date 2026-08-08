"""Reference solution for Exercise 25: Regular Expressions."""

import re


def contains_digit(text):
    return re.search(r"\d", text) is not None


def extract_numbers(text):
    return re.findall(r"\d+", text)


def mask_digits(text):
    return re.sub(r"\d+", "#", text)


def is_valid_hex_color(text):
    return re.match(r"^#[0-9a-fA-F]{6}$", text) is not None


def extract_date_parts(text):
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
    if match is None:
        return None
    return match.group(1), match.group(2), match.group(3)


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
