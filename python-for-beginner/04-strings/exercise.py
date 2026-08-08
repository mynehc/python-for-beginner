"""
Exercise 04: Strings

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def first_and_last(word):
    """Return a tuple (first_char, last_char) of word, using indexing."""
    # TODO: implement
    raise NotImplementedError


def reverse_string(word):
    """Return word reversed (hint: slicing with a step of -1)."""
    # TODO: implement
    raise NotImplementedError


def shout(sentence):
    """Return sentence in uppercase with "!" appended."""
    # TODO: implement
    raise NotImplementedError


def clean_and_split(text):
    """Strip whitespace from text, then split it into a list of words."""
    # TODO: implement
    raise NotImplementedError


def format_price(item, price):
    """Return "<item>: $<price to 2 decimal places>", e.g. "Coffee: $3.50"."""
    # TODO: implement
    raise NotImplementedError


def _check():
    assert first_and_last("Python") == ("P", "n")
    assert first_and_last("a") == ("a", "a")

    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("abc") == "cba"

    assert shout("hello") == "HELLO!"
    assert shout("already loud") == "ALREADY LOUD!"

    assert clean_and_split("  Hello, World!  ") == ["Hello,", "World!"]
    assert clean_and_split("  one two three  ") == ["one", "two", "three"]

    assert format_price("Coffee", 3.5) == "Coffee: $3.50"
    assert format_price("Book", 12) == "Book: $12.00"

    print("All checks passed!")


if __name__ == "__main__":
    _check()
