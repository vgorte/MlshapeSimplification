import sys
import numpy as np
import math
import matplotlib.pyplot as plt


def randomNumber(type):
    return {
        'standard-normal': np.random.standard_normal(3),
        'triangular': np.random.triangular(-2.1, 2.3, 2.5)
    }.get(type, np.random.uniform(-2.1, 2.5))


def randomRadian():
    deg = np.random.uniform(0, 360, 1)
    radian = deg * (math.pi / 180)
    return radian


def findRotationCenter(x, y):
    x_sorted = sorted(x)
    y_sorted = sorted(y)
    centerX = np.int(x_sorted[-1]) - np.int(x_sorted[0])
    centerY = np.int(y_sorted[-1]) - np.int(y_sorted[0])
    return centerX, centerY


def rotate(x, y, xo, yo, theta):  # rotate x,y around xo,yo by theta (rad)
    xr, yr = [], []

    for i in range(len(x)):
        xr.append(math.cos(theta) * (x[i] - xo) - math.sin(theta) * (y[i] - yo) + xo)
        yr.append(math.sin(theta) * (x[i] - xo) + math.cos(theta) * (y[i] - yo) + yo)
    return xr, yr


def extractAlteredCoordinates(shape, distType):
    x, y = [], []
    for v in shape:
        x.append(np.int(v[0]) + randomNumber(distType))
        y.append(np.int(v[1]) + randomNumber(distType))

    # join last point with the first point
    x[len(x) - 1] = x[0]
    y[len(y) - 1] = y[0]
    return x, y


def main(shapeFilePath, distType):
    shape = np.genfromtxt(shapeFilePath, delimiter=',')

    x, y = extractAlteredCoordinates(shape, distType)
    xo, yo = findRotationCenter(x, y)
    rad = randomRadian()
    xr, yr = rotate(x, y, xo, yo, rad)

    plt.plot(xr, yr)
    plt.axis('off')
    plt.savefig('filename.png', bbox_inches='tight')
    plt.show()


if (__name__ == "__main__"):
    shapeFilePath = sys.argv[1]
    distType = str(sys.argv[2])
    main(shapeFilePath, distType)
