from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

xRange = np.linspace(-10, 10, 8)
yRange = np.linspace(-10, 10, 8)
zRange = np.linspace(-10, 10, 8)


X, Y, Z = np.meshgrid(xRange, yRange, zRange)
U = X*Y
V = X + Z
W = Y + Z

n = 0
color_array = np.sqrt(((U - n) / 2) ** 2 + ((V - n) / 2) ** 2 + ((W - n) / 2) ** 2)

ax.quiver(X, Y, Z, U, V, W, color_array)
# for ii in np.arange(0, 360, 1):
#     ax.view_init(elev=10., azim=ii)
#     plt.savefig("movie%d.png" % ii)

plt.show()
