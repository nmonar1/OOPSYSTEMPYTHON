# main class

from perfume import VanillaPerfume, MuskyPerfume, FreshPerfume
from customer import Customer
from order import Order

def main():
    # Create a customer
    customer1 = Customer(1, "Amy Monari", "amymonari@gmail.com")

    # Create some perfumes
    vanilla_perfume = VanillaPerfume("Lataffa Eclaire", "Lataffa", "ksh4300", "100ml", "Vanilla")
    musky_perfume = MuskyPerfume("Byredo Blanche", "Byredo", "ksh3500", "50ml", "White Musk")
    fresh_perfume = FreshPerfume("Light Blue", "Dolce and Gabbana", "ksh4800", "90ml", "Fresh Spice")

    # Create an order
    order1 = Order(101, customer1)

    # Add perfumes to the order
    order1.add_perfume(vanilla_perfume)
    order1.add_perfume(musky_perfume)

    # Display order details
    print(order1.get_order_details())

    # Trying to remove a perfume that is in the order
    order1.remove_perfume(musky_perfume)

    # Trying to remove a perfume that is not in the order (exception handling)
    order1.remove_perfume(fresh_perfume)  

    # Display updated order details
    print(order1.get_order_details())

if __name__ == "__main__":
    main()
