from factory.system_factory import SYS_OBJECTS
import factory.system_factory as factory
from system.system_util import BUTTON
from model.model import RequestModel, ResponseModel
import system.sound_modes as sound_modes
from system.sound_modes import SOUND_MODE
from services.utils.system_util import (
    create_sound_mode_response,
    create_volume_algorithm_response,
    create_volume_device_response,
)
from services.utils.ws_connection_manager import WSConnectionManager
from services.utils.ir_connection_manager import IRConnectionManager
import logging
from fastapi import WebSocket, APIRouter
import asyncio
from volume.volume_util import (
    VOLUME_ALGORITHM,
    VOLUME_DEVICE,
    CURRENT_MUSES_VOLUME_ID,
    CURRENT_VOLUME_ID,
)
from services.utils.services_util import SOUND_MODE_DISPLAY_NAME, VOLUME_DISPLAY_NAME
from volume.volume_util import VOL_DIRECTION
from system.ir_remote_router import IrRemoteRouter

connection_manager: WSConnectionManager = factory.new(SYS_OBJECTS.WS_CONN_MANAGER)
ir_connection_manager: IRConnectionManager = factory.new(SYS_OBJECTS.IR_CONN_MANAGER)
system_app = APIRouter(prefix="/system")
ir_router: IrRemoteRouter = factory.new(SYS_OBJECTS.IR_ROUTER, ir_connection_manager)
logger = logging.getLogger(__name__)

volume = factory.new(SYS_OBJECTS.VOLUME, connection_manager)


@system_app.get("/sound_mode")
async def get_sound_mode():
    return create_sound_mode_response()


@system_app.put("/sound_mode")
async def update_sound_mode(request: RequestModel):
    try:
        mode = SOUND_MODE.PURE_DIRECT
        if request.value == "1":
            mode = SOUND_MODE.SEMI_PURE_DIRECT
        if request.value == "2":
            mode = SOUND_MODE.DSP
        sound_modes.update_sound_mode(mode.value)
        return create_sound_mode_response()
    except Exception as e:
        logger.error(e)


@system_app.get("/volume_algorithm")
async def get_volume_algorithm():
    return create_volume_algorithm_response(volume)


@system_app.put("/volume_algorithm")
async def update_volume_algorithm(request: RequestModel):
    try:
        algorithm = VOLUME_ALGORITHM.LOGARITHMIC
        if request.value == "0":
            algorithm = VOLUME_ALGORITHM.LINEAR
        volume.set_volume_algorithm(algorithm)
        return create_volume_algorithm_response(volume)
    except Exception as e:
        logger.error(e)


@system_app.get("/volume_device")
async def get_volume_device():
    print(volume)
    return create_volume_device_response(volume)


@system_app.put("/volume_device")
async def update_volume_device(request: RequestModel):
    try:
        global volume
        device = VOLUME_DEVICE.MUSES
        if request.value == "0":
            device = VOLUME_DEVICE.DAC
        volume.set_current_volume_device(device.value)

        # reload volume object to capture the device change
        volume = factory.new(SYS_OBJECTS.VOLUME, connection_manager)
        return create_volume_device_response(volume)
    except Exception as e:
        logger.error(e)


@system_app.websocket("/ws")
async def home_websocket(websocket: WebSocket):
    await connection_manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logger.error(e)


@system_app.websocket("/ws/ir_remote")
async def ir_remote_websocket(websocket: WebSocket):
    await ir_connection_manager.connect(websocket)
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
    if device == VOLUME_DEVICE.DAC.value:
        id = CURRENT_VOLUME_ID
    elif device == VOLUME_DEVICE.MUSES.value:
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
    await ir_router.handle_ws_routing(BUTTON.UP)


@system_app.get("/down")
async def volume_down():
    await volume.update_volume(VOL_DIRECTION.DOWN)
    await ir_router.handle_ws_routing(BUTTON.DOWN)


@system_app.get("/ok")
async def volume_down():
    await ir_router.handle_ws_routing(BUTTON.OK)
