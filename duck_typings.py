"""Duck typing is a form of polymorphism where the type or class of an object is less important than the methods it defines. If it looks like a duck and quacks like a duck, it’s a duck."""

class Duck:
    def quack(self):
        return "Quack"
    
class Person:
    def quack(self):
        return "I am quacking like a duck"
    
def make_quack(obj):
    print(obj.quack())

duck = Duck()
person = Person()

make_quack(duck)
make_quack(person)