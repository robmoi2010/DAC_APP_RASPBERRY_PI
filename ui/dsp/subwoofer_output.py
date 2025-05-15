import tkinter as tk
from tkinter import messagebox
import dsp.io as output
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


class SubwooferOutput(tk.Frame):
    def output_on_click(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            output.update_subwoofer_output(type)
            if type == 0:
                frame.btn1.config(fg=SELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
                frame.btn4.config(fg=UNSELECTED_COLOR)
                frame.btn5.config(fg=UNSELECTED_COLOR)
            if type == 1:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=SELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
                frame.btn4.config(fg=UNSELECTED_COLOR)
                frame.btn5.config(fg=UNSELECTED_COLOR)
            if type == 2:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=SELECTED_COLOR)
                frame.btn4.config(fg=UNSELECTED_COLOR)
                frame.btn5.config(fg=UNSELECTED_COLOR)
            if type == 3:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
                frame.btn4.config(fg=SELECTED_COLOR)
                frame.btn5.config(fg=UNSELECTED_COLOR)
            if type == 4:
                frame.btn1.config(fg=UNSELECTED_COLOR)
                frame.btn2.config(fg=UNSELECTED_COLOR)
                frame.btn3.config(fg=UNSELECTED_COLOR)
                frame.btn4.config(fg=UNSELECTED_COLOR)
                frame.btn5.config(fg=SELECTED_COLOR)

    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Select Subwoofer Output", font=("Arial", 16)).pack(pady=20)
        current_sub_output = output.get_current_subwoofer_output()
        self.btn1 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="COAXIAL",
            command=lambda: self.output_on_click("COAXIAL", 0),
        )
        self.btn1.bind("<FocusIn>", self.on_focus_in)
        self.btn1.bind("<FocusOut>", self.on_focus_out)
        if current_sub_output == 0:
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
            text="I2S_0",
            command=lambda: self.output_on_click("I2S_0", 1),
        )
        self.btn2.bind("<FocusIn>", self.on_focus_in)
        self.btn2.bind("<FocusOut>", self.on_focus_out)
        if current_sub_output == 1:
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
            text="I2S_1",
            command=lambda: self.output_on_click("I2S_1", 2),
        )
        self.btn3.bind("<FocusIn>", self.on_focus_in)
        self.btn3.bind("<FocusOut>", self.on_focus_out)
        if current_sub_output == 2:
            self.btn3.config(fg=SELECTED_COLOR)
        self.btn3.pack()
        self.btn4 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="I2S_2",
            command=lambda: self.output_on_click("I2S_2", 3),
        )
        self.btn4.bind("<FocusIn>", self.on_focus_in)
        self.btn4.bind("<FocusOut>", self.on_focus_out)
        if current_sub_output == 3:
            self.btn4.config(fg=SELECTED_COLOR)
        self.btn4.pack()
        self.btn5 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="I2S_3",
            command=lambda: self.output_on_click("I2S_3", 4),
        )
        self.btn5.bind("<FocusIn>", self.on_focus_in)
        self.btn5.bind("<FocusOut>", self.on_focus_out)
        if current_sub_output == 4:
            self.btn5.config(fg=SELECTED_COLOR)
        self.btn5.pack()
        self.btn6 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("Output"),
        )
        self.btn6.bind("<FocusIn>", self.on_focus_in)
        self.btn6.bind("<FocusOut>", self.on_focus_out)
        self.btn6.pack()
