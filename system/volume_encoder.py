import asyncio
from configs.app_config import Config
from gpiozero import RotaryEncoder, Button, Device
from gpiozero.pins.mock import MockFactory
from registry.register import register
from services.utils.ws_connection_manager import WSConnectionManager
from volume.volume_util import VOL_DIRECTION
from volume.system_volume import Volume
from repo.storage import Storage


@register
class VolumeEncoder:
    def __init__(
        self,
        connection_manager: WSConnectionManager,
        volume: Volume,
        storage: Storage,
        config: Config,
    ):
        self.config = config.config
        self.connection_manager = connection_manager
        self.volume = volume
        self.storage = storage
        Device.pin_factory = MockFactory()
        pinMapConfig = self.config["GPIO"]["PIN_MAP"]
        encoder = RotaryEncoder(
            pinMapConfig["ROTARY_PIN_A"], pinMapConfig["ROTARY_PIN_B"], max_steps=0
        )
        button = Button(pinMapConfig["ROTARY_BUTTON_PIN"])

        encoder.when_rotated = self.onRotate
        button.when_pressed = self.rotaryButtonPressed

    def onRotate(self):
        disabled = self.volume.is_volume_disabled()
        if not disabled:  # process if volume is not disabled, else ignore
            steps = self.encoder.steps
            self.encoder.steps = 0
            if steps > 0:  # volume up
                self.volume.update_volume(VOL_DIRECTION.UP)
            if steps < 0:  # volume down
                self.volume.update_volume(VOL_DIRECTION.DOWN)

    def rotaryButtonPressed(self):  # Either mute of disable volume
        knobButtonSetting = self.getButtonKnobMode()
        if knobButtonSetting == 0:  # for mute
            self.volume.mute()
        else:  # for disable volume
            self.volume.disable_enable_volume()

    def setRotaryButtonMode(self, mode):  # 0 for mute 1 for disable volume
        self.storage.write("KNOB_BUTTON_MODE", mode)

    def getButtonKnobMode(self):
        return self.storage.read("KNOB_BUTTON_MODE")
