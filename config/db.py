from pymongo import MongoClient
db_connection = MongoClient("mongodb://localhost:27017")
db = db_connection.myDatabase
collection = db["food"]