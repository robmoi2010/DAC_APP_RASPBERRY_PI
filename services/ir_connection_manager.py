from services.ws_connection_manager import WSConnectionManager


class IRConnectionManager(WSConnectionManager):
    def __init__(self):
        super().__init__()
