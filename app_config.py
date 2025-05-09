import json
import logging
from pathlib import Path


FILE_NAME = Path(__file__).parent/ "configs/Configs.json"
logger = logging.getLogger(__name__)
# future enhancement, load and access from memory
def getConfig():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(e)
