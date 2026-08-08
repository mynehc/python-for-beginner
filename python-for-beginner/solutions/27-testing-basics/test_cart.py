"""Reference solution for Exercise 27: Testing Basics."""

import pytest

from cart import ShoppingCart


@pytest.fixture
def sample_cart():
    cart = ShoppingCart()
    cart.add("apple", 2)
    cart.add("banana", 1)
    return cart


def test_add_increases_total_items(sample_cart):
    before = sample_cart.total_items()
    sample_cart.add("kiwi")
    assert sample_cart.total_items() == before + 1


def test_remove_missing_item_raises():
    cart = ShoppingCart()
    with pytest.raises(KeyError):
        cart.remove("kiwi")


@pytest.mark.parametrize(
    "item,expected",
    [
        ("apple", True),
        ("banana", True),
        ("kiwi", False),
    ],
)
def test_contains(sample_cart, item, expected):
    assert (item in sample_cart) is expected
