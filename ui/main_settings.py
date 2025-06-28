import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class MainSettings(tk.Frame):
    def get_current_row(self):
        ret = self.row_index
        self.row_index += 1
        return ret

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
    #             self.counter = l - 1
    #     if event.keysym == "Return":
    #         print("enter")
    #         dac.dac_volume.onEnter(self.counter)

    # def on_key_release(self, event):
    #     pass

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.row_index = 1
        self.counter = 0
        tk.Label(self, text="Main Settings", font=("Arial", 16)).grid(
            row=self.get_current_row(), column=0, sticky="nsew"
        )
        btn5 = GeneralButton(
            self, "DAC", command=lambda: controller.show_frame("DacSettings")
        )
        btn5.grid(row=self.get_current_row(), column=0, sticky="nsew")
        btn2 = GeneralButton(
            self, "DSP", command=lambda: controller.show_frame("DspSettings")
        )

        btn2.grid(row=self.get_current_row(), column=0, sticky="nsew")
        btn3 = GeneralButton(
            self, "System", command=lambda: controller.show_frame("SystemSettings")
        )
        btn3.grid(row=self.get_current_row(), column=0, sticky="nsew")
        btn4 = BackButton(self, command=lambda: controller.show_frame("Home"))
        btn4.grid(row=self.get_current_row(), column=0, sticky="nsew")
        # self.bind_all("<KeyPress>", self.on_key_press)
