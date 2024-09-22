"""Abstract classes can contain concrete methods that are shared among all subclasses, while still requiring subclasses to implement certain methods."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Zzz...")

class Dog(Animal):
    def sound(self):
        return "Woof!"

dog = Dog()
print(dog.sound())  # Output: Woof!
dog.sleep()         # Output: Zzz...