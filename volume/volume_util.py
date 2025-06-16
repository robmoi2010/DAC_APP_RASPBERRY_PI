from enum import Enum
import math


class VOL_DIRECTION(Enum):
    UP = 0
    DOWN = 1


class VOLUME_DEVICE(Enum):
    DAC = 0
    MUSES = 1


class VOLUME_ALGORITHM(Enum):
    LINEAR = 0
    LOGARITHMIC = 1


CURRENT_DEVICE_ID = "CURRENT_VOLUME_DEVICE"
CURRENT_MUSES_VOLUME_ID = "CURRENT_MUSES_VOLUME"
CURRENT_VOLUME_ID = "CURRENT_VOLUME"
VOLUME_ALGORITHM_ID = "VOLUME_ALGORITHM"


def map_value( x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min)) / ((in_max - in_min) + out_min)


def get_logarithmic_volume_level( vol, minimum, maximum):
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
