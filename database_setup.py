from dotenv import load_dotenv
import os
import pymysql
import json

#import products list
with open("data/products_list.json", 'r') as file:
    products_list = json.load(file)

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
    # cursor.execute("""CREATE TABLE IF NOT EXISTS products_table (
    # ProductsID int NOT NULL AUTO_INCREMENT,
    # ProductsName varchar(255) NOT NULL,
    # ProductPrice FLOAT NOT NULL,
    # PRIMARY KEY (ProductsID));""")
    
    #? inserting the data
    for product in products_list:
        cursor.execute("""INSERT INTO products_table (ProductsName, ProductPrice)
            VALUES (%s, %s)
        """, (product["name"], product["price"]))
        print(product)
    
    # Commit the changes to the database
    conn.commit()
    print("Data inserted successfully.")


except pymysql.Error as err:
    print(f"Error: {err}")


finally:
    if 'conn' in locals() and conn.open:
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
        