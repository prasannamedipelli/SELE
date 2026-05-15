import mysql.connector
#connect to mysql
# create a connection object  conn
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "ecommerce"
)
print("Connected successfully")
#close connection
conn.close()