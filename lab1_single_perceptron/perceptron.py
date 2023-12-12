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
        return list(point[0])

    def getLabel(self, point: list) -> int:
        return point[1]

    def predict(self, point: list) -> float:
        try:
            total = 0
            if len(point) == 1:
                point.append(point[0])
            for i in range(len(point)):
                total += point[i] * self.weights[i]
        except Exception as e:
            print(f"point: {point}\nError: {e}")

        return total + self.bias

    def train(self, points: list[list[list, int]]) -> None:
        for point in points:
            print(f"processed point: {point}")
            label = self.getLabel(point)
            print(f"label: {label}")
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
