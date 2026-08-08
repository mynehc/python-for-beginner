"""Reference solution for Exercise 20: Inheritance & Dunder Methods."""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def __str__(self):
        return f"{self.name} the {type(self).__name__}"

    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


def _check():
    generic = Animal("Generic")
    assert generic.speak() == "..."
    assert str(generic) == "Generic the Animal"

    rex = Dog("Rex")
    assert isinstance(rex, Dog)
    assert isinstance(rex, Animal)
    assert rex.speak() == "Rex says Woof!"
    assert str(rex) == "Rex the Dog"

    whiskers = Cat("Whiskers")
    assert whiskers.speak() == "Whiskers says Meow!"
    assert str(whiskers) == "Whiskers the Cat"
    assert not isinstance(whiskers, Dog)

    assert rex == Dog("Rex")
    assert rex != Dog("Buddy")
    assert rex != Cat("Rex")

    print("All checks passed!")


if __name__ == "__main__":
    _check()
