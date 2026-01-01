from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create / access database
db = client["mydatabase"]

# Create / access collection
collection = db["users"]

print("MongoDB connected successfully!")
user = {
    "name": "Roli",
    "age": 20,
    "skills": ["Python", "ML", "MongoDB"]
}

collection.insert_one(user)
print("Data inserted")
for doc in collection.find():
    print(doc)
result = collection.find_one({"name": "Roli"})
print(result)
collection.update_one(
    {"name": "Roli"},
    {"$set": {"age": 21}}
)
