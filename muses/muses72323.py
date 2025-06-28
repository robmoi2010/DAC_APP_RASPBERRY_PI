from dac.dac_volume import DISABLE_VOLUME_ID
from registry.register import register
from repo.storage import Storage
from services.utils.ws_connection_manager import WSConnectionManager
from volume.abstract_volume import AbstractVolume
from volume.volume_util import (
    VOL_DIRECTION,
    VOLUME_ALGORITHM,
    CURRENT_MUSES_VOLUME_ID,
    VOLUME_DEVICE,
    get_logarithmic_volume_level,
    map_value,
)
import configs.app_config as configuration
from muses.muses_comm import MusesComm

config = configuration.getConfig()["MUSES72323"]


@register
class Muses72323(AbstractVolume):

    def __init__(
        self, storage: Storage, comm: MusesComm, connection_manager: WSConnectionManager
    ):
        self.storage = storage
        self.comm = comm
        self.MAX_VOLUME = config["MAX_VOLUME"]
        self.MIN_VOLUME = config["MIN_VOLUME"]
        self.STEP = config["STEP"]
        self.connection_manager = connection_manager

    def update_volume(self, direction, volume_algorithm: VOLUME_ALGORITHM):
        curr_volume = self.get_current_volume()
        if direction == VOL_DIRECTION.UP:  # volume increase
            if (
                curr_volume >= self.MAX_VOLUME
            ):  # skip processing if volume is already at Max
                return 100
            curr_volume += self.STEP
        else:
            if (
                curr_volume <= self.MIN_VOLUME
            ):  # skip processing if volume is already at Minimum
                return 0
            curr_volume -= self.STEP
            print("after step:" + str(curr_volume))
        self.update_chip_volume(curr_volume, volume_algorithm)
        self.persist_volume(curr_volume)
        # return new percentage volume for ui update
        return self.get_percentage_volume(curr_volume)

    def update_chip_volume(self, vol, volume_algorithm: VOLUME_ALGORITHM):
        # if logarithmic is set adjust volume to logarithmic scale
        if (
            volume_algorithm == VOLUME_ALGORITHM.LOGARITHMIC
        ):  # fix issue of algorithm returning 0 during implementation
            vol = get_logarithmic_volume_level(
                abs(vol), self.MIN_VOLUME, self.MAX_VOLUME
            )
        print("prev_val:", str(vol))
        vol = self.map_db_to_reg_binary(vol)
        print("new val:" + str(vol))
        master_channel = config["MASTER_CHANNEL"]
        lsb_addr = None
        if master_channel == "R":
            lsb_addr = config["R_VOLUME_ADDR_REGISTER"]
        else:
            lsb_addr = config["L_VOLUME_ADDR_REGISTER"]
        msb_addr = format(int(vol), "09b")  # Convert to 9 bit binary
        print("msb:" + msb_addr)
        print("lsb:" + lsb_addr)
        data = msb_addr + lsb_addr
        print(data)
        l_pin = config["R_CHANNEL_CS_PIN"]
        r_pin = config["L_CHANNEL_CS_PIN"]
        self.comm.spi_write(r_pin, data)
        self.comm.spi_write(l_pin, data)

    def initialize_volume_chip(self):
        # link left and right channel volume control, enable zero cross and channels gain
        link_channels = config["R/L_LINK"]
        r_gain = config["R_CHANNEL_GAIN"]
        l_gain = config["L_CHANNEL_GAIN"]
        z_cross = config["ZERO_CROSS_DETECTION"]
        lsb_addr = config["SETTINGS_ADDR"]
        data = link_channels + l_gain + r_gain + z_cross + lsb_addr
        print("data:" + data)
        l_pin = config["R_CHANNEL_CS_PIN"]
        r_pin = config["L_CHANNEL_CS_PIN"]
        self.comm.spi_write(r_pin, data)
        self.comm.spi_write(l_pin, data)

    def mute(self):
        master_channel = config["MASTER_CHANNEL"]
        lsb_addr = None
        if master_channel == "R":
            lsb_addr = config["R_VOLUME_ADDR_REGISTER"]
        else:
            lsb_addr = config["L_VOLUME_ADDR_REGISTER"]
        msb_addr = "000000000"
        print("msb:" + msb_addr)
        print("lsb:" + lsb_addr)
        data = msb_addr + lsb_addr
        print(data)
        l_pin = config["R_CHANNEL_CS_PIN"]
        r_pin = config["L_CHANNEL_CS_PIN"]
        self.comm.spi_write(r_pin, data)
        self.comm.spi_write(l_pin, data)

    def get_percentage_volume(self, vol):
        p_vol = map_value(vol, self.MIN_VOLUME, self.MAX_VOLUME, 0, 100)
        return int(p_vol)

    def map_db_to_reg_binary(self, vol):
        vol = abs(vol)
        if vol == 0:  # 0 db corresponds with 32 binary equivalent
            return 32
        return (vol / self.STEP) + 32

    def get_current_volume(self):
        return self.storage.read(CURRENT_MUSES_VOLUME_ID)

    def is_volume_disabled(self):
        return self.storage.read(DISABLE_VOLUME_ID)

    def persist_volume(self, volume):
        self.storage.write(CURRENT_MUSES_VOLUME_ID, volume)

    def disable_enable_volume(self, selected, volume_algorithm: VOLUME_ALGORITHM):
        curr = self.storage.read(DISABLE_VOLUME_ID)
        if (curr == 0 and selected == 0) or (curr == 1 and selected == 1):
            return
        if selected == 1:
            self.update_chip_volume(self.MAX_VOLUME, volume_algorithm)  # disable volume
            self.storage.write(DISABLE_VOLUME_ID, 1)
            return 0  # disabled
        else:
            self.update_chip_volume(self.get_current_volume(), volume_algorithm)
            self.storage.write(DISABLE_VOLUME_ID, 0)
            return 1  # enabled

    def update_ui_volume(self, volume):
        return super().update_ui_volume(
            VOLUME_DEVICE.MUSES, self.connection_manager, volume
        )
