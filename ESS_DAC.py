import communication
import app_config
import storage

config = app_config.getConfig()["DAC"]["ADDR"]
DAC_I2C_ADDR = config["I2C_ADDR"]


def setI2sSlaveMode():
    communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)


def setLjSlaveMode():
    communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)
    communication.write(DAC_I2C_ADDR, config["DAC_TDM_VALID_EDGE_ADDR"], 1)


def setI2sMasterMode():
    communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)
    communication.write(DAC_I2C_ADDR, config["DAC_PCM_MASTER_MODE_ADDR"], 1)


def setSPDIFMode():
    communication.write(DAC_I2C_ADDR, config["DAC_ENABLE_SPDIF_DECODE_ADDR"], 1)
    communication.write(DAC_I2C_ADDR, config["DAC_AUTO_INPUT_SEL_ADDR"], 1)
    communication.write(DAC_I2C_ADDR, config["DAC_SPDIF_SEL_ADDR"], 6)  # GPIO4
    communication.write(DAC_I2C_ADDR, config["DAC_GPIO4_SDB_ADDR"], 1)
    communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)


def setTDMI2SSlaveModeAsync():
    communication.write(DAC_I2C_ADDR, config["DAC_AUTO_CH_DETECT_ADDR"], 1)
    communication.write(DAC_I2C_ADDR, config["DAC_TDM_CH1_SEL_ADDR"], 2)
    communication.write(DAC_I2C_ADDR, config["DAC_TDM_CH2_SEL_ADDR"], 3)
    communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)


def setTDMI2SSlaveModeSync():
    communication.write(DAC_I2C_ADDR, config["DAC_AUTO_CH_DETECT_ADDR"], 1)
    communication.write(DAC_I2C_ADDR, config["DAC_SYNC_MODE_ADDR"], 1)
    communication.write(DAC_I2C_ADDR, config["DAC_TDM_CH1_SEL_ADDR"], 2)
    communication.write(DAC_I2C_ADDR, config["DAC_TDM_CH2_SEL_ADDR"], 3)
    communication.write(DAC_I2C_ADDR, config["DAC_MODE_ADDR"], 1)


def initializeDAC():
    # setup dac for i2s master mode
    setI2sMasterMode()


def setDacMode(
    mode,
):  # 0 I2S Slave mode, 1 LJ Slave mode, 2 I2S Master mode, 3 SPDIF mode, 4 TDM I2S Slave mode Async, 5 TDM I2S Slave mode Sync
    print(mode)
    if mode == 0:
        setI2sSlaveMode()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    elif mode == 1:
        setLjSlaveMode()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    elif mode == 2:
        setI2sMasterMode()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    elif mode == 3:
        setSPDIFMode()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    elif mode == 4:
        setTDMI2SSlaveModeAsync()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    elif mode == 5:
        setTDMI2SSlaveModeSync()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    else:
        setSPDIFMode()
        storage.write("CURRENT_DAC_MODE", mode)
        return


def getCurrentDacMode():
    return storage.read("CURRENT_DAC_MODE")
