import tkinter as tk
import dac.dac_volume as dac_volume
from tkinter import messagebox
from util.styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    UNSELECTED_COLOR,
    BUTTON_FONT_SIZE,
    BUTTON_FONT,
    BUTTON_FONT_STYLE,
    BUTTON_ONFOCUS_BG,
)

btnFont = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)

ENABLE_VOL_TEXT = "Enable Volume"
DISABLE_VOL_TEXT = "Disable Volume"


class DacSettings(tk.Frame):
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

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
        self.volBtn.bind("<FocusIn>", self.on_focus_in)
        self.volBtn.bind("<FocusOut>", self.on_focus_out)
        self.volBtn.pack()
        self.mode1Btn=tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Filters",
            command=lambda: controller.show_frame("Filters"),
        )
        self.mode1Btn.bind("<FocusIn>", self.on_focus_in)
        self.mode1Btn.bind("<FocusOut>", self.on_focus_out)
        self.mode1Btn.pack()
        self.mode2Btn=tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="DAC Modes",
            command=lambda: controller.show_frame("DacModes"),
        )
        self.mode2Btn.bind("<FocusIn>", self.on_focus_in)
        self.mode2Btn.bind("<FocusOut>", self.on_focus_out)
        self.mode2Btn.pack()
        self.mode3Btn=tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Volume Mode",
            command=lambda: controller.show_frame("VolumeMode"),
        )
        self.mode3Btn.bind("<FocusIn>", self.on_focus_in)
        self.mode3Btn.bind("<FocusOut>", self.on_focus_out)
        self.mode3Btn.pack()
        self.mode5Btn=tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="THD Compensation",
            command=lambda: controller.show_frame(""),
        )
        self.mode5Btn.bind("<FocusIn>", self.on_focus_in)
        self.mode5Btn.bind("<FocusOut>", self.on_focus_out)
        self.mode5Btn.pack()
        self.mode4Btn=tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("MainSettings"),
        )
        self.mode4Btn.bind("<FocusIn>", self.on_focus_in)
        self.mode4Btn.bind("<FocusOut>", self.on_focus_out)
        self.mode4Btn.pack()
