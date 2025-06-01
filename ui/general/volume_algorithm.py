import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from volume.system_volume import VOLUME_ALGORITHM
import volume.system_volume as volume
from tkinter import messagebox
from util.styles import SELECTED_COLOR, UNSELECTED_COLOR


class VolumeAlgorithm(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def selection(self, selected: VOLUME_ALGORITHM):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selected.name
        )
        if answer:
            volume.set_volume_algorithm(selected)
            if selected == VOLUME_ALGORITHM.LINEAR:
                self.btn.config(fg=SELECTED_COLOR)
                self.btn3.config(fg=UNSELECTED_COLOR)
            else:
                self.btn.config(fg=UNSELECTED_COLOR)
                self.btn3.config(fg=SELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="Volume Algorithm", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )
        current = volume.get_current_volume_algorithm()
        self.btn = GeneralButton(
            self,
            "Linear",
            selected=current == VOLUME_ALGORITHM.LINEAR,
            command=lambda: self.selection(VOLUME_ALGORITHM.LINEAR),
        )
        self.btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn3 = GeneralButton(
            self,
            "Logarithmic",
            selected=current == VOLUME_ALGORITHM.LOGARITHMIC,
            command=lambda: self.selection(VOLUME_ALGORITHM.LOGARITHMIC),
        )
        self.btn3.grid(row=self.get_current_row(), column=0, sticky="nsew")

        btn2 = BackButton(
            self, command=lambda: controller.show_frame("GeneralSettings")
        )
        btn2.grid(row=self.get_current_row(), column=0, sticky="nsew")
