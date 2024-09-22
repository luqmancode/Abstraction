"""Abstract classes can define custom exceptions that are raised if certain methods are not implemented by subclasses."""

from abc import ABC, abstractmethod

class AbstractMethodNotImplemented(Exception):
    pass

class Animal(ABC):
    @abstractmethod
    def sound(self):
        raise AbstractMethodNotImplemented("Subclasses must implement 'sound' method")

class Dog(Animal):
    def sound(self):
        return "Woof!"

dog = Dog()
print(dog.sound())  # Output: Woof!