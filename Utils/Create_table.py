import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "root",
    database = "saucedemodb"
)
cursor = conn.cursor()
query = """
    CREATE TABLE EMPLOYEE (
    ID INT AUTO_INCREMENT PRIMARY KEY, 
    NAME VARCHAR(100),
    SALARY FLOAT
    )
    """
cursor.execute(query)
print("table created")
conn.close()