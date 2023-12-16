from point import Point
import random


class Perceptron:
    _weights = []
    _bias = 1
    _learning_rate = 0.1

    _activation_threshold = 1
    _failure_threshold = 0

    def __init__(self, weights: list[int], bias: float, activation_threshold: int) -> None:
        self._weights = weights
        self._bias = bias
        self._activation_threshold = activation_threshold

    def __init__(self) -> None:
        for i in range(2):
            self._weights.append(random.randint(1, 10))

    def __getLabel(self, point: list) -> int:
        return point[1]

    def __predict(self, point: Point) -> int:
        prediction = 0
        for i in range(len(self._weights)):
            prediction += self._weights[i] * point.get_coordinates()[i]
        prediction += self._bias
        if prediction >= self._activation_threshold:
            return 1
        elif prediction <= self._failure_threshold:
            return -1
        else:
            return 0

    def train_classification(self, points: list[Point]) -> None:
        for point in points:
            if self.__predict(point) >= self._activation_threshold:
                if point.get_label() == -1:
                    for i in range(len(self._weights)):
                        self._weights[i] -= point.get_coordinates()[i]
                    self._bias -= 1
            else:
                if point.get_label() == 1:
                    for i in range(len(self._weights)):
                        self._weights[i] += point.get_coordinates()[i]
                    self._bias += 1
            print(f"weights: {self._weights}, bias: {self._bias}")

    def get_linear_function_multipliers(self) -> list[float]:
        return [-self._weights[0] / self._weights[1], -self._bias / self._weights[1]]
    
    def verify(self, points: list[Point]) -> float:
        correct = 0
        for point in points:
            if point.get_label() == self.__predict(point):
                correct += 1
        return correct / len(points)

    def __str__(self) -> str:
        return f"Perceptron: {self._weights}, bias: {self._bias}, activation threshold: {self._activation_threshold}"
