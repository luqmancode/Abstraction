"""Mixins are classes that provide methods to other classes but are not meant to stand alone. They are often used to add functionality to multiple classes without using inheritance."""

class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")

class User(LoggerMixin):
    def __init__(self, name):
        self.name = name 

    def greet(self):
        self.log("This is from the Greetings: ")
        print("Good day!!!")

lm = LoggerMixin()
lm.log("Good Night")

user = User('Joseph')
user.greet()