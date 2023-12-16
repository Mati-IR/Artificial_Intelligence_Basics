import random
from point import Point
from point_generator import PointGenerator
from perceptron import Perceptron
import matplotlib.pyplot as plt
import mplcursors

def main():
    generator = PointGenerator(lambda x, y: 1 if y > x else -1)
    training_set = generator.generate(100)
    verification_set = generator.generate(100)
    

    perceptron = Perceptron()
    perceptron.train_classification(training_set)
    print(perceptron.verify(verification_set))
    print(perceptron)

    # Plot the points with tooltips
    fig, ax = plt.subplots()
    for point in training_set:
        marker = 'o' if point.get_label == 1 else 'x'
        color = 'red' if point.get_label() == 1 else 'blue'
        ax.scatter(point.get_coordinates()[0], point.get_coordinates()[1], marker=marker, color=color)

    cursor = mplcursors.cursor(hover=True)
    # plot y=x
    plt.plot([-100, 100], [-100, 100], color="green")
    plt.show()


if __name__ == "__main__":
    main()




