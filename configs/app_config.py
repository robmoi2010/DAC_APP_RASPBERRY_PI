import json
import logging

from registry.register import register


@register
class Config:
    FILE_NAME = "configs/Configs.json"
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.config = self.getConfig()

    def getConfig(self):
        try:
            with open(Config.FILE_NAME, "r") as f:
                return json.load(f)
        except Exception as e:
            Config.logger.error(e)
            raise e
