from enum import Enum

from registry.register import register
from repo.file_storage import FileStorage
from repo.mongo_storage import MongoStorage
import configs.app_config as app_config
from repo.sql_storage import SqlStorage


class STORAGE(Enum):
    FILE = 0
    MONGODB = 1
    SQL = 2


@register
class Storage:
    def __init__(
        self,
        file_storage: FileStorage,
        mongo_storage: MongoStorage,
        sql_storage: SqlStorage,
    ):
        default_db = app_config.getConfig()["SYSTEM"]["STORAGE"]
        if default_db == STORAGE.FILE.value:
            self.default_storage = file_storage
        elif default_db == STORAGE.MONGODB.value:
            self.default_storage = mongo_storage
        elif default_db == STORAGE.SQL.value:
            self.default_storage = sql_storage

    def write(self, addr, val):
        return self.default_storage.write(addr, val)

    def read(self, addr):
        return self.default_storage.read(addr)
