import tkinter as tk
import dac.dac_filters as dac_filters
from tkinter import messagebox
from util.styles import SELECTED_COLOR, UNSELECTED_COLOR
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


# 0 Minimum phase
# 1 Linear phase apodizing first roll-off
# 2 Linear phase fast roll-off
# 3 Linear phase slow roll-off low ripple
# 4 Linear phase slow roll-off
# 5 Minimum phase fast roll-off
# 6 Minimum phase slow roll-off
# 7 Minimum phase slow roll-off low dispersion
class Filters(tk.Frame):
    def filtersOnclick(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            dac_filters.updateFilter(type)
            if type == 0:
                frame.f0Btn.config(fg=SELECTED_COLOR)
                frame.f1Btn.config(fg=UNSELECTED_COLOR)
                frame.f2Btn.config(fg=UNSELECTED_COLOR)
                frame.f3Btn.config(fg=UNSELECTED_COLOR)
                frame.f4Btn.config(fg=UNSELECTED_COLOR)
                frame.f5Btn.config(fg=UNSELECTED_COLOR)
                frame.f6Btn.config(fg=UNSELECTED_COLOR)
                frame.f7Btn.config(fg=UNSELECTED_COLOR)
            if type == 1:
                frame.f0Btn.config(fg=UNSELECTED_COLOR)
                frame.f1Btn.config(fg=SELECTED_COLOR)
                frame.f2Btn.config(fg=UNSELECTED_COLOR)
                frame.f3Btn.config(fg=UNSELECTED_COLOR)
                frame.f4Btn.config(fg=UNSELECTED_COLOR)
                frame.f5Btn.config(fg=UNSELECTED_COLOR)
                frame.f6Btn.config(fg=UNSELECTED_COLOR)
                frame.f7Btn.config(fg=UNSELECTED_COLOR)
            if type == 2:
                frame.f0Btn.config(fg=UNSELECTED_COLOR)
                frame.f1Btn.config(fg=UNSELECTED_COLOR)
                frame.f2Btn.config(fg=SELECTED_COLOR)
                frame.f3Btn.config(fg=UNSELECTED_COLOR)
                frame.f4Btn.config(fg=UNSELECTED_COLOR)
                frame.f5Btn.config(fg=UNSELECTED_COLOR)
                frame.f6Btn.config(fg=UNSELECTED_COLOR)
                frame.f7Btn.config(fg=UNSELECTED_COLOR)
            if type == 3:
                frame.f0Btn.config(fg=UNSELECTED_COLOR)
                frame.f1Btn.config(fg=UNSELECTED_COLOR)
                frame.f2Btn.config(fg=UNSELECTED_COLOR)
                frame.f3Btn.config(fg=SELECTED_COLOR)
                frame.f4Btn.config(fg=UNSELECTED_COLOR)
                frame.f5Btn.config(fg=UNSELECTED_COLOR)
                frame.f6Btn.config(fg=UNSELECTED_COLOR)
                frame.f7Btn.config(fg=UNSELECTED_COLOR)
            if type == 4:
                frame.f0Btn.config(fg=UNSELECTED_COLOR)
                frame.f1Btn.config(fg=UNSELECTED_COLOR)
                frame.f2Btn.config(fg=UNSELECTED_COLOR)
                frame.f3Btn.config(fg=UNSELECTED_COLOR)
                frame.f4Btn.config(fg=SELECTED_COLOR)
                frame.f5Btn.config(fg=UNSELECTED_COLOR)
                frame.f6Btn.config(fg=UNSELECTED_COLOR)
                frame.f7Btn.config(fg=UNSELECTED_COLOR)
            if type == 5:
                frame.f0Btn.config(fg=UNSELECTED_COLOR)
                frame.f1Btn.config(fg=UNSELECTED_COLOR)
                frame.f2Btn.config(fg=UNSELECTED_COLOR)
                frame.f3Btn.config(fg=UNSELECTED_COLOR)
                frame.f4Btn.config(fg=UNSELECTED_COLOR)
                frame.f5Btn.config(fg=SELECTED_COLOR)
                frame.f6Btn.config(fg=UNSELECTED_COLOR)
                frame.f7Btn.config(fg=UNSELECTED_COLOR)
            if type == 6:
                frame.f0Btn.config(fg=UNSELECTED_COLOR)
                frame.f1Btn.config(fg=UNSELECTED_COLOR)
                frame.f2Btn.config(fg=UNSELECTED_COLOR)
                frame.f3Btn.config(fg=UNSELECTED_COLOR)
                frame.f4Btn.config(fg=UNSELECTED_COLOR)
                frame.f5Btn.config(fg=UNSELECTED_COLOR)
                frame.f6Btn.config(fg=SELECTED_COLOR)
                frame.f7Btn.config(fg=UNSELECTED_COLOR)
            if type == 7:
                frame.f0Btn.config(fg=UNSELECTED_COLOR)
                frame.f1Btn.config(fg=UNSELECTED_COLOR)
                frame.f2Btn.config(fg=UNSELECTED_COLOR)
                frame.f3Btn.config(fg=UNSELECTED_COLOR)
                frame.f4Btn.config(fg=UNSELECTED_COLOR)
                frame.f5Btn.config(fg=UNSELECTED_COLOR)
                frame.f6Btn.config(fg=UNSELECTED_COLOR)
                frame.f7Btn.config(fg=SELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        curr = dac_filters.getCurrentFilter()
        tk.Label(self, text="Select DAC Filter", font=("Arial", 16)).pack(pady=20)

        self.f0Btn = GeneralButton(
            self,
            "Minimum phase",
            selected=curr == 0,
            command=lambda: self.filtersOnclick("Minimum phase", 0),
        )
        self.f0Btn.pack()
        self.f1Btn = GeneralButton(
            self,
            "Linear phase apodizing first roll-off",
            selected=curr == 1,
            command=lambda: self.filtersOnclick(
                "Linear phase apodizing first roll-off", 1
            ),
        )
        self.f1Btn.pack()
        self.f2Btn = GeneralButton(
            self,
            "Linear phase fast roll-off",
            selected=curr == 2,
            command=lambda: self.filtersOnclick("Linear phase fast roll-off", 2),
        )
        self.f2Btn.pack()
        self.f3Btn = GeneralButton(
            self,
            "Linear phase slow roll-off low ripple",
            selected=curr == 3,
            command=lambda: self.filtersOnclick(
                "Linear phase slow roll-off low ripple", 3
            ),
        )

        self.f3Btn.pack()
        self.f4Btn = GeneralButton(
            self,
            "Linear phase slow roll-off",
            selected=curr == 4,
            command=lambda: self.filtersOnclick(
                "Linear phase slow roll-off low ripple", 4
            ),
        )
        self.f4Btn.pack()
        self.f5Btn = GeneralButton(
            self,
            "Minimum phase fast roll-off",
            selected=curr == 5,
            command=lambda: self.filtersOnclick(
                "Linear phase slow roll-off low ripple", 5
            ),
        )
        self.f5Btn.pack()
        self.f6Btn = GeneralButton(
            self,
            "Minimum phase slow roll-off",
            selected=curr == 6,
            command=lambda: self.filtersOnclick("Minimum phase slow roll-off", 6),
        )

        self.f6Btn.pack()
        self.f7Btn = GeneralButton(
            self,
            "Minimum phase slow roll-off low dispersion",
            selected=curr == 7,
            command=lambda: self.filtersOnclick(
                "Minimum phase slow roll-off low dispersion", 7
            ),
        )
        self.f7Btn.pack()
        self.f8Btn = BackButton(
            self, command=lambda: controller.show_frame("DacSettings")
        )
        self.f8Btn.pack()
