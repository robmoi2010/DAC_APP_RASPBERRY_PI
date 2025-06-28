import configs.app_config as app_config
from registry.register import register
from util.communication import Comm


config = app_config.getConfig()["ADAU1452"]["ADDR"]


@register
class DspComm:
    def __init__(self, comm: Comm):
        self.comm = comm

    def read(self, addr):
        return self.comm.read(config["I2C_ADDR_READ"], addr)

    def write(self, addr, value):
        return self.comm.write(config["I2C_ADDR_WRITE"], addr, value)
