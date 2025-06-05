import tkinter as tk
from tkinter import ttk
import factory.system_factory as factory
from factory.system_factory import SYS_OBJECTS
from general.sound_modes import SoundMode
import general.sound_modes as sound_modes

from ui.generics.general_button import GeneralButton

from util.styles import BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE

font = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)

volume = factory.new(SYS_OBJECTS.VOLUME)


class Home(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1

        return ret

    def on_key_press(self, event):
        if event.keysym == "Right":
            volume.update_volume(volume.VOL_DIRECTION.UP)
        if event.keysym == "Left":
            volume.update_volume(volume.VOL_DIRECTION.DOWN)

    # Volume rotary encoder mock
    volume_bar = None
    volume_label = None

    mode_label = None
    # def on_key_release(self, event):
    #     pass

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        # get current volume from storage
        currVolume = volume.get_percentage_volume(volume.get_current_volume())
        sound_mode: SoundMode = sound_modes.get_current_sound_mode()

        # tk.Label(self, text="Home", font=("Arial", 16)).grid(
        #     row=self.get_current_row(), column=0, sticky="nsew"
        # )
        global mode_label
        mode_label = tk.Label(
            self, text="Current Mode: " + sound_mode.name, font=("Arial", 10)
        )
        r = self.get_current_row()
        mode_label.grid(row=r, column=0, sticky="nsew")
        tk.Label(self, text="sample rate: xyz", font=("Arial", 10)).grid(
            row=r, column=0, sticky="nsw"
        )
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Thick.Horizontal.TProgressbar", thickness=200)
        global volume_bar
        volume_bar = ttk.Progressbar(
            self,
            orient="horizontal",
            length=400,
            style="Thick.Horizontal.TProgressbar",
            mode="determinate",
            maximum=100,
        )
        volume_bar.grid(row=self.get_current_row(), column=0, sticky="nsew")
        volume_bar["value"] = currVolume

        global volume_label
        volume_label = tk.Label(
            self, text=currVolume, fg="black", font=("Arial", 50, "bold")
        )
        volume_label.place(relx=0.5, rely=0.56, anchor="center")
        btn1 = GeneralButton(
            self, "Settings", command=lambda: controller.show_frame("MainSettings")
        )
        btn1.grid(row=self.get_current_row(), column=0, sticky="nsew")

        # for mocking volume rotary encoder
        self.bind("<KeyPress>", self.on_key_press)
        # self.bind("<KeyRelease>", self.on_key_release)
        self.focus_set()


def update_volume(currVolume):
    currVolume = volume.get_percentage_volume(currVolume)
    global volume_bar
    volume_bar["value"] = currVolume
    global volume_label
    volume_label.config(text=currVolume)


def update_sound_mode(mode):
    global mode_label
    mode_label.config(text="Current Mode: " + mode)
