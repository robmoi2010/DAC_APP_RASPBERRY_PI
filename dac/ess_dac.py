import util.communication as communication
import configs.app_config as app_config
import repo.storage as storage

config2 = app_config.getConfig()["DAC"]
config = config2["ADDR"]
DAC_I2C_ADDR = config["I2C_ADDR"]


def enable_dac_analog_section():
    addr = config["SYS_CONFIG"]
    mask = 0b00000010  # mask to change bit for enabling dac analog section
    data = communication.read(DAC_I2C_ADDR, addr)  # sys config register values
    data = data | mask
    communication.write(DAC_I2C_ADDR, addr, data)  # write back modified reg data


def set_i2s_slave_mode():
    enable_dac_analog_section()


def set_lj_slave_mode():
    addr = config["TDM_CONFIG_1"]
    mask = 0b11000000
    data = communication.read(DAC_I2C_ADDR, addr)
    data = data | mask
    communication.write(DAC_I2C_ADDR, addr, data)


def set_i2s_master_mode():
    addr = config["TDM_CONFIG_1"]
    mask = 0b10000000
    data = communication.read(DAC_I2C_ADDR, addr)
    data = data | mask
    communication.write(DAC_I2C_ADDR, addr, data)

    input_sel_addr = config["INPUT_SELECTION"]
    in_mask = 0b00010000
    data2 = communication.read(DAC_I2C_ADDR, input_sel_addr)
    data2 = data2 | in_mask
    communication.write(DAC_I2C_ADDR, input_sel_addr, data2)


def set_spdif_mode():
    # set input to spdif and auto input data format to auto
    input_sel_addr = config["INPUT_SELECTION"]
    in_mask = 0b00000111
    data2 = communication.read(DAC_I2C_ADDR, input_sel_addr)
    data2 = data2 | in_mask
    communication.write(DAC_I2C_ADDR, input_sel_addr, data2)

    # enable spdif decode
    addr = config["SYS_MODE_CONFIG"]
    smask = 0b00001000
    data = communication.read(DAC_I2C_ADDR, addr)
    data = data | smask
    communication.write(DAC_I2C_ADDR, addr, data)

    # set SDB for the spdf gpio pin
    gpio_pin = config2["GPIO"]["SPDIF_GPIO_PIN"]
    sdb_addr = config["DAC_GPIO_INPUT_ADDR"]
    sdb_mask = 0b00000001
    if gpio_pin > 1:
        sdb_mask = sdb_mask << gpio_pin
    data4 = communication.read(DAC_I2C_ADDR, sdb_addr)
    data4 = data4 | sdb_mask
    communication.write(DAC_I2C_ADDR, sdb_addr, data4)

    # set gpio pin for spdif
    spdf_addr = config["DAC_SPDIF_SEL_ADDR"]
    pin_value = gpio_pin + 2
    pin_bin = format(pin_value, "04b")
    gen_mask = 0b11110000
    n = pin_bin + "0000"
    pin_mask = int(n)
    data3 = communication.read(DAC_I2C_ADDR, spdf_addr)
    data3 = data3 & ~gen_mask  # reset to zero first
    data3 = data3 | pin_mask
    communication.write(DAC_I2C_ADDR, spdf_addr, data3)


def initialize_dac():
    # enable dac analog section
    enable_dac_analog_section()
    # setup dac for i2s master mode
    set_i2s_master_mode()


def set_dac_mode(
    mode,
):  # 0 I2S Slave mode, 1 LJ Slave mode, 2 I2S Master mode, 3 SPDIF mode, 4 TDM I2S Slave mode Async, 5 TDM I2S Slave mode Sync
    if mode == 0:
        set_i2s_slave_mode()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    elif mode == 1:
        set_lj_slave_mode()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    elif mode == 2:
        set_i2s_master_mode()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    elif mode == 3:
        set_spdif_mode()
        storage.write("CURRENT_DAC_MODE", mode)
        return
    else:
        set_spdif_mode()
        storage.write("CURRENT_DAC_MODE", mode)
        return


def get_current_dac_mode():
    return storage.read("CURRENT_DAC_MODE")


def is_second_order_compensation_enabled():
    return storage.read("SECOND_ORDER_COMPENSATION_ENABLED") == 1


def is_third_order_compensation_enabled():
    return storage.read("THIRD_ORDER_COMPENSATION_ENABLED") == 1


