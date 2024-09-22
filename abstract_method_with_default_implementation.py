"""Abstract methods can have default implementations that can be overridden by subclasses. This allows for flexibility in how methods are implemented."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    pass  # Uses the default implementation

dog = Dog()
print(dog.sound())  # Output: Woof!

cat = Cat()
print(cat.sound())  # Output: Some generic sound