from configs.app_config import Config
from registry.register import register
from util.communication import Comm


@register
class DacComm:
    def __init__(self, comm: Comm, config: Config):
        self.config = config.config["DAC"]["ADDR"]
        self.DAC_I2C_ADDR = self.config["I2C_ADDR"]
        self.comm = comm

    def read(self, addr):
        return self.comm.read(self.DAC_I2C_ADDR, addr)

    def write(self, addr, value):
        return self.comm.write(self.DAC_I2C_ADDR, addr, value)
