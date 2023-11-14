# TODO: add colors to the menu
# phone number bug
# more test


import pymysql
from dotenv import load_dotenv
import os
import json
import time
import functions

load_dotenv()
host_name = os.environ.get("mysql_host")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")
database_name = os.environ.get("mysql_db")

##? Establish a connection to the MySQL server
try:
    conn = pymysql.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    )
    #test
    if conn.open:
        print("Connected to the MySQL database")

    # Create a cursor object to interact with the database
    cursor = conn.cursor()
     
except pymysql.Error as err:
    print(f"Error: {err}")


valid_options = []
while True:
    # printing the menu and taking input
    functions.display_main_menu()
    customer_input = input("Please select an option: ")
    
    # 0- exit app
    if customer_input == "0":
        print("App closed.")
        break
    
    # 1- products menu  
    elif customer_input == "1":        
        while True:
            functions.display_product_menu()
            customer_input = input("please select a option: ")
            
            # 1- 1- creat new product
            if customer_input == "1":
                new_product_name = input("please enter the new product name: ")
                if not functions.check_valid_name(new_product_name,):
                    continue
                new_product_price = input("please enter the new product price: ")
                if not functions.check_valid_price(new_product_price):
                    continue
                
                sql = ("""INSERT INTO products_table (ProductsName, ProductPrice)
                       VALUES (%s, %s)""")
                data = (new_product_name, new_product_price)
                cursor.execute(sql, data)
                conn.commit()
                
                print(f"{new_product_name} added successfully.")
                time.sleep(1)
                
            # 1- 2- show product list  
            elif customer_input == "2":
                
                cursor.execute("SELECT * FROM products_table")
                products = cursor.fetchall()
                products_list = [{"id":product[0] ,"name": product[1], "price": product[2]} for product in products]
                
                functions.display_products_list(products_list, valid_options)
                input("\npress enter to go to main menu.")

            # 1- 3- rename a product  
            elif customer_input == "3":
                
                cursor.execute("SELECT * FROM products_table")
                products = cursor.fetchall()
                products_list = [{"id":product[0] ,"name": product[1], "price": product[2]} for product in products]
                
                valid_options.clear()
                functions.display_products_list(products_list, valid_options)
                print(f"    {0}- Cancel")
                
                try: 
                    edit_index_product = int(input("\nplease write the product number you want to rename: "))
                except:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
                    continue
                
                #cancel edit
                if edit_index_product == 0:
                    print("edit has been cancelled")
                    time.sleep(1)
                    continue
                    
                elif edit_index_product in valid_options:
                    edit_name_product = input("please write the new name for the product:")
                    if not functions.check_valid_name(edit_name_product):
                        continue
                    edit_name_price = input("please write the new price for the product:")
                    if not functions.check_valid_price(edit_name_price):
                        continue
                    
                    sql = "UPDATE products_table SET ProductsName = %s, ProductPrice = %s WHERE ProductsID  = %s"
                    data = (edit_name_product, float(edit_name_price), products_list[edit_index_product - 1]["id"])  
                    cursor.execute(sql, data)
                    conn.commit()
                    
                    print(f"Product has been updated to {edit_name_product} successfully.")
                    time.sleep(1)
                    
                    
                else:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
            
            # 1- 4- delete product 
            elif customer_input == "4":
                
                cursor.execute("SELECT * FROM products_table")
                products = cursor.fetchall()
                products_list = [{"id": product[0], "name": product[1], "price": product[2]} for product in products]
                
                valid_options.clear()
                functions.display_products_list(products_list, valid_options)
                print(f"    {0}- Cancel")
                
                try:
                    delete_index_product = int(input("please write the product number: "))
                except:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
                    continue
                
                #cancel delete
                if delete_index_product == 0:
                    print("deleting has been cancelled")
                    time.sleep(1)
                
                elif delete_index_product in valid_options:
                    sql = "DELETE FROM products_table WHERE ProductsID = %s"
                    data = (products_list[delete_index_product - 1]["id"])
                    cursor.execute(sql, data)
                    conn.commit()
                                        
                    print("Product deleted successfully.")
                    time.sleep(1)
                    
                else:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
                
            # 1- 0- Return to main menu
            elif customer_input == "0":
                break
                  
            # invalid input  
            else:
                print("invalid option. please select a number from the options above")
                time.sleep(1)

    # 2- couriers menu  
    elif customer_input == "2":  
        while True:
            functions.display_courier_menu()
            customer_input = input("Please select an option: ")      
            
            # 2- 1- creat new courier 
            if customer_input =="1":
                
                courier_name = input("please enter the new courier name: ")
                if not functions.check_valid_name(courier_name):
                    continue
                courier_phone_number = input("please enter the new courier phone number: ")
                if not functions.check_valid_phone_number(courier_phone_number):
                    continue
                
                sql = """INSERT INTO couriers_table (CouriersName, CouriersPhone)
                VALUES (%s, %s)"""
                data = (courier_name, courier_phone_number)
                cursor.execute(sql, data)
                conn.commit()
                
                # new_courier = {"name":courier_name, "phone": str(courier_phone_number)}
                # courier_list.append(new_courier)
                
                print(f"{courier_name} added successfully.")
                time.sleep(1)
            
            # 2- 2- print couriers list 
            elif customer_input =="2":
                
                cursor.execute("SELECT * FROM couriers_table")
                couriers = cursor.fetchall()
                couriers_list = [{"id": courier[0], "name": courier[1], "phone": courier[2]}for courier in couriers]
                
                functions.display_courier_list(couriers_list, valid_options)
                input("\npress enter to go to main menu.")
            
            # 2- 3- rename courier 
            elif customer_input == "3":
                
                cursor.execute("SELECT * FROM couriers_table")
                couriers = cursor.fetchall()
                couriers_list = [{"id": courier[0], "name": courier[1], "phone": courier[2]}for courier in couriers]
                
                valid_options.clear()
                functions.display_courier_list(couriers_list, valid_options)
                print(f"    {0}- Cancel")
                
                try:
                    edit_index_courier = int(input("\nplease write the courier number you want to rename: "))
                except:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
                    continue
                
                #cancel edit 
                if edit_index_courier == 0:
                    print("edit has been cancelled")
                    time.sleep(1)
                    continue
                    
                
                elif edit_index_courier in valid_options:
                        edit_name_courier = input("please write the new name for the courier:")
                        if not functions.check_valid_name(edit_name_courier):
                            continue
                        edit_phone_courier = input("please write the new phone for the courier:")
                        if not functions.check_valid_phone_number(edit_phone_courier):
                            continue
                        
                        sql = "UPDATE couriers_table SET CouriersName = %s, CouriersPhone = %s WHERE CouriersID = %s"
                        data = (edit_name_courier, edit_phone_courier, couriers_list[edit_index_courier - 1]["id"])
                        cursor.execute(sql, data)
                        conn.commit()
                        
                        # courier_list[edit_index_courier - 1]["name"] = edit_name_courier
                        # courier_list[edit_index_courier - 1]["phone"] = edit_phone_courier
                        
                        print("courier name updated successfully.")
                        time.sleep(1)
                        
                else:
                    print("Invalid input. Please enter a valid courier number.")
                    time.sleep(1)
            
            # 2- 4- delete courier 
            elif customer_input =="4":
                valid_options.clear()
                functions.display_courier_list(couriers_list, valid_options)
                print(f"    {0}- cancel")
                
                try:
                    delete_index_product = int(input("please write the courier number: "))
                except:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
                    continue
                
                #cancel edit
                if delete_index_product == 0:
                    print("deleting has been cancelled")
                    time.sleep(1)
                    continue
                    
                
                elif delete_index_product in valid_options:
                    
                    sql = "DELETE FROM couriers_table WHERE CouriersID = %s"
                    data = (couriers_list[delete_index_product - 1]["id"])
                    cursor.execute(sql, data)
                    conn.commit()
                    
                    #del couriers_list[delete_index_product - 1]
                    
                    print("courier deleted successfully.")
                    time.sleep(1)
                    
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
            functions.display_orders_menu()
            customer_input = input("Please select an option: ")
 
            #3- 1- create new order 
            if customer_input == "1":
                customer_name = input("Please enter the customer name: ")
                if not functions.check_valid_name(customer_name):
                    continue
                customer_address = input("Please enter the customer address: ")
                if not functions.check_valid_name(customer_address):
                    continue
                customer_phone_number = input("Please enter the customer phone number: ")
                if not functions.check_valid_phone_number(customer_phone_number):
                    continue
                courier_num = input("Please enter the courier number: ")
                if not functions.check_valid_courier(courier_num):
                    continue
                items = input("Please enter the order's items: ")
                if not functions.check_valid_name(items):
                    continue
                
                
                sql = """INSERT INTO orders_table (CustomerName, CustomerAddress, CustomerPhone, Courier, Status, Items)
                VALUES (%s, %s, %s, %s, %s, %s)"""
                data = (customer_name, customer_address, customer_phone_number, courier_num, "preparing",items)
                cursor.execute(sql, data)
                conn.commit()
                
                print("Order added to the list successfully")
                time.sleep(1)
                
            #3- 2- Show order list 
            elif customer_input == "2":
                
                orders_list = functions.load_orders_list(cursor)
                
                print(orders_list)
                functions.display_order_list(orders_list, valid_options)
                input("\nPress Enter to go to the main menu.")

            #3- 3- update order status 
            elif customer_input == "3":
                
                orders_list = functions.load_orders_list(cursor)
                
                valid_options.clear()
                functions.display_order_list(orders_list, valid_options)
                print("0- cancel")
                
                try:
                    num_order_edit = int(input("please select an order to update: "))
                
                except:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
                    continue
                
                #cancel edit
                if num_order_edit == 0:
                    print("edit has been cancelled")
                    time.sleep(1)
                    
                elif num_order_edit in valid_options:
                    order_status = orders_list[num_order_edit - 1]["status"]
                    
                    print("Order status is:", order_status)
                    time.sleep(1)
                    
                    status_order_edit = input("please enter the order new status: ")
                    
                    sql = "UPDATE orders_table SET Status = %s WHERE OrdersID = %s"
                    print(orders_list[num_order_edit - 1]["status"])
                    data = (status_order_edit, orders_list[num_order_edit - 1]["id"])
                    cursor.execute(sql, data)
                    conn.commit()
                    
                    print("Order status updated successfully")
                    time.sleep(1)
                    
                else:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
            
            #3- 4- UPDATE order 
            elif customer_input == "4":
                
                orders_list = functions.load_orders_list(cursor)
                
                valid_options.clear()
                functions.display_order_list(orders_list, valid_options)
                print("0- cancel")
                
                try:
                    num_order_edit = int(input("please select an order to update: "))               
                except:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
                    continue
                
                #cancel edit
                if num_order_edit == 0:
                    print("edit has been cancelled")
                    time.sleep(1)
                
                
                elif num_order_edit in valid_options:
                    name_order_edit = input(f"the old name is ({orders_list[num_order_edit - 1]['customer_name']}) please write the new name: ")
                    if not functions.check_valid_name(name_order_edit):
                        continue
                    adress_order_edit = input(f"the old address is ({orders_list[num_order_edit - 1]['customer_address']}) please write the new address: ")
                    if not functions.check_valid_name(adress_order_edit):
                        continue
                    phone_order_edit = input(f"the old phone is ({orders_list[num_order_edit - 1]['customer_phone']}) please enter the new phone number: ")
                    if not functions.check_valid_phone_number(phone_order_edit):
                        continue
                    courier_num_edit = input(f"the old name is ({orders_list[num_order_edit - 1]['courier']}) please enter the new courier number: ")
                    if not functions.check_valid_courier(courier_num_edit):
                        continue
                    status_order_edit = input(f"the old status is ({orders_list[num_order_edit - 1]['status']}) please enter the order new status: ")
                    if not functions.check_valid_name(status_order_edit):
                        continue
                    items_order_edit = input(f"the old items ({orders_list[num_order_edit - 1]['items']}) please enter the order new items: ")
                    if not functions.check_valid_name(items_order_edit):
                        continue
                    
                    sql = """UPDATE orders_table SET CustomerName = %s, CustomerAddress = %s, CustomerPhone = %s, Courier = %s, Status = %s, Items = %s 
                    WHERE OrdersID = %s """
                    data = (name_order_edit, adress_order_edit, phone_order_edit, courier_num_edit, status_order_edit, items_order_edit, orders_list[num_order_edit - 1]["id"])
                    cursor.execute(sql,data)
                    conn.commit()
                    
                    print("Order updated successfully")
                    time.sleep(1)
                
                # invalid input  
                else:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
                    
            #3- 5- delete order 
            elif customer_input == "5":
                
                orders_list = functions.load_orders_list(cursor)
                
                valid_options.clear()
                functions.display_order_list(orders_list, valid_options)
                print("0- cancel")
                
                try:
                    num_order_del = int(input("please select an order to delete: "))
                except:
                    print("Invalid input. Please enter a valid product number.")
                    time.sleep(1)
                    continue
                    
                #cancel deleting
                if num_order_del == 0:
                    print("deleting has been cancelled")
                    time.sleep(1)
                    
                elif num_order_del in valid_options:
                    
                    sql = "DELETE FROM orders_table WHERE OrdersID = %s"
                    data = (orders_list[num_order_del - 1]["id"])
                    cursor.execute(sql, data)
                    conn.commit()
                    
                    #del orders_list[int(num_order_del) - 1]
                    
                    print("Order deleted successfully")
                    time.sleep(1)
                    
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
