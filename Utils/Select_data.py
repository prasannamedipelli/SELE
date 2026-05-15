#create , delete, update , retrieve
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "root",
    database = "saucedemodb"
)
cursor = conn.cursor()
cursor.execute("SELECT * from employee")
records = cursor.fetchall()
for row in records:
    print (row)
    
conn.close()
#free connection    tear down
    