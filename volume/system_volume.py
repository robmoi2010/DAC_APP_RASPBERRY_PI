import repo.storage as storage

from volume.volume_util import (
    VOLUME_ALGORITHM,
    VOLUME_ALGORITHM_ID,
    VOLUME_DEVICE,
    CURRENT_DEVICE_ID,
)
import configs.app_config as configuration
import math

config = configuration.getConfig()
LOG_CURVE = 0.6


class Volume:
    def __init__(self):
        pass

    def get_current_volume_device(self):
        raise NotImplementedError

    def get_current_volume(self):
        raise NotImplementedError

    def persist_volume(self, volume):
        raise NotImplementedError

    def get_logarithmic_volume_level(self, vol, minimum, maximum):
        vol = max(maximum, min(minimum, vol))  # Clamp to valid range
        if vol == minimum or vol == maximum:
            return vol

        # Normalize and invert (so 0 = loudest)
        x = (minimum - vol) / minimum

        # Apply logarithmic curve
        log_scaled = math.log10(1 + 9 * x) / math.log10(10)  # Range: 0–1

        # Convert back to max–min scale, inverted
        adjusted = minimum - int(round(log_scaled * minimum))
        return adjusted

    def update_ui_volume(self, volume):
        # home.update_volume(volume)
        pass

    def map_value(self, x, in_min, in_max, out_min, out_max):
        return ((x - in_min) * (out_max - out_min)) / ((in_max - in_min) + out_min)

    def update_volume(self, direction):
        raise NotImplementedError

    def mute(self):
        raise NotImplementedError

    def get_percentage_volume(self, volume):
        raise NotImplementedError

    def set_current_volume_device(self):
        raise NotImplementedError

    def is_volume_disabled():
        raise NotImplementedError

    def get_current_volume_algorithm(self):
        algo = storage.read(VOLUME_ALGORITHM_ID)
        if algo == VOLUME_ALGORITHM.LINEAR.value:
            return VOLUME_ALGORITHM.LINEAR
        elif algo == VOLUME_ALGORITHM.LOGARITHMIC.value:
            return VOLUME_ALGORITHM.LOGARITHMIC

    def set_volume_algorithm(self, algo: VOLUME_ALGORITHM):
        storage.write(VOLUME_ALGORITHM_ID, algo.value)


def get_current_volume_device():
    device = storage.read(CURRENT_DEVICE_ID)
    if device == VOLUME_DEVICE.DAC.name:
        return VOLUME_DEVICE.DAC
    elif device == VOLUME_DEVICE.MUSES.name:
        return VOLUME_DEVICE.MUSES
