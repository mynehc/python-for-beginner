"""Reference solution for Exercise 09: Loops (for / while)."""


def sum_of_range(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def count_vowels(word):
    count = 0
    for char in word:
        if char in "aeiou":
            count += 1
    return count


def first_negative(numbers):
    for n in numbers:
        if n < 0:
            return n
    return None


def countdown(n):
    result = []
    while n >= 1:
        result.append(n)
        n -= 1
    return result


def skip_multiples_of_three(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            continue
        result.append(i)
    return result


def _check():
    assert sum_of_range(5) == 15
    assert sum_of_range(1) == 1
    assert sum_of_range(10) == 55

    assert count_vowels("hello world") == 3
    assert count_vowels("xyz") == 0
    assert count_vowels("aeiou") == 5

    assert first_negative([1, 2, -3, 4, -5]) == -3
    assert first_negative([1, 2, 3]) is None

    assert countdown(3) == [3, 2, 1]
    assert countdown(1) == [1]

    assert skip_multiples_of_three(9) == [1, 2, 4, 5, 7, 8]

    print("All checks passed!")


if __name__ == "__main__":
    _check()
