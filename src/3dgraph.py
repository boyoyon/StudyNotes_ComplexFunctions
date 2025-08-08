import numpy as np
import matplotlib.pyplot as plt

XRANGE = 5
YRANGE = 5

xs = np.linspace(-XRANGE, XRANGE, 100)
ys = np.linspace(-YRANGE, YRANGE, 100)

x, y = np.meshgrid(xs, ys)

u = x ** 2 - y ** 2

ax = plt.axes(projection='3d')
ax.plot_surface(x, y, u)
plt.show()
