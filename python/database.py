import pymongo
from bson import ObjectId

def insert_new_element(obj):
    collection.insert_one(obj)


connection = pymongo.MongoClient("mongodb://localhost:27017")
database = connection.sensitive_data
collection = database.data

data = list(collection.find())[0]
d = data
ObjectId()
hh = collection.find({"_id": ObjectId("62bb3c6f4f1bee1bdcd0529d")})[0]
data.update(hh)
# collection.delete_many({"_id": {"$nin": [ObjectId("62bb3c6f4f1bee1bdcd0529d"),
#                                        ObjectId("62b7d671a651f0d85aad28ab")]}})
print(data)
