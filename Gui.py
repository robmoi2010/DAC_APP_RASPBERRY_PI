import tkinter as tk
import DAC_VOLUME
import ESS_DAC
import DAC_FILTERS
from tkinter import messagebox

ENABLE_VOL_TEXT = "Enable Volume"
DISABLE_VOL_TEXT = "DIsable Volume"


def dacModesOnclick(selection, type):
    answer = messagebox.askyesno(
        "Confirmation", "Are you sure you want to select " + selection
    )
    if answer:
        ESS_DAC.setDacMode(type)


def filtersOnclick(selection, type):
    answer = messagebox.askyesno(
        "Confirmation", "Are you sure you want to select " + selection
    )
    if answer:
        DAC_FILTERS.updateFilter(type)


def volumeModeOnclick(selection, type):
    answer = messagebox.askyesno(
        "Confirmation", "Are you sure you want to select " + selection
    )
    if answer:
        DAC_VOLUME.setRotaryButtonMode(type)


def volumeDisableEnableOnclick(frame):
    if DAC_VOLUME.isVolumeDisabled() == 1:
        selection = "Enable"
        text = ENABLE_VOL_TEXT
    else:
        selection = "disable"
        text = DISABLE_VOL_TEXT
    answer = messagebox.askyesno(
        "Confirmation", "Are you sure you want to select " + selection
    )
    if answer:
        DAC_VOLUME.disableEnableVolume()
        frame.volBtn.config(text=text)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ESS Dac")
        self.geometry("400x300")

        self.frames = {}

        for F in (Home, Settings, Filters, VolumeMode, DacModes, VolumeMode):
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
        # get current volume from storage
        currVolume = DAC_VOLUME.getPercentageVolume(DAC_VOLUME.getCurrentVolume())
        tk.Label(self, text="Home", font=("Arial", 16)).pack(pady=20)
        tk.Label(self, text=currVolume, font=("Arial", 16)).pack(pady=20)
        tk.Button(
            self,
            text="Go to Settings",
            command=lambda: controller.show_frame("Settings"),
        ).pack()


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Settings", font=("Arial", 16)).pack(pady=20)
        disabled = DAC_VOLUME.isVolumeDisabled()
        if disabled == 1:
            text = ENABLE_VOL_TEXT
        else:
            text = DISABLE_VOL_TEXT
        self.volBtn = tk.Button(
            self,
            text=text,
            command=lambda: volumeDisableEnableOnclick(self),
        )
        self.volBtn.pack()
        tk.Button(
            self, text="Filters", command=lambda: controller.show_frame("Filters")
        ).pack()
        tk.Button(
            self, text="DAC Modes", command=lambda: controller.show_frame("DacModes")
        ).pack()
        tk.Button(
            self,
            text="Volume Mode",
            command=lambda: controller.show_frame("VolumeMode"),
        ).pack()
        tk.Button(
            self, text="Back", command=lambda: controller.show_frame("Home")
        ).pack()


