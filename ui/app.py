import tkinter as tk
from ui.dac.dac_settings import DacSettings
from ui.home import Home
from ui.dac.filters import Filters
from ui.dac.volume_modes import VolumeMode
from ui.dac.dac_modes import DacModes
from ui.main_settings import MainSettings
from ui.dair.digital_receiver_settings import DigitalReceiverSettings
from ui.dair.dir_settings import DirSettings
from ui.dair.dit_settings import DitSettings
from ui.dair.src_settings import SrcSettings

current_visible_frame = None
prev_frame = None


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ESS Dac")
        #  self.geometry("400x300")

        self.frames = {}

        for F in (
            Home,
            DacSettings,
            Filters,
            DigitalReceiverSettings,
            VolumeMode,
            DacModes,
            VolumeMode,
            MainSettings,
            DirSettings,
            DitSettings,
            SrcSettings,
        ):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        global prev_frame
        global current_visible_frame
        prev_frame = current_visible_frame
        current_visible_frame = frame
        frame.tkraise()
