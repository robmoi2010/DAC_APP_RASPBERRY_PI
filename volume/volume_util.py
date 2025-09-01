from enum import Enum
import json
import math

from model.model import ResponseModel
from services.utils.services_util import VOLUME_DISPLAY_NAME
from services.utils.ws_connection_manager import WS_TYPE


class VOL_DIRECTION(Enum):
    UP = 0
    DOWN = 1


class VOLUME_DEVICE(Enum):
    DAC = 0
    MUSES = 1
    ALPS = 2


class VOLUME_ALGORITHM(Enum):
    LINEAR = 0
    LOGARITHMIC = 1


CURRENT_DEVICE_ID = "CURRENT_VOLUME_DEVICE"
CURRENT_MUSES_VOLUME_ID = "CURRENT_MUSES_VOLUME"
CURRENT_VOLUME_ID = "CURRENT_VOLUME"
VOLUME_ALGORITHM_ID = "VOLUME_ALGORITHM"
CURRENT_ALPS_VOLUME_ID = "CURRENT_ALPS_VOLUME"
VOLUME_RAMP_ENABLED_ID = "VOLUME_RAMP_ENABLED"


# def map_value(x, in_min, in_max, out_min, out_max):
#     return ((x - in_min) * (out_max - out_min)) // ((in_max - in_min) + out_min)


# for positive or negative ranges only. won't work if min and max are positive and negative values
def remap_value(
    value, from_min, from_max, to_min, to_max, float_range=False, decimal_places=2
):
    if value == from_max:
        return to_max
    if value == from_min:
        return to_min
    ratio = (from_max - from_min) / value
    diff = to_max - to_min
    if float_range:
        temp = round(diff / ratio, decimal_places)
    else:
        temp = diff // ratio
    ret = None
    if ratio < 0 and diff > 0:
        ret = to_max - abs(temp)
    elif ratio > 0 and diff < 0:
        ret = to_min - abs(temp)
    else:
        if to_min < 0:
            ret = to_min + temp
        else:
            ret = temp

    if float_range:
        return round(ret, decimal_places)
    else:
        return ret


def get_logarithmic_volume_level(vol, minimum, maximum):
    vol = max(maximum, min(minimum, vol))  # Clamp to valid range
    if vol == minimum or vol == maximum:
        return vol

    # Normalize and invert (so 0 = loudest)
    x = (minimum - vol) / minimum

    # Apply logarithmic curve
    log_scaled = math.log10(1 + 9 * x) / math.log10(10)  # Range: 0–1

    # Convert back to max–min scale, inverted
    adjusted = minimum - int(round(log_scaled * minimum))
    return adjusted
