import tkinter as tk
from tkinter import messagebox
import dsp.io as output
from ui.styles import UNSELECTED_COLOR, SELECTED_COLOR
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from registry.register import get_instance
from dsp.io import DspIO
output = get_instance("dspio")


class MainOutput(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def output_on_click(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            output.update_main_output(type)
            if type == 0:
                frame.btn1.config(fg=SELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
                frame.btn4.config(fg=UNSELECTED_COLOR)
                frame.btn5.config(fg=UNSELECTED_COLOR)
            if type == 1:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=SELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
                frame.btn4.config(fg=UNSELECTED_COLOR)
                frame.btn5.config(fg=UNSELECTED_COLOR)
            if type == 2:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=SELECTED_COLOR)
                frame.btn4.config(fg=UNSELECTED_COLOR)
                frame.btn5.config(fg=UNSELECTED_COLOR)
            if type == 3:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
                frame.btn4.config(fg=SELECTED_COLOR)
                frame.btn5.config(fg=UNSELECTED_COLOR)
            if type == 4:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
                frame.btn4.config(fg=UNSELECTED_COLOR)
                frame.btn5.config(fg=SELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="Select Main Speakers Output", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )
        current_main_output = output.get_current_main_output()
        self.btn1 = GeneralButton(
            self,
            "COAXIAL",
            selected=current_main_output == 0,
            command=lambda: self.output_on_click("COAXIAL", 0),
        )
        self.btn1.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn2 = GeneralButton(
            self,
            "I2S_0",
            selected=current_main_output == 1,
            command=lambda: self.output_on_click("I2S_0", 1),
        )
        self.btn2.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn3 = GeneralButton(
            self,
            "I2S_1",
            selected=current_main_output == 2,
            command=lambda: self.output_on_click("I2S_1", 2),
        )
        self.btn3.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn4 = GeneralButton(
            self,
            "I2S_2",
            selected=current_main_output == 3,
            command=lambda: self.output_on_click("I2S_2", 3),
        )

        self.btn4.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn5 = GeneralButton(
            self,
            "I2S_3",
            selected=current_main_output == 4,
            command=lambda: self.output_on_click("I2S_3", 4),
        )

        self.btn5.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn6 = BackButton(
            self,
            command=lambda: controller.show_frame("Output"),
        )
        self.btn6.grid(row=self.get_current_row(), column=0, sticky="nsew")
