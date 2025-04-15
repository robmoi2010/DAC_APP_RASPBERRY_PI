import Storage
import AppConfig
import Communication

# 0 Minimum phase
# 1 Linear phase apodizing first roll-off
# 2 Linear phase fast roll-off
# 3 Linear phase slow roll-off low ripple
# 4 Linear phase slow roll-off
# 5 Minimum phase fast roll-off
# 6 Minimum phase slow roll-off
# 7 Minimum phase slow roll-off low dispersion
config = AppConfig.getConfig("DAC")


def updateFilter(filter):
    Communication.write(config["DAC_I2C_ADDR"], config["DAC_FILTER_SHAPE"], filter)
    Storage.write(config["CURR_FILTER_ADDR"], filter)


def getFilterName(filter, initials):
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
