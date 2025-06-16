import configs.app_config as app_config
from registry.register import register
from util.communication import Comm

config = app_config.getConfig()["DAC"]["ADDR"]
DAC_I2C_ADDR = config["I2C_ADDR"]


@register
class DacComm:
    def __init__(self, comm: Comm):
        self.comm = comm

    def read(self, addr):
        return self.comm.read(DAC_I2C_ADDR, addr)

    def write(self, addr, value):
        return self.comm.write(DAC_I2C_ADDR, addr, value)
