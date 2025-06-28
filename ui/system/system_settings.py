import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class SystemSettings(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        tk.Label(self, text="System settings", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )
        btn = GeneralButton(
            self, "Volume Device", command=lambda: controller.show_frame("VolumeDevice")
        )
        btn.grid(row=self.get_current_row(), column=0, sticky="nsew")
        btn3 = GeneralButton(
            self,
            "Volume Algorithm",
            command=lambda: controller.show_frame("VolumeAlgorithm"),
        )
        btn3.grid(row=self.get_current_row(), column=0, sticky="nsew")
        btn1 = GeneralButton(
            self, "Sound Modes", command=lambda: controller.show_frame("SoundModes")
        )
        btn1.grid(row=self.get_current_row(), column=0, sticky="nsew")

        btn2 = BackButton(self, command=lambda: controller.show_frame("MainSettings"))
        btn2.grid(row=self.get_current_row(), column=0, sticky="nsew")
        # self.bind_all("<KeyPress>", self.on_key_press)
