import sys
import clipboard
from database import *


def create_once():
    collection.update_one({"clipboard": []}, {"$set": {"exists": "true"}}, upsert=True)


create_once()

print(argv := sys.argv[1:])
if len(sys.argv) >= 2:
    print("Great")
    if argv[0] == "insert":
        print("Insert")
        collection.update_one({"_id": ObjectId("62cf88cdcc0698402d8a7106")},
                              {"$push": {"clipboard": clipboard.paste()}}, upsert=True)
    elif argv[0] == "show":
        print(collection.find_one({"_id": ObjectId("62cf88cdcc0698402d8a7106")})["clipboard"])
    else:
        print("Please enter different command!")
else:
    print("Pass one command please!")
