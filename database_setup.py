import pymysql

host = "3306"
user = "root"
password = "password"
database = "your_database"

# Establish a connection to the MySQL server
try:
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if conn.open:
        print("Connected to the MySQL database")

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Execute SQL queries using the cursor
    # For example, fetching data from a table:
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

except pymysql.Error as err:
    print(f"Error: {err}")

finally:
    if 'conn' in locals() and conn.open:
        cursor.close()
        conn.close()
        print("MySQL connection is closed")kuhuhk
        