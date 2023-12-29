import psycopg2
import os
from dotenv import load_dotenv

import csv
def open_project_csv(file):
    try:
        with open(file, "r") as csvfile:
            orders = csv.DictReader(csvfile, fieldnames=['date','location','name','order', 'price', 'payment metod'])
            orders_list=[]
            for order in orders:
                orders_list.append(order)
        return orders_list
    except FileNotFoundError:
        print("Error. File not found.")

data=open_project_csv("chesterfield_25-08-2021_09-00-00.csv")


load_dotenv()
host_name = os.environ.get("postgres_host")
database_name = os.environ.get("postgres_db")
user_name = os.environ.get("postgres_user")
user_password = os.environ.get("postgres_pass")

def setup_db_connection(host=host_name,
                        user=user_name,
                        password=user_password,
                        db=database_name):

    connection = psycopg2.connect(
        host=host,
        database=db,
        user=user,
        password=password
    )
    return connection

# Example query
try:
    # Establish a connection to the database
    connection = setup_db_connection()

    # Create a cursor object
    cursor = connection.cursor()

    # Example query
    #cursor.execute("SELECT version();")
#def add_to_database_customesr:
#def load_customers():

    # def load_customers():
    #     cursor=connection.cursor()
    #     for customer in data:
    #         cursor.execute('''insert into customers(name, location) values(%s,%s)''',(customer['name'],customer['location']))
    #         connection.commit()
    # load_customers()

    # sql=('''
    #     insert into customers (name, location)
    #     values (%s, %s)
    #     ''')
    # data_values=(data["name"], data["location"])
    # cursor.execute(sql, data_values)


    # for row in df.itertuples():
    #     cursor.execute('''
    #             INSERT INTO test_db (product_id, product_name, price)
    #             VALUES (?,?,?)
    #             ''',
    #             row.product_id,
    #             row.product_name,
    #             row.price
    #             )

    # Commit changes (if any)
    connection.commit()

    # Fetch and print the result
    result = cursor.fetchone()
    print("PostgreSQL Database Version:", result)

except Exception as e:
    print("Error: ", e)

finally:
    connection = setup_db_connection()

    # Create a cursor object
    cursor = connection.cursor()

    # Close the cursor and connection
    # if cursor:
    #     cursor.close()
    # if connection:
    #     connection.close()