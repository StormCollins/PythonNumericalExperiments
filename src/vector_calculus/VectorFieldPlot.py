import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.style
import matplotlib as mpl
from matplotlib.colors import Normalize
from Tableau import *
import matplotlib.cm as cm
mpl.style.use('default')


# functions
def calculate_derivatives(xy, t, coefficient_matrix):
    a = coefficient_matrix @ np.array(xy).T
    return [a[0], a[1]]


# model inputs
# matrix = np.array([[2, 1], [1, 2]]) # two positive eigenvalues
# matrix = np.array([[1, 2], [2, 1]]) # real, opposite signed eigenvalues
# matrix = np.array([[1, 2], [2, -1]]) # real, opposite signed eigenvalues
matrix = np.array([[1, 2], [-2, 3]]) # real, opposite signed eigenvalues
# Setup grid for calculation
xLow = yLow = -25
xHigh = yHigh = 25

numberOfGridPoints = 50

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


eigenvalues, eigenvectors = np.linalg.eig(matrix)

t = np.linspace(-3, 3, 50)
t = np.repeat(np.array([t]).T, 2, axis=1).T

eigenvector0_matrix = np.repeat(np.array([eigenvectors[:, 0]]).T, np.shape(t)[1], axis=1)
eigenvector1_matrix = np.repeat(np.array([eigenvectors[:, 1]]).T, np.shape(t)[1], axis=1)

c = 1

for c1 in [-c, c]:
    for c2 in [-c, c]:
        sol = c1 * eigenvector0_matrix * np.exp(eigenvalues[0] * t) \
              + c2 * eigenvector1_matrix * np.exp(eigenvalues[1] * t)
        plt.plot(sol[0, :], sol[1, :], color=tableau20[i], linestyle='dashed')
        i += 1


# y0 = [0.01, 0.01]
# t = np.linspace(0, 5, 1000)
# ys = odeint(calculate_derivatives, y0, t, args=(matrix,), color=tableau20[10])
# ax.plot(ys[:, 0], ys[:, 1], 'b-')

plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.xlim([xLow, xHigh])
plt.ylim([yLow, yHigh])
# fig.savefig('test.png')
plt.show()
