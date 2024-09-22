"""Abstract Base Classes are used to define a common interface for a set of subclasses. They cannot be instantiated directly and must be subclassed to provide concrete implementations of their abstract methods."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def sound(self):
        print(f"Dog {self.name} is saying Wooof")

class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def sound(self):
        print(f"Cat {self.name} is saying Meoww")

# animal = Animal() # TypeError: Can't instantiate abstract class Animal with abstract method sound
dog = Dog('Huskey', 4)
dog.sound()

cat = Cat('Mikey', 3)
cat.sound()

# Dog Huskey is saying Wooof
# Cat Mikey is saying Meoww
