from app import current_visible_frame, prev_frame


class RemoteNavigation:
    def __init__(self):
        self.current_index = 0

    def handle_up_button(self):
        children = current_visible_frame.winfo_children()
        if self.current_index == 0:
            self.current_index = len(children) - 1
        children[self.current_index].tk_focusPrev().focus_set()
        self.current_index -= 1

    def handle_down_button(self):
        children = current_visible_frame.winfo_children()
        if self.current_index == len(children) - 1:
            self.current_index = 0
        children[self.current_index].tk_focusPrev().focus_set()
        self.current_index += 1

    def handle_OK_button(self):
        children = current_visible_frame.winfo_children()
        self.current_index = 0
        children[self.current_index].invoke()

    def handle_back_button(self):
        self.current_index = 0
        prev_frame.tkraise()
