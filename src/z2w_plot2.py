import os, sys
import numpy as np
import matplotlib.pyplot as plt

def f(z):

    return z ** 2


XRANGE = 5
YRANGE = 5

argv = sys.argv

y = np.linspace(-YRANGE, YRANGE, 100)
x1 = np.array([-4]*100)
x2 = np.array([-2]*100)
x3 = np.array([ 0]*100)
x4 = np.array([ 2]*100)
x5 = np.array([ 4]*100)

z1 = x1 + 1j * y
w1 = f(z1)

z2 = x2 + 1j * y
w2 = f(z2)

z3 = x3 + 1j * y
w3 = f(z3)

z4 = x4 + 1j * y
w4 = f(z4)

z5 = x5 + 1j * y
w5 = f(z5)


# z平面の描画
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(x1,y)
plt.scatter(x2,y)
plt.scatter(x3,y)
plt.scatter(x4,y)
plt.scatter(x5,y)

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