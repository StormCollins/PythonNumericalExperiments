import numpy as np
import matplotlib.pyplot as plt

def calculateDerivatives(xy, matrix):
    x, y = xy
    return matrix*np.matrix(xy).getT()    


# Setup grid for calculation
xLow = -10
xHigh = 10
yLow = xLow
yHigh = xHigh

numberOfGridPoints = 20

xPoints = np.linspace(xLow, xHigh, numberOfGridPoints)
yPoints = np.linspace(yLow, yHigh, numberOfGridPoints)

xCoordinates, yCoordinates = np.meshgrid(xPoints, yPoints)
xPointCount, yPointCount = xCoordinates.shape

u, v = np.zeros(xCoordinates.shape), np.zeros(yCoordinates.shape)

matrix = np.matrix([[1, 2], [2, 1]])
for i in range(xPointCount):
    for j in range(yPointCount):
        x = xCoordinates[i, j]
        y = yCoordinates[i, j]
        derivatives = calculateDerivatives([x, y], matrix)
        u[i,j] = derivatives[0]
        v[i,j] = derivatives[1]
     

Q = plt.quiver(xCoordinates, yCoordinates, u, v, color='r')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim([xLow, xHigh])
plt.ylim([yLow, yHigh])
plt.show()