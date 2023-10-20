# display main menu
def display_main_menu():
    print("""
    Coffe Shop Menu
    ===============
    1- Product menu
    2- couriers menu
    3- Orders menu
    0- Exit app 
          """)
    
# display Product menu
def display_product_menu():
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
def display_courier_menu():
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
def display_orders_menu():
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
    
# display product lists
def display_products_list(products_list, valid_options):
    print("\n    Product List\n    ============")
    for index, product in enumerate(products_list, start=1):
        name = product['name']
        price = product['price']
        print(f"    {index}- {name.ljust(12)} {price:.2f}")
        print("    "+'-' * len(f"{index}- {name.ljust(12)} {price:.2f}"))
        valid_options.append(index)
        
def check_valid_name(new_product_name):
    while True:
        if new_product_name == "":
            print("Invalid price. Please enter a valid number.")
            time.sleep(1)
        else:
            return new_product_name