from dac.dac_volume import DacVolume
from registry.register import register
from muses.muses72323 import Muses72323
from alps.alps_pot import AlpsPot
from volume.abstract_volume import AbstractVolume
from volume.volume_util import (
    VOLUME_ALGORITHM,
    VOLUME_ALGORITHM_ID,
    VOLUME_DEVICE,
    CURRENT_DEVICE_ID,
)
import configs.app_config as configuration
from repo.storage import Storage

config = configuration.getConfig()
LOG_CURVE = 0.6


@register
class Volume:
    def __init__(
        self, muses: Muses72323, dac_volume: DacVolume, storage: Storage, alps: AlpsPot
    ):
        self.storage = storage
        default = self.get_current_volume_device()
        if default == VOLUME_DEVICE.DAC.value:
            self.default_volume: AbstractVolume = dac_volume
        elif default == VOLUME_DEVICE.ALPS.value:
            self.default_volume: AbstractVolume = alps
        elif default == VOLUME_DEVICE.MUSES.value:
            self.default_volume: AbstractVolume = muses

    def get_current_volume_device(self):
        return self.storage.read(CURRENT_DEVICE_ID)

    def persist_volume(self, volume):
        self.default_volume.persist_volume(volume)

    async def update_volume(self, direction):
        vol = self.default_volume.update_volume(
            direction, self.get_current_volume_algorithm()
        )
        try:
            await self.default_volume.update_ui_volume(vol)
        except Exception as e:
            pass
        return vol

    def mute(self):
        self.default_volume.mute()

    def get_percentage_volume(self, volume):
        return self.default_volume.get_percentage_volume(volume)

    def set_current_volume_device(self, device):
        self.storage.write(CURRENT_DEVICE_ID, device)

    def is_volume_disabled(self):
        return self.default_volume.is_volume_disabled()

    def get_current_volume_algorithm(self):
        algo = self.storage.read(VOLUME_ALGORITHM_ID)
        if algo == VOLUME_ALGORITHM.LINEAR.value:
            return VOLUME_ALGORITHM.LINEAR
        elif algo == VOLUME_ALGORITHM.LOGARITHMIC.value:
            return VOLUME_ALGORITHM.LOGARITHMIC

    def set_volume_algorithm(self, algo: VOLUME_ALGORITHM):
        self.storage.write(VOLUME_ALGORITHM_ID, algo.value)

    def get_current_volume(self):
        return self.default_volume.get_current_volume()

    def disable_enable_volume(self, selected):
        return self.default_volume.disable_enable_volume(
            selected, self.get_current_volume_algorithm()
        )
