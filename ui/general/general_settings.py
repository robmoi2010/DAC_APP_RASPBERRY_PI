import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class GeneralSettings(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.counter = 0
        tk.Label(self, text="General settings", font=("Arial", 16)).pack(pady=20)
        btn5 = GeneralButton(
            self, "Sound Modes", command=lambda: controller.show_frame("SoundModes")
        )
        btn5.pack()

        btn4 = BackButton(self, command=lambda: controller.show_frame("MainSettings"))
        btn4.pack()
        # self.bind_all("<KeyPress>", self.on_key_press)
