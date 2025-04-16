import tkinter as tk
from tkinter import messagebox
import DAC_VOLUME
from Styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    SELECTED_COLOR,
    UNSELECTED_COLOR,
    BUTTON_FONT_SIZE,
    BUTTON_FONT,
    BUTTON_FONT_STYLE,
)

btnFont = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)


class VolumeMode(tk.Frame):
    def volumeModeOnclick(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            DAC_VOLUME.setRotaryButtonMode(type)
            if type == 0:
                frame.muteBtn.config(fg=SELECTED_COLOR)
                frame.dVolBtn.config(fg=UNSELECTED_COLOR)
            else:
                frame.dVolBtn.config(fg=SELECTED_COLOR)
                frame.muteBtn.config(fg=UNSELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(
            self, text="Select volume knob press functionality", font=("Arial", 16)
        ).pack(pady=20)
        selected = DAC_VOLUME.getButtonKnobMode()
        print(selected)
        self.muteBtn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Mute",
            command=lambda: self.volumeModeOnclick("Mute", 0),
        )
        self.muteBtn.pack()
        if selected == 0:
            self.muteBtn.config(fg=SELECTED_COLOR)

        self.dVolBtn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Disable/Enable volume",
            command=lambda: self.volumeModeOnclick("Disable/Enable volume", 1),
        )
        self.dVolBtn.pack()
        if selected == 1:
            self.dVolBtn.config(fg=SELECTED_COLOR)

        tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("Settings"),
        ).pack()
