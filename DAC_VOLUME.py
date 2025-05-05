import Storage
import AppConfig
import Communication
from gpiozero import RotaryEncoder, Button, Device
from gpiozero.pins.mock import MockFactory

Device.pin_factory = MockFactory()

DAC_MIN_VOL = 255
DAC_MAX_VOL = 0
LOG_CURVE = 6
config = AppConfig.getConfig()
addrConfig = config["DAC"]["ADDR"]
pinMapConfig = config["GPIO"]["PIN_MAP"]
print(pinMapConfig["ROTARY_PIN_A"])
encoder = RotaryEncoder(
    pinMapConfig["ROTARY_PIN_A"], pinMapConfig["ROTARY_PIN_B"], max_steps=0
)
button = Button(pinMapConfig["ROTARY_BUTTON_PIN"])


def getLogarithmicVolumeLevel(vol):
    return pow(vol, 1 / LOG_CURVE)


def getCurrentVolume():
    return Storage.read("CURRENT_VOLUME")


def persistVolume(volume):
    Storage.write("CURRENT_VOLUME", volume)


def setVolume(volume):
    # hold both channels
    # Communication.write(addrConfig["I2C_ADDR"], addrConfig["VOLUME_HOLD"], 1)
    # update volume of both channels
    Communication.write(addrConfig["I2C_ADDR"], addrConfig["VOLUME_CH1"], volume)
    Communication.write(addrConfig["I2C_ADDR"], addrConfig["VOLUME_CH2"], volume)
    # release hold on both channels


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


def isVolumeDisabled():
    return Storage.read("DISABLE_VOLUME")


def disableEnableVolume():
    curr = Storage.read("DISABLE_VOLUME")
    print(curr)
    if curr == 0:
        setVolume(DAC_MAX_VOL)  # disable volume
        Storage.write("DISABLE_VOLUME", 1)
        return 0  # disabled
    else:
        setVolume(getCurrentVolume())
        Storage.write("DISABLE_VOLUME", 0)
        return 1  # enabled


def onRotate():
    disabled = isVolumeDisabled()
    if disabled == False:  # process if volume is not disabled, else ignore
        steps = encoder.steps
        encoder.steps = 0
        if steps > 0:  # volume up
            updateVolume("up")
        if steps < 0:  # volume down
            updateVolume("down")


def muteDac():
    Communication.write(addrConfig["I2C_ADDR"], addrConfig["DAC_MUTE"], 3)


def unmuteDac():
    Communication.write(addrConfig["I2C_ADDR"], addrConfig["DAC_MUTE"], 0)


def rotaryButtonPressed():  # Either mute of disable volume
    knobButtonSetting = getButtonKnobMode()
    if knobButtonSetting == 0:  # for mute
        muted = Storage.read("DAC_MUTED")
        if muted == 1:
            unmuteDac()
            Storage.write("DAC_MUTED", 0)
        else:
            muteDac()
            Storage.write("DAC_MUTED", 1)
    else:  # for disable volume
        disableEnableVolume()


def getButtonKnobMode():
    return Storage.read("KNOB_BUTTON_MODE")


def getPercentageVolume(volume):
    val = map_value(volume, DAC_MIN_VOL, DAC_MAX_VOL, 0, 100)
    return int(val)


def map_value(x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min)) / ((in_max - in_min) + out_min)


def setRotaryButtonMode(mode):  # 0 for mute 1 for disable volume
    Storage.write("KNOB_BUTTON_MODE", mode)


encoder.when_rotated = onRotate
button.when_pressed = rotaryButtonPressed
