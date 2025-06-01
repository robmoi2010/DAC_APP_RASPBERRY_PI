import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class DspSettings(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="Dsp Settings", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )

        self.btn1 = GeneralButton(
            self, "Input", command=lambda: controller.show_frame("Input")
        )
        self.btn1.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn2 = GeneralButton(
            self, "Output", command=lambda: controller.show_frame("Output")
        )
        self.btn2.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.btn4 = BackButton(
            self, command=lambda: controller.show_frame("MainSettings")
        )
        self.btn4.grid(row=self.get_current_row(), column=0, sticky="nsew")
