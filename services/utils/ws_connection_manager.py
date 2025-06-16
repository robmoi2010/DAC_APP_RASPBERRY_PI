from enum import Enum
from fastapi import WebSocket
import logging

from registry.register import register


class WS_TYPE(Enum):
    HOME_DATA = 0
    IR_REMOTE = 1


@register
class WSConnectionManager:
    def __init__(self):
        self.connections = {}
        self.logger = logging.getLogger(__name__)

    async def connect(self, type: WS_TYPE, websocket: WebSocket):
        self.connections[type.name] = websocket
        await websocket.accept()

    async def send_data(self, type: WS_TYPE, message: str):
        try:
            await self.connections[type.name].send_text(message)
        except Exception as e:
            self.logger.error(e)
