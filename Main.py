#!C:\Users\admin\AppData\Local\Programs\Python\Python313 python
import logging
import os
import shutil
import unittest

from repo.sql_storage import SqlStorage
from tests.volume import test_volume_util
from ui.app import App
import registry.register as register
from dac.ess_dac import Dac
import uvicorn

app_window = None
logger = logging.getLogger(__name__)


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
    try:
        dac: Dac = register.get_instance("dac")
        dac.initialize_dac()
    except Exception as e:
        logger.error(e)
    try:
        storage: SqlStorage = register.get_instance("sqlstorage")
        storage.initialize()
    except Exception as e:
        logger.error(e)
    try:
        muses = register.get_instance("muses72323")
        muses.initialize_volume_chip()
    except Exception as e:
        logger.error(e)


def run_tests():
    test_volume_util.TestVolumeUtil().test_map_value()


if __name__ == "__main__":
    initialize_device()
    run_tests()
    uvicorn.run("services.root_service:app", host="0.0.0.0", port=8000, reload=True)
    get_app_window()
