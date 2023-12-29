from connection import connection
import re
import csv
import pandas as pd
import datetime
import time

def open_project_csv(file):
    try:
        with open(file, "r") as csvfile:
            orders = csv.DictReader(csvfile, fieldnames=['date','location','name','order', 'price', 'payment_method'])

            orders_list=[]
            for order in orders:

                orders_list.append(order)
            return orders_list
    except FileNotFoundError:
        print("Error. File not found.")

data=open_project_csv("chesterfield_25-08-2021_09-00-00.csv")


def load_customers():
    cursor=connection.cursor()
    for customer in data:
        cursor.execute('''insert into customers(name, location) values(%s,%s)''',(customer['name'],customer['location']))
        connection.commit()


def load_orders():
    print('Loading data to Orders')
    time.sleep(2)
    cursor=connection.cursor()
    data=open_project_csv("chesterfield_25-08-2021_09-00-00.csv")
    cursor.execute('select customer_id from customers order by customer_id asc limit 1')
    customer_id=cursor.fetchone()[0]
    if customer_id==None:
        customer_id=1
    print('Loading data to Order items')
    time.sleep(2)

    for index,order in enumerate(data,start=customer_id):
        # loading data to orders table

        cursor.execute(''' insert into orders (date,customer_id,payment_method,total_price) values (%s,%s,%s,%s)
                       ''',[datetime.datetime.now(),index,order['payment_method'],order['price']])
        connection.commit()
        # loading data to order_items table

        products=products_preprocessing([order])
        for product in products:

            cursor.execute('select product_id from products where name=(%s)',[product['name']]) # getting product id products table
            product_id=cursor.fetchone()[0]
            df=pd.DataFrame(products)
            count_value=(df['name'] == product['name']).sum() # counting product quanity form given order

            cursor.execute('''select order_id  from orders ORDER BY order_id DESC LIMIT 1;''') # getting the order id for latest order
            order_id=cursor.fetchone()[0]
            # storing data into order item table

            cursor.execute('''insert into order_items (order_id,product_id,quantity) values(%s,%s,%s)''',(int(order_id),int(product_id),int(count_value)))
            connection.commit()
    print("Done")

def load_products():
    print('Loading Product to Database')
    time.sleep(2)
    data=open_project_csv("chesterfield_25-08-2021_09-00-00.csv")
    print('Performing Tranformation')
    time.sleep(2)
    data=products_preprocessing(data)
    df=pd.DataFrame(data)
    df=df.drop_duplicates(subset=['name', 'price'])
    products=df.to_dict('records')
    cursor=connection.cursor()


    for product in products:
        cursor.execute('''insert into products (name,total_price) values (%s,%s)
                       ''',[product['name'],product['price']])
        connection.commit()


def products_preprocessing(data):

    """
    1): converted "Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45"
    to ['Regular', 'Flavoured', 'iced', 'latte', '-', 'Hazelnut', '-', '2.75,'], ['Large', 'Latte', '-', '2.45']
    2): converted ['Regular', 'Flavoured', 'iced', 'latte', '-', 'Hazelnut', '-', '2.75,'], ['Large', 'Latte', '-', '2.45']
    to [{'name': ' Regular Flavoured iced latte Hazelnut', 'price': 2.75}, {'name': ' Large Latte', 'price': 2.45}]

    returns [{'name': ' Regular Flavoured iced latte Hazelnut', 'price': 2.75}, {'name': ' Large Latte', 'price': 2.45}]
    """

    # spliting ths strings like
    # from "Regular Flavoured iced latte - Hazelnut - 2.75"
    # to ['Regular', 'Flavoured', 'iced', 'latte', '-', 'Hazelnut', '-', '2.75,']
    list_order=[order['order'].split() for order in data]
    splited_products=[]
    pattern = re.compile(r'^\d+\.\d+$')
    for order in list_order:
        for _,value in enumerate(order):
            if pattern.match(value.rstrip(',')): # matching the name to pattern
                splited_products.append(order[:order.index(value)+1]) # appending the order to
                order=order[order.index(value)+1:]

    products=[]
    for product in splited_products:
        temp_dict={'name':'',
            'price':0}

        for name in product:
            if name.isalpha():
                temp_dict['name']=temp_dict['name']+" "+name
            else:
                if name=='-':
                    continue
                else:
                    temp_dict['price']=float(name.rstrip(','))
        products.append(temp_dict)
    return products
def truncate_db():
    cursor=connection.cursor()
    sql_commands = [
    'DELETE FROM order_items',
    'DELETE FROM orders',
    'DELETE FROM customers',
    'DELETE FROM products'
    ]

     #Execute the SQL statements
    for command in sql_commands:
        cursor.execute(command)

    # Commit the changes (if needed) and close the connection
    connection.commit()


truncate_db()
load_customers()
load_products()
load_orders()