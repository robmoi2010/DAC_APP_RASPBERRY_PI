import volume.system_volume as volume
import configs.app_config as configuration
import util.communication as comm

config = configuration.getConfig()["MUSES72323"]
MAX_VOLUME = config["MAX_VOLUME"]
MIN_VOLUME = config["MIN_VOLUME"]
STEP = config["STEP"]


class Muses72323:
    def __init__(self):
        pass

    def update_volume(self, direction):
        curr_volume = volume.get_current_volume()
        if direction == volume.VOL_DIRECTION.UP:  # volume increase
            if curr_volume >= MAX_VOLUME:  # skip processing if volume is already at Max
                return
            curr_volume += STEP
        else:
            if (
                curr_volume <= MIN_VOLUME
            ):  # skip processing if volume is already at Minimum
                return
            curr_volume -= STEP
        self.update_chip_volume(curr_volume)
        volume.persist_volume(curr_volume)
        # update ui with the new volume
        volume.update_ui_volume(curr_volume)

    def update_chip_volume(self, vol):
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
        p_vol = volume.map_value(vol, MIN_VOLUME, MAX_VOLUME, 0, 100)
        print(p_vol)
        return int(p_vol)

    def map_db_to_reg_binary(self, vol):
        vol = abs(vol)
        if vol == 0:  # 0 db corresponds with 32 binary equivalent
            return 32
        return (vol / STEP) + 32
