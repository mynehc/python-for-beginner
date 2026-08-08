"""Reference solution for Exercise 10: Tuples."""


def make_point(x, y):
    return (x, y)


def sum_point(point):
    x, y = point
    return x + y


def first_two(t):
    return (t[0], t[1])


def count_occurrences(t, value):
    return t.count(value)


def combine(a, b):
    return a + b


def _check():
    assert make_point(3, 4) == (3, 4)

    assert sum_point((3, 4)) == 7
    assert sum_point((0, 0)) == 0

    assert first_two((1, 2, 3, 4)) == (1, 2)
    assert first_two(("a", "b")) == ("a", "b")

    assert count_occurrences((1, 2, 2, 3, 2), 2) == 3
    assert count_occurrences((1, 2, 3), 9) == 0

    assert combine((1, 2), (3, 4)) == (1, 2, 3, 4)
    assert combine((), (1,)) == (1,)

    print("All checks passed!")


if __name__ == "__main__":
    _check()
