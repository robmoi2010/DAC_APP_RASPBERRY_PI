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


class DspSettings(tk.Frame):
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Dsp Settings", font=("Arial", 16)).pack(pady=20)

        self.volBtn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Select Input",
            command=lambda: controller.show_frame("Input"),
        )
        self.volBtn.bind("<FocusIn>", self.on_focus_in)
        self.volBtn.bind("<FocusOut>", self.on_focus_out)
        self.volBtn.pack()
        self.mode1Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Select Mains Output",
            command=lambda: controller.show_frame("MainOutput"),
        )
        self.mode1Btn.bind("<FocusIn>", self.on_focus_in)
        self.mode1Btn.bind("<FocusOut>", self.on_focus_out)
        self.mode1Btn.pack()
        self.mode2Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Select Subwoofer Output",
            command=lambda: controller.show_frame("SubwooferOutput"),
        )
        self.mode2Btn.bind("<FocusIn>", self.on_focus_in)
        self.mode2Btn.bind("<FocusOut>", self.on_focus_out)
        self.mode2Btn.pack()
        self.mode4Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("MainSettings"),
        )
        self.mode4Btn.bind("<FocusIn>", self.on_focus_in)
        self.mode4Btn.bind("<FocusOut>", self.on_focus_out)
        self.mode4Btn.pack()
