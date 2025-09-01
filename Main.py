#!C:\Users\admin\AppData\Local\Programs\Python\Python313 python
import logging

from ui.app import App
import uvicorn

app_window = None
logger = logging.getLogger(__name__)


def get_app_window():
    global app_window
    if app_window is None:
        app_window = App()
        app_window.mainloop()
    return app_window

if __name__ == "__main__":
    uvicorn.run("services.root_service:app", host="0.0.0.0", port=8000)
