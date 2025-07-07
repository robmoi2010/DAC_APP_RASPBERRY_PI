from model.model import ResponseModel
from registry.register import get_instance
from services.utils.services_util import SOUND_MODE_DISPLAY_NAME, VOLUME_DISPLAY_NAME
from system.sound_modes import SOUND_MODE
from system.system_util import SOUND_MODE_ID
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
        description="Dsp core is bypassed and the main speakers dac receives digitally unprocesses signal. Subwoofer is turned off",
        display_name=SOUND_MODE.PURE_DIRECT.name,
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value=is_selected(current.value, 1),
        description="Mains speakers digital signal bypasses dsp core. No filters or time alignment are applied. Subwoofer signal is dsp processesed and low pass filter, PEQ and timealignment is applied to it.",
        display_name=SOUND_MODE.SEMI_PURE_DIRECT.name,
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2", value=is_selected(current.value, 2), 
        description="Mains and subwoofer digital signals are dsp processed and filters, EQ and time alignment are applied to them.",
        display_name=SOUND_MODE.DSP.name
    )
    list.append(r2)
    return list


def create_volume_algorithm_response(volume):
    current: VOLUME_ALGORITHM = volume.get_current_volume_algorithm()
    list = []
    r0 = ResponseModel(
        key="0",
        value=is_selected(current.value, 0),
        description="Volume level changes linearly",
        display_name=VOLUME_ALGORITHM.LINEAR.name,
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value=is_selected(current.value, 1),
        description="Volume level changes logarithmically",
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
        description="Ess dac digital volume.",
        display_name=VOLUME_DEVICE.DAC.name,
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value=is_selected(current, 1),
        description="Muses digitally controlled analog volume. Muses chip hardware must be implemented and connected to the dac",
        display_name=VOLUME_DEVICE.MUSES.name,
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2",
        value=is_selected(current, 2),
        description="Motorized alps volume pot. Hardware must be implemented first",
        display_name=VOLUME_DEVICE.ALPS.name,
    )
    list.append(r2)
    return list

def create_home_data(volume):
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
