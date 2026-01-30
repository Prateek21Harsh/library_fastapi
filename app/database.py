import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))
db = client["library"]

books_collection = db["books"]
members_collection = db["members"]
transactions_collection = db["transactions"]