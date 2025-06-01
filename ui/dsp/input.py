import tkinter as tk
from tkinter import messagebox
import dsp.io as input
from util.styles import UNSELECTED_COLOR, SELECTED_COLOR
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class Input(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def inputOnclick(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            input.update_current_input(type)
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

    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="Select Input", font=("Arial", 16)).grid(row=self.get_current_row(), column=0, sticky="nsew")
        current_input = input.get_current_input()
        self.btn1 = GeneralButton(
            self,
            "TOSLINK",
            selected=current_input == 0,
            command=lambda: self.inputOnclick("TOSLINK", 0),
        )
        self.btn1.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn2 = GeneralButton(
            self,
            "I2S_0",
            selected=current_input == 1,
            command=lambda: self.inputOnclick("I2S_0", 1),
        )
        self.btn2.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn3 = GeneralButton(
            self,
            "I2S_1",
            selected=current_input == 2,
            command=lambda: self.inputOnclick("I2S_1", 2),
        )
        self.btn3.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn4 = GeneralButton(
            self,
            "I2S_2",
            selected=current_input == 3,
            command=lambda: self.inputOnclick("I2S_2", 3),
        )
        self.btn4.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn5 = GeneralButton(
            self,
            "I2S_3",
            selected=current_input == 4,
            command=lambda: self.inputOnclick("I2S_3", 4),
        )
        self.btn5.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn6 = BackButton(
            self, command=lambda: controller.show_frame("DspSettings")
        )
        self.btn6.grid(row=self.get_current_row(), column=0, sticky="nsew")
