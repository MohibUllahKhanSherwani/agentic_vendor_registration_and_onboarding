import os
from pymongo import MongoClient
from VendorRegistrationAndOnboarding.utils.utilities import load_env
load_env()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("APP_NAME")

print(MONGO_URI)
class MongoHandler:

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]

    def get_db(self):
        return self.db
    
mongo_handler = MongoHandler()
db = mongo_handler.get_db()