
class Point:
    def __init__(self, x, y, label):
        self._x = x if x is not None else 0
        self._y = y if y is not None else 0
        self._label = label if label is not None else 0

    def get_coordinates(self) -> list[int]:
        return [self._x, self._y]

    def set_coordinates(self, x, y):
        self._x = x
        self._y = y

    def __set_label(self, label):
        self._label = label

    def get_label(self):
        return self._label

    def __str__(self) -> str:
        return f"Point: {self._x}, {self._y}, {self._label}"

    def __repr__(self) -> str:
        return f"Point: {self._x}, {self._y}, {self._label}"
