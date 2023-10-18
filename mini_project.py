#LOAD products from products.csv    
# LOAD couriers from couriers.csv    
# LOAD orders from orders.csv





import json
import time
 
#import orders list
# with open("orders_list.json", 'r') as file:
# orders_dict = json.load(file)

orders_dict = [
    {"customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2, # Courier index
  "status": "preparing",
  "items": "1, 3, 4" }# Product index 
 ]
    
# #import products list
# with open("products_list.json", 'r') as file:
# products_dict = json.load(file)
    
products_dict = {
    "Espresso": 1.99,
    "Cappuccino": 2.49,
    "Latte": 2.99,
    "Mocha": 3.49,
    "Americano": 2.29,
    "Macchiato": 2.79,
    "Milk": 1.00
}

#import courier list
# with open("courier_list.json", 'r') as file:
# courier_dict = json.load(file)

courier_dict = [
    {"name": "John", "phone": "0789887889"},
    {"name": "Alice", "phone": "0734567890"},
    {"name": "Michael", "phone": "0722222222"},
    {"name": "Emily", "phone": "0711111111"},
    {"name": "Ahmed", "phone": "0799999999"}
]

# display main menu
def main_menu():
    print("""
    Coffe Shop Menu
    ===============
    1- Product menu
    2- couriers menu
    3- Orders menu
    0- Exit app 
          """)

# display Product menu
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

# display couriers menu    
def courier_menu():
    print("""
    courier Menu
    ============ 
    1- Create new courier
    2- Couriers list
    3- Update an existing courier
    4- Delete a courier
    0- Return to Main menu
          """)

# display Orders menu    
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
    
