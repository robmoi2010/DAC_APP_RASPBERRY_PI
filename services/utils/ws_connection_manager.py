from fastapi import WebSocket
import logging

logger = logging.getLogger(__name__)


class WSConnectionManager:
    def __init__(self):
        pass

    async def connect(self, websocket: WebSocket):
        self.websocket = websocket
        await websocket.accept()

    async def send_data(self, message: str):
        try:
            await self.websocket.send_text(message)
        except Exception as e:
            logger.error(e)
