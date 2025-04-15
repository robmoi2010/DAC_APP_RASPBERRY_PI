import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ESS Dac")
        self.geometry("400x300")

        self.frames = {}

        for F in (Home, Settings, Filters, DacModes):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text=, font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Go to Settings", command=lambda: controller.show_frame("SettingsPage")).pack()
class Settings(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Home Page", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Go to Settings", command=lambda: controller.show_frame("SettingsPage")).pack()
        tk.Button(self, text="Go to Advanced", command=lambda: controller.show_frame("AdvancedPage")).pack()


class Filters(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Settings Page", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage")).pack()


class DacModes(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Advanced Page", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage")).pack()
