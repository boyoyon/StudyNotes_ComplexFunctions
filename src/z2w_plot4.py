import os, sys
import numpy as np
import matplotlib.pyplot as plt

def f(z):

    return z ** 2


XRANGE = 5
YRANGE = 5

argv = sys.argv

x = np.linspace(-XRANGE, XRANGE, 100)
y = np.linspace(-YRANGE, YRANGE, 100)
y1 = -y - 4
y2 = -y - 2
y3 = -y
y4 = -y + 2
y5 = -y + 4


z1 = x + 1j * y1
w1 = f(z1)

z2 = x + 1j * y2
w2 = f(z2)

z3 = x + 1j * y3
w3 = f(z3)

z4 = x + 1j * y4
w4 = f(z4)

z5 = x + 1j * y5
w5 = f(z5)


# z平面の描画
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(x,y1)
plt.scatter(x,y2)
plt.scatter(x,y3)
plt.scatter(x,y4)
plt.scatter(x,y5)

plt.title("z-plane")

# w平面の描画
plt.subplot(1, 2, 2)

plt.scatter(w1.real, w1.imag)
plt.scatter(w2.real, w2.imag)
plt.scatter(w3.real, w3.imag)
plt.scatter(w4.real, w4.imag)
plt.scatter(w5.real, w5.imag)

plt.title("w-plane")

plt.tight_layout()

base = os.path.basename(argv[0])
filename = os.path.splitext(base)[0]
dst_path = '%s.png' % filename
plt.savefig(dst_path)
print('save %s' % dst_path)

plt.show()