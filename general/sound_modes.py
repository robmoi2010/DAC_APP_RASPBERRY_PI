from enum import Enum
import repo.storage as storage
from dsp.io import CURRENT_MAIN_OUTPUT_ID
import ui.home as home
from dsp.router import (
    SUBWOOFER_OUTPUT_SOURCE_ID,
)
import configs.app_config as configuration
import util.communication as comm

SOUND_MODE_ID = "SOUND_MODE"
config = configuration.getConfig()["ADAU1452"]["ADDR"]


class SoundMode(Enum):
    PURE_DIRECT = 0
    SEMI_PURE_DIRECT = 1
    DSP = 2


def get_current_sound_mode():
    print(storage.read(SOUND_MODE_ID))
    return storage.read(SOUND_MODE_ID)


def get_sound_mode_name(mode):
    if mode == SoundMode.PURE_DIRECT.value:
        return SoundMode.PURE_DIRECT.name
    elif mode == SoundMode.SEMI_PURE_DIRECT.value:
        return SoundMode.SEMI_PURE_DIRECT.name
    elif mode == SoundMode.DSP.value:
        return SoundMode.DSP.name
    


def update_sound_mode(mode):
    storage.write(SOUND_MODE_ID, mode)
    if mode == SoundMode.PURE_DIRECT.value:
        handle_pure_direct()
        update_ui_sound_mode(SoundMode.PURE_DIRECT.name)
    elif mode == SoundMode.SEMI_PURE_DIRECT.value:
        handle_semi_pure_direct()
        update_ui_sound_mode(SoundMode.SEMI_PURE_DIRECT.name)
    elif mode == SoundMode.DSP.value:
        handle_dsp_mode()
        update_ui_sound_mode(SoundMode.DSP.name)


def update_ui_sound_mode(mode):
    home.update_sound_mode(mode)


def handle_pure_direct():
    # get current mains output
    current_output = storage.read(CURRENT_MAIN_OUTPUT_ID)

    # update routing on DSP to bypass the device core and route input to output without processing

    # Get current register value and update parts that need updating
    current_out_name = get_output_source_select_name(current_output)
    current = comm.read(config["I2C_ADDR_READ"], config[current_out_name])
    new_value = current & ~(1 << 2)
    new_value = new_value & ~(1 << 1)
    new_value = new_value | (1 << 0)

    comm.write(config["I2C_ADDR_WRITE"], config[current_out_name], new_value)


def handle_semi_pure_direct():
    # set mains to pure direct
    handle_pure_direct()

    # current sub output port
    current_sub_out = storage.read(SUBWOOFER_OUTPUT_SOURCE_ID)
    name = get_output_source_select_name(current_sub_out)
    current_reg = comm.read(config["I2C_ADDR_READ"], config[name])

    # change required bits to change sub out input to dsp core
    new_reg = current_reg & ~(1 << 2)
    new_reg = new_reg | (1 << 1)
    new_reg = new_reg & ~(1 << 0)

    # update device reg
    comm.write(config["I2C_ADDR_READ"], config[name], new_reg)


def handle_dsp_mode():
    mains_output = storage.read(CURRENT_MAIN_OUTPUT_ID)
    sub_output = storage.read(SUBWOOFER_OUTPUT_SOURCE_ID)

    # update mains reg values for routing mains through dsp core for processing
    mains_name = get_output_source_select_name(mains_output)
    current = comm.read(config["I2C_ADDR_READ"], config[mains_name])
    new_value = current & ~(1 << 2)
    new_value = new_value | (1 << 1)
    new_value = new_value & ~(1 << 0)

    comm.write(config["I2C_ADDR_WRITE"], config[mains_name], new_value)

    # update sub reg values
    sub_name = get_output_source_select_name(sub_output)
    current_reg = comm.read(config["I2C_ADDR_READ"], config[sub_name])

    # change required bits to change sub out input to dsp core
    new_reg = current_reg & ~(1 << 2)
    new_reg = new_reg | (1 << 1)
    new_reg = new_reg & ~(1 << 0)

    # update device reg
    comm.write(config["I2C_ADDR_READ"], config[sub_name], new_reg)


def get_output_source_select_name(port):
    if port == 0:
        return "SOUT_SOURCE0"
    if port == 1:
        return "SOUT_SOURCE1"
    if port == 2:
        return "SOUT_SOURCE2"
    if port == 3:
        return "SOUT_SOURCE3"
    if port == 4:
        return "SOUT_SOURCE4"
