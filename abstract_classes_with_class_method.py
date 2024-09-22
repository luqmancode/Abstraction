"""Abstract classes can define class methods that are shared among all subclasses, while still requiring subclasses to implement certain instance methods."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 
    
    @classmethod
    def species(cls):
        return cls.__name__
    
class Dog(Animal):
    def sound(self):
        print(f"Dog makes Woff")

dog = Dog()
dog.sound()
print(dog.species())