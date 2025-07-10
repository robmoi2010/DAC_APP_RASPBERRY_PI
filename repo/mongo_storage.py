from pymongo import MongoClient
from configs import app_config
from registry.register import register
from repo.init_data import init_data


@register
class MongoStorage:
    url = app_config.getConfig()["MONGODB"]["URL"]

    def __init__(self):
        # super().__init__()
        # Connect to MongoDB
        self.client = MongoClient("mongodb://" + self.url)

        # Access the database (creates it if it doesn't exist)
        self.db = self.client.dac
        self.records = self.db.records

    def read(self, key):
        record = self.records.find_one({key: {"$exists": True}})
        if record is not None:
            return record[key]
        else:
            return None

    def write(self, key, value):
        r = self.read(key)
        return self.records.update_one({key: r}, {"$set": {key: value}})

    def create(self, key, value):
        return self.records.insert_one({key: value})

    def initialize(self):
        print("initializing...")
        for key, value in init_data.items():
            if self.read(key) is None:
                self.create(key, value)
                print("inserting record")
