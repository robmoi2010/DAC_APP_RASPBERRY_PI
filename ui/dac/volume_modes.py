import tkinter as tk
from tkinter import messagebox

import general.volume_encoder as volume_encoder
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


class VolumeMode(tk.Frame):
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def volumeModeOnclick(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            volume_encoder.setRotaryButtonMode(type)
            if type == 0:
                frame.muteBtn.config(fg=SELECTED_COLOR)
                frame.dVolBtn.config(fg=UNSELECTED_COLOR)
            else:
                frame.dVolBtn.config(fg=SELECTED_COLOR)
                frame.muteBtn.config(fg=UNSELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(
            self, text="Select volume knob press functionality", font=("Arial", 16)
        ).pack(pady=20)
        selected = volume_encoder.getButtonKnobMode()
        print(selected)
        self.muteBtn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Mute",
            command=lambda: self.volumeModeOnclick("Mute", 0),
        )
        self.muteBtn.bind("<FocusIn>", self.on_focus_in)
        self.muteBtn.bind("<FocusOut>", self.on_focus_out)
        self.muteBtn.pack()
        if selected == 0:
            self.muteBtn.config(fg=SELECTED_COLOR)

        self.dVolBtn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Disable/Enable volume",
            command=lambda: self.volumeModeOnclick("Disable/Enable volume", 1),
        )
        self.dVolBtn.bind("<FocusIn>", self.on_focus_in)
        self.dVolBtn.bind("<FocusOut>", self.on_focus_out)
        self.dVolBtn.pack()
        if selected == 1:
            self.dVolBtn.config(fg=SELECTED_COLOR)

        self.mode0Btn = tk.Button(
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
        self.mode0Btn.bind("<FocusIn>", self.on_focus_in)
        self.mode0Btn.bind("<FocusOut>", self.on_focus_out)
        self.mode0Btn.pack()
