import Storage
import AppConfig
import Communication
from gpiozero import RotaryEncoder, Button

DAC_MIN_VOL = 255
DAC_MAX_VOL = 0
LOG_CURVE = 6
config = AppConfig.getConfig()
addrConfig = config["DAC"]["ADDR"]
storageConfig = config["DAC"]["STORAGE"]
pinMapConfig = config["GPIO"]["PIN_MAP"]

encoder = RotaryEncoder(
    pinMapConfig["ROTARY_PIN_A"], pinMapConfig["ROTARY_PIN_B"], max_steps=0
)
button = Button(pinMapConfig["ROTARY_BUTTON_PIN"])


def getLogarithmicVolumeLevel(vol):
    return pow(vol, 1 / LOG_CURVE)


def getCurrentVolume():
    return 0
    # return Storage.read(storageConfig["CURR_VOL_ADDR"])


def persistVolume(volume):
    Storage.write(storageConfig["CURR_VOL_ADDR"], volume)


def setVolume(volume):
    # add logic for channels hold before volume change
    Communication.write(addrConfig["DAC_I2C_ADDR"], addrConfig["VOLUME_CH1"], volume)
    Communication.write(addrConfig["DAC_I2C_ADDR"], addrConfig["VOLUME_CH2"], volume)


def updateVolume(direction):
    currVol = getCurrentVolume()
    steps = config["DAC"]["VOLUME"]["VOLUME_STEPS"]  # get volume steps from config
    if direction == "up":  # volume increase
        currVol -= steps  # dacs lower value=increase
        if currVol < DAC_MAX_VOL:
            currVol = DAC_MAX_VOL
    else:
        currVol += steps  # dacs higher value=decrease
        if currVol > DAC_MIN_VOL:
            currVol = DAC_MIN_VOL
    # currVol = getLogarithmicVolumeLevel(currVol)  # change from linear to logarithmic
    setVolume(currVol)
    persistVolume(currVol)


def disableEnableVolume():
    curr = Storage.read(storageConfig["DISABLE_VOL_ADDR"])
    if curr == 0:
        setVolume(DAC_MAX_VOL)  # disable volume
        Storage.write(storageConfig["DISABLE_VOL_ADDR"], 1)
        return 0  # disabled
    else:
        setVolume(getCurrentVolume())
        Storage.write(storageConfig["DISABLE_VOL_ADDR"], 0)
        return 1  # enabled


def onRotate():
    steps = encoder.steps
    encoder.steps = 0
    if steps > 0:  # volume up
        updateVolume("up")
    if steps < 0:  # volume down
        updateVolume("down")


def rotaryButtonPressed():  #
    pass


def getPercentageVolume(volume):
    return map_value(volume, DAC_MIN_VOL, DAC_MAX_VOL, 0, 100)


def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


encoder.when_rotated = onRotate
button.when_pressed = rotaryButtonPressed
