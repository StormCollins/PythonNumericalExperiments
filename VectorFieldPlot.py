import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.style
import matplotlib as mpl
from Tableau import *
mpl.style.use('default')


# functions
def calculate_derivatives(xy, t, coefficient_matrix):
    a = coefficient_matrix @ np.array(xy).T
    return [a[0], a[1]]


# model inputs
matrix = np.array([[1, 2], [2, 1]])

# Setup grid for calculation
xLow = yLow = -10
xHigh = yHigh = 10

numberOfGridPoints = 15

xPoints = np.linspace(xLow, xHigh, numberOfGridPoints)
yPoints = np.linspace(yLow, yHigh, numberOfGridPoints)

xCoordinates, yCoordinates = np.meshgrid(xPoints, yPoints)
xPointCount, yPointCount = xCoordinates.shape

u, v = np.zeros(xCoordinates.shape), np.zeros(yCoordinates.shape)

# can this region be simplified???
for i in range(xPointCount):
    for j in range(yPointCount):
        x = xCoordinates[i, j]
        y = yCoordinates[i, j]
        derivatives = calculate_derivatives([x, y], 0, matrix)
        u[i, j] = derivatives[0]
        v[i, j] = derivatives[1]

fig, ax = plt.subplots(figsize=(7, 7))

n = 0
color_array = np.sqrt(((v - n) / 2) ** 2 + ((u - n) / 2) ** 2)
Q = ax.quiver(xCoordinates, yCoordinates, u, v, color_array, alpha=0.8)

# some explicit solutions
i = 0
t = np.linspace(-2, 0.8, 50)
for c1 in [-1, 1]:
    for c2 in [-1, 1]:
        xValues = -c1 * np.exp(-t) + c2 * np.exp(3 * t)
        yValues = c1 * np.exp(-t) + c2 * np.exp(3 * t)
        plt.plot(xValues, yValues, color=tableau20[i], linestyle='dashed')
        i += 1

t = np.linspace(-1.2, 0.4, 50)
for c1 in [-3, 3]:
    for c2 in [-3, 3]:
        xValues = -c1 * np.exp(-t) + c2 * np.exp(3 * t)
        yValues = c1 * np.exp(-t) + c2 * np.exp(3 * t)
        plt.plot(xValues, yValues, color=tableau20[i], linestyle='dashed')
        i += 1

y0 = [-9, 10]
t = np.linspace(-1, 0, 10)
ys = odeint(calculate_derivatives, y0, t, args=(matrix,))
ax.plot(ys[:, 0], ys[:, 1], 'b-')

plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.xlim([xLow, xHigh])
plt.ylim([yLow, yHigh])
# fig.savefig('test.png')
plt.show()
