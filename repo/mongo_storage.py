from pymongo import MongoClient
from configs import app_config
from registry.register import register


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
        data = {
            "KNOB_BUTTON_MODE": 0,
            "DISABLE_VOLUME": 0,
            "CURRENT_FILTER": 2,
            "CURRENT_DAC_MODE": 2,
            "DAC_MUTED": 0,
            "CURRENT_VOLUME": 128.5,
            "CURRENT_MUSES_VOLUME": -25,
            "CURRENT_INPUT": 4,
            "CURRENT_MAIN_OUTPUT": 3,
            "CURRENT_SUBWOOFER_OUTPUT": 2,
            "MAINS_INPUT_SINK": 2,
            "SUBWOOFER_INPUT_SINK": 2,
            "SUBWOOFER_OUTPUT_SOURCE": 2,
            "MAINS_OUTPUT_SOURCE": 1,
            "SOUND_MODE": 2,
            "SECOND_ORDER_COMPENSATION_ENABLED": 1,
            "THIRD_ORDER_COMPENSATION_ENABLED": 1,
            "THIRD_ORDER_COEFFICIENTS_STORED": 0,
            "SECOND_ORDER_COEFFICIENTS_STORED": 0,
            "CURRENT_VOLUME_DEVICE": 0,
            "VOLUME_ALGORITHM": 0,
            "SECOND_ORDER_ENABLE_COEFFICIENTS_1": "0110",
            "SECOND_ORDER_ENABLE_COEFFICIENTS_2": "0110",
            "SECOND_ORDER_ENABLE_COEFFICIENTS_3": "0110",
            "SECOND_ORDER_ENABLE_COEFFICIENTS_4": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_1": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_2": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_3": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_4": "0110",
            "CURRENT_ALPS_VOLUME": 0,
            "OVERSAMPLING_ENABLED": 1,
        }
        for key, value in data.items():
            if self.read(key) is None:
                self.create(key, value)
                print("inserting record")
