"""
Exercise 14: Scope & Recursion

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""

counter = 0  # module-level global used by increment_counter()


def increment_counter():
    """Increment the global `counter` by 1, using the `global` keyword."""
    # TODO: implement
    raise NotImplementedError


def factorial(n):
    """Return n! recursively. factorial(0) == factorial(1) == 1 (base case)."""
    # TODO: implement
    raise NotImplementedError


def fibonacci(n):
    """Return the nth Fibonacci number recursively (fibonacci(0) == 0, fibonacci(1) == 1)."""
    # TODO: implement
    raise NotImplementedError


def sum_recursive(numbers):
    """Return the sum of numbers, recursively (no sum(), no loop)."""
    # TODO: implement
    raise NotImplementedError


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
