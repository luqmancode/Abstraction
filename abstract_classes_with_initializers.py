"""Abstract classes can define initializers that are shared among all subclasses, while still requiring subclasses to implement certain methods."""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass 

class Cat(Animal):
    def sound(self):
        print(f"{self.name} makes Meow")

cat = Cat('keke')
cat.sound()