from factory.system_factory import SYS_OBJECTS
import factory.system_factory as factory
from model.model import ResponseModel
import general.sound_modes as sound_modes
from services.ws_connection_manager import WSConnectionManager
import logging
from fastapi import WebSocket, APIRouter
import asyncio
from volume.volume_util import (
    VOLUME_DEVICE,
    CURRENT_MUSES_VOLUME_ID,
    CURRENT_VOLUME_ID,
)
from services.services_util import SOUND_MODE_DISPLAY_NAME, VOLUME_DISPLAY_NAME
from volume.volume_util import VOL_DIRECTION

connection_manager: WSConnectionManager = factory.new(SYS_OBJECTS.WS_CONN_MANAGER)
system_app = APIRouter(prefix="/system")
volume = factory.new(SYS_OBJECTS.VOLUME, connection_manager)

logger = logging.getLogger(__name__)


@system_app.websocket("/ws")
async def home_websocket(websocket: WebSocket):
    await connection_manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logger.error(e)


@system_app.get("/volume")
async def current_volume():
    current = volume.get_current_volume()
    device: VOLUME_DEVICE = volume.get_current_volume_device()
    id = None
    if device == VOLUME_DEVICE.DAC:
        id = CURRENT_VOLUME_ID
    elif device == VOLUME_DEVICE.MUSES:
        id = CURRENT_MUSES_VOLUME_ID

    return ResponseModel(key=id, value=str(current), display_name=VOLUME_DISPLAY_NAME)


@system_app.get("/home")
async def home():
    list = []
    # get current volume
    current = volume.get_percentage_volume(volume.get_current_volume())
    device: VOLUME_DEVICE = volume.get_current_volume_device()
    id = None
    if device == VOLUME_DEVICE.DAC:
        id = CURRENT_VOLUME_ID
    elif device == VOLUME_DEVICE.MUSES:
        id = CURRENT_MUSES_VOLUME_ID
    list.append(
        ResponseModel(key=id, value=str(current), display_name=VOLUME_DISPLAY_NAME)
    )

    # get current sound mode
    mode = sound_modes.get_current_sound_mode()
    list.append(
        ResponseModel(
            key=sound_modes.SOUND_MODE_ID,
            value=mode.name,
            display_name=SOUND_MODE_DISPLAY_NAME,
        )
    )
    return list


@system_app.put("/volume/update")
async def update_volume(response: ResponseModel):
    print("rsp:" + response.value)
    volume.update_volume(response.value)
    return response


@system_app.get("/up")
async def volume_up():
    await volume.update_volume(VOL_DIRECTION.UP)
    


@system_app.get("/down")
async def volume_down():
    await volume.update_volume(VOL_DIRECTION.DOWN)
    
