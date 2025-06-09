from enum import Enum
import json
from configs import app_config
from services.ir_connection_manager import IRConnectionManager

from volume.system_volume import Volume
from volume.volume_util import VOL_DIRECTION
from model.model import ResponseModel
from general.general_util import BUTTON


volume: Volume = None


class IrRemoteRouter:

    def __init__(self, init_object: IRConnectionManager = None):
        self.ir_connection_manager = init_object

    def handle_remote_button(self, button):
        if button == BUTTON.VOLUME_UP:
            volume.updateVolume(VOL_DIRECTION.UP)
        elif button == BUTTON.VOLUME_DOWN:
            volume.updateVolume(VOL_DIRECTION.DOWN)
        elif button == BUTTON.POWER:
            pass
        elif button == BUTTON.MUTE:
            volume.mute()
        elif button == BUTTON.UP:
            self.handle_ws_routing(button)
            # remoteNav.handle_up_button()
        elif button == BUTTON.DOWN:
            self.handle_ws_routing(button)
        # remoteNav.handle_down_button()
        elif button == BUTTON.OK:
            # remoteNav.handle_OK_button()
            self.handle_ws_routing(button)

    async def handle_ws_routing(self, button: BUTTON):
        response: ResponseModel = ResponseModel(
            key=str(button.value), value=button.name, display_name=button.name
        )
        await self.ir_connection_manager.send_data(response.model_dump_json())
