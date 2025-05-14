import tkinter as tk
from util.styles import (
    RELIEF,
    BUTTON_BG,
    BUTTON_HEIGHT,
    BUTTON_WIDTH,
    UNSELECTED_COLOR,
    BUTTON_FONT_SIZE,
    BUTTON_FONT,
    BUTTON_FONT_STYLE,
    BUTTON_ONFOCUS_BG
)

btnFont = (BUTTON_FONT, BUTTON_FONT_SIZE, BUTTON_FONT_STYLE)


class MainSettings(tk.Frame):
    def on_focus_in(self, event):
        event.widget.config(bg=BUTTON_ONFOCUS_BG)

    def on_focus_out(self, event):
        event.widget.config(bg=BUTTON_BG)

    # def on_key_press(self, event):
    #     if event.keysym == "Right":
    #         print("right")
    #         l = dac.dac_volume.onKeyRight(self.counter)
    #         self.counter += 1
    #         if self.counter >= l:
    #             self.counter = 0
    #     if event.keysym == "Left":
    #         print("left")
    #         l = dac.dac_volume.onkeyLeft(self.counter)
    #         self.counter -= 1
    #         if self.counter < 0:
    #             self.counter = l-1
    #     if event.keysym == "Return":
    #         print("enter")
    #         dac.dac_volume.onEnter(self.counter)

    # def on_key_release(self, event):
    #     pass

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.counter = 0
        tk.Label(self, text="Main Settings", font=("Arial", 16)).pack(pady=20)
        btn5 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="DAC",
            command=lambda: controller.show_frame("DacSettings"),
        )
        btn5.bind("<FocusIn>", self.on_focus_in)
        btn5.bind("<FocusOut>", self.on_focus_out)
        btn5.pack()
        btn2 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="DSP",
            command=lambda: controller.show_frame("DspSettings"),
        )
        btn2.bind("<FocusIn>", self.on_focus_in)
        btn2.bind("<FocusOut>", self.on_focus_out)
        btn2.pack()
        btn3 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="General",
            command=lambda: controller.show_frame(""),
        )
        btn3.bind("<FocusIn>", self.on_focus_in)
        btn3.bind("<FocusOut>", self.on_focus_out)
        btn3.pack()
        btn4 = tk.Button(
            self,
            relief=RELIEF,
            font=btnFont,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=UNSELECTED_COLOR,
            text="Back",
            command=lambda: controller.show_frame("Home"),
        )
        btn4.bind("<FocusIn>", self.on_focus_in)
        btn4.bind("<FocusOut>", self.on_focus_out)
        btn4.pack()
        # self.bind_all("<KeyPress>", self.on_key_press)
