import random
from point import Point


class PointGenerator:
    def __init__(self, function) -> None:
        self._function = function

    def set_function(self, function) -> None:
        self._function = function

    def __generate_point(self) -> None | Point:
        if self._function is None:
            return None

        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        label = None
        try:
            label = self._function(x, y)
            if label not in [-1, 1]:
                raise ValueError(f"Label is not -1 or 1: {label}")
        except Exception as e:
            print(f"Error in generate points for data: \nx: {x}\ny: {y}\nself.function: {self._function}\nError: {e}")
            label = None
        return Point(x, y, label)

    def generate(self, amount: int) -> None | list[Point]:
        if self._function is None:
            return None

        points = []
        for i in range(amount):
            points.append(self.__generate_point())
        return points
