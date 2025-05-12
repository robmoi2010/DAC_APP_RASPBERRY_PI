import tkinter as tk
from tkinter import ttk
import dac.dac_volume as dac_volume

# from dac.dac_volume import VOL_DIRECTION
import configs.app_config as app_config
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
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    def on_key_press(self, event):
        if event.keysym == "Right":
            dac_volume.updateVolume(dac_volume.VOL_DIRECTION.UP)
        if event.keysym == "Left":
            dac_volume.updateVolume(dac_volume.VOL_DIRECTION.DOWN)

    # Volume rotary encoder mock
    volume_bar = None
    volume_label = None

    # def on_key_release(self, event):
    #     pass

    def __init__(self, parent, controller):
        super().__init__(parent)
        # get current volume from storage
        currVolume = dac_volume.getPercentageVolume(dac_volume.getCurrentVolume())
        tk.Label(self, text="Home", font=("Arial", 16)).pack(pady=20)
        # canvas = tk.Canvas(self, width=200, height=30)
        # canvas.pack(expand=True)
        # canvas.create_rectangle(0, 0, currVolume * 2, 30, outline="red", fill="green")
        # canvas.create_text(100, 15, text=currVolume, font=("Arial", 25), fill="red")
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
        volume_label.place(relx=0.5, rely=0.5, anchor="center")
        btn1=tk.Button(
            self,
            relief=RELIEF,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Go to Settings",
            font=font,
            command=lambda: controller.show_frame("MainSettings"),
        )
        btn1.bind("<FocusIn>", self.on_focus_in)
        btn1.bind("<FocusOut>", self.on_focus_out)
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
