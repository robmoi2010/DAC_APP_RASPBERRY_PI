import repo.storage as storage
import configs.app_config as app_config
import util.communication as communication

# 0 Minimum phase
# 1 Linear phase apodizing first roll-off
# 2 Linear phase fast roll-off
# 3 Linear phase slow roll-off low ripple
# 4 Linear phase slow roll-off
# 5 Minimum phase fast roll-off
# 6 Minimum phase slow roll-off
# 7 Minimum phase slow roll-off low dispersion
config = app_config.getConfig()["DAC"]["ADDR"]
DAC_I2C_ADDR = config["I2C_ADDR"]
CURRENT_FILTER_ID = "CURRENT_FILTER"


def update_filter(filter):
    filter_shape_addr = config["DAC_FILTER_SHAPE"]
    gen_mask = 0b00000111
    msb = "00000"
    # lsb = format(str(filter), "03b")
    # filter_mask = int(msb + lsb)
    # data = communication.read(DAC_I2C_ADDR, filter_shape_addr)
    # data = data & ~gen_mask  # reset the bits to zero first
    # data = data | filter_mask
    # communication.write(DAC_I2C_ADDR, filter_shape_addr, data)
    storage.write(CURRENT_FILTER_ID, filter)


def get_current_filter():
    return storage.read(CURRENT_FILTER_ID)


def get_filter_name(filter, initials):
    if initials == 0:
        if filter == 0:
            return "Minimum phase"
        elif filter == 1:
            return "Linear phase apodizing first roll-off"
        elif filter == 2:
            return "Linear phase fast roll-off"
        elif filter == 3:
            return "Linear phase slow roll-off low ripple"
        elif filter == 4:
            return "Linear phase slow roll-off"
        elif filter == 5:
            return "Minimum phase fast roll-off"
        elif filter == 6:
            return "Minimum phase slow roll-off"
        elif filter == 7:
            return "Minimum phase slow roll-off low dispersion"
        else:
            return "Minimum Phase"
    else:
        if filter == 0:
            return "MP"
        elif filter == 1:
            return "LPAFR"
        elif filter == 2:
            return "LPFR"
        elif filter == 3:
            return "LPSRLR"
        elif filter == 4:
            return "LPSR"
        elif filter == 5:
            return "MPFR"
        elif filter == 6:
            return "MPSR"
        elif filter == 7:
            return "MPSRLD"
        else:
            return "MP"
