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


class GeneralSettings(tk.Frame):
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.counter = 0
        tk.Label(self, text="General settings", font=("Arial", 16)).pack(pady=20)
        btn5 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Sound Modes",
            command=lambda: controller.show_frame("SoundModes"),
        )
        btn5.bind("<FocusIn>", self.on_focus_in)
        btn5.bind("<FocusOut>", self.on_focus_out)
        btn5.pack()

        btn4 = tk.Button(
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
        btn4.bind("<FocusIn>", self.on_focus_in)
        btn4.bind("<FocusOut>", self.on_focus_out)
        btn4.pack()
        # self.bind_all("<KeyPress>", self.on_key_press)
