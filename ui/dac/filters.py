import tkinter as tk
from tkinter import messagebox
from dac.dac_filters import DacFilters
from util.styles import SELECTED_COLOR, UNSELECTED_COLOR
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from registry.register import get_instance

dac_filters: DacFilters = get_instance("dacfilters")


# 0 Minimum phase
# 1 Linear phase apodizing first roll-off
# 2 Linear phase fast roll-off
# 3 Linear phase slow roll-off low ripple
# 4 Linear phase slow roll-off
# 5 Minimum phase fast roll-off
# 6 Minimum phase slow roll-off
# 7 Minimum phase slow roll-off low dispersion
class Filters(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def filtersOnclick(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            dac_filters.update_filter(type)
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
        self.row_index = 1
        curr = dac_filters.get_current_filter()
        tk.Label(self, text="Select DAC Filter", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )

        self.f0Btn = GeneralButton(
            self,
            "Minimum phase",
            selected=curr == 0,
            command=lambda: self.filtersOnclick("Minimum phase", 0),
        )
        self.f0Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.f1Btn = GeneralButton(
            self,
            "Linear phase apodizing first roll-off",
            selected=curr == 1,
            command=lambda: self.filtersOnclick(
                "Linear phase apodizing first roll-off", 1
            ),
        )
        self.f1Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.f2Btn = GeneralButton(
            self,
            "Linear phase fast roll-off",
            selected=curr == 2,
            command=lambda: self.filtersOnclick("Linear phase fast roll-off", 2),
        )
        self.f2Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.f3Btn = GeneralButton(
            self,
            "Linear phase slow roll-off low ripple",
            selected=curr == 3,
            command=lambda: self.filtersOnclick(
                "Linear phase slow roll-off low ripple", 3
            ),
        )

        self.f3Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.f4Btn = GeneralButton(
            self,
            "Linear phase slow roll-off",
            selected=curr == 4,
            command=lambda: self.filtersOnclick(
                "Linear phase slow roll-off low ripple", 4
            ),
        )
        self.f4Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.f5Btn = GeneralButton(
            self,
            "Minimum phase fast roll-off",
            selected=curr == 5,
            command=lambda: self.filtersOnclick(
                "Linear phase slow roll-off low ripple", 5
            ),
        )
        self.f5Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.f6Btn = GeneralButton(
            self,
            "Minimum phase slow roll-off",
            selected=curr == 6,
            command=lambda: self.filtersOnclick("Minimum phase slow roll-off", 6),
        )

        self.f6Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.f7Btn = GeneralButton(
            self,
            "Minimum phase slow roll-off low dispersion",
            selected=curr == 7,
            command=lambda: self.filtersOnclick(
                "Minimum phase slow roll-off low dispersion", 7
            ),
        )
        self.f7Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.f8Btn = BackButton(
            self, command=lambda: controller.show_frame("DacSettings")
        )
        self.f8Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
