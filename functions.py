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
        print(f"    {index}- {name.ljust(12)} {price:.2f}£")
        print("    "+'-' * len(f"{index}- {name.ljust(12)} {price:.2f}"))
        valid_options.append(index)

# display courier list
def display_courier_list(courier_list, valid_options):
    print("\n    courier list\n    ============")
    for index, courier in enumerate(courier_list, start=1):
        name = courier['name']
        phone = courier['phone']
        print(f"    {index}- {name.ljust(12)} {phone}")
        print("    "+'-' * len(f"{index}- {name.ljust(12)} {phone}"))
        valid_options.append(index)

# display order list
def display_order_list(orders_list, valid_options):
    print("\nOrder List")
    print("=" * 50)
    for index, order in enumerate(orders_list, start=1):
        print(f"Order {index}:")
        print(f"Customer Name:      {order['customer_name']}")
        print("-" * 50)
        print(f"Customer Address:   {order['customer_address']}")
        print("-" * 50)
        print(f"Customer Phone:     {order['customer_phone']}")
        print("-" * 50)
        print(f"Courier:            {order['courier']}")
        print("-" * 50)
        print(f"Status:             {order['status']}")
        print("-" * 50)
        print(f"Items:              {order['items']}")
        print("=" * 50)
        valid_options.append(index)
        
#check name is valid
def check_valid_name(name):
    """
    if name is valid return True,
    if name is not valid (blank) return False.
    """
    if name == "":
        print("process has been cancelled, input cant be blank.")
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
        p = int(phone)
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

#check courier number is valid
def check_valid_courier(courier):
    try:
        courier = int(courier)
        if courier < 0:
            print("process has been cancelled, courier number must be non negative numeric number.")
            time.sleep(1)
            return False
        return True
    except ValueError:
        print("process has been cancelled, courier number must be non negative numeric number.")
        time.sleep(1)
        return False