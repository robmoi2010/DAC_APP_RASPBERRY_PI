import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from registry.register import get_instance
from volume.system_volume import VOLUME_DEVICE
from tkinter import messagebox
from util.styles import SELECTED_COLOR, UNSELECTED_COLOR

volume=get_instance("volume")

class VolumeDevice(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def selection(self, selection):
        text = None
        if selection == VOLUME_DEVICE.DAC.name:
            text = VOLUME_DEVICE.DAC.name
        else:
            text = VOLUME_DEVICE.MUSES.name
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + text
        )
        if answer:
            volume.set_current_volume_device(selection)
            if selection == VOLUME_DEVICE.DAC.name:
                self.btn1.config(fg=SELECTED_COLOR)
                self.btn2.config(fg=UNSELECTED_COLOR)
            else:
                self.btn1.config(fg=UNSELECTED_COLOR)
                self.btn2.config(fg=SELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="Volume Device", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )
        current = volume.get_current_volume_device()
        self.btn1 = GeneralButton(
            self,
            "DAC",
            selected=current == VOLUME_DEVICE.DAC.name,
            command=lambda: self.selection(VOLUME_DEVICE.DAC.name),
        )
        self.btn1.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn2 = GeneralButton(
            self,
            "MUSES",
            selected=current == VOLUME_DEVICE.MUSES.name,
            command=lambda: self.selection(VOLUME_DEVICE.MUSES.name),
        )
        self.btn2.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn3 = BackButton(
            self,
            command=lambda: controller.show_frame("GeneralSettings"),
        ).grid(row=self.get_current_row(), column=0, sticky="nsew")
