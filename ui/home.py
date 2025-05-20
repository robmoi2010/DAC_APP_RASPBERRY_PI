import tkinter as tk
from tkinter import ttk
import dac.dac_volume as dac_volume
import general.sound_modes as sound_modes
from ui.generics.general_button import GeneralButton

from util.styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    UNSELECTED_COLOR,
    BUTTON_FONT,
    BUTTON_FONT_SIZE,
    BUTTON_FONT_STYLE,
    BUTTON_ONFOCUS_BG,
)

font = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)


class Home(tk.Frame):
    def on_key_press(self, event):
        if event.keysym == "Right":
            dac_volume.updateVolume(dac_volume.VOL_DIRECTION.UP)
        if event.keysym == "Left":
            dac_volume.updateVolume(dac_volume.VOL_DIRECTION.DOWN)

    # Volume rotary encoder mock
    volume_bar = None
    volume_label = None

    mode_label = None
    # def on_key_release(self, event):
    #     pass

    def __init__(self, parent, controller):
        super().__init__(parent)
        # get current volume from storage
        currVolume = dac_volume.getPercentageVolume(dac_volume.getCurrentVolume())
        sound_mode = sound_modes.get_sound_mode_name(
            sound_modes.get_current_sound_mode()
        )
        tk.Label(self, text="Home", font=("Arial", 16)).pack(pady=20)
        global mode_label
        mode_label = tk.Label(
            self, text="Current Mode: " + sound_mode, font=("Arial", 16)
        )
        mode_label.pack(pady=20)
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
        volume_bar.pack(expand=True)
        volume_bar["value"] = currVolume

        global volume_label
        volume_label = tk.Label(
            self, text=currVolume, fg="black", font=("Arial", 50, "bold")
        )
        volume_label.place(relx=0.5, rely=0.56, anchor="center")
        btn1 = GeneralButton(
            self, "Settings", command=lambda: controller.show_frame("MainSettings")
        )
        btn1.pack()

        # for mocking volume rotary encoder
        self.bind("<KeyPress>", self.on_key_press)
        # self.bind("<KeyRelease>", self.on_key_release)
        self.focus_set()


def updateVolume(currVolume):
    currVolume = dac_volume.getPercentageVolume(currVolume)
    global volume_bar
    volume_bar["value"] = currVolume
    global volume_label
    volume_label.config(text=currVolume)


def update_sound_mode(mode):
    global mode_label
    mode_label.config(text="Current Mode: " + mode)
