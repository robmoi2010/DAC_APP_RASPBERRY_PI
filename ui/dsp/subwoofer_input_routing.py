import tkinter as tk
from tkinter import messagebox
import dsp.router as router
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


class SubwooferInputRouting(tk.Frame):
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def route_on_click(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            router.update_subwoofer_input_sink(type)
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

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Select Subwoofer Input Sink", font=("Arial", 16)).pack(pady=20)
        current_input_sink = router.get_subwoofer_input_sink()
        self.btn1 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Output",
            command=lambda: self.route_on_click("Output", 0),
        )
        self.btn1.bind("<FocusIn>", self.on_focus_in)
        self.btn1.bind("<FocusOut>", self.on_focus_out)
        if current_input_sink == 0:
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
            text="Dsp Core",
            command=lambda: self.route_on_click("Dsp Core", 1),
        )
        self.btn2.bind("<FocusIn>", self.on_focus_in)
        self.btn2.bind("<FocusOut>", self.on_focus_out)
        if current_input_sink == 1:
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
            text="ASRC",
            command=lambda: self.route_on_click("ASRC", 2),
        )
        self.btn3.bind("<FocusIn>", self.on_focus_in)
        self.btn3.bind("<FocusOut>", self.on_focus_out)
        if current_input_sink == 2:
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
            text="Back",
            command=lambda: controller.show_frame("SourceRouting"),
        )
        self.btn4.bind("<FocusIn>", self.on_focus_in)
        self.btn4.bind("<FocusOut>", self.on_focus_out)
        self.btn4.pack()
