"""Reference solution for Exercise 13: Functions."""


def power(base, exponent=2):
    return base ** exponent


def full_name(first, last, middle=None):
    if middle is None:
        return f"{first} {last}"
    return f"{first} {middle} {last}"


def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def build_profile(**details):
    return details


def safe_divide(a, b):
    if b == 0:
        return None
    return a / b


def _check():
    assert power(3) == 9
    assert power(2, 3) == 8
    assert power(base=5, exponent=0) == 1

    assert full_name("Ava", "Lee") == "Ava Lee"
    assert full_name("Ava", "Lee", "Marie") == "Ava Marie Lee"

    assert sum_all(1, 2, 3) == 6
    assert sum_all() == 0
    assert sum_all(5) == 5

    assert build_profile(name="Ava", age=30) == {"name": "Ava", "age": 30}
    assert build_profile() == {}

    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None

    print("All checks passed!")


if __name__ == "__main__":
    _check()
