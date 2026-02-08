
from abc import ABC, abstractmethod

class class_new_product(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def change_quantity(self, qty):
        pass

    @abstractmethod
    def change_price(self, prc):
        pass

    @abstractmethod
    def change_name(self, nm):
        pass





