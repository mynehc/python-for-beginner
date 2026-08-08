"""
Exercise 19: OOP Basics (Classes & Objects)

Implement the BankAccount class below. Run this file directly to
self-check:
    python3 exercise.py
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        """Store owner and balance as instance attributes."""
        # TODO: implement
        raise NotImplementedError

    def deposit(self, amount):
        """Add amount to self.balance."""
        # TODO: implement
        raise NotImplementedError

    def withdraw(self, amount):
        """Subtract amount from self.balance; raise ValueError if amount > balance."""
        # TODO: implement
        raise NotImplementedError

    def get_balance(self):
        """Return the current balance."""
        # TODO: implement
        raise NotImplementedError


def _check():
    account = BankAccount("Ava", 100)
    assert account.owner == "Ava"
    assert account.get_balance() == 100

    account.deposit(50)
    assert account.get_balance() == 150

    account.withdraw(30)
    assert account.get_balance() == 120

    try:
        account.withdraw(1000)
        assert False, "expected ValueError"
    except ValueError as e:
        assert str(e) == "insufficient funds"
    assert account.get_balance() == 120  # unchanged after failed withdrawal

    # instances are independent
    other = BankAccount("Sam")  # default balance
    assert other.get_balance() == 0
    other.deposit(10)
    assert other.get_balance() == 10
    assert account.get_balance() == 120  # unaffected by `other`

    print("All checks passed!")


if __name__ == "__main__":
    _check()
