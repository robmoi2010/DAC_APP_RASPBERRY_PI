import json
import threading
import logging
import asyncio
from fastapi import WebSocket, APIRouter, logger
from dac import DacMetadata
from system.system_util import BUTTON
from model.model import RequestModel, ResponseModel
from system.sound_modes import SOUND_MODE, SoundMode
from services.utils.system_util import (
    create_home_data,
    create_sound_mode_response,
    create_volume_algorithm_response,
    create_volume_device_response,
)
from system.ir_remote_router import IrRemoteRouter
from services.utils.ws_connection_manager import WS_TYPE
import registry.register as register
from volume.volume_util import (
    VOLUME_ALGORITHM,
    VOLUME_DEVICE,
    CURRENT_MUSES_VOLUME_ID,
    CURRENT_VOLUME_ID,
    VOL_DIRECTION,
)
from services.utils.services_util import VOLUME_DISPLAY_NAME


# Setup
system_app = APIRouter(prefix="/system")
logging.basicConfig(
    level=logging.ERROR, format="[%(levelname)s] %(filename)s:%(lineno)d - %(message)s"
)


connection_manager_task = asyncio.create_task(
    register.get_instance("wsconnectionmanager")
)
volume_task = None
sound_modes_task = None
dac_metadata_task = None
ir_router_task = None


@system_app.on_event("startup")
async def startup():
    # === Startup ===
    global volume_task
    global sound_modes_task
    global dac_metadata_task
    global ir_router_task
    volume_task = asyncio.create_task(register.get_instance("volume"))
    sound_modes_task = asyncio.create_task(register.get_instance("soundmode"))
    dac_metadata_task = asyncio.create_task(register.get_instance("dacmetadata"))
    ir_router_task = asyncio.create_task(register.get_instance("irremoterouter"))


async def safe_get(task, name):
    obj = await task
    if not obj:
        logger.error(f"[DI] Failed to resolve '{name}'")
    return obj


@system_app.get("/sound_mode")
async def get_sound_mode():
    return create_sound_mode_response(await safe_get(sound_modes_task, "soundmodes"))


@system_app.put("/sound_mode")
async def update_sound_mode(request: RequestModel):
    try:
        sound_modes: SoundMode = await safe_get(sound_modes_task, "soundmodes")
        if not sound_modes:
            return
        mode = (
            SOUND_MODE(int(request.value))
            if request.value in ["1", "2"]
            else SOUND_MODE.PURE_DIRECT
        )
        sound_modes.update_sound_mode(mode.value)
        return create_sound_mode_response(sound_modes)
    except Exception as e:
        logging.error(e)


@system_app.get("/volume_algorithm")
async def get_volume_algorithm():
    volume = await safe_get(volume_task, "volume")
    return create_volume_algorithm_response(volume)


@system_app.put("/volume_algorithm")
async def update_volume_algorithm(request: RequestModel):
    try:
        volume = await safe_get(volume_task, "volume")
        if not volume:
            return
        algorithm = (
            VOLUME_ALGORITHM.LINEAR
            if request.value == "0"
            else VOLUME_ALGORITHM.LOGARITHMIC
        )
        volume.set_volume_algorithm(algorithm)
        return create_volume_algorithm_response(volume)
    except Exception as e:
        logging.error(e)


@system_app.get("/volume_device")
async def get_volume_device():
    volume = await safe_get(volume_task, "volume")
    return create_volume_device_response(volume)


@system_app.put("/volume_device")
async def update_volume_device(request: RequestModel):
    try:
        volume = await safe_get(volume_task, "volume")
        if not volume:
            return
        device = {
            "0": VOLUME_DEVICE.DAC,
            "1": VOLUME_DEVICE.MUSES,
            "2": VOLUME_DEVICE.ALPS,
        }.get(request.value)
        if device is not None:
            volume.set_current_volume_device(device.value)
            refreshed = await register.get_instance("volume", force_new=True)
            return create_volume_device_response(refreshed)
    except Exception as e:
        logging.error(e)


