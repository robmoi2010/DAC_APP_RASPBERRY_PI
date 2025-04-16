class MenuItem:
    def __init__(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def class_name(self):
        return self._class_name

    @property
    def index(self):
        return self._index

    @property
    def selected(self):
        return self._selected

    @name.setter
    def name(self, name):
        self._name = name

    @class_name.setter
    def class_name(self, class_name):
        self._class_name = class_name

    @index.setter
    def index(self, index):
        self._index = index

    @selected.setter
    def selected(self, selected):
        self._selected = selected
