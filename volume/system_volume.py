import repo.storage as storage
import ui.home as home
from enum import Enum
import configs.app_config as configuration
from volume.muses72323 import Muses72323
import dac.dac_volume as dac_volume

config = configuration.getConfig()
LOG_CURVE = 0.6


class VOL_DIRECTION(Enum):
    UP = 0
    DOWN = 1


def get_current_volume():
    master_vol_dev = config["SYSTEM"]["MASTER_VOLUME_DEVICE"]
    if master_vol_dev == "MUSES":
        return storage.read("CURRENT_MUSES_VOLUME")
    elif master_vol_dev == "DAC":
        return storage.read("CURRENT_VOLUME")


def persist_volume(volume):
    master_vol_dev = config["SYSTEM"]["MASTER_VOLUME_DEVICE"]
    if master_vol_dev == "MUSES":
        storage.write("CURRENT_MUSES_VOLUME", volume)
    elif master_vol_dev == "DAC":
        storage.write("CURRENT_VOLUME", volume)


def get_logarithmic_volume_level(vol):
    return pow(vol, 1 / LOG_CURVE)


def update_ui_volume(volume):
    home.update_volume(volume)


def map_value(x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min)) / ((in_max - in_min) + out_min)


def update_volume(direction):
    master_vol_dev = config["SYSTEM"]["MASTER_VOLUME_DEVICE"]
    if master_vol_dev == "MUSES":
        Muses72323().update_volume(direction)
    elif master_vol_dev == "DAC":
        dac_volume.updateVolume(direction)


def mute():
    master_vol_dev = config["SYSTEM"]["MASTER_VOLUME_DEVICE"]
    if master_vol_dev == "MUSES":
        Muses72323().mute()
    elif master_vol_dev == "DAC":
        dac_volume.mute()


def get_percentage_volume(volume):
    master_vol_dev = config["SYSTEM"]["MASTER_VOLUME_DEVICE"]
    if master_vol_dev == "MUSES":
        return Muses72323().get_percentage_volume(volume)
    elif master_vol_dev == "DAC":
        return dac_volume.get_percentage_volume(volume)
