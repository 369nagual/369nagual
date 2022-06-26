import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017")
database = connection.sensitive_data
collection = database.data

data = list(collection.find())[0]
