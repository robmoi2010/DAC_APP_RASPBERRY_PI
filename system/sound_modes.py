from enum import Enum

from dsp.io import CURRENT_MAIN_OUTPUT_ID
from registry.register import register
from repo.storage import Storage
from system.system_util import SOUND_MODE_ID, SUBWOOFER_OUTPUT_SOURCE_ID
import ui.home as home

from configs.app_config import Config
from dsp.dsp_comm import DspComm


class SOUND_MODE(Enum):
    PURE_DIRECT = 0
    SEMI_PURE_DIRECT = 1
    DSP = 2


@register
class SoundMode:
    def __init__(self, comm: DspComm, storage: Storage, config: Config):
        self.config = config.config["ADAU1452"]["ADDR"]
        self.comm = comm
        self.storage = storage

    def get_current_sound_mode(self):
        mode = self.storage.read(SOUND_MODE_ID)
        if mode == SOUND_MODE.DSP.value:
            return SOUND_MODE.DSP
        elif mode == SOUND_MODE.PURE_DIRECT.value:
            return SOUND_MODE.PURE_DIRECT
        elif mode == SOUND_MODE.SEMI_PURE_DIRECT.value:
            return SOUND_MODE.SEMI_PURE_DIRECT

    def get_sound_mode_name(self, mode):
        if mode == SOUND_MODE.PURE_DIRECT.value:
            return SOUND_MODE.PURE_DIRECT.name
        elif mode == SOUND_MODE.SEMI_PURE_DIRECT.value:
            return SOUND_MODE.SEMI_PURE_DIRECT.name
        elif mode == SOUND_MODE.DSP.value:
            return SOUND_MODE.DSP.name

    def update_sound_mode(self, mode):
        self.storage.write(SOUND_MODE_ID, mode)
        if mode == SOUND_MODE.PURE_DIRECT.value:
            self.handle_pure_direct()
            # update_ui_sound_mode(SOUND_MODE.PURE_DIRECT.name)
        elif mode == SOUND_MODE.SEMI_PURE_DIRECT.value:
            self.handle_semi_pure_direct()
            # update_ui_sound_mode(SOUND_MODE.SEMI_PURE_DIRECT.name)
        elif mode == SOUND_MODE.DSP.value:
            self.handle_dsp_mode()
            # update_ui_sound_mode(SOUND_MODE.DSP.name)

    def update_ui_sound_mode(self, mode):
        home.update_sound_mode(mode)

    def handle_pure_direct(self):
        # get current mains output
        current_output = self.storage.read(CURRENT_MAIN_OUTPUT_ID)

        # update routing on DSP to bypass the device core and route input to output without processing

        # Get current register value and update parts that need updating
        current_out_name = self.get_output_source_select_name(current_output)
        current = self.comm.read(self.config[current_out_name])
        new_value = current & ~(1 << 2)
        new_value = new_value & ~(1 << 1)
        new_value = new_value | (1 << 0)

        self.comm.write(self.config[current_out_name], new_value)

    def handle_semi_pure_direct(self):
        # set mains to pure direct
        self.handle_pure_direct()

        # current sub output port
        current_sub_out = self.storage.read(SUBWOOFER_OUTPUT_SOURCE_ID)
        name = self.get_output_source_select_name(current_sub_out)
        current_reg = self.comm.read(self.config[name])

        # change required bits to change sub out input to dsp core
        new_reg = current_reg & ~(1 << 2)
        new_reg = new_reg | (1 << 1)
        new_reg = new_reg & ~(1 << 0)

        # update device reg
        self.comm.write(self.config[name], new_reg)

    def handle_dsp_mode(self):
        mains_output = self.storage.read(CURRENT_MAIN_OUTPUT_ID)
        sub_output = self.storage.read(SUBWOOFER_OUTPUT_SOURCE_ID)

        # update mains reg values for routing mains through dsp core for processing
        mains_name = self.get_output_source_select_name(mains_output)
        current = self.comm.read(self.config[mains_name])
        new_value = current & ~(1 << 2)
        new_value = new_value | (1 << 1)
        new_value = new_value & ~(1 << 0)

        self.comm.write(self.config[mains_name], new_value)

        # update sub reg values
        sub_name = self.get_output_source_select_name(sub_output)
        current_reg = self.comm.read(self.config[sub_name])

        # change required bits to change sub out input to dsp core
        new_reg = current_reg & ~(1 << 2)
        new_reg = new_reg | (1 << 1)
        new_reg = new_reg & ~(1 << 0)

        # update device reg
        self.comm.write(self.config[sub_name], new_reg)

    def get_output_source_select_name(self, port):
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
