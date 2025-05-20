from util.styles import BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT
from ui.generics.general_button import GeneralButton


class BackButton(GeneralButton):
    def __init__(self, parent, command):
        super().__init__(parent, "Back", command=command)
        self.config(
            width=BACK_BUTTON_WIDTH,
            height=BACK_BUTTON_HEIGHT,
        )
