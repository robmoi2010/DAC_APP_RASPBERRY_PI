import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from tkinter import messagebox
from ui.styles import SELECTED_COLOR, UNSELECTED_COLOR
from registry.register import register, get_instance

volume = get_instance("volume")
class DacVolumeSettings(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def enable_disable(self, selected):
        txt = None
        if selected == 0:
            txt = "Enable"
        else:
            txt = "Disable"
        answer = messagebox.askyesno("Confirmation", "are you sure you want to " + txt)
        if answer:
            volume.disable_enable_volume(selected)
            if selected == 0:
                self.btn1.config(fg=SELECTED_COLOR)
                self.btn2.config(fg=UNSELECTED_COLOR)
            else:
                self.btn1.config(fg=UNSELECTED_COLOR)
                self.btn2.config(fg=SELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="Dac Volume", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )
        active = not volume.is_volume_disabled()

        self.btn1 = GeneralButton(
            self, "Enable", selected=active, command=lambda: self.enable_disable(0)
        )
        self.btn1.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn2 = GeneralButton(
            self,
            "Disable",
            selected=not active,
            command=lambda: self.enable_disable(1),
        )
        self.btn2.grid(row=self.get_current_row(), column=0, sticky="nsew")

        self.btn3 = BackButton(
            self,
            command=lambda: controller.show_frame("DacSettings"),
        )
        self.btn3.grid(row=self.get_current_row(), column=0, sticky="nsew")
