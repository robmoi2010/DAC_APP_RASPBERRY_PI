import tkinter as tk
from tkinter import messagebox

import general.volume_encoder as volume_encoder
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from util.styles import SELECTED_COLOR, UNSELECTED_COLOR


class VolumeMode(tk.Frame):
    def volumeModeOnclick(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            volume_encoder.setRotaryButtonMode(type)
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
        selected = volume_encoder.getButtonKnobMode()
        self.muteBtn = GeneralButton(
            self,
            "Mute",
            selected=selected == 0,
            command=lambda: self.volumeModeOnclick("Mute", 0),
        )
        self.muteBtn.pack()
        self.dVolBtn = GeneralButton(
            self,
            "Disable/Enable volume",
            selected=selected == 1,
            command=lambda: self.volumeModeOnclick("Disable/Enable volume", 1),
        )
        self.dVolBtn.pack()

        self.mode0Btn = BackButton(
            self,
            command=lambda: controller.show_frame("DacSettings"),
        )
        self.mode0Btn.pack()
