"""Reference solution for Exercise 08: Lists."""


def first_and_last_items(items):
    return items[0], items[-1]


def add_to_front(items, item):
    return [item] + items


def remove_item(items, target):
    items.remove(target)
    return items


def total_and_average(numbers):
    total = sum(numbers)
    return total, total / len(numbers)


def sort_descending(numbers):
    return sorted(numbers, reverse=True)


def _check():
    assert first_and_last_items([1, 2, 3, 4]) == (1, 4)
    assert first_and_last_items(["only"]) == ("only", "only")

    original = [1, 2, 3]
    result = add_to_front(original, 0)
    assert result == [0, 1, 2, 3]
    assert original == [1, 2, 3]

    items = ["a", "b", "c", "b"]
    result = remove_item(items, "b")
    assert result == ["a", "c", "b"]
    assert items == ["a", "c", "b"]

    assert total_and_average([1, 2, 3]) == (6, 2.0)
    assert total_and_average([10, 20]) == (30, 15.0)

    numbers = [3, 1, 4, 1, 5]
    result = sort_descending(numbers)
    assert result == [5, 4, 3, 1, 1]
    assert numbers == [3, 1, 4, 1, 5]

    print("All checks passed!")


if __name__ == "__main__":
    _check()
