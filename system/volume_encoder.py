import configs.app_config as app_config
from gpiozero import RotaryEncoder, Button, Device
from gpiozero.pins.mock import MockFactory
from services.utils import ws_connection_manager
from registry.register import register, get_instance
from volume.volume_util import VOL_DIRECTION
from volume.system_volume import Volume
from repo.storage import Storage

config = app_config.getConfig()

Device.pin_factory = MockFactory()

pinMapConfig = config["GPIO"]["PIN_MAP"]
encoder = RotaryEncoder(
    pinMapConfig["ROTARY_PIN_A"], pinMapConfig["ROTARY_PIN_B"], max_steps=0
)
connection_manager: ws_connection_manager = get_instance("wsconnectionmanager")
button = Button(pinMapConfig["ROTARY_BUTTON_PIN"])
volume: Volume = get_instance("volume", connection_manager)
storage: Storage = get_instance("storage")


@register
class VolumeEncoder:
    def __init__(self):
        pass

    def onRotate(self):
        disabled = volume.is_volume_disabled()
        if not disabled:  # process if volume is not disabled, else ignore
            steps = encoder.steps
            encoder.steps = 0
            if steps > 0:  # volume up
                volume.update_volume(VOL_DIRECTION.UP)
            if steps < 0:  # volume down
                volume.update_volume(VOL_DIRECTION.DOWN)

    def rotaryButtonPressed(self):  # Either mute of disable volume
        knobButtonSetting = self.getButtonKnobMode()
        if knobButtonSetting == 0:  # for mute
            volume.mute()
        else:  # for disable volume
            volume.disable_enable_volume()

    def setRotaryButtonMode(self, mode):  # 0 for mute 1 for disable volume
        storage.write("KNOB_BUTTON_MODE", mode)

    def getButtonKnobMode(self):
        return storage.read("KNOB_BUTTON_MODE")

    encoder.when_rotated = onRotate
    button.when_pressed = rotaryButtonPressed
