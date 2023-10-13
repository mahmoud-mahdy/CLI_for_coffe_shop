import time

valid_options = []

product_list = [
    "Espresso",
    "Americano",
    "Latte",
    "Cappuccino",
    "Macchiato",
]

orders_list = [{"customer_name": "John",
                "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                "customer_phone": "0789887334",
                "status": "preparing"}, 
               {"customer_name": "Alice",
                "customer_address": "Apt 3B, 45 Elm Avenue, NEW YORK, NY 10001",
                "customer_phone": "212-555-7890", 
                "status": "pending"},
               {"customer_name": "Michael",
                "customer_address": "123 Oak Street, SAN FRANCISCO, CA 94101",
                "customer_phone": "415-123-4567",
                "status": "shipped"},
               {"customer_name": "Emily",
                "customer_address": "789 Maple Lane, LOS ANGELES, CA 90001",
                "customer_phone": "323-555-1234",
                "status": "delivered"}
               ]

def main_menu():
    print("""
    Coffe Shop Menu
    ===============
    1- Product menu
    2- Orders menu
    0- Exit app 
          """)
    
def product_menu():
    print("""
    Products Menu
    ===============
    1- Create New product
    2- Product list
    3- Edit product list
    4- Delete a product
    0- Return to Main menu
    """)
    
def orders_menu():
    print("""
    Orders Menu
    ===========
    1- Create New order
    2- Order list
    3- Update an order status
    4- Update an order
    5- Delete an order
    0- Return to Main menu
    """)
    

while True:
    #printing the menu and taking input
    main_menu()
    customer_input = input("Please select an option: ")
    
    #exit app
    if customer_input == "0":
        print("App closed.")
        break
    
    #open products menu
    elif customer_input == "1":        
        while True:
            product_menu()
            customer_input = input("please select a option: ")
            
            # creat new product
            if customer_input == "1":
                new_product = input("please enter the new product: ")
                product_list.append(new_product)
                print(f"{new_product} added successfully.")
                time.sleep(1)
                
            #show product list
            elif customer_input == "2":
                print("\n    Product List\n    ============")
                for index, product in enumerate(product_list, start=1):
                    print(f"    {index}- {product}")
                input("\npress enter to go to main menu.")
            
            #rename a product
            elif customer_input == "3":
                valid_options.clear()
                print("\n    Product List\n    ============")
                for index, product in enumerate(product_list, start=1):
                    print(f"    {index}- {product}")
                    valid_options.append(index)
                    
                while True:
                    edit_index_product = int(input("\nplease write the product number you want to rename: "))
                    
                    if edit_index_product in valid_options:
                            edit_name_product = input("please write the new name for the product:")
                            product_list[edit_index_product - 1] = (f"{edit_name_product}")
                            print("Product name updated successfully.")
                            time.sleep(1)
                            break
                    else:
                        print("Invalid input. Please enter a valid product number.")
                        time.sleep(1)
            
            #delete product
            elif customer_input == "4":
                valid_options.clear()
                print("\n    Product List\n    ============")
                for index, product in enumerate(product_list, start=1):
                    print(f"    {index}- {product}")
                    valid_options.append(index)
                while True:
                    delete_index_product = int(input("please write the product number: "))
                    if delete_index_product in valid_options:
                        del product_list[delete_index_product - 1]
                        print("Product deleted successfully.")
                        time.sleep(1)
                        break
                    else:
                        print("Invalid input. Please enter a valid product number.")
                        time.sleep(1)
                
            # Return to main menu
            elif customer_input == "0":
                break
                  
            #invalid input  
            else:
                print("invalid option. please select a number from the options above")
                time.sleep(1)

    #open orders menu
    elif customer_input == "2":
        while True:
            orders_menu()
            customer_input = input("Please select an option: ")
 
            #create new order    
            if customer_input == "1":
                customer_name = input("Please enter the customer name: ")
                customer_address = input("Please enter the customer address: ")
                customer_phone_number = int( input ("Please enter the customer phone number: "))
                new_customer = {
                    "customer_name": customer_name,
                    "customer_address": customer_address,
                    "customer_phone": customer_phone_number,
                    "status": "preparing"
                    }
                orders_list.append(new_customer)
                print("Order added to the list successfully")
                time.sleep(1)
                
            # Show order list
            elif customer_input == "2":
                print("\nOrder List")
                print("=" * 50)
                for index, order in enumerate(orders_list, start=1):
                    print(f"Order {index}:")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Customer Address: {order['customer_address']}")
                    print(f"Customer Phone: {order['customer_phone']}")
                    print(f"Status: {order['status']}")
                    print("-" * 50)
                input("\nPress Enter to go to the main menu.")

            #update order status
            elif customer_input == "3":
                print("\nOrder List")
                print("=" * 50)
                for index, order in enumerate(orders_list, start=1):
                    print(f"Order {index}:")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Customer Address: {order['customer_address']}")
                    print(f"Customer Phone: {order['customer_phone']}")
                    print(f"Status: {order['status']}")
                    print("-" * 50)
                    
                num_order_edit = int(input("please select an order to update: "))
                order_status = orders_list[num_order_edit - 1]["status"]
                
                print("Order status is:", order_status)
                time.sleep(1)
                
                status_order_edit = input("please enter the order new status: ")
                orders_list[num_order_edit - 1]["status"] = status_order_edit
                print("Order status updated successfully")
                time.sleep(1)
            
            #UPDATE order
            elif customer_input == "4":
                print("\nOrder List")
                print("=" * 50)
                for index, order in enumerate(orders_list, start=1):
                    print(f"Order {index}:")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Customer Address: {order['customer_address']}")
                    print(f"Customer Phone: {order['customer_phone']}")
                    print(f"Status: {order['status']}")
                    print("-" * 50)

                num_order_edit = int(input("please select an order to update: "))
                
                name_order_edit = input("please write the new name: ")
                adress_order_edit = input("please write the new address: ")
                phone_order_edit = int(input("please enter the new phone number: "))
                status_order_edit = input("please enter the order new status: ")
                
                orders_list[num_order_edit - 1]["customer_name"] = name_order_edit
                orders_list[num_order_edit - 1]["customer_address"] = adress_order_edit
                orders_list[num_order_edit - 1]["customer_phone"] = phone_order_edit
                orders_list[num_order_edit - 1]["status"] = status_order_edit
                
                print("Order updated successfully")
                time.sleep(1)
                
            #delete order
            elif customer_input == "5":
                print("\nOrder List")
                print("=" * 50)
                for index, order in enumerate(orders_list, start=1):
                    print(f"Order {index}:")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Customer Address: {order['customer_address']}")
                    print(f"Customer Phone: {order['customer_phone']}")
                    print(f"Status: {order['status']}")
                    print("-" * 50)
                    
                num_order_del = int(input("please select an order to delete: "))
                del orders_list[num_order_del - 1]
                print("Order deleted successfully")
                time.sleep(1)
                
                
            # Return to main menu
            elif customer_input == "0":
                break
            
            #invalid input
            else:
                print("invalid option. please select a number from the options above")
                time.sleep(1)
        
    #invalid input
    else:
        print("invalid option. please select a number from the options above")
        time.sleep(1)