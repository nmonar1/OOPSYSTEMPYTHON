# OOPSYSTEMPYTHON
# MONARI NICOLE GESARE
# **student number:** 168330
# Project Title: Perfume Shop Management System

## Project Description:  
 The system is designed in Python using Object-Oriented Programming concepts: encapsulation, inheritance, polymorphism, and abstraction.

## Key Features
The purpose of this system is to manage perfumes by category (e.g., Vanilla, Musky, Fresh), track customer orders, and handle basic operations for adding and removing items within an order. The project is interactive, user-friendly, and demonstrates exception handling.

## System Components

1. **Classes and Inheritance**:  
   - The abstract base class, 'Perfume', with attributes (e.g., name, brand, price,quantity) and enforces a 'get_info()' method (it's an abstract method that the subclasses implement),get_name(self) method, get_brand(self)method, get_price(self)method, get_quantity(self)method.
   - Subclasses VanillaPerfume, MuskyPerfume, and FreshPerfume inherit from Perfume, adding unique notes specific to each perfume category.
   - The Customer class manages customer information, and the Order class handles customer orders, supporting adding and removing perfumes.

2. **Polymorphism and Abstraction**:  
   - Perfume's abstract method 'get_info()' is overridden in each subclass to provide detailed perfume information according to the specific category, demonstrating polymorphism.
   - from abc import ABC, abstractmethod in the Perfume class demonstrates abstraction

3. **Encapsulation and Access Control**:  
   - Private attributes (e.g., price and quantity) are encapsulated within each class, accessible only through specific methods, maintaining control over data access and manipulation.

4. **Functionality**:  
   - **Order Workflow**: The system supports operations such as adding and removing perfumes from an order, displaying the order summary, and handling errors (e.g., removing a perfume that isn’t in the order).
   - **Exception Handling**: The system provides error messages if an item is unavailable or cannot be removed.


