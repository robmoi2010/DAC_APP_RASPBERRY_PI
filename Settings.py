import tkinter as tk
import dac_volume
from tkinter import messagebox
from styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    UNSELECTED_COLOR,
    BUTTON_FONT_SIZE,
    BUTTON_FONT,
    BUTTON_FONT_STYLE,
)

btnFont = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)

ENABLE_VOL_TEXT = "Enable Volume"
DISABLE_VOL_TEXT = "Disable Volume"


class Settings(tk.Frame):
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
        tk.Label(self, text="Settings", font=("Arial", 16)).pack(pady=20)
        disabled = dac_volume.isVolumeDisabled()
        if disabled == 1:
            text = ENABLE_VOL_TEXT
        else:
            text = DISABLE_VOL_TEXT
        self.volBtn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text=text,
            command=lambda: self.volumeDisableEnableOnclick(),
        )
        self.volBtn.pack()
        tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Filters",
            command=lambda: controller.show_frame("Filters"),
        ).pack()
        tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="DAC Modes",
            command=lambda: controller.show_frame("DacModes"),
        ).pack()
        tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Volume Mode",
            command=lambda: controller.show_frame("VolumeMode"),
        ).pack()
        tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("Home"),
        ).pack()
