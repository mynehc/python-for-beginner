"""Reference solution for Exercise 05: Input, Output & Type Conversion."""


def sum_from_text(a_text, b_text):
    return int(a_text) + int(b_text)


def average_from_text(a_text, b_text, c_text):
    return (float(a_text) + float(b_text) + float(c_text)) / 3


def parse_yes_no(text):
    return text.strip().lower() == "yes"


def format_line(label, value):
    return f"{label}: {value}"


def _check():
    assert sum_from_text("3", "4") == 7
    assert isinstance(sum_from_text("3", "4"), int)
    assert sum_from_text("-2", "5") == 3

    assert average_from_text("1", "2", "3") == 2.0
    assert isinstance(average_from_text("1", "2", "3"), float)
    assert average_from_text("10", "20", "30") == 20.0

    assert parse_yes_no("yes") is True
    assert parse_yes_no("Yes") is True
    assert parse_yes_no("  YES  ") is True
    assert parse_yes_no("no") is False
    assert parse_yes_no("No") is False

    assert format_line("Age", 25) == "Age: 25"
    assert format_line("Name", "Ava") == "Name: Ava"

    print("All checks passed!")


if __name__ == "__main__":
    _check()
