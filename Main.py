from ui.app import App

import repo.mongo_repo as mongo_repo
from volume.muses72323 import Muses72323
import dac.ess_dac as dac

app_window = None


def get_app_window():
    global app_window
    if app_window is None:
        app_window = App()
        app_window.mainloop()
    return app_window


def main():
    window = get_app_window()
    window.mainloop()


def initialize_device():
    dac.initialize_dac()
    mongo_repo.initialize()
    Muses72323().initialize_volume_chip()


if __name__ == "__main__":
    initialize_device()
    get_app_window()
