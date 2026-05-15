from pymongo import MongoClient
import pandas as pd

# connect to mongodb
client =MongoClient(
    "mongodb://localhost:27017/"
)

db = client["company_db"]

employees = db["employees"]
print("mongodb connected")

sample_data= [
    {
        "emp_id" :101,
        "name" : "vivek",
        "department": "qa"
        
    },
    {
         "emp_id" :108,
        "name" : "himanshu",
        "department": "developer"
    },
    {
         "emp_id" :109,
        "name" : "vivek",
        "department": "qa"
        
    },
    
    {
         "emp_id" :101,
        "name" : "vivek",
        "department": "qa"
        
    }
]

employees.insert_many(sample_data)
print("Sample data inserted")

#read data
data = list(employees.find())
print("mongodb records")
for d in data:
    print(d)
    
## convert to pandas dataframe

df= pd.DataFrame(data)

print("Pandas dataframe")
print(df)

# highes salary
high_salary = df[df["salary"] == "100"]

print(high_salary)

#group

summary = df.groupby('department')['salary'].mean()
print(summary)