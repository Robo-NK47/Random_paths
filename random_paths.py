import numpy as np
import math
import random
import matplotlib.pyplot as plt


class Path:
    def __init__(self, x_initial, y_initial):
        self.path = [[(x_initial, y_initial)]]

    def generate_line(self, p_i, f):
        (x_i, y_i) = p_i
        x_direction = random.choice([-1, 1])
        y_direction = random.choice([-1, 1])
        x_f = x_i
        while x_f == x_i:
            x_f = x_i + x_direction * random.randint(-5, 5)

        y_f = y_i + y_direction * random.randint(-5, 5)

        incline = (y_f - y_i) / (x_f - x_i)
        if f:
            x_direction = 1
            incline = 0
        line_length = math.sqrt(((x_f - x_i) ** 2) + ((y_f - y_i) ** 2))
        resolution = 100
        segments = range(int(line_length) * resolution)
        increment = line_length / resolution

        # print(f'Line , length: {int(line_length)}, increment: {increment:.4f}, incline: {incline:.4f}')

        line = []
        for i in segments:
            x = x_i + x_direction * i * increment
            y = y_i + incline * (i * increment)
            line.append((x, y))

        return line[1:]

    def generate_arc(self, p_i):
        (x_i, y_i) = p_i
        r = random.randint(1, 10)
        degrees = random.randint(1, 359)
        direction = random.choice([-1, 1])

        # print(f'Arc, R: {r}, degrees: {degrees}, direction: {direction}')

        arc = []
        for degree in range(degrees):
            x_arc = direction * r * np.cos(0.0174532925 * degree)
            y_arc = direction * r * np.sin(0.0174532925 * degree)
            x = x_i + x_arc - direction * r
            y = y_i + y_arc
            arc.append((x, y))

        return arc[1:]

    def generate_path(self):
        segments = random.randint(2, 10)
        first = True
        for _ in range(segments):
            segment_type = random.choice(['line', 'arc'])
            if segment_type == 'line' or first:
                self.path.append(self.generate_line(self.path[-1][-1], first))
                first = False

            if segment_type == 'arc':
                self.path.append(self.generate_arc(self.path[-1][-1]))


def plot_path(raw_path):
    X = []
    Y = []
    for segment in raw_path:
        for point in segment:
            X.append(point[0])
            Y.append(point[1])

    C = range(len(X))
    plt.scatter(X, Y, c=C)
    plt.show()


x_0 = 0  # input("Please enter the x_0 coordinate: ")
y_0 = 0  # input("Please enter the y_0 coordinate: ")

path = Path(x_0, y_0)
path.generate_path()
plot_path(path.path)
