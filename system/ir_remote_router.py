from registry.register import register
from services.utils.ws_connection_manager import WS_TYPE, WSConnectionManager

from volume.system_volume import Volume
from volume.volume_util import VOL_DIRECTION
from model.model import ResponseModel
from system.system_util import BUTTON


@register
class IrRemoteRouter:

    def __init__(self, volume: Volume, connection_manager: WSConnectionManager = None):
        self.connection_manager = connection_manager
        self.volume = volume

    def handle_remote_button(self, button):
        if button == BUTTON.VOLUME_UP:
            self.volume.updateVolume(VOL_DIRECTION.UP)
        elif button == BUTTON.VOLUME_DOWN:
            self.volume.updateVolume(VOL_DIRECTION.DOWN)
        elif button == BUTTON.POWER:
            pass
        elif button == BUTTON.MUTE:
            self.volume.mute()
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
        await self.connection_manager.send_data(
            WS_TYPE.IR_REMOTE, response.model_dump_json()
        )
