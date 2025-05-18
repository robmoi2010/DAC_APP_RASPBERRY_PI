import tkinter as tk
from tkinter import messagebox
import general.sound_modes
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
    SELECTED_COLOR,
)

btnFont = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)


class SoundModes(tk.Frame):
    def mode_on_click(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            general.sound_modes.update_sound_mode(type)
            if type == 0:
                frame.btn1.config(fg=SELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)      
            if type == 1:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=SELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
            if type == 2:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=SELECTED_COLOR)
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Select Sound Mode", font=("Arial", 16)).pack(
            pady=20
        )
        current_sound_mode = general.sound_modes.get_current_sound_mode()
        self.btn1 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Pure Direct",
            command=lambda: self.mode_on_click("Pure Direct", 0),
        )
        self.btn1.bind("<FocusIn>", self.on_focus_in)
        self.btn1.bind("<FocusOut>", self.on_focus_out)
        if current_sound_mode == 0:
            self.btn1.config(fg=SELECTED_COLOR)
        self.btn1.pack()
        self.btn2 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Semi-Pure Direct(mains direct, sub DSP)",
            command=lambda: self.mode_on_click("Semi-Pure Direct", 1),
        )
        self.btn2.bind("<FocusIn>", self.on_focus_in)
        self.btn2.bind("<FocusOut>", self.on_focus_out)
        if current_sound_mode == 1:
            self.btn2.config(fg=SELECTED_COLOR)
        self.btn2.pack()
        self.btn3 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="DSP",
            command=lambda: self.mode_on_click("DSP", 2),
        )
        self.btn3.bind("<FocusIn>", self.on_focus_in)
        self.btn3.bind("<FocusOut>", self.on_focus_out)
        if current_sound_mode == 2:
            self.btn3.config(fg=SELECTED_COLOR)
        self.btn3.pack()
        
        self.btn6 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("GeneralSettings"),
        )
        self.btn6.bind("<FocusIn>", self.on_focus_in)
        self.btn6.bind("<FocusOut>", self.on_focus_out)
        self.btn6.pack()
