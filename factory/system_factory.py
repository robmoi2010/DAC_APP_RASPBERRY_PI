from enum import Enum
from fastapi import FastAPI
from volume.muses72323 import Muses72323
from dac.dac_volume import DacVolume
import volume.system_volume as sys_volume


class SYS_OBJECTS(Enum):
    FASTAPI = 0
    MUSES = 1
    VOLUME = 2
    DAC_VOLUME = 3


def new(type: SYS_OBJECTS):
    if type == SYS_OBJECTS.FASTAPI:
        return FastAPI()
    if type == SYS_OBJECTS.MUSES:
        return Muses72323()
    if type==SYS_OBJECTS.DAC_VOLUME:
        return DacVolume()
    if type == SYS_OBJECTS.VOLUME:
        device = sys_volume.get_current_volume_device()
        if device == sys_volume.VOLUME_DEVICE.DAC:
            return DacVolume()
        elif device == sys_volume.VOLUME_DEVICE.MUSES:
            return Muses72323()
