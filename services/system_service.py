from system.system_util import BUTTON, SOUND_MODE_ID
from model.model import RequestModel, ResponseModel
from system.sound_modes import SOUND_MODE
from services.utils.system_util import (
    create_sound_mode_response,
    create_volume_algorithm_response,
    create_volume_device_response,
)
from services.utils.ws_connection_manager import WS_TYPE, WSConnectionManager
import logging
from fastapi import WebSocket, APIRouter
import asyncio
from registry.register import get_instance
from volume.volume_util import (
    CURRENT_ALPS_VOLUME_ID,
    VOLUME_ALGORITHM,
    VOLUME_DEVICE,
    CURRENT_MUSES_VOLUME_ID,
    CURRENT_VOLUME_ID,
)
from services.utils.services_util import SOUND_MODE_DISPLAY_NAME, VOLUME_DISPLAY_NAME
from volume.volume_util import VOL_DIRECTION
from system.ir_remote_router import IrRemoteRouter

connection_manager: WSConnectionManager = get_instance("wsconnectionmanager")
system_app = APIRouter(prefix="/system")
ir_router: IrRemoteRouter = get_instance("irremoterouter")
logging.basicConfig(
    level=logging.ERROR, format="[%(levelname)s] %(filename)s:%(lineno)d - %(message)s"
)

volume = get_instance("volume")
sound_modes = get_instance("soundmode")


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
        logging.error(e)


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
        logging.error(e)


@system_app.get("/volume_device")
async def get_volume_device():
    print(volume)
    return create_volume_device_response(volume)


@system_app.put("/volume_device")
async def update_volume_device(request: RequestModel):
    try:
        global volume
        device = None
        if request.value == "0":
            device = VOLUME_DEVICE.DAC
        if request.value == "1":
            device = VOLUME_DEVICE.MUSES
        if request.value == "2":
            device = VOLUME_DEVICE.ALPS
        volume.set_current_volume_device(device.value)

        # reload volume object to capture the device change
        volume = get_instance("volume", force_new=True)
        return create_volume_device_response(volume)
    except Exception as e:
        logging.error(e)


@system_app.websocket("/ws")
async def home_websocket(websocket: WebSocket):
    await connection_manager.connect(WS_TYPE.HOME_DATA, websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logging.error(e)


@system_app.websocket("/ws/ir_remote")
async def ir_remote_websocket(websocket: WebSocket):
    await connection_manager.connect(WS_TYPE.IR_REMOTE, websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logging.error(e)


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
    id = "CURRENT_VOLUME"
    list.append(
        ResponseModel(key=id, value=str(current), display_name=VOLUME_DISPLAY_NAME)
    )

    # get current sound mode
    mode = sound_modes.get_current_sound_mode()
    list.append(
        ResponseModel(
            key=SOUND_MODE_ID,
            value=mode.name,
            display_name=SOUND_MODE_DISPLAY_NAME,
        )
    )
    return list


@system_app.put("/volume/update")
async def update_volume(response: ResponseModel):
    volume.update_volume(response.value)
    return response


@system_app.get("/volume/up")
async def volume_up():
    await volume.update_volume(VOL_DIRECTION.UP)


@system_app.get("/volume/down")
async def volume_down():
    await volume.update_volume(VOL_DIRECTION.DOWN)


@system_app.get("/ok")
async def volume_down():
    await ir_router.handle_ws_routing(BUTTON.OK)


@system_app.get("/up")
async def ir_nav_up():
    await ir_router.handle_ws_routing(BUTTON.UP)


@system_app.get("/down")
async def ir_nav_down():
    await ir_router.handle_ws_routing(BUTTON.DOWN)
