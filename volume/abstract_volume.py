from abc import ABC, abstractmethod
import json

from model.model import ResponseModel
from registry.register import register
from services.utils.services_util import VOLUME_DISPLAY_NAME
from services.utils.ws_connection_manager import WS_TYPE, WSConnectionManager
from volume.volume_util import (
    VOL_DIRECTION,
    VOLUME_ALGORITHM,
    VOLUME_DEVICE,
)


@register
class AbstractVolume(ABC):
    @abstractmethod
    def update_volume(
        self, direction: VOL_DIRECTION, volume_algorithm: VOLUME_ALGORITHM
    ):
        pass

    @abstractmethod
    def mute(self):
        pass

    @abstractmethod
    def get_percentage_volume(self, vol):
        pass

    @abstractmethod
    def get_current_volume(self):
        pass

    @abstractmethod
    def is_volume_disabled(self):
        pass

    @abstractmethod
    def persist_volume(self, volume):
        pass

    @abstractmethod
    def disable_enable_volume(self, selected, volume_algorithm: VOLUME_ALGORITHM):
        pass

    @abstractmethod
    def process_new_volume(self, currVol, volume_algorithm: VOLUME_ALGORITHM):
        pass

    @abstractmethod
    def get_volume_from_percentage(self, percentage):
        pass

    @abstractmethod
    def get_max_volume(self):
        pass

    @abstractmethod
    def get_min_volume(self):
        pass

    @abstractmethod
    def is_volume_more_than(self, volume1, volume2):
        pass

    async def update_ui_volume(
        self, device: VOLUME_DEVICE, connection_manager: WSConnectionManager, volume
    ):
        list = []
        id = "CURRENT_VOLUME"
        response = ResponseModel(
            key=id, value=str(volume), display_name=VOLUME_DISPLAY_NAME
        )
        list.append(response)
        data = [dt.model_dump() for dt in list]
        await connection_manager.send_data(WS_TYPE.HOME_DATA, json.dumps(data))
