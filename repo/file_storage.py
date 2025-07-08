import json
import logging
from pathlib import Path
from registry.register import register

FILE_NAME = Path(__file__).parent / "../configs/Storage.json"


@register
class FileStorage:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def read(self, addr):
        try:
            with open(FILE_NAME, "r") as f:
                data = json.load(f)
            return data[addr]
        except Exception as e:
            self.logger.error(e)

    def write(self, addr, val):
        try:
            with open(FILE_NAME, "r") as f:
                data = json.load(f)
            data[addr] = val
            with open(FILE_NAME, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            self.logger.error(e)

    def initialize(self):
        print("initializing...")
        data = {
            "KNOB_BUTTON_MODE": 0,
            "DISABLE_VOLUME": 0,
            "CURRENT_FILTER": 2,
            "CURRENT_DAC_MODE": 2,
            "DAC_MUTED": 0,
            "CURRENT_VOLUME": 128.5,
            "CURRENT_MUSES_VOLUME": -25,
            "CURRENT_INPUT": 4,
            "CURRENT_MAIN_OUTPUT": 3,
            "CURRENT_SUBWOOFER_OUTPUT": 2,
            "MAINS_INPUT_SINK": 2,
            "SUBWOOFER_INPUT_SINK": 2,
            "SUBWOOFER_OUTPUT_SOURCE": 2,
            "MAINS_OUTPUT_SOURCE": 1,
            "SOUND_MODE": 2,
            "SECOND_ORDER_COMPENSATION_ENABLED": 1,
            "THIRD_ORDER_COMPENSATION_ENABLED": 1,
            "THIRD_ORDER_COEFFICIENTS_STORED": 0,
            "SECOND_ORDER_COEFFICIENTS_STORED": 0,
            "CURRENT_VOLUME_DEVICE": 0,
            "VOLUME_ALGORITHM": 0,
            "SECOND_ORDER_ENABLE_COEFFICIENTS_1": "0110",
            "SECOND_ORDER_ENABLE_COEFFICIENTS_2": "0110",
            "SECOND_ORDER_ENABLE_COEFFICIENTS_3": "0110",
            "SECOND_ORDER_ENABLE_COEFFICIENTS_4": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_1": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_2": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_3": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_4": "0110",
            "CURRENT_ALPS_VOLUME": 0,
            "OVERSAMPLING_ENABLED": 1,
        }
        for key, value in data.items():
            if self.read(key) is None:
                self.write(key, value)
                print("inserting record")
