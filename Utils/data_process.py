import mysql.connector
import numpy as np
conn = mysql.connector.connect(
    
    host ="localhost",
    user="root",
    password="root",
    database="saucedemodb"
    
)

cusors = conn.cursor()

cusors.execute("SELECT SALARY FROM WORKERS")

data = cusors.fetchall()
# convert tupple data into Numpy array

print(data)

salary_array = np.array(data)

print("*******array format*******")
print(salary_array)

#apply operation

# average salary
print("average salary of workers " ,np.mean(salary_array))
print(" Maximum salary ",np.max(salary_array))