@system_app.websocket("/ws")
async def home_websocket(websocket: WebSocket):
    await websocket.accept()
    connection_manager = await safe_get(connection_manager_task, "connectionmanager")
    if not connection_manager:
        return
    await connection_manager.connect(WS_TYPE.HOME_DATA, websocket)
    volume = await safe_get(volume_task, "volume")
    if not volume:
        return

    # Send initial home data
    home_data = [
        dt.model_dump()
        for dt in create_home_data(
            volume, sound_modes=await safe_get(sound_modes_task, "soundmode")
        )
    ]
    await connection_manager.send_data(WS_TYPE.HOME_DATA, json.dumps(home_data))

    # Start DAC metadata polling thread if not started
    dac_metadata: DacMetadata = await safe_get(dac_metadata_task, "dacmetadata")
    if dac_metadata and not dac_metadata.polling_started():
        thread = threading.Thread(target=dac_metadata.poll_audio_metadata, daemon=True)
        thread.start()

    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logging.error(e)


@system_app.websocket("/ws/ir_remote")
async def ir_remote_websocket(websocket: WebSocket):
    await websocket.accept()
    connection_manager = await safe_get(connection_manager_task, "connectionmanager")
    if not connection_manager:
        return
    await connection_manager.connect(WS_TYPE.IR_REMOTE, websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logging.error(e)


@system_app.get("/volume")
async def current_volume():
    volume = await safe_get(volume_task, "volume")
    if not volume:
        return
    current = volume.get_current_volume()
    device = volume.get_current_volume_device()
    id = CURRENT_MUSES_VOLUME_ID if device == VOLUME_DEVICE.MUSES else CURRENT_VOLUME_ID
    return ResponseModel(key=id, value=str(current), display_name=VOLUME_DISPLAY_NAME)


@system_app.get("/home")
async def home():
    volume = await safe_get(volume_task, "volume")
    return create_home_data(volume, await safe_get(sound_modes_task, "soundmodes"))


@system_app.put("/volume")
async def update_volume(request: RequestModel):
    volume = await safe_get(volume_task, "volume")
    if not volume:
        return
    new_volume = await volume.set_volume_from_ui(int(request.value))
    return ResponseModel(key="0", value=str(new_volume), display_name="")


@system_app.get("/volume/up")
async def volume_up():
    volume = await safe_get(volume_task, "volume")
    if not volume:
        return
    vol = await volume.update_volume(VOL_DIRECTION.UP)
    return ResponseModel(key="0", value=str(vol), display_name="")


@system_app.get("/volume/down")
async def volume_down():
    volume = await safe_get(volume_task, "volume")
    if not volume:
        return
    vol = await volume.update_volume(VOL_DIRECTION.DOWN)
    return ResponseModel(key="0", value=str(vol), display_name="")


@system_app.get("/ok")
async def ok_button():
    ir_router: IrRemoteRouter = await safe_get(ir_router_task, "irrouter")
    if ir_router:
        await ir_router.handle_ws_routing(BUTTON.OK)


@system_app.get("/up")
async def ir_nav_up():
    ir_router: IrRemoteRouter = await safe_get(ir_router_task, "irrouter")
    if ir_router:
        await ir_router.handle_ws_routing(BUTTON.UP)


@system_app.get("/down")
async def ir_nav_down():
    ir_router: IrRemoteRouter = await safe_get(ir_router_task, "irrouter")
    if ir_router:
        await ir_router.handle_ws_routing(BUTTON.DOWN)


@system_app.get("/volume_ramp")
async def is_volume_ramp_enabled():
    volume = await safe_get(volume_task, "volume")
    active = volume.is_volume_ramp_enabled() if volume else False
    ret = "1" if active else "0"
    return ResponseModel(key="0", value=ret, display_name=ret)


@system_app.put("/volume_ramp")
async def update_volume_ramp(request: RequestModel):
    try:
        volume = await safe_get(volume_task, "volume")
        if not volume:
            return
        volume.update_volume_ramp(int(request.value))
        return ResponseModel(key="0", value=request.value, display_name=request.value)
    except Exception as e:
        logging.error(e)
