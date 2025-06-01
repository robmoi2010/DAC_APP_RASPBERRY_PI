import repo.storage as storage
import ui.home as home
from enum import Enum
import configs.app_config as configuration
from volume.muses72323 import Muses72323
import dac.dac_volume as dac_volume
import math

config = configuration.getConfig()
LOG_CURVE = 0.6


class VOL_DIRECTION(Enum):
    UP = 0
    DOWN = 1


class VOLUME_DEVICE(Enum):
    DAC = 0
    MUSES = 1


class VOLUME_ALGORITHM(Enum):
    LINEAR = 0
    LOGARITHMIC = 1


def get_current_volume_device():
    return storage.read("CURRENT_VOLUME_DEVICE")


def get_current_volume():
    master_vol_dev = get_current_volume_device()
    if master_vol_dev == "MUSES":
        return storage.read("CURRENT_MUSES_VOLUME")
    elif master_vol_dev == "DAC":
        return storage.read("CURRENT_VOLUME")


def persist_volume(volume):
    master_vol_dev = get_current_volume_device()
    if master_vol_dev == "MUSES":
        storage.write("CURRENT_MUSES_VOLUME", volume)
    elif master_vol_dev == "DAC":
        storage.write("CURRENT_VOLUME", volume)


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


def update_ui_volume(volume):
    home.update_volume(volume)


def map_value(x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min)) / ((in_max - in_min) + out_min)


def update_volume(direction):
    master_vol_dev = get_current_volume_device()
    if master_vol_dev == "MUSES":
        Muses72323().update_volume(direction)
    elif master_vol_dev == "DAC":
        dac_volume.update_volume(direction)


def mute():
    master_vol_dev = get_current_volume_device()
    if master_vol_dev == "MUSES":
        Muses72323().mute()
    elif master_vol_dev == "DAC":
        dac_volume.mute()


def get_percentage_volume(volume):
    master_vol_dev = get_current_volume_device()
    if master_vol_dev == "MUSES":
        return Muses72323().get_percentage_volume(volume)
    elif master_vol_dev == "DAC":
        return dac_volume.get_percentage_volume(volume)


def set_current_volume_device(volume_device):
    storage.write("CURRENT_VOLUME_DEVICE", volume_device)


def get_current_volume_algorithm():
    algo = storage.read("VOLUME_ALGORITHM")
    if algo == VOLUME_ALGORITHM.LINEAR.value:
        return VOLUME_ALGORITHM.LINEAR
    else:
        return VOLUME_ALGORITHM.LOGARITHMIC


def set_volume_algorithm(algo: VOLUME_ALGORITHM):
    storage.write("VOLUME_ALGORITHM", algo.value)
