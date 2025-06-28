from registry.register import register
from util.communication import Comm


@register
class MusesComm:
    def __init__(self, comm: Comm):
        self.comm = comm

    def spi_write(self, cs_pin, command):
        return self.comm.spi_write(cs_pin, command)
