from point import Point
import random

class Perceptron:
    _weights = []
    _bias = 1

    _activation_threshold = 1
    _failure_threshold = 0

    def __init__(self, weights: list[int], bias: float, activation_threshold: int) -> None:
        self._weights = weights
        self._bias = bias
        self._activation_threshold = activation_threshold

    def __init__(self) -> None:
        for i in range(random.randint(2, 5)):
            self._weights.append(random.randint(1, 10))
        bias = 1

    def __getLabel(self, point: list) -> int:
        return point[1]

#TODO: Bug here, should probably return 1 or -1 and not float
    def __predict(self, point: list[int]) -> float:
        try:
            total = 0
            for i in range(len(point)):
                total += point[i] * self._weights[i]
        except Exception as e:
            print(f"point: {point}\nError: {e}")

        return total + self._bias

    def train(self, points: list[Point]) -> None:
        for point in points:
            print(f"processed point: {point}")
            sum = self.__predict(point)
            error = point.get_label() - sum
            if error != 0:
                for weight in self._weights:
                    weight += error
                self._bias += error

    def verify(self, points: list[Point]) -> float:
        correct = 0
        for point in points:
            if point.get_label() == self.__predict(point.get_coordinates()):
                correct += 1
        return correct / len(points)

    def __str__(self) -> str:
        return f"Perceptron: {self._weights}, {self._bias}, {self._activation_threshold}"
