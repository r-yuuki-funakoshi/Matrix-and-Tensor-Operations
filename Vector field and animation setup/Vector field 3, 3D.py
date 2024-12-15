import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2))

# Make the direction data for the arrows
u = np.sin(x**2)
v = 0
w = 0

ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

plt.show()
