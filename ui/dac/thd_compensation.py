import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class ThdCompensation(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="THD Compensation", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )

        self.mode1Btn = GeneralButton(
            self,
            "2ND Order",
            command=lambda: controller.show_frame("SecondOrderCompensation"),
        )
        self.mode1Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.mode2Btn = GeneralButton(
            self,
            "3RD Order",
            command=lambda: controller.show_frame("ThirdOrderCompensation"),
        )
        self.mode2Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.mode4Btn = BackButton(
            self,
            command=lambda: controller.show_frame("DacSettings"),
        )
        self.mode4Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
