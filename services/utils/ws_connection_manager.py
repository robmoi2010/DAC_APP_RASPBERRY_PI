import asyncio
from enum import Enum
from queue import Empty, Queue
import threading
import time
import traceback
from fastapi import WebSocket, WebSocketDisconnect
import logging

from registry.register import register


class WS_TYPE(Enum):
    HOME_DATA = 0
    IR_REMOTE = 1


ws_connect_queue = Queue()
ws_send_data_queue = Queue()
connections = {}


@register
class WSConnectionManager:
    """Web-socket connection manager class. Manages all web socket connection types."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def connect(self, type: WS_TYPE, websocket: WebSocket) -> None:
        ws_connect_queue.put({"type": type, "websocket": websocket})

    async def _connect(self, type: WS_TYPE, websocket: WebSocket) -> None:
        if type.name not in connections:
            connections[type.name] = [websocket]
        else:
            connections[type.name].append(websocket)

    async def send_data(self, type: WS_TYPE, message: str):
        ws_send_data_queue.put({"type": type, "msg": message})

    async def _send_data(self, type: WS_TYPE, message: str) -> None:
        try:
            if type.name in connections:
                for conn in connections[type.name]:
                    try:
                        await conn.send_text(message)
                    except (RuntimeError, WebSocketDisconnect):
                        connections[type.name].remove(conn)
                    except Exception as e:
                        self.logger.error(traceback.format_exc())
        except Exception as e:
            self.logger.error(traceback.format_exc())

    def ws_connect_queue_consumer(self):
        print("[ws_connect_consumer] Thread started")
        while True:
            try:
                conn = ws_connect_queue.get(block=True)
                print(
                    f"[ws_connect_consumer] Received connect request for '{conn["type"]}'"
                )
                asyncio.run(self._connect(conn["type"], conn["websocket"]))
            except Exception as e:
                self.logger.error(traceback.format_exc())
                print(f"[ws_connect_consumer ERROR] While creating connection: {e}")
            finally:
                time.sleep(0.1)

    def ws_send_data_queue_consumer(self):
        print("[ws_data_send consumer] Thread started")
        while True:
            try:
                conn = ws_send_data_queue.get(block=True)
                asyncio.run(self._send_data(conn["type"], conn["msg"]))
            except Exception as e:
                self.logger.error(traceback.format_exc())
                print(f"[ws_data_send consumer ERROR] While sending data: {e}")
            finally:
                time.sleep(0.001)

    def start_consumers(self):
        threading.Thread(target=self.ws_connect_queue_consumer, daemon=True).start()
        threading.Thread(target=self.ws_send_data_queue_consumer, daemon=True).start()
