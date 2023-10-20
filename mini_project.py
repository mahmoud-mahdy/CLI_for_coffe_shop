import json
import time
import menus

 
# import orders list
with open("orders_list.json", 'r') as file:
    orders_list = json.load(file)

#import products list
with open("products_list.json", 'r') as file:
    products_list = json.load(file)
    
#import courier list
with open("courier_list.json", 'r') as file:
    courier_list = json.load(file)



valid_options = []
while True:
    # printing the menu and taking input
    menus.display_main_menu()
    customer_input = input("Please select an option: ")
    
    # 0- exit app
    if customer_input == "0":
        print("App closed.")
        break
    
    # 1- open products menu
    elif customer_input == "1":        
        while True:
            menus.display_product_menu()
            customer_input = input("please select a option: ")
            
            # creat new product
            if customer_input == "1":
                new_product_name = input("please enter the new product: ")
                menus.check_valid_name(new_product_name)
                while True:
                    new_product_price = input("please enter the new product price: ")
                    try:
                        new_product_price = float(new_product_price)
                        break
                    except ValueError:
                        print("Invalid price. Please enter a valid number.")
                        time.sleep(1)
                 
                new_product = {"name":new_product_name, "price":new_product_price}
                
                products_list.append(new_product)
                print(f"{new_product_name} added successfully.")
                time.sleep(1)
                
            #show product list
            elif customer_input == "2":
                menus.display_products_list(products_list, valid_options)
                input("\npress enter to go to main menu.")


            #rename a product
            elif customer_input == "3":
                valid_options.clear()
                menus.display_products_list(products_list, valid_options)
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
                        edit_name_price = input("please write the new name for the product:")
                        products_list[edit_index_product - 1] = (f"{edit_name_product}")
                        print(f"Product {product['name']} updated successfully.")
                        time.sleep(1)
                        break
                        
                    else:
                        print("Invalid input. Please enter a valid product number.")
                        time.sleep(1)
            
            #delete product
            elif customer_input == "4":
                valid_options.clear()
                print("\n    Product List\n    ============")
                for index, product in enumerate(products_list, start=1):
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
                        del products_list[delete_index_product - 1]
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
            menus.display_courier_menu()
            customer_input = input("Please select an option: ")
            
            # 2- 1- creat new courier
            if customer_input =="1":
                courier_name = input("please enter the new courier name: ")
                courier_phone_number = input("please enter the new courier phone number: ")
                
                courier_list["name"] = courier_name
                courier_list["phone"] = courier_phone_number
                
                print(f"{courier_name} added successfully.")
                
                time.sleep(1)
            
            # print couriers list
            elif customer_input =="2":
                print("\n    couriers List\n    =============")
                for index, courier in enumerate(courier_list, start=1):
                    print(f"    {index}- {courier}")
                input("\npress enter to go to main menu.")
            
            #rename courier
            elif customer_input == "3":
                valid_options.clear()
                print("\n    courier List\n    ============")
                for index, courier in enumerate(courier_list, start=1):
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
                            courier_list[edit_index_courier - 1] = (f"{edit_name_courier}")
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
                for index, courier in enumerate(courier_list, start=1):
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
                        del courier_list[delete_index_product - 1]
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
            menus.display_orders_menu()
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
                orders_list.append(new_customer)
                print("Order added to the list successfully")
                time.sleep(1)
                
            #3- 2- Show order list
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

            #3- 3- update order status
            elif customer_input == "3":
                print("\nOrder List")
                print("=" * 50)
                valid_options.clear()
                for index, order in enumerate(orders_list, start=1):
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
                        order_status = orders_list[num_order_edit - 1]["status"]
                        
                        print("Order status is:", order_status)
                        time.sleep(1)
                        
                        status_order_edit = input("please enter the order new status: ")
                        orders_list[num_order_edit - 1]["status"] = status_order_edit
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
                for index, order in enumerate(orders_list, start=1):
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
                        
                        orders_list[num_order_edit - 1]["customer_name"] = name_order_edit
                        orders_list[num_order_edit - 1]["customer_address"] = adress_order_edit
                        orders_list[num_order_edit - 1]["customer_phone"] = phone_order_edit
                        orders_list[num_order_edit - 1]["status"] = status_order_edit
                        
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
                for index, order in enumerate(orders_list, start=1):
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
                        del orders_list[num_order_del - 1]
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
    json.dump(products_list, file)

#save changes to orders_list  
with open("orders_list.json", 'w') as file:
    json.dump(orders_list, file)
    
#save changes to courier_list
with open("courier_list.json", 'w') as file:
    json.dump(courier_list, file)
