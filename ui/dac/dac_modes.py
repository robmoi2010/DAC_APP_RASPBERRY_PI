import tkinter as tk
from dac.ess_dac import Dac
from registry.register import register, get_instance
from tkinter import messagebox
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton
from ui.styles import SELECTED_COLOR, UNSELECTED_COLOR

dac: Dac = get_instance("dac")


class DacModes(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    # 0 I2S Slave mode, 1 LJ Slave mode, 2 I2S Master mode, 3 SPDIF mode, 4 TDM I2S Slave mode Async, 5 TDM I2S Slave mode Sync
    def dacModesOnclick(frame, selection, type):
        answer = messagebox.askyesno(
            "Confirmation", "Are you sure you want to select " + selection
        )
        if answer:
            dac.setDacMode(type)
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

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="Select Dac Modes", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )
        currentMode = dac.get_current_dac_mode()

        self.mode0Btn = GeneralButton(
            self,
            "I2S Slave mode",
            selected=currentMode == 0,
            command=lambda: self.dacModesOnclick("I2S Slave mode", 0),
        )
        self.mode0Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.mode1Btn = GeneralButton(
            self,
            "LJ Slave mode",
            selected=currentMode == 1,
            command=lambda: self.dacModesOnclick("LJ Slave mode", 1),
        )
        self.mode1Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.mode2Btn = GeneralButton(
            self,
            "I2S Master mode",
            selected=currentMode == 2,
            command=lambda: self.dacModesOnclick("I2S Master mode", 2),
        )
        self.mode2Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")

        self.mode3Btn = GeneralButton(
            self,
            "SPDIF mode",
            selected=currentMode == 3,
            command=lambda: self.dacModesOnclick("SPDIF mode", 3),
        )
        self.mode3Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        self.mode6Btn = BackButton(
            self, command=lambda: controller.show_frame("DacSettings")
        )
        self.mode6Btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
