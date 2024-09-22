"""Abstract properties are properties that must be implemented by subclasses. They are defined using the @abstractproperty decorator (or @property with @abstractmethod)."""

from math import pi
from abc import ABC, abstractproperty, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length 
        self.breadth = breadth 

    @property
    def area(self):
        return self.length * self.breadth
    
class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return self._radius * 2 * pi
    
rectangle = Rectangle(5, 6)
print(rectangle.area)

circle = Circle(10)
print(circle.area)
