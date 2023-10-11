import psycopg2

#conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=12345678")
#cur = conn.cursor()
#conn.set_session(autocommit=True)

#cur.execute("create database myfirstdb")
#conn.close()

conn = psycopg2.connect("host=127.0.0.1 dbname=myfirstdb user=postgres password=12345678")
cur = conn.cursor()
conn.set_session(autocommit=True)
#cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar, age int, gender varchar, subject varchar, marks int);")

#sql_insert = "INSERT INTO students (student_id, name, age, gender, subject, marks) VALUES (%s, %s, %s, %s, %s, %s)"
#data = (1, "Raj", 23, "Male", "Python", 85)
#cur.execute(sql_insert, data)

#sql_insert = "INSERT INTO students (student_id, name, age, gender, subject, marks) VALUES (%s, %s, %s, %s, %s, %s)"
#data = (2, "Priya", 22, "Female", "Python", 86)
#cur.execute(sql_insert, data)


cur.execute("SELECT * FROM students;")
row = cur.fetchone()
while row:
    print(row)
    row = cur. fetchone()
    
cur.close()
conn.close()
