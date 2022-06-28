#!/usr/bin/env python3
from pymongo import MongoClient
import time
import os
import bcrypt


def update_password(col, new_password):
    fltr = {"vk_login": "vitkashubin@gmail.com"}
    update_to = {"$set": {"vk_password": new_password}}
    u = col.update_one(fltr, update_to)
    return find_password(fltr={"vk_password": new_password}, find="vk_password")


def find_password(fltr=None, find=None):
    if fltr is None:
        fltr = {"vk_login": "vitkashubin@gmail.com"}
    if find is True:
        return collection.find(fltr)[0][find]
    elif find == "object":
        return collection.find(fltr)[0]
    else:
        return collection.find(fltr)[0]["vk_password"]


connection = MongoClient("mongodb://localhost:27017")

db = connection.sensitive_data
collection = db.data

# password = collection.find({"vk_login": "vitkashubin@gmail.com"})[0]["vk_password"].encode("utf-8")

# password = collection.find({"vk_login": "vitkashubin@gmail.com"})[0]["vk_password"]
filter_find = [{"git_login": "369nagual"}, "vk_login"]
password = find_password(*filter_find)

print(password)

update_password(collection, "Yustas2008/2020")
