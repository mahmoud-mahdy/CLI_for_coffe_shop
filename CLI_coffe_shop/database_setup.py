from dotenv import load_dotenv
import os
import pymysql
import json


# import orders list
with open("data/orders_list.json", 'r') as file:
    orders_list = json.load(file)

# #import products list
# with open("data/products_list.json", 'r') as file:
#     products_list = json.load(file)
    
# #import courier list
# with open("data/couriers_list.json", 'r') as file:
#     courier_list = json.load(file)


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
    
    
    ##? Execute SQL queries using the cursor
    #? making the table
    # cursor.execute("""CREATE TABLE IF NOT EXISTS orders_table (
    # OrdersID int NOT NULL AUTO_INCREMENT,
    # CustomerName varchar(255) NOT NULL ,
    # CustomerAddress varchar(255) NOT NULL,
    # CustomerPhone varchar(15) NOT NULL,
    # Courier int NOT NULL,
    # Status varchar(255) NOT NULL,
    # Items varchar(255),
    # PRIMARY KEY (OrdersID));
    # """)
    
    #? inserting the data
    # for courier in courier_list:
    #     cursor.execute("""INSERT INTO couriers_table (CouriersName, CouriersPhone)
    #         VALUES (%s, %s)
    #     """, (courier["name"], courier["phone"]))
    #     print(courier)
    
    # for order in orders_list:
    #     cursor.execute("""INSERT INTO orders_table (CustomerName, CustomerAddress, CustomerPhone, Courier, Status, Items)
    #                 VALUES (%s,%s,%s,%s,%s,%s)""", (order["customer_name"], order["customer_address"], order["customer_phone"], order["courier"], order["status"], order["items"]))
    
    
    # Commit the changes to the database
    conn.commit()
    print("committed")


except pymysql.Error as err:
    print(f"Error: {err}")


finally:
    if 'conn' in locals() and conn.open:
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
        