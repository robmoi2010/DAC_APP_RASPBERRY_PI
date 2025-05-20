import tkinter as tk
import dac.ess_dac as ess_dac
from tkinter import messagebox
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from util.styles import SELECTED_COLOR, UNSELECTED_COLOR


class DacModes(tk.Frame):
    # 0 I2S Slave mode, 1 LJ Slave mode, 2 I2S Master mode, 3 SPDIF mode, 4 TDM I2S Slave mode Async, 5 TDM I2S Slave mode Sync
    def dacModesOnclick(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            ess_dac.setDacMode(type)
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
        currentMode = ess_dac.getCurrentDacMode()

        self.mode0Btn = GeneralButton(
            self,
            "I2S Slave mode",
            selected=currentMode == 0,
            command=lambda: self.dacModesOnclick("I2S Slave mode", 0),
        )
        self.mode0Btn.pack()
        self.mode1Btn = GeneralButton(
            self,
            "LJ Slave mode",
            selected=currentMode == 1,
            command=lambda: self.dacModesOnclick("LJ Slave mode", 1),
        )
        self.mode1Btn.pack()
        self.mode2Btn = GeneralButton(
            self,
            "I2S Master mode",
            selected=currentMode == 2,
            command=lambda: self.dacModesOnclick("I2S Master mode", 2),
        )
        self.mode2Btn.pack()

        self.mode3Btn = GeneralButton(
            self,
            "SPDIF mode",
            selected=currentMode == 3,
            command=lambda: self.dacModesOnclick("SPDIF mode", 3),
        )
        self.mode3Btn.pack()

        self.mode4Btn = GeneralButton(
            self,
            "TDM I2S Slave mode Async",
            selected=currentMode == 4,
            command=lambda: self.dacModesOnclick("TDM I2S Slave mode Async", 4),
        )
        self.mode4Btn.pack()
        self.mode5Btn = GeneralButton(
            self,
            "TDM I2S Slave mode Sync",
            selected=currentMode == 5,
            command=lambda: self.dacModesOnclick("TDM I2S Slave mode Sync", 5),
        )
        self.mode5Btn.pack()
        self.mode6Btn = BackButton(
            self, command=lambda: controller.show_frame("DacSettings")
        )
        self.mode6Btn.pack()
