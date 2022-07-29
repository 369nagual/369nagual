import pymongo
from bson import ObjectId


def find_element(numbers):
    return list(collection.find())[numbers]


def insert_new_element(obj, value="DefaultValue"):
    if isinstance(obj, dict):
        collection.insert_one(obj)
    else:
        collection.insert_one({value: obj})


def delete_last_element():
    element = list(collection.find())[-1]
    collection.delete_one({'_id': ObjectId(element["_id"])})
    print(list(collection.find()))
    print(len(list(collection.find())))


def insert_in_last_element():
    element = list(collection.find())[-1]
    collection.find(element)


connection = pymongo.MongoClient("mongodb://localhost:27017")
database = connection.sensitive_data
collection = database.data

# insert_new_element("just a value", "value")

# print(find_element(-1))
# for i in range(len(list(collection.find()))):
#     print(list(collection.find())[i])

collection.update_one({"_id": ObjectId("62cf7370ee0a6a4f8e5dcafe")}, {"$set": {"DefaultValue": "Value"}}, upsert=True)
# print(list(collection.find({"_id": ObjectId("62cf7370ee0a6a4f8e5dcafe")})))
# delete_last_element()
