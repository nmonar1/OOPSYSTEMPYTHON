from perfume import VanillaPerfume, MuskyPerfume, FreshPerfume
from customer import Customer
from order import Order

def display_menu():
    # Display options for the user
    print("\nHey there!! Welcome to SCENTSATION")
    print("1. Add a perfume to the order")
    print("2. Remove a perfume from the order")
    print("3. View order details")
    print("4. Exit")

def main():
    # Create a customer
    customer1 = Customer(1, "Amy Monari", "amymonari@gmail.com")

    # Create some perfumes
    vanilla_perfume = VanillaPerfume("Lataffa Eclaire", "Lataffa", "ksh4300", "100ml", "Vanilla")
    musky_perfume = MuskyPerfume("Byredo Blanche", "Byredo", "ksh3500", "50ml", "White Musk")
    fresh_perfume = FreshPerfume("Light Blue", "Dolce and Gabbana", "ksh4800", "90ml", "Fresh Spice")

    # Create an order
    order1 = Order(101, customer1)

    # Interactive menu
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable perfumes:")
            print("1. Vanilla Perfume")
            print("2. Musky Perfume")
            print("3. Fresh Perfume")
            perfume_choice = input("Select a perfume to add to the order: ")

            if perfume_choice == '1':
                order1.add_perfume(vanilla_perfume)
            elif perfume_choice == '2':
                order1.add_perfume(musky_perfume)
            elif perfume_choice == '3':
                order1.add_perfume(fresh_perfume)
            else:
                print("Invalid choice. Please try again.")

        elif choice == '2':
            print("\nPerfumes in your order:")
            for i, perfume in enumerate(order1._Order__perfumes, start=1):
                print(f"{i}. {perfume.get_info()}")

            remove_choice = input("Enter the number of the perfume to remove: ")
            try:
                perfume_to_remove = order1._Order__perfumes[int(remove_choice) - 1]
                order1.remove_perfume(perfume_to_remove)
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")

        elif choice == '3':
            # Display order details
            print("\nOrder Details:")
            print(order1.get_order_details())

        elif choice == '4':
            print(" Thank you for making an order!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
