import time

product_list = [
    "Espresso",
    "Americano",
    "Latte",
    "Cappuccino",
    "Macchiato",
]

def main_menu():
    print("""
    Coffe Shop Menu
    ===============
    1- Product menu
    0- Exit app 
          """)
    
def product_menu():
    print("""
    Products Menu
    ===============
    1- Create New product
    2- Product List
    3- Edit product list
    4- Delete product
    0- Return to Main menu
    """)
    
options = []
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
                options.clear()
                print("\n    Product List\n    ============")
                for index, product in enumerate(product_list, start=1):
                    print(f"    {index}- {product}")
                    options.append(index)
                    
                while True:
                    edit_index_product = int(input("\nplease write the product number you want to delete: "))
                    
                    if edit_index_product in options:
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
                options.clear()
                print("\n    Product List\n    ============")
                for index, product in enumerate(product_list, start=1):
                    print(f"    {index}- {product}")
                    options.append(index)
                while True:
                    delete_index_product = int(input("please write the product number: "))
                    if delete_index_product in options:
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
                    
            else:
                print("invalid option. please select a number from the options above")
                time.sleep(1)
    else:
        print("invalid option. please select a number from the options above")
        time.sleep(1)