import tkinter as tk
import dac.dac_volume as dac_volume
from tkinter import messagebox
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


ENABLE_VOL_TEXT = "Enable Volume"
DISABLE_VOL_TEXT = "Disable Volume"


class DacSettings(tk.Frame):
    def volumeDisableEnableOnclick(frame):
        if dac_volume.isVolumeDisabled() == 1:
            selection = "Enable"
            text = ENABLE_VOL_TEXT
        else:
            selection = "disable"
            text = DISABLE_VOL_TEXT
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            dac_volume.disableEnableVolume()
            frame.volBtn.config(text=text)

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Dac Settings", font=("Arial", 16)).pack(pady=20)
        disabled = dac_volume.isVolumeDisabled()
        if disabled == 1:
            text = ENABLE_VOL_TEXT
        else:
            text = DISABLE_VOL_TEXT
        self.volBtn = GeneralButton(
            self, text, command=lambda: self.volumeDisableEnableOnclick()
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
            self,
            "Volume Mode",
            command=lambda: controller.show_frame("VolumeMode")
        )
        self.mode3Btn.pack()
        self.mode5Btn = GeneralButton(
            self,
            "THD Compensation",
            command=lambda: controller.show_frame(""),
        )
        self.mode5Btn.pack()
        self.mode4Btn = BackButton(
            self,
            command=lambda: controller.show_frame("MainSettings"),
        )
        self.mode4Btn.pack()
