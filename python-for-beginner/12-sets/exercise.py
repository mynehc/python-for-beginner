"""
Exercise 12: Sets

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def unique_items(items):
    """Return the set of unique items in the list."""
    # TODO: implement
    raise NotImplementedError


def common_elements(a, b):
    """Return the set of elements present in both list a and list b."""
    # TODO: implement using set intersection (&)
    raise NotImplementedError


def only_in_first(a, b):
    """Return the set of elements in list a that are NOT in list b."""
    # TODO: implement using set difference (-)
    raise NotImplementedError


def add_item(s, item):
    """Add item to set s (mutate it) and return s."""
    # TODO: implement
    raise NotImplementedError


def is_subset(a, b):
    """Return whether every element of set a is also in set b."""
    # TODO: implement
    raise NotImplementedError


def _check():
    assert unique_items([1, 2, 2, 3, 1]) == {1, 2, 3}
    assert unique_items([]) == set()

    assert common_elements([1, 2, 3], [2, 3, 4]) == {2, 3}
    assert common_elements([1, 2], [3, 4]) == set()

    assert only_in_first([1, 2, 3], [2, 3]) == {1}
    assert only_in_first([1, 2], [1, 2]) == set()

    s = {1, 2}
    result = add_item(s, 3)
    assert result == {1, 2, 3}
    assert s == {1, 2, 3}

    assert is_subset({1, 2}, {1, 2, 3}) is True
    assert is_subset({1, 4}, {1, 2, 3}) is False

    print("All checks passed!")


if __name__ == "__main__":
    _check()
