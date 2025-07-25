from registry.register import get_instance
import configs.app_config as app_config
from registry.register import register
from dac.dac_comm import DacComm
from services.utils.ws_connection_manager import WSConnectionManager
from volume.abstract_volume import AbstractVolume
from volume.volume_util import (
    VOLUME_ALGORITHM,
    VOL_DIRECTION,
    CURRENT_VOLUME_ID,
    VOLUME_DEVICE,
    get_logarithmic_volume_level,
    remap_value,
)
from repo.storage import Storage

DAC_MIN_VOL = 255
DAC_MAX_VOL = 0
LOG_CURVE = 6
config = app_config.getConfig()

addrConfig = config["DAC"]["ADDR"]
DISABLE_VOLUME_ID = "DISABLE_VOLUME"
DAC_MUTED_ID = "DAC_MUTED"


@register
class DacVolume(AbstractVolume):
    def __init__(
        self,
        dac_comm: DacComm,
        storage: Storage,
        connection_manager: WSConnectionManager,
    ):
        self.dac_comm = dac_comm
        self.storage = storage
        self.connection_manager = connection_manager

    # def onkeyLeft(counter):
    #     from ui.app import current_visible_frame

    #     children = current_visible_frame.winfo_children()
    #     print(counter)
    #     children[counter].tk_focusPrev().focus_set()
    #     return len(children)

    # def onEnter(counter):
    #     from ui.app import current_visible_frame

    #     children = current_visible_frame.winfo_children()
    #     print(counter)
    #     children[counter].invoke()

    # def onKeyRight(counter):
    #     from ui.app import current_visible_frame

    #     children = current_visible_frame.winfo_children()

    #     children[counter].tk_focusNext().focus_set()
    #     return len(children)

    def set_volume(
        self,
        vol,
        volume_algorithm: VOLUME_ALGORITHM,
    ):
        # if logarithmic is set adjust volume to logarithmic scale
        if volume_algorithm == VOLUME_ALGORITHM.LOGARITHMIC:
            vol = get_logarithmic_volume_level(vol, DAC_MIN_VOL, DAC_MAX_VOL)
        # hold both channels
        hold_addr = addrConfig["DAC_SPDIF_SEL_ADDR"]
        hold_mask = 0b00001000
        data = self.dac_comm.read(hold_addr)
        data = data | hold_mask
        self.dac_comm.write(hold_addr, data)

        # update volume of both channels
        volume_1_addr = addrConfig["VOLUME_CH1"]
        volume_2_addr = addrConfig["VOLUME_CH2"]
        # volume_data = format(vol, "08b")
        # dac_comm.write(volume_1_addr, volume_data)
        # dac_comm.write(volume_2_addr, volume_data)

        # release hold on both channels
        data = data & ~hold_mask
        self.dac_comm.write(hold_addr, data)

    def update_volume(self, direction, volume_algorithm: VOLUME_ALGORITHM):
        currVol = self.get_current_volume()
        steps = config["DAC"]["VOLUME"]["VOLUME_STEPS"]  # get volume steps from config
        if direction == VOL_DIRECTION.UP:  # volume increase
            if currVol <= DAC_MAX_VOL:  # skip processing if volume is already at Max
                return 100
            currVol -= steps  # dacs lower value=increase
        else:
            if (
                currVol >= DAC_MIN_VOL
            ):  # skip processing if volume is already at Minimum
                return 0
            currVol += steps  # dacs higher value=decrease
        return self.process_new_volume(currVol, volume_algorithm)

    def process_new_volume(self, currVol, volume_algorithm: VOLUME_ALGORITHM):
        self.set_volume(currVol, volume_algorithm)
        self.persist_volume(currVol)
        # return new volume as percentage for ui update
        return self.get_percentage_volume(currVol)

    def is_volume_disabled(self):
        return self.storage.read(DISABLE_VOLUME_ID)

    def disable_enable_volume(self, selected, volume_algorithm: VOLUME_ALGORITHM):
        curr = self.storage.read(DISABLE_VOLUME_ID)
        if (curr == 0 and selected == 0) or (curr == 1 and selected == 1):
            return
        if selected == 1:
            self.set_volume(DAC_MAX_VOL, volume_algorithm)  # disable volume
            self.storage.write(DISABLE_VOLUME_ID, 1)
            return 0  # disabled
        else:
            self.set_volume(self.get_current_volume(), volume_algorithm)
            self.storage.write(DISABLE_VOLUME_ID, 0)
            return 1  # enabled

    def mute_dac(self):
        mute_addr = addrConfig["DAC_MUTE"]
        mute_mask = 0b00000011
        data = self.dac_comm.read(mute_addr)
        data = data | mute_mask
        self.dac_comm.write(mute_addr, data)

    def unmute_dac(self):
        mute_addr = addrConfig["DAC_MUTE"]
        mute_mask = 0b00000011
        data = self.dac_comm.read(mute_addr)
        data = data & ~mute_mask
        self.dac_comm.write(mute_addr, data)

    def mute(self):
        muted = self.storage.read(DAC_MUTED_ID)
        if muted == 1:
            self.unmute_dac()
            self.storage.write(DAC_MUTED_ID, 0)
        else:
            self.mute_dac()
            self.storage.write(DAC_MUTED_ID, 1)

    def get_percentage_volume(self, vol):
        val = remap_value(vol, DAC_MIN_VOL, DAC_MAX_VOL, 0, 100)
        return val

    def persist_volume(self, volume):
        self.storage.write(CURRENT_VOLUME_ID, volume)

    def get_current_volume(self):
        return self.storage.read(CURRENT_VOLUME_ID)

    def update_ui_volume(self, volume):
        return super().update_ui_volume(
            VOLUME_DEVICE.DAC, self.connection_manager, volume
        )

    def get_volume_from_percentage(self, percentage):
        return remap_value(percentage, 0, 100, DAC_MIN_VOL, DAC_MAX_VOL)

    def get_max_volume(self):
        return DAC_MAX_VOL

    def get_min_volume(self):
        return DAC_MIN_VOL

    def is_volume_more_than(self, volume1, volume2):  # higher volume=lower value
        return volume1 < volume2
