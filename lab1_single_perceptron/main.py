import random
from point import Point
from point_generator import PointGenerator
from perceptron import Perceptron


def main():
    generator = PointGenerator(lambda x, y: 1 if y > x else -1)
    training_set = generator.generate(100)
    verification_set = generator.generate(100)

    perceptron = Perceptron()
    perceptron.train(training_set)
    print(perceptron.verify(verification_set))
    print(perceptron)


if __name__ == "__main__":
    main()




