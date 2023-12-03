import psycopg2
import os

def setup_db_connection():
    connection = psycopg2.connect(
        host='localhost',
        database='sprint1_db',
        user='root',
        password='root'
    )
    return connection
# Example query
try:
    # Establish a connection to the database
    connection = setup_db_connection()
    # Create a cursor object
    cursor = connection.cursor()
    # Example query
    cursor.execute("SELECT version();")
    # Commit changes (if any)
    connection.commit()
    # Fetch and print the result
    result = cursor.fetchone()
    # print("PostgreSQL Database Version:", result)
except Exception as e:
    print("Error: ", e)
