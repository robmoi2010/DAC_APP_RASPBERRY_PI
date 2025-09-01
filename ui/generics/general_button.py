import tkinter as tk
from ui.styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    UNSELECTED_COLOR,
    BUTTON_FONT,
    BUTTON_FONT_SIZE,
    BUTTON_FONT_STYLE,
    BUTTON_ONFOCUS_BG,
    SELECTED_COLOR
)

font = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)


class GeneralButton(tk.Button):
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def __init__(self, parent, text, selected=None, command=None):
        super().__init__(
            parent,
            relief=RELIEF,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text=text,
            font=font,
            command=command
        )
        if selected:
            self.config(fg=SELECTED_COLOR)
        else:
            self.config(fg=UNSELECTED_COLOR)
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
