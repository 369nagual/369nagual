import pymongo


def find_element(numbers):
    return list(collection.find())[numbers]


connection = pymongo.MongoClient("mongodb://localhost:27017")
database = connection.sensitive_data
collection = database.data

# find by ObjectId
# ObjectId() #1
# hh = collection.find({"_id": ObjectId("62bb3c6f4f1bee1bdcd0529d")})[0]
