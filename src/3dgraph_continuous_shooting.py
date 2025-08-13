import numpy as np
import matplotlib.pyplot as plt

XRANGE = 5
YRANGE = 5

xs = np.linspace(-XRANGE, XRANGE, 100)
ys = np.linspace(-YRANGE, YRANGE, 100)

x, y = np.meshgrid(xs, ys)

z = x + 1j * y
#w = z ** 2
w = np.sin(z)

ax = plt.axes(projection='3d')

ax.plot_surface(x, y, w.real)

elevation = 30

for i, azimuth in enumerate(range(0, 360, 5)):

    ax.view_init(elev=elevation, azim=azimuth)

    dst_path = '%04d.png' % (i+1)
    plt.savefig(dst_path)

