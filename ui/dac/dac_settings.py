import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from registry.register import register, get_instance
from volume.volume_util import VOLUME_DEVICE
from volume.system_volume import Volume

ENABLE_VOL_TEXT = "Enable Volume"
DISABLE_VOL_TEXT = "Disable Volume"

volume: Volume = get_instance("volume")


class DacSettings(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="Dac Settings", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )
        current_vol_device = volume.get_current_volume_device()
        if current_vol_device == VOLUME_DEVICE.DAC.name:
            self.volBtn = GeneralButton(
                self,
                "Volume Settings",
                command=lambda: controller.show_frame("DacVolumeSettings"),
            )
            self.volBtn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.mode1Btn = GeneralButton(
            self,
            "Filters",
            command=lambda: controller.show_frame("Filters"),
        )
        self.mode1Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.mode2Btn = GeneralButton(
            self, "DAC Modes", command=lambda: controller.show_frame("DacModes")
        )
        self.mode2Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        if current_vol_device == VOLUME_DEVICE.DAC.name:
            self.mode3Btn = GeneralButton(
                self, "Volume Mode", command=lambda: controller.show_frame("VolumeMode")
            )
            self.mode3Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.mode5Btn = GeneralButton(
            self,
            "THD Compensation",
            command=lambda: controller.show_frame("ThdCompensation"),
        )
        self.mode5Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.mode4Btn = BackButton(
            self,
            command=lambda: controller.show_frame("MainSettings"),
        )
        self.mode4Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
