from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


#Create data
t = np.linspace(-np.pi, np.pi,1000)

x = np.sin(t)
y = np.cos(t)

ax = plt.axes(projection='3d')

plt.plot(t, x, [-1.5]*1000, lw=5, color='blue')
plt.plot(t, [-1.5]*1000, y, lw=5, color='green')
plt.plot([5] * 1000, x, y, lw=5, color='darkgray')
plt.plot(t, x, y, lw=5, color='darkgray')
plt.tight_layout()

elevation = 30

for i, azimuth in enumerate(range(0, 360, 5)):

    ax.view_init(elev=elevation, azim=azimuth)

    dst_path = '%04d.png' % (i+1)
    plt.savefig(dst_path)
    print('save %s' % dst_path)

