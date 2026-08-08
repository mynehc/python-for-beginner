"""Reference solution for Exercise 12: Sets."""


def unique_items(items):
    return set(items)


def common_elements(a, b):
    return set(a) & set(b)


def only_in_first(a, b):
    return set(a) - set(b)


def add_item(s, item):
    s.add(item)
    return s


def is_subset(a, b):
    return a <= b


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
