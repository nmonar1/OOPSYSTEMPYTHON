
#order class
class Order:

    def __init__(self, order_id, customer, perfumes=None):
        self.__order_id = order_id
        self.__customer = customer
        self.__perfumes = perfumes if perfumes is not None else []

    def add_perfume(self, perfume):#Adding a perfume to an order
        self.__perfumes.append(perfume)
        print(f"{perfume.get_info()} has been added to the order.")

    def remove_perfume(self, perfume):#Removes a perfume from the order
        # handling exceptions
        try:
            self.__perfumes.remove(perfume)
            print(f"{perfume.get_info()} has been removed from the order.")
        except ValueError:
            print("Error:The perfume is not in the order")

    def get_order_details(self):
        #display order details
        perfume_details = [perfume.get_info() for perfume in self.__perfumes]
        return f"Order ID: {self.__order_id}, Customer: {self.__customer.get_details()}, Perfumes: {', '.join(perfume_details)}"
