"""Reference solution for Exercise 19: OOP Basics (Classes & Objects)."""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance


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
    assert account.get_balance() == 120

    other = BankAccount("Sam")
    assert other.get_balance() == 0
    other.deposit(10)
    assert other.get_balance() == 10
    assert account.get_balance() == 120

    print("All checks passed!")


if __name__ == "__main__":
    _check()
