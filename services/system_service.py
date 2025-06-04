from factory.system_factory import SYS_OBJECTS
import factory.system_factory as factory
from model.model import ResponseModel
import general.sound_modes as sound_modes
from volume.system_volume import VOLUME_DEVICE

system_app = factory.new(SYS_OBJECTS.FASTAPI)
VOLUME_DISPLAY_NAME = "Volume"
volume = factory.new(SYS_OBJECTS.VOLUME)


@system_app.get("/volume")
async def current_volume():
    current = volume.get_current_volume()
    device: VOLUME_DEVICE = volume.get_current_volume_device()
    id = None
    if device == VOLUME_DEVICE.DAC:
        id = volume.CURRENT_VOLUME_ID
    elif device == VOLUME_DEVICE.MUSES:
        id = volume.CURRENT_MUSES_VOLUME_ID

    return ResponseModel(key=id, value=str(current), display_name=VOLUME_DISPLAY_NAME)


@system_app.get("/home")
async def home():
    list = []
    # get current volume
    current = volume.get_current_volume()
    device: VOLUME_DEVICE = volume.get_current_volume_device()
    id = None
    if device == VOLUME_DEVICE.DAC:
        id = volume.CURRENT_VOLUME_ID
    elif device == VOLUME_DEVICE.MUSES:
        id = volume.CURRENT_MUSES_VOLUME_ID
    list.append(
        ResponseModel(key=id, value=str(current), display_name=VOLUME_DISPLAY_NAME)
    )

    # get current sound mode
    mode = sound_modes.get_current_sound_mode()
    list.append(
        ResponseModel(
            key=sound_modes.SOUND_MODE_ID, value=mode.name, display_name=mode.name
        )
    )
    return list


@system_app.put("/volume/update")
async def update_volume(response: ResponseModel):
    print("rsp:" + response.value)
    volume.update_volume(response.value)
    return response
