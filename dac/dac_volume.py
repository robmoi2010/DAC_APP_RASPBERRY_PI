import repo.storage as storage
import configs.app_config as app_config
import util.communication as communication
import volume.system_volume as sys_volume
from volume.system_volume import Volume
from volume.system_volume import VOLUME_ALGORITHM


DAC_MIN_VOL = 255
DAC_MAX_VOL = 0
LOG_CURVE = 6
config = app_config.getConfig()

addrConfig = config["DAC"]["ADDR"]
DAC_I2C_ADDR = addrConfig["I2C_ADDR"]
DISABLE_VOLUME_ID = "DISABLE_VOLUME"
DAC_MUTED_ID = "DAC_MUTED"


class DacVolume(Volume):
    def __init__(self):
        super().__init__()

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

    def set_volume(self, vol):
        # if logarithmic is set adjust volume to logarithmic scale
        if super.get_current_volume_algorithm() == VOLUME_ALGORITHM.LOGARITHMIC:
            vol = super.get_logarithmic_volume_level(vol, DAC_MIN_VOL, DAC_MAX_VOL)
            print("vol:" + str(vol))
        # hold both channels
        hold_addr = addrConfig["DAC_SPDIF_SEL_ADDR"]
        hold_mask = 0b00001000
        data = communication.read(DAC_I2C_ADDR, hold_addr)
        data = data | hold_mask
        communication.write(DAC_I2C_ADDR, hold_addr, data)

        # update volume of both channels
        volume_1_addr = addrConfig["VOLUME_CH1"]
        volume_2_addr = addrConfig["VOLUME_CH2"]
        volume_data = format(vol, "08b")
        communication.write(DAC_I2C_ADDR, volume_1_addr, volume_data)
        communication.write(DAC_I2C_ADDR, volume_2_addr, volume_data)

        # release hold on both channels
        data = data & ~hold_mask
        communication.write(DAC_I2C_ADDR, hold_addr, data)

    def update_volume(self, direction):
        currVol = super.get_current_volume()
        steps = config["DAC"]["VOLUME"]["VOLUME_STEPS"]  # get volume steps from config
        if direction == super.VOL_DIRECTION.UP:  # volume increase
            if currVol <= DAC_MAX_VOL:  # skip processing if volume is already at Max
                return
            currVol -= steps  # dacs lower value=increase
        else:
            if (
                currVol >= DAC_MIN_VOL
            ):  # skip processing if volume is already at Minimum
                return
            currVol += steps  # dacs higher value=decrease
        self.set_volume(currVol)
        super.persist_volume(currVol)
        # update ui with the new volume
        super.update_ui_volume(currVol)

    def is_volume_disabled(self):
        return storage.read(DISABLE_VOLUME_ID)

    def disable_enable_volume(self, selected):
        curr = storage.read(DISABLE_VOLUME_ID)
        if (curr == 0 and selected == 0) or (curr == 1 and selected == 1):
            return
        if selected == 1:
            self.set_volume(DAC_MAX_VOL)  # disable volume
            storage.write(DISABLE_VOLUME_ID, 1)
            return 0  # disabled
        else:
            self.set_volume(self.get_current_volume())
            storage.write(DISABLE_VOLUME_ID, 0)
            return 1  # enabled

    def mute_dac(self):
        mute_addr = addrConfig["DAC_MUTE"]
        mute_mask = 0b00000011
        data = communication.read(DAC_I2C_ADDR, mute_addr)
        data = data | mute_mask
        communication.write(DAC_I2C_ADDR, mute_addr, data)

    def unmute_dac(self):
        mute_addr = addrConfig["DAC_MUTE"]
        mute_mask = 0b00000011
        data = communication.read(DAC_I2C_ADDR, mute_addr)
        data = data & ~mute_mask
        communication.write(DAC_I2C_ADDR, mute_addr, data)

    def mute(self):
        muted = storage.read(DAC_MUTED_ID)
        if muted == 1:
            self.unmute_dac()
            storage.write(DAC_MUTED_ID, 0)
        else:
            self.mute_dac()
            storage.write(DAC_MUTED_ID, 1)

    def get_percentage_volume(self, vol):
        val = super.map_value(vol, DAC_MIN_VOL, DAC_MAX_VOL, 0, 100)
        return int(val)

    def set_current_volume_device():
        storage.write(sys_volume.CURRENT_DEVICE_ID, sys_volume.VOLUME_DEVICE.DAC.name)

    def get_current_volume_device(self):
        return sys_volume.VOLUME_DEVICE.DAC

    def get_current_volume(self):
        return storage.read(sys_volume.CURRENT_VOLUME_ID)

    def persist_volume(self, volume):
        storage.write(sys_volume.CURRENT_VOLUME_ID, volume)
