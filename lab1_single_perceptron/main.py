import random

training_set =     [({-1, 2}, -1), ({-4, -2}, -1), ({-3, 1}, -1), ({0, 0}, -1), ({3, 1}, 1), ({-4, -5}, 1), ({4, -1}, 1)]
verification_set = [({-2, 1}, -1), ({-3, 2}, -1), ({-1, 0}, -1), ({1, 1}, -1), ({2, 2}, 1), ({-2, -2}, 1), ({2, -1}, 1)]

class Perceptron:
    weights = []
    bias = 1

    activation_threshold = 1
    failure_threshold = 0

    def __init__(self, weights: list[int], bias: float, activation_threshold: int) -> None:
        self.weights = weights
        self.bias = bias
        self.activation_threshold = activation_threshold

    def __init__(self) -> None:
        for i in range(random.randint(2, 5)):
            self.weights.append(random.randint(1, 10))
        bias = 1

    def getCoordinates(self, point: list) -> list:
        a = list(point[0])
        return list(point[0])

    def getLabel(self, point: list) -> int:
        a = point[1]
        return point[1]

    def predict(self, point: list) -> float:
        total = 0
        #for weight in self.weights:
        #    for coordinate in point:
        #        total += weight * coordinate
        print(point)
        total = self.weights[0] + self.weights[1] * point[-1]
        return total + self.bias

    def train(self, points: list[dict[list, int]]) -> None:
        for point in points:
            label = self.getLabel(point)
            sum = self.predict(self.getCoordinates(point))
            error = label - sum
            if error != 0:
                for weight in self.weights:
                    weight += error
                self.bias += error

    def verify(self, points: list[dict[list, int]]) -> float:
        correct = 0
        for point in points:
            label = self.getLabel(point)
            sum = self.predict(self.getCoordinates(point))
            if label == sum:
                correct += 1
        return correct / len(points)

    def __str__(self) -> str:
        return f"Perceptron: {self.weights}, {self.bias}, {self.activation_threshold}"


def main():
    perceptron = Perceptron()
    perceptron.train(training_set)
    print(perceptron.verify(verification_set))
    print(perceptron)


if __name__ == "__main__":
    main()