def enable_disable_second_order_compensation(selected):
    active = is_second_order_compensation_enabled()
    if (selected==1 and active) or (selected==0 and not active):
        return
    reg_1_addr = config["THD_2ND_ORDER_1"]
    reg_2_addr = config["THD_2ND_ORDER_2"]
    reg_3_addr = config["THD_2ND_ORDER_3"]
    reg_4_addr = config["THD_2ND_ORDER_4"]
    print("abc:" + str(active))
    if selected==0:  # disable
        data = 0b00000000
        # store reg values for enabling the setting if not stored yet
        if not storage.read("SECOND_ORDER_COEFFICIENTS_STORED"):
            data1 = communication.read(DAC_I2C_ADDR, reg_1_addr)
            data2 = communication.read(DAC_I2C_ADDR, reg_2_addr)
            data3 = communication.read(DAC_I2C_ADDR, reg_3_addr)
            data4 = communication.read(DAC_I2C_ADDR, reg_4_addr)
            storage.write("SECOND_ORDER_ENABLE_COEFFICIENTS_1", str(data1))
            storage.write("SECOND_ORDER_ENABLE_COEFFICIENTS_2", str(data2))
            storage.write("SECOND_ORDER_ENABLE_COEFFICIENTS_3", str(data3))
            storage.write("SECOND_ORDER_ENABLE_COEFFICIENTS_4", str(data4))
            storage.write("SECOND_ORDER_COEFFICIENTS_STORED", 1)
        # fill all registers with zeros to disable
        communication.write(DAC_I2C_ADDR, reg_1_addr, data)
        communication.write(DAC_I2C_ADDR, reg_2_addr, data)
        communication.write(DAC_I2C_ADDR, reg_3_addr, data)
        communication.write(DAC_I2C_ADDR, reg_4_addr, data)

        storage.write("SECOND_ORDER_COMPENSATION_ENABLED", 0)
    else:  # enable
        # use coefficients stored in memory to enable
        data1 = storage.read("SECOND_ORDER_ENABLE_COEFFICIENTS_1")
        data2 = storage.read("SECOND_ORDER_ENABLE_COEFFICIENTS_2")
        data3 = storage.read("SECOND_ORDER_ENABLE_COEFFICIENTS_3")
        data4 = storage.read("SECOND_ORDER_ENABLE_COEFFICIENTS_4")

        communication.write(DAC_I2C_ADDR, reg_1_addr, data1)
        communication.write(DAC_I2C_ADDR, reg_2_addr, data2)
        communication.write(DAC_I2C_ADDR, reg_3_addr, data3)
        communication.write(DAC_I2C_ADDR, reg_4_addr, data4)
        storage.write("SECOND_ORDER_COMPENSATION_ENABLED", 1)


def enable_disable_third_order_compensation(selected):
    active = is_third_order_compensation_enabled()
    if (selected==1 and active) or (selected==0 and not active):
        return
    reg_1_addr = config["THD_3RD_ORDER_1"]
    reg_2_addr = config["THD_3RD_ORDER_2"]
    reg_3_addr = config["THD_3RD_ORDER_3"]
    reg_4_addr = config["THD_3RD_ORDER_4"]
    if selected==0:  # disable
        data = 0b00000000
        # store reg values for enabling the setting if not stored yet
        if not storage.read("THIRD_ORDER_COEFFICIENTS_STORED"):
            data1 = communication.read(DAC_I2C_ADDR, reg_1_addr)
            data2 = communication.read(DAC_I2C_ADDR, reg_2_addr)
            data3 = communication.read(DAC_I2C_ADDR, reg_3_addr)
            data4 = communication.read(DAC_I2C_ADDR, reg_4_addr)
            storage.write("THIRD_ORDER_ENABLE_COEFFICIENTS_1", str(data1))
            storage.write("THIRD_ORDER_ENABLE_COEFFICIENTS_2", str(data2))
            storage.write("THIRD_ORDER_ENABLE_COEFFICIENTS_3", str(data3))
            storage.write("THIRD_ORDER_ENABLE_COEFFICIENTS_4", str(data4))
            storage.write("THIRD_ORDER_COEFFICIENTS_STORED", 1)
        # fill all registers with zeros to disable
        communication.write(DAC_I2C_ADDR, reg_1_addr, data)
        communication.write(DAC_I2C_ADDR, reg_2_addr, data)
        communication.write(DAC_I2C_ADDR, reg_3_addr, data)
        communication.write(DAC_I2C_ADDR, reg_4_addr, data)

        storage.write("THIRD_ORDER_COMPENSATION_ENABLED", 0)
    else:  # enable
        # use coefficients stored in memory to enable
        data1 = storage.read("THIRD_ORDER_ENABLE_COEFFICIENTS_1")
        data2 = storage.read("THIRD_ORDER_ENABLE_COEFFICIENTS_2")
        data3 = storage.read("THIRD_ORDER_ENABLE_COEFFICIENTS_3")
        data4 = storage.read("THIRD_ORDER_ENABLE_COEFFICIENTS_4")

        communication.write(DAC_I2C_ADDR, reg_1_addr, data1)
        communication.write(DAC_I2C_ADDR, reg_2_addr, data2)
        communication.write(DAC_I2C_ADDR, reg_3_addr, data3)
        communication.write(DAC_I2C_ADDR, reg_4_addr, data4)

        storage.write("THIRD_ORDER_COMPENSATION_ENABLED", 1)
