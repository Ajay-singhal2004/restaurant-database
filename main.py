from database import initialize_database
import customers
import menu
import orders
import reservations

def main():
    initialize_database()
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Add Menu Item")
        print("4. View Menu")
        print("5. Create Order")
        print("6. View Orders")
        print("7. Make Reservation")
        print("8. View Reservations")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            customers.add_customer(name, phone, email)
        elif choice == "2":
            customers.view_customers()
        elif choice == "3":
            name = input("Item Name: ")
            price = float(input("Price: "))
            menu.add_menu_item(name, price)
        elif choice == "4":
            menu.view_menu()
        elif choice == "5":
            cid = int(input("Customer ID: "))
            table = int(input("Table Number: "))
            total = float(input("Total Price: "))
            orders.create_order(cid, table, total)
        elif choice == "6":
            orders.view_orders()
        elif choice == "7":
            cid = int(input("Customer ID: "))
            table = int(input("Table Number: "))
            time = input("Reservation Time (YYYY-MM-DD HH:MM:SS): ")
            reservations.make_reservation(cid, table, time)
        elif choice == "8":
            reservations.view_reservations()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
