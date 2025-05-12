from pymongo import MongoClient
import configs.app_config as app_config

url = app_config.getConfig()["MONGODB"]["URL"]
# Connect to MongoDB
client = MongoClient("mongodb://" + url)

# Access the database (creates it if it doesn't exist)
db = client.dac
records = db.records


def read(key):
    return records.find_one({key: {"$exists": True}})


def update(key, value):
    r = read(key)
    return records.update_one({key: r[key]}, {"$set": {key: value}})


def create(key, value):
    return records.insert_one({key: value})


def initialize():
    data = {
        "KNOB_BUTTON_MODE": 1,
        "DISABLE_VOLUME": 0,
        "CURRENT_FILTER": 4,
        "CURRENT_DAC_MODE": 2,
        "DAC_MUTED": 0,
        "CURRENT_VOLUME": 158.33221831520527,
    }
    for key, value in data.items():
        if read(key) == None:
            create(key, value)
            print("inserting record")
