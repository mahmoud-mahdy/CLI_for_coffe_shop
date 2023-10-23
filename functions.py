import time

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

#check name is valid
def check_valid_name(name):
    """
    if name is valid return True,
    if name is not valid (blank) return False.
    """
    if name == "":
        print("process has been cancelled, name cant be blank.")
        time.sleep(1)
        return False
    return True

#check price is valid
def check_valid_price(price):
    """
    if price is float >= 0  return True,
    else return False.
    """
    try:
        price = float(price)
        if price >= 0:
            return True
        else:
            print("process has been cancelled, Price must be a non-negative number.")
            time.sleep(1)
            return False
    
    except ValueError:
        print("process has been cancelled, Please enter a numeric value.")
        time.sleep(1)
        return False

#check phone number is valid
def check_valid_phone_number(phone):
    """
    return true if phone number is valid (10 numbers)
    else return false
    """
    try:
        phone = int(phone)
        if len(str(phone)) == 10:
            return True
        else:
            print("process has been cancelled, Phone number must be 10 numbers.")
            time.sleep(1)
            return False
    except ValueError:
        print("process has been cancelled, Phone number must be 10 numbers.")
        time.sleep(1)
        return False