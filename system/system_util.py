from enum import Enum

from configs import app_config


config = app_config.getConfig()
irConfig = config["IR_REMOTE"]["BUTTON_HASH"]
SOUND_MODE_ID = "SOUND_MODE"
SUBWOOFER_OUTPUT_SOURCE_ID = "SUBWOOFER_OUTPUT_SOURCE"
class BUTTON(Enum):
    UP = 0
    DOWN = 1
    POWER = 2
    OK = 3
    BACK = 4
    VOLUME_UP = 5
    VOLUME_DOWN = 6
    MUTE = 7
