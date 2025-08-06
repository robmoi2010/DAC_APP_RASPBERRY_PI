import json
import logging
from pathlib import Path
from registry.register import register
from repo.init_data import init_data


@register
class FileStorage:
    FILE_NAME = Path(__file__).parent / "../configs/Storage.json"

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def read(self, addr):
        try:
            with open(self.FILE_NAME, "r") as f:
                data = json.load(f)
            return data[addr]
        except Exception as e:
            self.logger.error(e)

    def write(self, addr, val):
        try:
            with open(self.FILE_NAME, "r") as f:
                data = json.load(f)
            data[addr] = val
            with open(self.FILE_NAME, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            self.logger.error(e)

    def initialize(self):
        print("initializing...")
        for key, value in init_data.items():
            if self.read(key) is None:
                self.write(key, value)
                print("inserting record")
