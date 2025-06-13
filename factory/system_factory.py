from enum import Enum
from fastapi import FastAPI
from repo import storage
from volume.muses72323 import Muses72323
from dac.dac_volume import DacVolume
import volume.system_volume as sys_volume
from services.utils.ws_connection_manager import WSConnectionManager
from services.utils.ir_connection_manager import IRConnectionManager
from system.ir_remote_router import IrRemoteRouter
from volume.volume_util import CURRENT_DEVICE_ID, VOLUME_DEVICE

connection_manager = None
ir_connecction_manager = None


class SYS_OBJECTS(Enum):
    FASTAPI = 0
    MUSES = 1
    VOLUME = 2
    DAC_VOLUME = 3
    WS_CONN_MANAGER = 4
    IR_CONN_MANAGER = 5
    IR_ROUTER = 6


def new(type: SYS_OBJECTS, init_object=None):
    if type == SYS_OBJECTS.FASTAPI:
        return FastAPI()
    if type == SYS_OBJECTS.MUSES:
        return Muses72323()
    if type == SYS_OBJECTS.DAC_VOLUME:
        return DacVolume()
    if type == SYS_OBJECTS.VOLUME:
        device = get_current_volume_device()
        if device == sys_volume.VOLUME_DEVICE.DAC:
            return DacVolume(init_object)
        elif device == sys_volume.VOLUME_DEVICE.MUSES:
            return Muses72323(init_object)
    if type == SYS_OBJECTS.WS_CONN_MANAGER:
        global connection_manager
        if connection_manager is None:
            connection_manager = WSConnectionManager()
        return connection_manager
    if type == SYS_OBJECTS.IR_CONN_MANAGER:
        global ir_connecction_manager
        if ir_connecction_manager is None:
            ir_connecction_manager = IRConnectionManager()
        return ir_connecction_manager
    if type == SYS_OBJECTS.IR_ROUTER:
        return IrRemoteRouter(init_object)


def get_current_volume_device():
    device = storage.read(CURRENT_DEVICE_ID)
    if device == VOLUME_DEVICE.DAC.value:
        return VOLUME_DEVICE.DAC
    elif device == VOLUME_DEVICE.MUSES.value:
        return VOLUME_DEVICE.MUSES
