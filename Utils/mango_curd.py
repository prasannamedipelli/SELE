from pymongo import MongoClient
# connect mongodb
client =MongoClient(
    "mongodb://localhost:27017/"
)
print("MongoDB connected")
db = client["company_db"]
employees = db["employees"]
#mongodb uses lazy creation  , empty database not stored
#create a collection
employee ={
    "name" : "yogesh",
    "salary" : "100"
}
employees.insert_one(employee)
print("database and collection created successfully")
print("database created")

#data retrieval
print("read operation started**")

all_employees = employees.find()

for emp in all_employees:
    print(emp)
    
## update operation

employees.update_one(
    {"name":"yogesh"},
    {
        "$set": {
            "salary": "senior qa"
        }
    }
)

print("employee updated")

print("delete operation  ***")
employees.delete_one({"name": "vishal"})

print("deletion done")
client.close()