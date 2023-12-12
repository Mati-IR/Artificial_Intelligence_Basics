
class Point:
    def __init__(self, x, y, label):
        self._x = x if x is not None else 0
        self._y = y if y is not None else 0
        self.label = label if label is not None else lambda x: x

    def get_coordinates(self):
        return [self._x, self._y]

    def set_coordinates(self, x, y):
        self._x = x
        self._y = y

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label

    def __str__(self) -> str:
        return f"Point: {self._x}, {self._y}, {self.label}"

    def __repr__(self) -> str:
        return f"Point: {self._x}, {self._y}, {self.label}"
