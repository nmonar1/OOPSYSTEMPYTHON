class Customer:
    # Customer class to store customer details

    def __init__(self, customer_id, name, email):
        self.__customer_id = customer_id  # Private attribute
        self.__name = name                # Private attribute
        self.__email = email              # Private attribute

    def get_details(self):
        # Returns details of the customer
        return f"ID: {self.__customer_id}, Name: {self.__name}, Email: {self.__email}"
