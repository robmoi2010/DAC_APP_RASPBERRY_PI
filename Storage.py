import json
import logging

FILE_NAME = "Storage.json"
logger = logging.getLogger(__name__)


def write(addr, data):
    try:
        with open(FILE_NAME, "r") as f:
            data = json.read(f)
    except Exception as e:
        logger.error(e)
    data[addr] = data
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logger.error(e)


def read(addr):
    try:
        with open(FILE_NAME, "r") as f:
            data = json.read(f)
            return data[addr]
    except Exception as e:
        logger.error(e)
