import tkinter as tk
from tkinter import messagebox
import general.sound_modes
from util.styles import UNSELECTED_COLOR, SELECTED_COLOR
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class SoundModes(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def mode_on_click(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            general.sound_modes.update_sound_mode(type)
            if type == 0:
                frame.btn1.config(fg=SELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
            if type == 1:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=SELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
            if type == 2:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=SELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="Select Sound Mode", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )
        current_sound_mode = general.sound_modes.get_current_sound_mode()
        self.btn1 = GeneralButton(
            self,
            "Pure Direct",
            selected=current_sound_mode == 0,
            command=lambda: self.mode_on_click("Pure Direct", 0),
        )
        self.btn1.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn2 = GeneralButton(
            self,
            "Semi-Pure Direct(mains direct, sub DSP)",
            selected=current_sound_mode == 1,
            command=lambda: self.mode_on_click("Semi-Pure Direct", 1),
        )
        self.btn2.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn3 = GeneralButton(
            self,
            "DSP",
            selected=current_sound_mode == 2,
            command=lambda: self.mode_on_click("DSP", 2),
        )

        self.btn3.grid(row=self.get_current_row(), column=0, sticky="nsew")

        self.btn6 = BackButton(
            self,
            command=lambda: controller.show_frame("GeneralSettings"),
        )
        self.btn6.grid(row=self.get_current_row(), column=0, sticky="nsew")
