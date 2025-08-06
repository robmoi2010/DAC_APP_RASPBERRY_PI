from configs.app_config import Config
from registry.register import register
from dac.dac_comm import DacComm
from repo.storage import Storage
from services.utils.ws_connection_manager import WSConnectionManager


@register
class Dac:
    def __init__(
        self,
        dac_comm: DacComm,
        storage: Storage,
        ws_connection: WSConnectionManager,
        config: Config,
    ):
        self.config = config.config["DAC"]
        self.addr_config = self.config["ADDR"]
        self.DAC_I2C_ADDR = self.addr_config["I2C_ADDR"]
        self.dac_comm = dac_comm
        self.storage = storage
        self.ws_connection = ws_connection

    def enable_dac_analog_section(self):
        addr = self.addr_config["SYS_CONFIG"]
        mask = 0b00000010  # mask to change bit for enabling dac analog section
        data = self.dac_comm.read(addr)  # sys config register values
        data = data | mask
        self.dac_comm.write(addr, data)  # write back modified reg data

    def set_i2s_slave_mode(self):
        self.enable_dac_analog_section()

    def set_lj_slave_mode(self):
        addr = self.addr_config["TDM_CONFIG_1"]
        mask = 0b11000000
        data = self.dac_comm.read(addr)
        data = data | mask
        self.dac_comm.write(addr, data)

    def set_i2s_master_mode(self):
        addr = self.addr_config["TDM_CONFIG_1"]
        mask = 0b10000000
        data = self.dac_comm.read(addr)
        data = data | mask
        self.dac_comm.write(addr, data)

        input_sel_addr = self.addr_config["INPUT_SELECTION"]
        in_mask = 0b00010000
        data2 = self.dac_comm.read(input_sel_addr)
        data2 = data2 | in_mask
        self.dac_comm.write(input_sel_addr, data2)

    def set_spdif_mode(self):
        # set input to spdif and auto input data format to auto
        input_sel_addr = self.addr_config["INPUT_SELECTION"]
        in_mask = 0b00000111
        data2 = self.dac_comm.read(input_sel_addr)
        data2 = data2 | in_mask
        self.dac_comm.write(input_sel_addr, data2)

        # enable spdif decode
        addr = self.addr_config["SYS_MODE_CONFIG"]
        smask = 0b00001000
        data = self.dac_comm.read(addr)
        data = data | smask
        self.dac_comm.write(addr, data)

        # set SDB for the spdf gpio pin
        gpio_pin = self.config["GPIO"]["SPDIF_GPIO_PIN"]
        sdb_addr = self.addr_config["DAC_GPIO_INPUT_ADDR"]
        sdb_mask = 0b00000001
        if gpio_pin > 1:
            sdb_mask = sdb_mask << gpio_pin
        data4 = self.dac_comm.read(sdb_addr)
        data4 = data4 | sdb_mask
        self.dac_comm.write(sdb_addr, data4)

        # set gpio pin for spdif
        spdf_addr = self.addr_config["DAC_SPDIF_SEL_ADDR"]
        pin_value = gpio_pin + 2
        pin_bin = format(pin_value, "04b")
        gen_mask = 0b11110000
        n = pin_bin + "0000"
        pin_mask = int(n)
        data3 = self.dac_comm.read(spdf_addr)
        data3 = data3 & ~gen_mask  # reset to zero first
        data3 = data3 | pin_mask
        self.dac_comm.write(spdf_addr, data3)

    def initialize_dac(self):
        # enable dac analog section
        self.enable_dac_analog_section()
        # setup dac for i2s master mode
        self.set_i2s_master_mode()

    def set_dac_mode(
        self,
        mode,
    ):  # 0 I2S Slave mode, 1 LJ Slave mode, 2 I2S Master mode, 3 SPDIF mode, 4 TDM I2S Slave mode Async, 5 TDM I2S Slave mode Sync
        if mode == 0:
            self.set_i2s_slave_mode()
            self.storage.write("CURRENT_DAC_MODE", mode)
            return
        elif mode == 1:
            self.set_lj_slave_mode()
            self.storage.write("CURRENT_DAC_MODE", mode)
            return
        elif mode == 2:
            self.set_i2s_master_mode()
            self.storage.write("CURRENT_DAC_MODE", mode)
            return
        elif mode == 3:
            self.set_spdif_mode()
            self.storage.write("CURRENT_DAC_MODE", mode)
            return
        else:
            self.set_spdif_mode()
            self.storage.write("CURRENT_DAC_MODE", mode)
            return

    def get_current_dac_mode(self):
        return self.storage.read("CURRENT_DAC_MODE")

    def is_second_order_compensation_enabled(self):
        return self.storage.read("SECOND_ORDER_COMPENSATION_ENABLED") == 1

    def is_third_order_compensation_enabled(self):
        return self.storage.read("THIRD_ORDER_COMPENSATION_ENABLED") == 1

    def is_oversampling_enabled(self):
        return self.storage.read("OVERSAMPLING_ENABLED") == 1

    def enable_disable_second_order_compensation(self, selected):
        active = self.is_second_order_compensation_enabled()
        if (selected == 1 and active) or (selected == 0 and not active):
            return
        reg_1_addr = self.addr_config["THD_2ND_ORDER_1"]
        reg_2_addr = self.addr_config["THD_2ND_ORDER_2"]
        reg_3_addr = self.addr_config["THD_2ND_ORDER_3"]
        reg_4_addr = self.addr_config["THD_2ND_ORDER_4"]

        if selected == 0:  # disable
            data = 0b00000000
            # store reg values for enabling the setting if not stored yet
            if not self.storage.read("SECOND_ORDER_COEFFICIENTS_STORED"):
                data1 = self.dac_comm.read(reg_1_addr)
                data2 = self.dac_comm.read(reg_2_addr)
                data3 = self.dac_comm.read(reg_3_addr)
                data4 = self.dac_comm.read(reg_4_addr)
                self.storage.write("SECOND_ORDER_ENABLE_COEFFICIENTS_1", str(data1))
                self.storage.write("SECOND_ORDER_ENABLE_COEFFICIENTS_2", str(data2))
                self.storage.write("SECOND_ORDER_ENABLE_COEFFICIENTS_3", str(data3))
                self.storage.write("SECOND_ORDER_ENABLE_COEFFICIENTS_4", str(data4))
                self.storage.write("SECOND_ORDER_COEFFICIENTS_STORED", 1)
            # fill all registers with zeros to disable
            self.dac_comm.write(reg_1_addr, data)
            self.dac_comm.write(reg_2_addr, data)
            self.dac_comm.write(reg_3_addr, data)
            self.dac_comm.write(reg_4_addr, data)

            self.storage.write("SECOND_ORDER_COMPENSATION_ENABLED", 0)
        else:  # enable
            # use coefficients stored in memory to enable
            data1 = self.storage.read("SECOND_ORDER_ENABLE_COEFFICIENTS_1")
            data2 = self.storage.read("SECOND_ORDER_ENABLE_COEFFICIENTS_2")
            data3 = self.storage.read("SECOND_ORDER_ENABLE_COEFFICIENTS_3")
            data4 = self.storage.read("SECOND_ORDER_ENABLE_COEFFICIENTS_4")

            self.dac_comm.write(reg_1_addr, data1)
            self.dac_comm.write(reg_2_addr, data2)
            self.dac_comm.write(reg_3_addr, data3)
            self.dac_comm.write(reg_4_addr, data4)
            self.storage.write("SECOND_ORDER_COMPENSATION_ENABLED", 1)

    def enable_disable_third_order_compensation(self, selected):
        active = self.is_third_order_compensation_enabled()
        if (selected == 1 and active) or (selected == 0 and not active):
            return
        reg_1_addr = self.addr_config["THD_3RD_ORDER_1"]
        reg_2_addr = self.addr_config["THD_3RD_ORDER_2"]
        reg_3_addr = self.addr_config["THD_3RD_ORDER_3"]
        reg_4_addr = self.addr_config["THD_3RD_ORDER_4"]
        if selected == 0:  # disable
            data = 0b00000000
            # store reg values for enabling the setting if not stored yet
            if not self.storage.read("THIRD_ORDER_COEFFICIENTS_STORED"):
                data1 = self.dac_comm.read(reg_1_addr)
                data2 = self.dac_comm.read(reg_2_addr)
                data3 = self.dac_comm.read(reg_3_addr)
                data4 = self.dac_comm.read(reg_4_addr)
                self.storage.write("THIRD_ORDER_ENABLE_COEFFICIENTS_1", str(data1))
                self.storage.write("THIRD_ORDER_ENABLE_COEFFICIENTS_2", str(data2))
                self.storage.write("THIRD_ORDER_ENABLE_COEFFICIENTS_3", str(data3))
                self.storage.write("THIRD_ORDER_ENABLE_COEFFICIENTS_4", str(data4))
                self.storage.write("THIRD_ORDER_COEFFICIENTS_STORED", 1)
            # fill all registers with zeros to disable
            self.dac_comm.write(reg_1_addr, data)
            self.dac_comm.write(reg_2_addr, data)
            self.dac_comm.write(reg_3_addr, data)
            self.dac_comm.write(reg_4_addr, data)

            self.storage.write("THIRD_ORDER_COMPENSATION_ENABLED", 0)
        else:  # enable
            # use coefficients stored in memory to enable
            data1 = self.storage.read("THIRD_ORDER_ENABLE_COEFFICIENTS_1")
            data2 = self.storage.read("THIRD_ORDER_ENABLE_COEFFICIENTS_2")
            data3 = self.storage.read("THIRD_ORDER_ENABLE_COEFFICIENTS_3")
            data4 = self.storage.read("THIRD_ORDER_ENABLE_COEFFICIENTS_4")

            self.dac_comm.write(reg_1_addr, data1)
            self.dac_comm.write(reg_2_addr, data2)
            self.dac_comm.write(reg_3_addr, data3)
            self.dac_comm.write(reg_4_addr, data4)

            self.storage.write("THIRD_ORDER_COMPENSATION_ENABLED", 1)

    def enable_disable_oversampling(self, selected):
        active = self.is_oversampling_enabled()
        if (selected == 1 and active) or (selected == 0 and not active):
            return
        if selected == 0:  # disable
            # code for registry access and disabling oversampling here

            self.storage.write("OVERSAMPLING_ENABLED", 0)
        else:
            # code for registry access and enabling oversampling here
            self.storage.write("OVERSAMPLING_ENABLED", 1)

    def get_dpll_bandwidth(self):  # Dac digital phase locked loop setting
        return self.storage.read("DPLL_BANDWIDTH")

    def set_dpll_bandwidth(
        self, value
    ):  # The lower the value the better the jitter reduction at stability cost.
        if value < 1 or value > 15:  # out of range(1-15) 4d
            return
        # code for accessing register and setting the dpll bandwidth value here

        self.storage.write("DPLL_BANDWIDTH", value)
