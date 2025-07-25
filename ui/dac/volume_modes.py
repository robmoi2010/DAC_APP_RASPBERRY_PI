import tkinter as tk
from tkinter import messagebox

from registry.register import get_instance
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from ui.styles import SELECTED_COLOR, UNSELECTED_COLOR
from system.volume_encoder import VolumeEncoder


volume_encoder: VolumeEncoder = get_instance("volumeencoder")


class VolumeMode(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

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
        self.row_index = 1
        tk.Label(
            self, text="Select volume knob press functionality", font=("Arial", 16)
        ).grid(row=self.get_current_row(), column=0, sticky="nsew")
        selected = volume_encoder.getButtonKnobMode()
        self.muteBtn = GeneralButton(
            self,
            "Mute",
            selected=selected == 0,
            command=lambda: self.volumeModeOnclick("Mute", 0),
        )
        self.muteBtn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.dVolBtn = GeneralButton(
            self,
            "Disable/Enable volume",
            selected=selected == 1,
            command=lambda: self.volumeModeOnclick("Disable/Enable volume", 1),
        )
        self.dVolBtn.grid(row=self.get_current_row(), column=0, sticky="nsew")

        self.mode0Btn = BackButton(
            self,
            command=lambda: controller.show_frame("DacSettings"),
        )
        self.mode0Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
