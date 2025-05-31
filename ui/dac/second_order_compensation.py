import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
import dac.ess_dac as dac
from tkinter import messagebox
from util.styles import SELECTED_COLOR, UNSELECTED_COLOR


class SecondOrderCompensation(tk.Frame):
    def enable_disable(self, selected):
        txt = None
        if selected == 0:
            txt = "Enable"
        else:
            txt = "Disable"
        answer = messagebox.askyesno("Confirmation", "are you sure you want to " + txt)
        if answer:
            dac.enable_disable_second_order_compensation(selected)
            if selected == 0:
                self.btn1.config(fg=SELECTED_COLOR)
                self.btn2.config(fg=UNSELECTED_COLOR)
            else:
                self.btn1.config(fg=UNSELECTED_COLOR)
                self.btn2.config(fg=SELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="2nd Order Compensation", font=("Arial", 16)).pack(pady=20)
        active = dac.is_second_order_compensation_enabled()

        self.btn1 = GeneralButton(
            self, "Enable", selected=active, command=lambda: self.enable_disable(0)
        )
        self.btn1.pack()
        self.btn2 = GeneralButton(
            self,
            "Disable",
            selected=not active,
            command=lambda: self.enable_disable(1),
        )
        self.btn2.pack()

        self.btn3 = BackButton(
            self,
            command=lambda: controller.show_frame("ThdCompensation"),
        )
        self.btn3.pack()
