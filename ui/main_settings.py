import tkinter as tk
from ui.generics.general_button import GeneralButton
from ui.generics.back_button import BackButton


class MainSettings(tk.Frame):
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
        self.counter = 0
        tk.Label(self, text="Main Settings", font=("Arial", 16)).pack(pady=20)
        btn5 = GeneralButton(
            self, "DAC", command=lambda: controller.show_frame("DacSettings")
        )
        btn5.pack()
        btn2 = GeneralButton(
            self, "DSP", command=lambda: controller.show_frame("DspSettings")
        )

        btn2.pack()
        btn3 = GeneralButton(
            self, "General", command=lambda: controller.show_frame("GeneralSettings")
        )
        btn3.pack()
        btn4 = BackButton(self, command=lambda: controller.show_frame("Home"))
        btn4.pack()
        # self.bind_all("<KeyPress>", self.on_key_press)
