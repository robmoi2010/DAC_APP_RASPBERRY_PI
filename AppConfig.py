import json
import logging

logger = logging.getLogger(__name__)
#get config for certain root e.g DAC
def getConfig():
    try:
        with open ("Configs.json", "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(e)
    
    