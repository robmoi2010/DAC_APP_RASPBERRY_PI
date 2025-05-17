from enum import Enum
import repo.storage as storage
from dsp.io import CURRENT_INPUT_ID, CURRENT_MAIN_OUTPUT_ID
from dsp.router import MAINS_INPUT_SINK_ID, MAINS_OUTPUT_SOURCE_ID
import configs.app_config as configuration
import util.communication as comm

SOUND_MODE_ID = "SOUND_MODE"
config = configuration.getConfig()["ADAU1452"]["ADDR"]


class SoundMode(Enum):
    PURE_DIRECT = (0,)
    SEMI_PURE_DIRECT = (1,)
    DSP = 2


def get_current_sound_mode():
    return storage.read(SOUND_MODE_ID)


def update_sound_mode(mode):
    storage.write(SOUND_MODE_ID, mode)


def handlePureDirect():
    # get current input
    current_input = storage.read(CURRENT_INPUT_ID)
    # get current mains output
    current_output = storage.read(CURRENT_MAIN_OUTPUT_ID)

    # set source and sink to each other
    storage.write(MAINS_OUTPUT_SOURCE_ID, current_input)
    storage.write(MAINS_INPUT_SINK_ID, current_output)
    # update routing on DSP

    # Get current register value and update parts that need updating
    current = comm.read(config["ADDR"], config["SOUT_SOURCE0"])
    newValue = current & ~(1 << 2)
    newValue = newValue & ~(1 << 1)
    newValue = newValue | (1 << 0)

    comm.write(newValue)
    
def handleSemiPureDirect():
    pass
    
def getSourceName(source)
    pass
