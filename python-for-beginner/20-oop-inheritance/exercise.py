"""
Exercise 20: Inheritance & Dunder Methods

Implement the methods marked TODO below. Run this file directly to
self-check:
    python3 exercise.py
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Generic default sound; Dog and Cat override this."""
        return "..."

    def __str__(self):
        """Return "<name> the <ClassName>", e.g. "Rex the Dog"."""
        # TODO: implement
        raise NotImplementedError

    def __eq__(self, other):
        """True if other is the exact same class as self AND has the same name."""
        # TODO: implement
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        """Return "<name> says Woof!"."""
        # TODO: implement
        raise NotImplementedError


class Cat(Animal):
    def speak(self):
        """Return "<name> says Meow!"."""
        # TODO: implement
        raise NotImplementedError


def _check():
    generic = Animal("Generic")
    assert generic.speak() == "..."
    assert str(generic) == "Generic the Animal"

    rex = Dog("Rex")
    assert isinstance(rex, Dog)
    assert isinstance(rex, Animal)  # inheritance: a Dog IS an Animal
    assert rex.speak() == "Rex says Woof!"
    assert str(rex) == "Rex the Dog"

    whiskers = Cat("Whiskers")
    assert whiskers.speak() == "Whiskers says Meow!"
    assert str(whiskers) == "Whiskers the Cat"
    assert not isinstance(whiskers, Dog)

    assert rex == Dog("Rex")
    assert rex != Dog("Buddy")
    assert rex != Cat("Rex")  # same name, different class -> not equal

    print("All checks passed!")


if __name__ == "__main__":
    _check()
