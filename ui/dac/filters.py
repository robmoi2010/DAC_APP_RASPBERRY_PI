import tkinter as tk
import dac.dac_filters as dac_filters
from tkinter import messagebox
from util.styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    SELECTED_COLOR,
    UNSELECTED_COLOR,
    BUTTON_FONT_SIZE,
    BUTTON_FONT,
    BUTTON_FONT_STYLE,
    BUTTON_ONFOCUS_BG,
)

btnFont = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)


# 0 Minimum phase
# 1 Linear phase apodizing first roll-off
# 2 Linear phase fast roll-off
# 3 Linear phase slow roll-off low ripple
# 4 Linear phase slow roll-off
# 5 Minimum phase fast roll-off
# 6 Minimum phase slow roll-off
# 7 Minimum phase slow roll-off low dispersion
class Filters(tk.Frame):
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

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

        self.f0Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Minimum phase",
            command=lambda: self.filtersOnclick("Minimum phase", 0),
        )
        self.f0Btn.bind("<FocusIn>", self.on_focus_in)
        self.f0Btn.bind("<FocusOut>", self.on_focus_out)
        if curr == 0:
            self.f0Btn.config(fg=SELECTED_COLOR)
        self.f0Btn.pack()
        self.f1Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Linear phase apodizing first roll-off",
            command=lambda: self.filtersOnclick(
                "Linear phase apodizing first roll-off", 1
            ),
        )
        self.f1Btn.bind("<FocusIn>", self.on_focus_in)
        self.f1Btn.bind("<FocusOut>", self.on_focus_out)
        if curr == 1:
            self.f1Btn.config(fg=SELECTED_COLOR)
        self.f1Btn.pack()
        self.f2Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Linear phase fast roll-off",
            command=lambda: self.filtersOnclick("Linear phase fast roll-off", 2),
        )
        self.f2Btn.bind("<FocusIn>", self.on_focus_in)
        self.f2Btn.bind("<FocusOut>", self.on_focus_out)
        if curr == 2:
            self.f2Btn.config(fg=SELECTED_COLOR)
        self.f2Btn.pack()
        self.f3Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Linear phase slow roll-off low ripple",
            command=lambda: self.filtersOnclick(
                "Linear phase slow roll-off low ripple", 3
            ),
        )
        self.f3Btn.bind("<FocusIn>", self.on_focus_in)
        self.f3Btn.bind("<FocusOut>", self.on_focus_out)
        if curr == 3:
            self.f3Btn.config(fg=SELECTED_COLOR)
        self.f3Btn.pack()
        self.f4Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Linear phase slow roll-off",
            command=lambda: self.filtersOnclick(
                "Linear phase slow roll-off low ripple", 4
            ),
        )
        self.f4Btn.bind("<FocusIn>", self.on_focus_in)
        self.f4Btn.bind("<FocusOut>", self.on_focus_out)
        if curr == 4:
            self.f4Btn.config(fg=SELECTED_COLOR)
        self.f4Btn.pack()
        self.f5Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Minimum phase fast roll-off",
            command=lambda: self.filtersOnclick(
                "Linear phase slow roll-off low ripple", 5
            ),
        )
        self.f5Btn.bind("<FocusIn>", self.on_focus_in)
        self.f5Btn.bind("<FocusOut>", self.on_focus_out)
        if curr == 5:
            self.f5Btn.config(fg=SELECTED_COLOR)
        self.f5Btn.pack()
        self.f6Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Minimum phase slow roll-off",
            command=lambda: self.filtersOnclick("Minimum phase slow roll-off", 6),
        )
        self.f6Btn.bind("<FocusIn>", self.on_focus_in)
        self.f6Btn.bind("<FocusOut>", self.on_focus_out)
        if curr == 6:
            self.f6Btn.config(fg=SELECTED_COLOR)
        self.f6Btn.pack()
        self.f7Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Minimum phase slow roll-off low dispersion",
            command=lambda: self.filtersOnclick(
                "Minimum phase slow roll-off low dispersion", 7
            ),
        )
        self.f7Btn.bind("<FocusIn>", self.on_focus_in)
        self.f7Btn.bind("<FocusOut>", self.on_focus_out)
        if curr == 7:
            self.f7Btn.config(fg=SELECTED_COLOR)
        self.f7Btn.pack()
        self.f8Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("DacSettings"),
        )
        self.f8Btn.bind("<FocusIn>", self.on_focus_in)
        self.f8Btn.bind("<FocusOut>", self.on_focus_out)
        self.f8Btn.pack()
