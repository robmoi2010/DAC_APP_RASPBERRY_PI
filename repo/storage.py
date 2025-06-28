from enum import Enum

from registry.register import register
from repo.file_storage import FileStorage
from repo.mongo_storage import MongoStorage
import configs.app_config as app_config


class STORAGE(Enum):
    FILE = 0
    MONGODB = 1


@register
class Storage:
    def __init__(self, file_storage: FileStorage, mongo_storage: MongoStorage):
        default_db = app_config.getConfig()["SYSTEM"]["STORAGE"]
        if default_db == 0:
            self.default_storage = file_storage
        else:
            self.default_storage = mongo_storage

    def write(self, addr, val):
        return self.default_storage.write(addr, val)

    def read(self, addr):
        return self.default_storage.read(addr)
