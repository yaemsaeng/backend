from pymongo import MongoClient
db_connection = MongoClient("mongodb+srv://boat:1234@cluster0.rmsa1et.mongodb.net/")
db = db_connection.myDB
collection = db["test"]