from configs.app_config import Config
from registry.register import register
from util.communication import Comm


@register
class DspComm:
    def __init__(self, comm: Comm, config: Config):
        self.comm = comm
        self.config = config.config["ADAU1452"]["ADDR"]

    def read(self, addr):
        return self.comm.read(self.config["I2C_ADDR_READ"], addr)

    def write(self, addr, value):
        return self.comm.write(self.config["I2C_ADDR_WRITE"], addr, value)
