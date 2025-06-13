import repo.storage as storage
import configs.app_config as app_config
from factory.system_factory import SYS_OBJECTS
import factory.system_factory as factory
from gpiozero import RotaryEncoder, Button, Device
from gpiozero.pins.mock import MockFactory
from services.utils.ws_connection_manager import WSConnectionManager

config = app_config.getConfig()

Device.pin_factory = MockFactory()

pinMapConfig = config["GPIO"]["PIN_MAP"]
print(pinMapConfig["ROTARY_PIN_A"])
encoder = RotaryEncoder(
    pinMapConfig["ROTARY_PIN_A"], pinMapConfig["ROTARY_PIN_B"], max_steps=0
)
connection_manager=None
button = Button(pinMapConfig["ROTARY_BUTTON_PIN"])
volume = factory.new(SYS_OBJECTS.VOLUME, connection_manager)


def onRotate():
    disabled = volume.is_volume_disabled()
    if not disabled:  # process if volume is not disabled, else ignore
        steps = encoder.steps
        encoder.steps = 0
        if steps > 0:  # volume up
            volume.update_volume(volume.VOL_DIRECTION.UP)
        if steps < 0:  # volume down
            volume.update_volume(volume.VOL_DIRECTION.DOWN)


def rotaryButtonPressed():  # Either mute of disable volume
    knobButtonSetting = getButtonKnobMode()
    if knobButtonSetting == 0:  # for mute
        volume.mute()
    else:  # for disable volume
        volume.disable_enable_volume()


def setRotaryButtonMode(mode):  # 0 for mute 1 for disable volume
    storage.write("KNOB_BUTTON_MODE", mode)


def getButtonKnobMode():
    return storage.read("KNOB_BUTTON_MODE")


encoder.when_rotated = onRotate
button.when_pressed = rotaryButtonPressed
