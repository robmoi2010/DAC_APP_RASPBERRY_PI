import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class DspSettings(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Dsp Settings", font=("Arial", 16)).pack(pady=20)

        self.btn1 = GeneralButton(
            self, "Input", command=lambda: controller.show_frame("Input")
        )
        self.btn1.pack()
        self.btn2 = GeneralButton(
            self, "Output", command=lambda: controller.show_frame("Output")
        )
        self.btn2.pack()
        self.btn4 = BackButton(
            self, command=lambda: controller.show_frame("MainSettings")
        )
        self.btn4.pack()
