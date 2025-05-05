import tkinter as tk
from tkinter import ttk
import DAC_VOLUME
import AppConfig
from Styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    UNSELECTED_COLOR,
    BUTTON_FONT,
    BUTTON_FONT_SIZE,
    BUTTON_FONT_STYLE,
)

VOLUME_POLL_DURATION = AppConfig.getConfig()["DAC"]["VOLUME"]["VOLUME_UI_POLL_DURATION"]


font = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)


class Home(tk.Frame):
    #Volume rotary encoder mock
    def on_key_press(self, event):
        if event.keysym == "Right":
            DAC_VOLUME.updateVolume("up")
        if event.keysym == "Left":
            DAC_VOLUME.updateVolume("down")

    def on_key_release(self, event):
        pass

    def __init__(self, parent, controller):
        super().__init__(parent)
        # get current volume from storage
        currVolume = DAC_VOLUME.getPercentageVolume(DAC_VOLUME.getCurrentVolume())
        tk.Label(self, text="Home", font=("Arial", 16)).pack(pady=20)
        # canvas = tk.Canvas(self, width=200, height=30)
        # canvas.pack(expand=True)
        # canvas.create_rectangle(0, 0, currVolume * 2, 30, outline="red", fill="green")
        # canvas.create_text(100, 15, text=currVolume, font=("Arial", 25), fill="red")
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Thick.Horizontal.TProgressbar", thickness=200)
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
        label = tk.Label(self, text=currVolume, fg="black", font=("Arial", 50, "bold"))
        label.place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(
            self,
            relief=RELIEF,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Go to Settings",
            font=font,
            command=lambda: controller.show_frame("Settings"),
        ).pack()

        def poll_volume():
            currVolume = DAC_VOLUME.getPercentageVolume(DAC_VOLUME.getCurrentVolume())
            volume_bar["value"] = currVolume
            label.config(text=currVolume)
            self.after(VOLUME_POLL_DURATION, poll_volume)

        poll_volume()
        # for mocking volume rotary encoder
        self.bind("<KeyPress>", self.on_key_press)
        self.bind("<KeyRelease>", self.on_key_release)
        self.focus_set()
