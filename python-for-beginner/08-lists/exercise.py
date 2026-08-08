"""
Exercise 08: Lists

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""


def first_and_last_items(items):
    """Return a tuple (first, last) of items, using indexing."""
    # TODO: implement
    raise NotImplementedError


def add_to_front(items, item):
    """Return a NEW list with item at the front. Don't modify the original items."""
    # TODO: implement
    raise NotImplementedError


def remove_item(items, target):
    """Remove the first occurrence of target from items (in place) and return items."""
    # TODO: implement
    raise NotImplementedError


def total_and_average(numbers):
    """Return a tuple (total, average) using sum() and len()."""
    # TODO: implement
    raise NotImplementedError


def sort_descending(numbers):
    """Return a NEW list of numbers sorted largest to smallest. Don't mutate the original."""
    # TODO: implement
    raise NotImplementedError


def _check():
    assert first_and_last_items([1, 2, 3, 4]) == (1, 4)
    assert first_and_last_items(["only"]) == ("only", "only")

    original = [1, 2, 3]
    result = add_to_front(original, 0)
    assert result == [0, 1, 2, 3]
    assert original == [1, 2, 3]  # original must be unchanged

    items = ["a", "b", "c", "b"]
    result = remove_item(items, "b")
    assert result == ["a", "c", "b"]
    assert items == ["a", "c", "b"]  # mutated in place

    assert total_and_average([1, 2, 3]) == (6, 2.0)
    assert total_and_average([10, 20]) == (30, 15.0)

    numbers = [3, 1, 4, 1, 5]
    result = sort_descending(numbers)
    assert result == [5, 4, 3, 1, 1]
    assert numbers == [3, 1, 4, 1, 5]  # original must be unchanged

    print("All checks passed!")


if __name__ == "__main__":
    _check()
