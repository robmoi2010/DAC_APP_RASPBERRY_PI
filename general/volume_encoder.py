import repo.storage as storage
import configs.app_config as app_config
import dac.dac_volume as dac_volume
from dac.dac_volume import VOL_DIRECTION
from gpiozero import RotaryEncoder, Button, Device
from gpiozero.pins.mock import MockFactory

config = app_config.getConfig()

Device.pin_factory = MockFactory()

pinMapConfig = config["GPIO"]["PIN_MAP"]
print(pinMapConfig["ROTARY_PIN_A"])
encoder = RotaryEncoder(
    pinMapConfig["ROTARY_PIN_A"], pinMapConfig["ROTARY_PIN_B"], max_steps=0
)
button = Button(pinMapConfig["ROTARY_BUTTON_PIN"])


def onRotate():
    disabled = dac_volume.isVolumeDisabled()
    if not disabled:  # process if volume is not disabled, else ignore
        steps = encoder.steps
        encoder.steps = 0
        if steps > 0:  # volume up
            dac_volume.updateVolume(VOL_DIRECTION.UP)
        if steps < 0:  # volume down
            dac_volume.updateVolume(VOL_DIRECTION.DOWN)


def rotaryButtonPressed():  # Either mute of disable volume
    knobButtonSetting = getButtonKnobMode()
    if knobButtonSetting == 0:  # for mute
        dac_volume.muteUnmuteDac()
    else:  # for disable volume
        dac_volume.disableEnableVolume()


def setRotaryButtonMode(mode):  # 0 for mute 1 for disable volume
    storage.write("KNOB_BUTTON_MODE", mode)


def getButtonKnobMode():
    return storage.read("KNOB_BUTTON_MODE")


encoder.when_rotated = onRotate
button.when_pressed = rotaryButtonPressed
