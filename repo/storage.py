#import json
import logging

import repo.mongo_repo as mongo_repo
from pathlib import Path


FILE_NAME = Path(__file__).parent / "../configs/Storage.json"
logger = logging.getLogger(__name__)


def write(addr, val):
    try:
        # with open(FILE_NAME, "r") as f:
        #     data = json.load(f)
        # data[addr] = val
        # with open(FILE_NAME, "w") as f:
        #     json.dump(data, f, indent=4)
        mongo_repo.update(addr, val)
    except Exception as e:
        logger.error(e)


def read(addr):
    try:
        # with open(FILE_NAME, "r") as f:
        #     data = json.load(f)
        #     return data[addr]
        return mongo_repo.read(addr)[addr]
    except Exception as e:
        logger.error(e)
