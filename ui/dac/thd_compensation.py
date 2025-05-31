import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class ThdCompensation(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THD Compensation", font=("Arial", 16)).pack(pady=20)

        self.mode1Btn = GeneralButton(
            self,
            "2ND Order",
            command=lambda: controller.show_frame("SecondOrderCompensation"),
        )
        self.mode1Btn.pack()
        self.mode2Btn = GeneralButton(
            self,
            "3RD Order",
            command=lambda: controller.show_frame("ThirdOrderCompensation"),
        )
        self.mode2Btn.pack()
        self.mode4Btn = BackButton(
            self,
            command=lambda: controller.show_frame("DacSettings"),
        )
        self.mode4Btn.pack()
