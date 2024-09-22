"""Encapsulation is the practice of hiding the internal state and functionality of an object and only allowing access through a public interface. This is often achieved using private and protected members."""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Not enough funds to withdraw")

    def get_balance(self):
        print(f"Balance: {self.__balance}")

account = BankAccount('David', 5000)
account.get_balance()
account.withdraw(6000)
account.deposit(1000)
account.withdraw(6000)
account.get_balance()