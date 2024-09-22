"""Abstract classes can define static methods that are shared among all subclasses, while still requiring subclasses to implement certain instance methods."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @staticmethod
    def info():  # No self or cls
        return "This is an Animal Kingdom Info"
    
class Dog(Animal):
    def sound(self):
        print("Dog makes Wooff")

dog = Dog()
dog.sound()
print(dog.info())