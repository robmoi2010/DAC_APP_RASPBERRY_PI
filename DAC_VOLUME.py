import storage
import app_config
import communication

from enum import Enum


class VOL_DIRECTION(Enum):
    UP = 0
    DOWN = 1


DAC_MIN_VOL = 255
DAC_MAX_VOL = 0
LOG_CURVE = 6
config = app_config.getConfig()
addrConfig = config["DAC"]["ADDR"]


def getLogarithmicVolumeLevel(vol):
    return pow(vol, 1 / LOG_CURVE)


def getCurrentVolume():
    return storage.read("CURRENT_VOLUME")


def persistVolume(volume):
    storage.write("CURRENT_VOLUME", volume)


def setVolume(volume):
    # hold both channels
    # communication.write(addrConfig["I2C_ADDR"], addrConfig["VOLUME_HOLD"], 1)
    # update volume of both channels
    communication.write(addrConfig["I2C_ADDR"], addrConfig["VOLUME_CH1"], volume)
    communication.write(addrConfig["I2C_ADDR"], addrConfig["VOLUME_CH2"], volume)
    # release hold on both channels


def updateVolume(direction):
    currVol = getCurrentVolume()
    steps = config["DAC"]["VOLUME"]["VOLUME_STEPS"]  # get volume steps from config
    if direction == VOL_DIRECTION.UP:  # volume increase
        if currVol <= DAC_MAX_VOL:  # skip processing if volume is already at Max
            return
        currVol -= steps  # dacs lower value=increase

    else:
        if currVol >= DAC_MIN_VOL:  # skip processing if volume is already at Minimum
            return
        currVol += steps  # dacs higher value=decrease

    # currVol = getLogarithmicVolumeLevel(currVol)  # change from linear to logarithmic
    setVolume(currVol)
    persistVolume(currVol)


def isVolumeDisabled():
    return storage.read("DISABLE_VOLUME")


def disableEnableVolume():
    curr = storage.read("DISABLE_VOLUME")
    if curr == 0:
        setVolume(DAC_MAX_VOL)  # disable volume
        storage.write("DISABLE_VOLUME", 1)
        return 0  # disabled
    else:
        setVolume(getCurrentVolume())
        storage.write("DISABLE_VOLUME", 0)
        return 1  # enabled


def muteDac():
    communication.write(addrConfig["I2C_ADDR"], addrConfig["DAC_MUTE"], 3)


def unmuteDac():
    communication.write(addrConfig["I2C_ADDR"], addrConfig["DAC_MUTE"], 0)


def muteUnmuteDac():
    muted = storage.read("DAC_MUTED")
    if muted == 1:
        unmuteDac()
        storage.write("DAC_MUTED", 0)
    else:
        muteDac()
        storage.write("DAC_MUTED", 1)

def getPercentageVolume(volume):
    val = map_value(volume, DAC_MIN_VOL, DAC_MAX_VOL, 0, 100)
    return int(val)


def map_value(x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min)) / ((in_max - in_min) + out_min)
