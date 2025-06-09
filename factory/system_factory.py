from enum import Enum
from fastapi import FastAPI
from volume.muses72323 import Muses72323
from dac.dac_volume import DacVolume
import volume.system_volume as sys_volume
from services.ws_connection_manager import WSConnectionManager
from services.ir_connection_manager import IRConnectionManager
from general.ir_remote_router import IrRemoteRouter

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
        device = sys_volume.get_current_volume_device()
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
