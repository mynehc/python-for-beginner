"""Reference solution for Exercise 14: Scope & Recursion."""

counter = 0


def increment_counter():
    global counter
    counter += 1


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])


def _check():
    global counter
    counter = 0
    increment_counter()
    increment_counter()
    increment_counter()
    assert counter == 3

    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(6) == 8

    assert sum_recursive([]) == 0
    assert sum_recursive([5]) == 5
    assert sum_recursive([1, 2, 3, 4]) == 10

    print("All checks passed!")


if __name__ == "__main__":
    _check()
