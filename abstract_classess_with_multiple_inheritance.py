"""Abstract classes can be used in multiple inheritance scenarios, allowing subclasses to inherit from multiple abstract classes."""

from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass  

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass 

class Duck(Flyable, Swimmable):
    def fly(self):
        print("It can Fly")

    def swim(self):
        print("It can swim")

duck = Duck()
duck.fly()
duck.swim()