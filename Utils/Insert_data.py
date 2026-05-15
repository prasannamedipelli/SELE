import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="saucedemodb"
)

values = ("vishal", 7500)

print("connected with db")

cursor = conn.cursor()

sql = """INSERT INTO employee (name,salary) VALUES(%s,%s)"""

cursor.execute(sql, values)

conn.commit()

print("data inserted")

conn.close()

#teardown