#!/usr/bin/env python3
from pymongo import MongoClient
import bcrypt


def update_password(new_password):
    fltr = {"vk_login": "vitkashubin@gmail.com"}
    update_to = {"$set": {"vk_password": new_password}}
    collection.update_one(fltr, update_to)
    print("Successfully updated")
    return find_password(fltr={"vk_password": new_password}, find="vk_password")


def hash_password(passwd):
    passwd = passwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(passwd, salt)
    print("Successfully generated hash")
    return hashed_password


def check_password(passwd, hashed_password):
    passwd = passwd.encode('utf-8')
    password_boolean = bcrypt.checkpw(passwd, hashed_password)
    print("Password checked successfully")
    return password_boolean


def find_password(fltr=None, find=None):
    if fltr is None:
        fltr = {"vk_login": "vitkashubin@gmail.com"}
    if find == "object":
        return collection.find(fltr)[0]
    elif find:
        return collection.find(fltr)[0][find]
    else:
        return collection.find(fltr)[0]["vk_password"]


connection = MongoClient("mongodb://localhost:27017")

db = connection.sensitive_data
collection = db.data

# password = input("Enter password for changing current password!")
# password = ""
# update_password(password)
# hashed = hash_password(password)
# print(f"Hash password: %s" % hashed)
#
# updated_password = update_password(hashed)
# print(f"Updated password: %s" % updated_password)
#
# if check_password(password, find_password()):
#     print("Login successful")
# else:
#     print("Login failed")
