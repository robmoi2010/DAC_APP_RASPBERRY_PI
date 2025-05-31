import tkinter as tk
import dac.dac_volume as dac_volume
from tkinter import messagebox
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


ENABLE_VOL_TEXT = "Enable Volume"
DISABLE_VOL_TEXT = "Disable Volume"


class DacSettings(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Dac Settings", font=("Arial", 16)).pack(pady=20)
        self.volBtn = GeneralButton(
            self, "Volume Settings", command=lambda: controller.show_frame("DacVolumeSettings")
        )
        self.volBtn.pack()
        self.mode1Btn = GeneralButton(
            self,
            "Filters",
            command=lambda: controller.show_frame("Filters"),
        )
        self.mode1Btn.pack()
        self.mode2Btn = GeneralButton(
            self, "DAC Modes", command=lambda: controller.show_frame("DacModes")
        )
        self.mode2Btn.pack()
        self.mode3Btn = GeneralButton(
            self, "Volume Mode", command=lambda: controller.show_frame("VolumeMode")
        )
        self.mode3Btn.pack()
        self.mode5Btn = GeneralButton(
            self,
            "THD Compensation",
            command=lambda: controller.show_frame("ThdCompensation"),
        )
        self.mode5Btn.pack()
        self.mode4Btn = BackButton(
            self,
            command=lambda: controller.show_frame("MainSettings"),
        )
        self.mode4Btn.pack()
