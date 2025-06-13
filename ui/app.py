import tkinter as tk
from ui.dac.dac_settings import DacSettings
from ui.home import Home
from ui.dac.filters import Filters
from ui.dac.volume_modes import VolumeMode
from ui.dac.dac_modes import DacModes
from ui.main_settings import MainSettings
from ui.dsp.dsp_settings import DspSettings
from ui.dsp.input import Input
from ui.dsp.main_output import MainOutput
from ui.dsp.subwoofer_output import SubwooferOutput
from ui.dsp.output import Output
from ui.system.sound_modes import SoundModes
from ui.system.system_settings import SystemSettings
from ui.dac.thd_compensation import ThdCompensation
from ui.dac.second_order_compensation import SecondOrderCompensation
from ui.dac.third_order_compensation import ThirdOrderCompensation
from ui.dac.dac_volume_settings import DacVolumeSettings
from ui.system.volume_device import VolumeDevice
from ui.system.volume_algorithm import VolumeAlgorithm

current_visible_frame = None
prev_frame = None


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ESS Dac")
        self.geometry("600x400")

        self.frames = {}
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        for F in (
            Home,
            DacSettings,
            Filters,
            VolumeMode,
            DacModes,
            VolumeMode,
            MainSettings,
            DspSettings,
            Input,
            MainOutput,
            SubwooferOutput,
            Output,
            SoundModes,
            SystemSettings,
            ThdCompensation,
            SecondOrderCompensation,
            ThirdOrderCompensation,
            DacVolumeSettings,
            VolumeDevice,
            VolumeAlgorithm,
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
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.tkraise()
