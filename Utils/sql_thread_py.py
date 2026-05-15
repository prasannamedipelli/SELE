import threading
import mysql.connector

def fetch_data(table_name):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "saucedemodb"
    )
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")

    data = cursor.fetchall()

    print(f"{table_name} rows : ", len(data))

    conn.close()

t1= threading.Thread(target=fetch_data, args=("workers",))
t2= threading.Thread(target=fetch_data, args=("employee",))
t3= threading.Thread(target=fetch_data, args=("login_users",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()