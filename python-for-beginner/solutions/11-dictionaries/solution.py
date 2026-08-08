"""Reference solution for Exercise 11: Dictionaries."""


def get_or_default(d, key, default):
    return d.get(key, default)


def add_or_update(d, key, value):
    d[key] = value
    return d


def word_counts(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def merge_with_overrides(defaults, overrides):
    return {**defaults, **overrides}


def invert(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted


def _check():
    assert get_or_default({"a": 1}, "a", 0) == 1
    assert get_or_default({"a": 1}, "b", 0) == 0

    d = {"a": 1}
    result = add_or_update(d, "b", 2)
    assert result == {"a": 1, "b": 2}
    assert d == {"a": 1, "b": 2}

    assert word_counts(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}
    assert word_counts([]) == {}

    assert merge_with_overrides({"a": 1, "b": 2}, {"b": 20}) == {"a": 1, "b": 20}
    assert merge_with_overrides({"a": 1}, {}) == {"a": 1}

    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}

    print("All checks passed!")


if __name__ == "__main__":
    _check()
