import numpy as np
import matplotlib.pyplot as plt

XRANGE = 5
YRANGE = 5

xs = np.linspace(-XRANGE, XRANGE, 100)
ys = np.linspace(-YRANGE, YRANGE, 100)

x, y = np.meshgrid(xs, ys)

z = x + 1j * y
w = z ** 2

ax = plt.axes(projection='3d')

ax.plot_surface(x, y, w.real)
#ax.plot_surface(x, y, w.imag)

plt.show()
