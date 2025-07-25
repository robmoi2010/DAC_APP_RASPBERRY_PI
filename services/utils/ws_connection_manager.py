from enum import Enum
import threading
from fastapi import WebSocket, WebSocketDisconnect
import logging

from registry.register import register


class WS_TYPE(Enum):
    HOME_DATA = 0
    IR_REMOTE = 1


ws_lock = threading.RLock()


@register
class WSConnectionManager:
    """Web-socket connection manager class. Manages all web socket connection types."""

    def __init__(self):
        self.connections = {}
        self.logger = logging.getLogger(__name__)

    async def connect(self, type: WS_TYPE, websocket: WebSocket):
        with ws_lock:
            if type.name not in self.connections:
                self.connections[type.name] = [websocket]
            else:
                self.connections[type.name].append(websocket)

    async def send_data(self, type: WS_TYPE, message: str):
        with ws_lock:
            try:
                if type.name in self.connections:
                    for conn in self.connections[type.name]:
                        try:
                            await conn.send_text(message)
                        except (RuntimeError, WebSocketDisconnect):
                            self.connections[type.name].remove(conn)
                        except Exception as e:
                            self.logger.error(e)
            except Exception as e:
                self.logger.error(e)
