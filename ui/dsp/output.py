import tkinter as tk

from util.styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    UNSELECTED_COLOR,
    BUTTON_FONT_SIZE,
    BUTTON_FONT,
    BUTTON_FONT_STYLE,
    BUTTON_ONFOCUS_BG,
)

btnFont = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)


class Output(tk.Frame):
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Outputs", font=("Arial", 16)).pack(pady=20)
        self.btn2 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Mains Output",
            command=lambda: controller.show_frame("MainOutput"),
        )
        self.btn2.bind("<FocusIn>", self.on_focus_in)
        self.btn2.bind("<FocusOut>", self.on_focus_out)
        self.btn2.pack()
        self.btn2 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Subwoofer Output",
            command=lambda: controller.show_frame("SubwooferOutput"),
        )
        self.btn2.bind("<FocusIn>", self.on_focus_in)
        self.btn2.bind("<FocusOut>", self.on_focus_out)
        self.btn2.pack()
        self.btn4 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("DspSettings"),
        )
        self.btn4.bind("<FocusIn>", self.on_focus_in)
        self.btn4.bind("<FocusOut>", self.on_focus_out)
        self.btn4.pack()
