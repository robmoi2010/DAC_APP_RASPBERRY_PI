# Confirm ess dac register format and value format during implementation

# import board

# import busio
import logging

from registry.register import register

# import digitalio

# i2c = busio.I2C(board.SCL, board.SDA)
# spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)


@register
class Comm:
    def __init__(self):
        pass

    def read(self, devAddr, addr):
        try:
            # while not i2c.try_lock():
            #     pass
            # i2c.writeto(devAddr, bytes([addr]))
            # results = bytearray(20)
            # i2c.readfrom(devAddr, results)
            # return results
            return 1111111111
        except Exception as e:
            logging.error(e)
        finally:
            # i2c.unlock()
            pass

    def write(self, devAddr, addr, value):
        try:
            # while not i2c.try_lock():
            #     pass
            # i2c.writeto(devAddr, bytes([addr, value]))
            pass
        except Exception as e:
            logging.error(e)
        finally:
            # i2c.unlock()
            pass

    def get_board_pin(self, pin):
        # if pin == 0:
        #     return board.A0
        # elif pin == 1:
        #     return board.A1
        # elif pin == 2:
        #     return board.A2
        # elif pin == 3:
        #     return board.A3
        # elif pin == 4:
        #     return board.A4
        # elif pin == 5:
        #     return board.A5
        # else:
        #     return board.A0
        pass

    def spi_write(self, cs_pin, command):
        # cs = digitalio.DigitalInOut(get_board_pin(cs_pin))  # Choose an available GPIO pin
        # cs.direction = digitalio.Direction.OUTPUT
        # cs.value = True
        # # Wait for SPI to be ready
        # while not spi.try_lock():
        #     pass
        # try:
        #     spi.configure(baudrate=1000000, phase=0, polarity=0)
        #     cs.value = False
        #     spi.write(command)
        #     cs.value = True
        # except Exception as e:
        #     logging.error(e)
        pass
