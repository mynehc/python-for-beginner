"""Reference solution for Exercise 15: Comprehensions."""


def squares_up_to(n):
    return [i ** 2 for i in range(1, n + 1)]


def evens_only(numbers):
    return [n for n in numbers if n % 2 == 0]


def upper_words(words):
    return [w.upper() for w in words]


def length_map(words):
    return {w: len(w) for w in words}


def unique_lengths(words):
    return {len(w) for w in words}


def _check():
    assert squares_up_to(4) == [1, 4, 9, 16]
    assert squares_up_to(1) == [1]

    assert evens_only([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert evens_only([1, 3, 5]) == []

    assert upper_words(["hi", "there"]) == ["HI", "THERE"]

    assert length_map(["hi", "hello", "hey"]) == {"hi": 2, "hello": 5, "hey": 3}

    assert unique_lengths(["hi", "hello", "hey", "yo"]) == {2, 5, 3}

    print("All checks passed!")


if __name__ == "__main__":
    _check()
