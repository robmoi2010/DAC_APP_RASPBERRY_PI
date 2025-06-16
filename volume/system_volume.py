from dac.dac_volume import DacVolume
from registry.register import register, get_instance
from services.utils.ws_connection_manager import WS_TYPE, WSConnectionManager
from muses.muses72323 import Muses72323
from volume.volume_util import (
    VOLUME_ALGORITHM,
    VOLUME_ALGORITHM_ID,
    VOLUME_DEVICE,
    CURRENT_DEVICE_ID,
    CURRENT_VOLUME_ID,
    CURRENT_MUSES_VOLUME_ID,
)
import configs.app_config as configuration
import math
from model.model import ResponseModel
from services.utils.services_util import VOLUME_DISPLAY_NAME
import json
from repo.storage import Storage

config = configuration.getConfig()
LOG_CURVE = 0.6


@register
class Volume:
    def __init__(
        self,
        muses: Muses72323,
        dac_volume: DacVolume,
        storage: Storage,
        connection_manager: WSConnectionManager = None,
    ):
        self.storage = storage
        self.connection_manager: WSConnectionManager = connection_manager
        default = self.get_current_volume_device()
        if default == VOLUME_DEVICE.DAC:
            self.default_volume = dac_volume
        else:
            self.default_volume = muses

    def get_current_volume_device(self):
        return self.storage.read(CURRENT_DEVICE_ID)

    def persist_volume(self, volume):
        self.default_volume.persist_volume(volume)

    async def update_volume(self, direction):
        vol = self.default_volume.update_volume(
            direction, self.get_current_volume_algorithm()
        )
        return await self.update_ui_volume(vol)

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

    async def update_ui_volume(self, vol):
        list = []
        device = self.get_current_volume_device()
        id = None
        if device == VOLUME_DEVICE.DAC.value:
            id = CURRENT_VOLUME_ID
        elif device == VOLUME_DEVICE.MUSES.value:
            id = CURRENT_MUSES_VOLUME_ID
        response = ResponseModel(
            key=id, value=str(vol), display_name=VOLUME_DISPLAY_NAME
        )
        list.append(response)
        data = [dt.model_dump() for dt in list]
        await self.connection_manager.send_data(WS_TYPE.HOME_DATA, json.dumps(data))

    def get_current_volume(self):
        return self.default_volume.get_current_volume()

    def disable_enable_volume(self, selected):
        return self.default_volume.disable_enable_volume(
            selected, self.get_current_volume_algorithm()
        )
