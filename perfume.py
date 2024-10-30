# perfume.py
from abc import ABC, abstractmethod

class Perfume(ABC):
    #Abstract base class representing a perfume

    def __init__(self, name, brand, price, quantity):
        self.__name = name          # Private attribute
        self.__brand = brand        # Private attribute
        self.__price = price        # Private attribute
        self.__quantity = quantity  # Private attribute

    @abstractmethod
    def get_info(self):#abstract method
        pass

    def get_name(self):
        #Returns name of the perfume
        return self.__name

    def get_brand(self):
        #Returns brand of the perfume
        return self.__brand

    def get_price(self):
        #Returns price of the perfume
        return self.__price

    def get_quantity(self):
        #Returns quantity of the perfume
        return self.__quantity

# inheritance from perfume class
class VanillaPerfume(Perfume):
    #Subclass for Vanilla perfumes

    def __init__(self, name, brand, price, quantity, vanilla_note):
        super().__init__(name, brand, price, quantity)
        self.__vanilla_note = vanilla_note

    def get_info(self):
        """Returns information about the vanilla perfume, also shows polymorphism"""
        return f"{self.get_name()} ({self.get_brand()}), Price: ${self.get_price()}, Quantity: {self.get_quantity()}, Vanilla Note: {self.__vanilla_note}"

class MuskyPerfume(Perfume):
    #Subclass for Musky perfumes

    def __init__(self, name, brand, price, quantity, musky_note):
        super().__init__(name, brand, price, quantity)
        self.__musky_note = musky_note

    def get_info(self):
        """Returns information about the musky perfume, also shows polymorphism"""
        return f"{self.get_name()} ({self.get_brand()}), Price: ${self.get_price()}, Quantity: {self.get_quantity()}, Musky Note: {self.__musky_note}"

class FreshPerfume(Perfume):
    #Subclass for Fresh perfumes

    def __init__(self, name, brand, price, quantity, fresh_note):
        super().__init__(name, brand, price, quantity)
        self.__fresh_note = fresh_note

    def get_info(self):
        """Returns information about the fresh perfume, also shows polymorphism"""
        return f"{self.get_name()} ({self.get_brand()}), Price: ${self.get_price()}, Quantity: {self.get_quantity()}, Fresh Note: {self.__fresh_note}"
