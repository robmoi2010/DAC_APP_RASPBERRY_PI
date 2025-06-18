from model.model import ResponseModel
from registry.register import get_instance
from system.sound_modes import SOUND_MODE
from volume import system_volume
from volume.volume_util import VOLUME_ALGORITHM, VOLUME_DEVICE

sound_modes = get_instance("soundmode")


def is_selected(current_item, index):
    selected = "0"
    if current_item == index:
        selected = "1"
    return selected


def create_sound_mode_response():
    current: SOUND_MODE = sound_modes.get_current_sound_mode()
    list = []
    r0 = ResponseModel(
        key="0",
        value=is_selected(current.value, 0),
        display_name=SOUND_MODE.PURE_DIRECT.name,
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value=is_selected(current.value, 1),
        display_name=SOUND_MODE.SEMI_PURE_DIRECT.name,
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2", value=is_selected(current.value, 2), display_name=SOUND_MODE.DSP.name
    )
    list.append(r2)
    return list


def create_volume_algorithm_response(volume):
    current: VOLUME_ALGORITHM = volume.get_current_volume_algorithm()
    list = []
    r0 = ResponseModel(
        key="0",
        value=is_selected(current.value, 0),
        display_name=VOLUME_ALGORITHM.LINEAR.name,
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value=is_selected(current.value, 1),
        display_name=VOLUME_ALGORITHM.LOGARITHMIC.name,
    )
    list.append(r1)
    return list


def create_volume_device_response(volume: system_volume):
    current = volume.get_current_volume_device()
    if current == VOLUME_DEVICE.DAC.value:
        selected = "0"
    if current == VOLUME_DEVICE.MUSES.value:
        selected = "1"
    if current == VOLUME_DEVICE.ALPS.value:
        selected = "2"
    list = []
    r0 = ResponseModel(
        key="0",
        value=is_selected(current, 0),
        display_name=VOLUME_DEVICE.DAC.name,
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value=is_selected(current, 1),
        display_name=VOLUME_DEVICE.MUSES.name,
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2",
        value=is_selected(current, 2),
        display_name=VOLUME_DEVICE.ALPS.name,
    )
    list.append(r2)
    return list
