import Communication
import AppConfig

config = AppConfig.getConfig()["DAC"]["ADDR"]
DAC_I2C_ADDR = config["DAC_I2C_ADDR"]


def setI2sSlaveMode():
    Communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)


def setLjSlaveMode():
    Communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)
    Communication.write(DAC_I2C_ADDR, config["DAC_TDM_VALID_EDGE_ADDR"], 1)


def setI2sMasterMode():
    Communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)
    Communication.write(DAC_I2C_ADDR, config["DAC_PCM_MASTER_MODE_ADDR"], 1)


def setSPDIFMode():
    Communication.write(DAC_I2C_ADDR, config["DAC_ENABLE_SPDIF_DECODE_ADDR"], 1)
    Communication.write(DAC_I2C_ADDR, config["DAC_AUTO_INPUT_SEL_ADDR"], 1)
    Communication.write(DAC_I2C_ADDR, config["DAC_SPDIF_SEL_ADDR"], 6) # GPIO4
    Communication.write(DAC_I2C_ADDR, config["DAC_GPIO4_SDB_ADDR"], 1)
    Communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)


def setTDMI2SSlaveModeAsync():
    Communication.write(DAC_I2C_ADDR, config["DAC_AUTO_CH_DETECT_ADDR"], 1)
    Communication.write(DAC_I2C_ADDR, config["DAC_TDM_CH1_SEL_ADDR"], 2)
    Communication.write(DAC_I2C_ADDR, config["DAC_TDM_CH2_SEL_ADDR"], 3)
    Communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)


def setTDMI2SSlaveModeSync():
    Communication.write(DAC_I2C_ADDR, config["DAC_AUTO_CH_DETECT_ADDR"], 1)
    Communication.write(DAC_I2C_ADDR, config["DAC_SYNC_MODE_ADDR"], 1)
    Communication.write(DAC_I2C_ADDR, config["DAC_TDM_CH1_SEL_ADDR"], 2)
    Communication.write(DAC_I2C_ADDR, config["DAC_TDM_CH2_SEL_ADDR"], 3)
    Communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)


def initializeDAC():
    # setup dac for i2s master mode
    setI2sMasterMode()


def setDacMode(
    mode,
):  # 0 I2S Slave mode, 1 LJ Slave mode, 2 I2S Master mode, 3 SPDIF mode, 4 TDM I2S Slave mode Async, 5 TDM I2S Slave mode Sync
    if mode == 0:
        setI2sSlaveMode()
        return
    elif mode == 1:
        setLjSlaveMode()
        return
    elif mode == 2:
        setI2sMasterMode()
        return
    elif mode == 3:
        setSPDIFMode()
        return
    elif mode == 4:
        setTDMI2SSlaveModeAsync()
        return
    elif mode == 5:
        setTDMI2SSlaveModeSync()
        return
    else:
        setSPDIFMode()
        return
