import tkinter as tk
import ESS_DAC
from tkinter import messagebox
from Styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    SELECTED_COLOR,
    UNSELECTED_COLOR,
    BUTTON_FONT_SIZE,
    BUTTON_FONT,
    BUTTON_FONT_STYLE,
)

btnFont = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)


class DacModes(
    tk.Frame
):  # 0 I2S Slave mode, 1 LJ Slave mode, 2 I2S Master mode, 3 SPDIF mode, 4 TDM I2S Slave mode Async, 5 TDM I2S Slave mode Sync
    def dacModesOnclick(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            ESS_DAC.setDacMode(type)
            if type == 0:
                frame.mode0Btn.config(fg=SELECTED_COLOR)
                frame.mode1Btn.config(fg=UNSELECTED_COLOR)
                frame.mode2Btn.config(fg=UNSELECTED_COLOR)
                frame.mode3Btn.config(fg=UNSELECTED_COLOR)
                frame.mode4Btn.config(fg=UNSELECTED_COLOR)
                frame.mode5Btn.config(fg=UNSELECTED_COLOR)
            if type == 1:
                frame.mode0Btn.config(fg=UNSELECTED_COLOR)
                frame.mode1Btn.config(fg=SELECTED_COLOR)
                frame.mode2Btn.config(fg=UNSELECTED_COLOR)
                frame.mode3Btn.config(fg=UNSELECTED_COLOR)
                frame.mode4Btn.config(fg=UNSELECTED_COLOR)
                frame.mode5Btn.config(fg=UNSELECTED_COLOR)
            if type == 2:
                frame.mode0Btn.config(fg=UNSELECTED_COLOR)
                frame.mode1Btn.config(fg=UNSELECTED_COLOR)
                frame.mode2Btn.config(fg=SELECTED_COLOR)
                frame.mode3Btn.config(fg=UNSELECTED_COLOR)
                frame.mode4Btn.config(fg=UNSELECTED_COLOR)
                frame.mode5Btn.config(fg=UNSELECTED_COLOR)
            if type == 3:
                frame.mode0Btn.config(fg=UNSELECTED_COLOR)
                frame.mode1Btn.config(fg=UNSELECTED_COLOR)
                frame.mode2Btn.config(fg=UNSELECTED_COLOR)
                frame.mode3Btn.config(fg=SELECTED_COLOR)
                frame.mode4Btn.config(fg=UNSELECTED_COLOR)
                frame.mode5Btn.config(fg=UNSELECTED_COLOR)
            if type == 4:
                frame.mode0Btn.config(fg=UNSELECTED_COLOR)
                frame.mode1Btn.config(fg=UNSELECTED_COLOR)
                frame.mode2Btn.config(fg=UNSELECTED_COLOR)
                frame.mode3Btn.config(fg=UNSELECTED_COLOR)
                frame.mode4Btn.config(fg=SELECTED_COLOR)
                frame.mode5Btn.config(fg=UNSELECTED_COLOR)
            if type == 5:
                frame.mode0Btn.config(fg=UNSELECTED_COLOR)
                frame.mode1Btn.config(fg=UNSELECTED_COLOR)
                frame.mode2Btn.config(fg=UNSELECTED_COLOR)
                frame.mode3Btn.config(fg=UNSELECTED_COLOR)
                frame.mode4Btn.config(fg=UNSELECTED_COLOR)
                frame.mode5Btn.config(fg=SELECTED_COLOR)

    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Select Dac Modes", font=("Arial", 16)).pack(pady=20)
        currentMode = ESS_DAC.getCurrentDacMode()

        self.mode0Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="I2S Slave mode",
            command=lambda: self.dacModesOnclick("I2S Slave mode", 0),
        )
        self.mode0Btn.pack()
        if currentMode == 0:
            self.mode0Btn.config(fg=SELECTED_COLOR)
        self.mode1Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="LJ Slave mode",
            command=lambda: self.dacModesOnclick("LJ Slave mode", 1),
        )
        self.mode1Btn.pack()
        if currentMode == 1:
            self.mode1Btn.config(fg=SELECTED_COLOR)
        self.mode2Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="I2S Master mode",
            command=lambda: self.dacModesOnclick("I2S Master mode", 2),
        )
        self.mode2Btn.pack()
        if currentMode == 2:
            self.mode2Btn.config(fg=SELECTED_COLOR)
        self.mode3Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="SPDIF mode",
            command=lambda: self.dacModesOnclick("SPDIF mode", 3),
        )
        self.mode3Btn.pack()
        if currentMode == 3:
            self.mode3Btn.config(fg=SELECTED_COLOR)
        self.mode4Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="TDM I2S Slave mode Async",
            command=lambda: self.dacModesOnclick("TDM I2S Slave mode Async", 4),
        )
        self.mode4Btn.pack()
        if currentMode == 4:
            self.mode4Btn.config(fg=SELECTED_COLOR)
        self.mode5Btn = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="TDM I2S Slave mode Sync",
            command=lambda: self.dacModesOnclick("TDM I2S Slave mode Sync", 5),
        )
        self.mode5Btn.pack()
        if currentMode == 5:
            self.mode5Btn.config(fg=SELECTED_COLOR)
        tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("Settings"),
        ).pack()
