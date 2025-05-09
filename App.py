import tkinter as tk
from settings import Settings
from home import Home
from filters import Filters
from volume_modes import VolumeMode
from dac_modes import DacModes


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ESS Dac")
        #  self.geometry("400x300")

        self.frames = {}

        for F in (Home, Settings, Filters, VolumeMode, DacModes, VolumeMode):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
