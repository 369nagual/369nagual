import pymongo
from bson import ObjectId


def find_element(numbers):
    return list(collection.find())[numbers]


def insert_new_element(obj):
    collection.insert_one(obj)


def delete_last_element():
    element = list(collection.find())[-1]
    collection.delete_one({'_id': ObjectId(element["_id"])})


connection = pymongo.MongoClient("mongodb://localhost:27017")
database = connection.sensitive_data
collection = database.data

# find by ObjectId
# ObjectId() #1
# hh = collection.find({"_id": ObjectId("62bb3c6f4f1bee1bdcd0529d")})[0]