# 0 Minimum phase
# 1 Linear phase apodizing first roll-off
# 2 Linear phase fast roll-off
# 3 Linear phase slow roll-off low ripple
# 4 Linear phase slow roll-off
# 5 Minimum phase fast roll-off
# 6 Minimum phase slow roll-off
# 7 Minimum phase slow roll-off low dispersion
class Filters(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Select DAC Filter", font=("Arial", 16)).pack(pady=20)
        self.mpBtn = tk.Button(
            self,
            text="Minimum phase",
            fg="red",
            command=lambda: filtersOnclick("Minimum phase", 0),
        )
        self.mpBtn
        tk.Button(
            self,
            text="Linear phase apodizing first roll-off",
            command=lambda: filtersOnclick("Linear phase apodizing first roll-off", 1),
        ).pack()
        tk.Button(
            self,
            text="Linear phase fast roll-off",
            command=lambda: filtersOnclick("Linear phase fast roll-off", 2),
        ).pack()
        tk.Button(
            self,
            text="Linear phase slow roll-off low ripple",
            command=lambda: filtersOnclick("Linear phase slow roll-off low ripple", 3),
        ).pack()
        tk.Button(
            self,
            text="Linear phase slow roll-off",
            command=lambda: filtersOnclick("Linear phase slow roll-off low ripple", 4),
        ).pack()
        tk.Button(
            self,
            text="Minimum phase fast roll-off",
            command=lambda: filtersOnclick("Linear phase slow roll-off low ripple", 5),
        ).pack()
        tk.Button(
            self,
            text="Minimum phase slow roll-off",
            command=lambda: filtersOnclick("Minimum phase slow roll-off", 6),
        ).pack()
        tk.Button(
            self,
            text="Minimum phase slow roll-off low dispersion",
            command=lambda: filtersOnclick(
                "Minimum phase slow roll-off low dispersion", 7
            ),
        ).pack()
        tk.Button(
            self, text="Back", command=lambda: controller.show_frame("Settings")
        ).pack()


class VolumeMode(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(
            self, text="Select volume knob press functionality", font=("Arial", 16)
        ).pack(pady=20)
        tk.Button(
            self, text="Mute", command=lambda: volumeModeOnclick("Mute", 0)
        ).pack()
        tk.Button(
            self,
            text="Disable/Enable volume",
            command=lambda: volumeModeOnclick("Disable/Enable volume", 1),
        ).pack()
        tk.Button(
            self, text="Back", command=lambda: controller.show_frame("Settings")
        ).pack()


class DacModes(
    tk.Frame
):  # 0 I2S Slave mode, 1 LJ Slave mode, 2 I2S Master mode, 3 SPDIF mode, 4 TDM I2S Slave mode Async, 5 TDM I2S Slave mode Sync
    def __init__(self, parent, controller):
        filterLst = []
        filterItem = FilterItems()
        filterItem.index = 0
        filterItem.name = "I2S Slave mode"
        filterItem.selected = 1
        filterItem1 = FilterItems()
        filterItem1.index = 1
        filterItem1.name = "LJ Slave mode"
        filterItem1.selected = 0
        filterItem2 = FilterItems()
        filterItem2.index = 2
        filterItem2.name = "I2S Master mode"
        filterItem2.selected = 0
        filterItem3 = FilterItems()
        filterItem3.index = 3
        filterItem3.name = "SPDIF mode"
        filterItem3.selected = 0
        filterItem4 = FilterItems()
        filterItem4.index = 4
        filterItem4.name = "TDM I2S Slave mode Async"
        filterItem4.selected = 0
        filterItem5 = FilterItems()
        filterItem5.index = 5
        filterItem5.name = "TDM I2S Slave mode Sync"
        filterItem5.selected = 0
        
        filterLst.append(filterItem)
        filterLst.append(filterItem1)
        filterLst.append(filterItem3)
        filterLst.append(filterItem4)
        filterLst.append(filterItem5)
        filterLst.append(filterItem6)
        
        super().__init__(parent)
        tk.Label(self, text="Select Dac Modes", font=("Arial", 16)).pack(pady=20)
        tk.Button(
            self,
            text="I2S Slave mode",
            command=lambda: dacModesOnclick("I2S Slave mode", 0),
        ).pack()
        tk.Button(
            self,
            text="LJ Slave mode",
            command=lambda: dacModesOnclick("LJ Slave mode", 1),
        ).pack()
        tk.Button(
            self,
            text="I2S Master mode",
            command=lambda: dacModesOnclick("I2S Master mode", 2),
        ).pack()
        tk.Button(
            self, text="SPDIF mode", command=lambda: dacModesOnclick("SPDIF mode", 3)
        ).pack()
        tk.Button(
            self,
            text="TDM I2S Slave mode Async",
            command=lambda: dacModesOnclick("TDM I2S Slave mode Async", 4),
        ).pack()
        tk.Button(
            self,
            text="TDM I2S Slave mode Sync",
            command=lambda: dacModesOnclick("TDM I2S Slave mode Sync", 5),
        ).pack()
        tk.Button(
            self, text="Back", command=lambda: controller.show_frame("Settings")
        ).pack()


class FilterItems:
    def __init__(self):
        pass

    @property
    def name(self):
        return self.name

    @property
    def index(self):
        return self.index

    @property
    def selected(self):
        return self.selected

    @name.setter
    def name(self, name):
        self.name = name

    @index.setter
    def index(self, index):
        self.index = index

    @selected.setter
    def selected(self, selected):
        self.selected = selected
