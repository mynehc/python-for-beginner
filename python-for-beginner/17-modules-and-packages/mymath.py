"""
A tiny local module used by exercise.py to demonstrate importing your own
code, not just the standard library.
"""


def square(n):
    """Return n squared."""
    return n * n


def cube(n):
    """Return n cubed."""
    return n ** 3


def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0