valid_options = []
while True:
    #printing the menu and taking input
    main_menu()
    customer_input = input("Please select an option: ")
    
    #exit app
    if customer_input == "0":
        print("App closed.")
        break
    
    # 1- open products menu
    elif customer_input == "1":        
        while True:
            product_menu()
            customer_input = input("please select a option: ")
            
            # creat new product
            if customer_input == "1":
                new_product = input("please enter the new product: ")
                products_dict.append(new_product)
                print(f"{new_product} added successfully.")
                time.sleep(1)
                
            #show product list
            elif customer_input == "2":
                print("\n    Product List\n    ============")
                for index, product in enumerate(products_dict, start=1):
                    print(f"    {index}- {product}")
                input("\npress enter to go to main menu.")
            
            #rename a product
            elif customer_input == "3":
                valid_options.clear()
                print("\n    Product List\n    ============")
                for index, product in enumerate(products_dict, start=1):
                    print(f"    {index}- {product}")
                    valid_options.append(index)
                print(f"    {0}- Cancel")
                    
                while True:
                    edit_index_product = int(input("\nplease write the product number you want to rename: "))
                    #cancel edit
                    if edit_index_product == 0:
                        print("edit has been cancelled")
                        time.sleep(1)
                        break
                    
                    elif edit_index_product in valid_options:
                        edit_name_product = input("please write the new name for the product:")
                        products_dict[edit_index_product - 1] = (f"{edit_name_product}")
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
                for index, product in enumerate(products_dict, start=1):
                    print(f"    {index}- {product}")
                    valid_options.append(index)
                print(f"    {0}- Cancel")    
                    
                while True:
                    delete_index_product = int(input("please write the product number: "))
                    
                    #cancel edit
                    if delete_index_product == 0:
                        print("deleting has been cancelled")
                        time.sleep(1)
                        break
                    
                    elif delete_index_product in valid_options:
                        del products_dict[delete_index_product - 1]
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

    # 2- couriers menu
    elif customer_input == "2":
        while True:
            courier_menu()
            customer_input = input("Please select an option: ")
            
            # 2- 1- creat new courier
            if customer_input =="1":
                courier_name = input("please enter the new courier name: ")
                courier_phone_number = input("please enter the new courier phone number: ")
                
                courier_dict.append(courier_name)
                
                
                print(f"{courier_name} added successfully.")
                
                time.sleep(1)
            
            # print couriers list
            elif customer_input =="2":
                print("\n    couriers List\n    =============")
                for index, courier in enumerate(courier_dict, start=1):
                    print(f"    {index}- {courier}")
                input("\npress enter to go to main menu.")
            
            #rename courier
            elif customer_input == "3":
                valid_options.clear()
                print("\n    courier List\n    ============")
                for index, courier in enumerate(courier_dict, start=1):
                    print(f"    {index}- {courier}")
                    valid_options.append(index)
                print(f"    {0}- Cancel")
                
                while True:
                    edit_index_courier = int(input("\nplease write the courier number you want to rename: "))
                    
                    #cancel edit
                    if edit_index_courier == 0:
                        print("edit has been cancelled")
                        time.sleep(1)
                        break
                    
                    elif edit_index_courier in valid_options:
                            edit_name_courier = input("please write the new name for the courier:")
                            courier_dict[edit_index_courier - 1] = (f"{edit_name_courier}")
                            print("courier name updated successfully.")
                            time.sleep(1)
                            break
                    else:
                        print("Invalid input. Please enter a valid courier number.")
                        time.sleep(1)
            
            # delete courier
            elif customer_input =="4":
                valid_options.clear()
                print("\n    couriers List\n    =============")
                for index, courier in enumerate(courier_dict, start=1):
                    print(f"    {index}- {courier}")
                    valid_options.append(index)
                print(f"    {0}- cancel")
                
                while True:
                    delete_index_product = int(input("please write the courier number: "))
                    
                    #cancel edit
                    if delete_index_product == 0:
                        print("deleting has been cancelled")
                        time.sleep(1)
                        break
                    
                    elif delete_index_product in valid_options:
                        del courier_dict[delete_index_product - 1]
                        print("courier deleted successfully.")
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
            
    #3- open orders menu
    elif customer_input == "3":
        while True:
            orders_menu()
            customer_input = input("Please select an option: ")
 
            #3- 1- create new order    
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
                orders_dict.append(new_customer)
                print("Order added to the list successfully")
                time.sleep(1)
                
            #3- 2- Show order list
            elif customer_input == "2":
                print("\nOrder List")
                print("=" * 50)
                for index, order in enumerate(orders_dict, start=1):
                    print(f"Order {index}:")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Customer Address: {order['customer_address']}")
                    print(f"Customer Phone: {order['customer_phone']}")
                    print(f"Status: {order['status']}")
                    print("-" * 50)
                input("\nPress Enter to go to the main menu.")

            #3- 3- update order status
            elif customer_input == "3":
                print("\nOrder List")
                print("=" * 50)
                valid_options.clear()
                for index, order in enumerate(orders_dict, start=1):
                    print(f"Order {index}:")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Customer Address: {order['customer_address']}")
                    print(f"Customer Phone: {order['customer_phone']}")
                    print(f"Status: {order['status']}")
                    print("-" * 50)
                    valid_options.append(index)
                print("0- cancel")
                
                while True:
                    num_order_edit = int(input("please select an order to update: "))
                    
                    #cancel edit
                    if num_order_edit == 0:
                        print("edit has been cancelled")
                        time.sleep(1)
                        break
                    
                    elif num_order_edit in valid_options:
                        order_status = orders_dict[num_order_edit - 1]["status"]
                        
                        print("Order status is:", order_status)
                        time.sleep(1)
                        
                        status_order_edit = input("please enter the order new status: ")
                        orders_dict[num_order_edit - 1]["status"] = status_order_edit
                        print("Order status updated successfully")
                        time.sleep(1)
                        break
                    
                    else:
                        print("Invalid input. Please enter a valid product number.")
                        time.sleep(1)
            
            #3- 4- UPDATE order
            elif customer_input == "4":
                print("\nOrder List")
                print("=" * 50)
                valid_options.clear()
                for index, order in enumerate(orders_dict, start=1):
                    print(f"Order {index}:")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Customer Address: {order['customer_address']}")
                    print(f"Customer Phone: {order['customer_phone']}")
                    print(f"Status: {order['status']}")
                    print("-" * 50)
                    valid_options.append(index)
                print("0- cancel")
                
                while True:
                    num_order_edit = int(input("please select an order to update: "))
                    
                    #cancel edit
                    if num_order_edit == 0:
                        print("edit has been cancelled")
                        time.sleep(1)
                        break
                    
                    elif num_order_edit in valid_options:
                        name_order_edit = input("please write the new name: ")
                        adress_order_edit = input("please write the new address: ")
                        phone_order_edit = int(input("please enter the new phone number: "))
                        status_order_edit = input("please enter the order new status: ")
                        
                        orders_dict[num_order_edit - 1]["customer_name"] = name_order_edit
                        orders_dict[num_order_edit - 1]["customer_address"] = adress_order_edit
                        orders_dict[num_order_edit - 1]["customer_phone"] = phone_order_edit
                        orders_dict[num_order_edit - 1]["status"] = status_order_edit
                        
                        print("Order updated successfully")
                        time.sleep(1)
                        break
                    
                    else:
                        print("Invalid input. Please enter a valid product number.")
                        time.sleep(1)
            #3- 5- delete order
            elif customer_input == "5":
                print("\nOrder List")
                print("=" * 50)
                valid_options.clear()
                for index, order in enumerate(orders_dict, start=1):
                    print(f"Order {index}:")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Customer Address: {order['customer_address']}")
                    print(f"Customer Phone: {order['customer_phone']}")
                    print(f"Status: {order['status']}")
                    print("-" * 50)
                    valid_options.append(index)
                print("0- cancel")
                
                while True:    
                    num_order_del = int(input("please select an order to delete: "))
                    
                    #cancel deleting
                    if num_order_del == 0:
                        print("deleting has been cancelled")
                        time.sleep(1)
                        break
                    
                    elif num_order_del in valid_options:
                        del orders_dict[num_order_del - 1]
                        print("Order deleted successfully")
                        time.sleep(1)
                        break
                    
                    else:
                        print("Invalid input. Please enter a valid product number.")
                        time.sleep(1)
                
            #3- 0- Return to main menu
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


#save changes to products_list
with open("products_list.json", 'w') as file:
    json.dump(products_dict, file)

#save changes to orders_list  
with open("orders_list.json", 'w') as file:
    json.dump(orders_dict, file)
    
#save changes to courier_list
with open("courier_list.json", 'w') as file:
    json.dump(courier_dict, file)
