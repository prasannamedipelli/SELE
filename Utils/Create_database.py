#create database
import mysql.connector
#connection with mysql
conn = mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    password = "root"
)
cursor = conn.cursor()
# this cursor  help you to execute queries
#cursor.execute("CREATE DATABASE SAUCEDEMODB")
cursor.execute("CREATE DATABASE IF NOT EXISTS SAUCEDEMODB")
print("Database created")
conn.close()