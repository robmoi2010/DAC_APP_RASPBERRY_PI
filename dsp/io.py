from enum import Enum
from registry.register import register
from repo.storage import Storage

CURRENT_INPUT_ID = "CURRENT_INPUT"
CURRENT_MAIN_OUTPUT_ID = "CURRENT_MAIN_OUTPUT"
CURRENT_SUBWOOFER_ID = "CURRENT_SUBWOOFER_OUTPUT"


class Input(Enum):
    TOSLINK = 0
    I2S_INPUT0 = 1
    I2S_INPUT1 = 2
    I2S_INPUT2 = 3
    I2S_INPUT3 = 4


class Output(Enum):
    COAX_OUTPUT = 0
    I2S_OUTPUT0 = 1
    I2S_OUTPUT1 = 2
    I2S_OUTPUT2 = 3
    I2S_OUTPUT3 = 4


@register
class DspIO:
    def __init__(self, storage: Storage):
        self.storage = storage

    def update_current_input(self, input):
        # Store current input to storage
        self.storage.write(CURRENT_INPUT_ID, int(input))

    def get_current_input(self):
        return self.storage.read(CURRENT_INPUT_ID)

    def update_main_output(self, output):
        self.storage.write(CURRENT_MAIN_OUTPUT_ID, int(output))

    def get_current_main_output(self):
        return self.storage.read(CURRENT_MAIN_OUTPUT_ID)

    def update_subwoofer_output(self, output):
        self.storage.write(CURRENT_SUBWOOFER_ID, int(output))

    def get_current_subwoofer_output(self):
        return self.storage.read(CURRENT_SUBWOOFER_ID)
