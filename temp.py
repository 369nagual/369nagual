from pymongo import MongoClient
import datetime


def create_db(mydict, db_name="main", col_name="main", date=False):
    global connection
    now = datetime.datetime.now()
    now = now.strftime("%d-%m-%Y %H:%M:%S")
    db_in = connection[db_name]
    collection_in = db_in[col_name]
    if date:
        mydict["date"] = now
    db_id = collection_in.insert_one(mydict).inserted_id
    return {"db_name": db_name, "col_name": col_name, "db_id": db_id}

    # db_dict = create_db(data, "sensitive_data", "data", date=True)
    # print(db_dict)


connection = MongoClient("localhost", 27017)
db = connection.sensitive_data
collection = db.data
data = list(db.data.find())[0]
