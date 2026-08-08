"""Reference solution for Exercise 22: Iterators & Generators."""


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


def even_numbers_up_to(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i


def first_two(iterable):
    it = iter(iterable)
    return next(it), next(it)


def squares_generator_expr(n):
    return (i ** 2 for i in range(n))


def _check():
    assert list(count_up_to(5)) == [1, 2, 3, 4, 5]
    assert list(count_up_to(1)) == [1]

    assert list(even_numbers_up_to(10)) == [2, 4, 6, 8, 10]
    assert list(even_numbers_up_to(1)) == []

    assert first_two([10, 20, 30]) == (10, 20)
    assert first_two("abcdef") == ("a", "b")
    assert first_two(count_up_to(5)) == (1, 2)

    gen = squares_generator_expr(5)
    assert list(gen) == [0, 1, 4, 9, 16]

    print("All checks passed!")


if __name__ == "__main__":
    _check()
