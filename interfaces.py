"""Interfaces define a contract that classes must adhere to. In Python, interfaces are often simulated using Abstract Base Classes (ABC) with abstract methods."""

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

credit_card = CreditCardPayment()
credit_card.pay(100)  # Output: Paid 100 using Credit Card

paypal = PayPalPayment()
paypal.pay(200)  # Output: Paid 200 using PayPal