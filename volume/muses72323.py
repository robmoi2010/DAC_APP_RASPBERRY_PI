from volume.system_volume import Volume
import volume.system_volume as sys_volume
import configs.app_config as configuration
import util.communication as comm
import repo.storage as storage

config = configuration.getConfig()["MUSES72323"]


class Muses72323(Volume):
    def __init__(self):
        super.__init__()
        self.MAX_VOLUME = config["MAX_VOLUME"]
        self.MIN_VOLUME = config["MIN_VOLUME"]
        self.STEP = config["STEP"]

    def update_volume(self, direction):
        curr_volume = super.get_current_volume()
        if direction == super.VOL_DIRECTION.UP:  # volume increase
            if (
                curr_volume >= self.MAX_VOLUME
            ):  # skip processing if volume is already at Max
                return
            curr_volume += self.STEP
        else:
            if (
                curr_volume <= self.MIN_VOLUME
            ):  # skip processing if volume is already at Minimum
                return
            curr_volume -= self.STEP
            print("after step:" + str(curr_volume))
        self.update_chip_volume(curr_volume)
        super.persist_volume(curr_volume)
        # update ui with the new volume
        super.update_ui_volume(curr_volume)

    def update_chip_volume(self, vol):
        # if logarithmic is set adjust volume to logarithmic scale
        if (
            super.get_current_volume_algorithm() == super.VOLUME_ALGORITHM.LOGARITHMIC
        ):  # fix issue of algorithm returning 0 during implementation
            vol = super.get_logarithmic_volume_level(
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
        comm.spi_write(r_pin, data)
        comm.spi_write(l_pin, data)

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
        comm.spi_write(r_pin, data)
        comm.spi_write(l_pin, data)

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
        comm.spi_write(r_pin, data)
        comm.spi_write(l_pin, data)

    def get_percentage_volume(self, vol):
        print(vol)
        p_vol = super.map_value(vol, self.MIN_VOLUME, self.MAX_VOLUME, 0, 100)
        print(p_vol)
        return int(p_vol)

    def map_db_to_reg_binary(self, vol):
        vol = abs(vol)
        if vol == 0:  # 0 db corresponds with 32 binary equivalent
            return 32
        return (vol / self.STEP) + 32

    def set_current_volume_device(self):
        storage.write(self.CURRENT_DEVICE_ID, sys_volume.VOLUME_DEVICE.MUSES.name)

    def get_current_volume_device(self):
        sys_volume.VOLUME_DEVICE.MUSES

    def get_current_volume(self):
        return storage.read(sys_volume.CURRENT_MUSES_VOLUME_ID)

    def persist_volume(self, volume):
        storage.write(sys_volume.CURRENT_MUSES_VOLUME_ID, volume)
