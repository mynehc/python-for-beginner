"""
Exercise 27: Testing Basics

Write the tests described in README.md against the ShoppingCart class in
cart.py. Run with:
    python3 -m pytest -v
"""

import pytest

from cart import ShoppingCart


# TODO: define a `sample_cart` fixture returning a ShoppingCart with
# 2 "apple" and 1 "banana" already added.


# TODO: def test_add_increases_total_items(sample_cart): ...


# TODO: def test_remove_missing_item_raises(): ...
#   hint: use `with pytest.raises(KeyError):`


# TODO: @pytest.mark.parametrize(...) test_contains covering at least 3 cases
