import json
import logging


FILE_NAME = "configs/Configs.json"
logger = logging.getLogger(__name__)


# future enhancement, load and access from memory
def getConfig():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(e)
