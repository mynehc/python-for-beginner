"""
Exercise 24: Standard Library Tour

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""

import json
from collections import Counter
from datetime import datetime


def days_between(date1_text, date2_text):
    """Parse two "YYYY-MM-DD" strings and return the absolute number of days between them."""
    # TODO: implement using datetime.strptime
    raise NotImplementedError


def format_pretty_date(year, month, day):
    """Return the date formatted as "Month DD, YYYY", e.g. "January 05, 2026"."""
    # TODO: implement using datetime(...).strftime
    raise NotImplementedError


def to_json(data):
    """Return `data` serialized as a JSON string."""
    # TODO: implement using json.dumps
    raise NotImplementedError


def from_json(text):
    """Return the Python value parsed from the JSON string `text`."""
    # TODO: implement using json.loads
    raise NotImplementedError


def most_common_word(words):
    """Return the single most common word in the list `words`."""
    # TODO: implement using collections.Counter
    raise NotImplementedError


def _check():
    assert days_between("2026-01-01", "2026-01-15") == 14
    assert days_between("2026-01-15", "2026-01-01") == 14  # order-independent

    assert format_pretty_date(2026, 1, 5) == "January 05, 2026"
    assert format_pretty_date(2026, 12, 25) == "December 25, 2026"

    assert to_json({"a": 1}) == '{"a": 1}'
    assert to_json([1, 2, 3]) == "[1, 2, 3]"

    assert from_json('{"a": 1}') == {"a": 1}
    assert from_json("[1, 2, 3]") == [1, 2, 3]

    assert most_common_word(["a", "b", "a", "c", "b", "a"]) == "a"

    print("All checks passed!")


if __name__ == "__main__":
    _check()
