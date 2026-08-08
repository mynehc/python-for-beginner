"""Reference solution for Exercise 24: Standard Library Tour."""

import json
from collections import Counter
from datetime import datetime


def days_between(date1_text, date2_text):
    d1 = datetime.strptime(date1_text, "%Y-%m-%d")
    d2 = datetime.strptime(date2_text, "%Y-%m-%d")
    return abs((d2 - d1).days)


def format_pretty_date(year, month, day):
    return datetime(year, month, day).strftime("%B %d, %Y")


def to_json(data):
    return json.dumps(data)


def from_json(text):
    return json.loads(text)


def most_common_word(words):
    return Counter(words).most_common(1)[0][0]


def _check():
    assert days_between("2026-01-01", "2026-01-15") == 14
    assert days_between("2026-01-15", "2026-01-01") == 14

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
