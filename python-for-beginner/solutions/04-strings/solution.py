"""Reference solution for Exercise 04: Strings."""


def first_and_last(word):
    return word[0], word[-1]


def reverse_string(word):
    return word[::-1]


def shout(sentence):
    return sentence.upper() + "!"


def clean_and_split(text):
    return text.strip().split()


def format_price(item, price):
    return f"{item}: ${price:.2f}"


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
