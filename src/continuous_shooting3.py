import cv2, glob, imageio, os, sys
import numpy as np
import matplotlib.pyplot as plt

XRANGE = 5
YRANGE = 5

AZIMUTH_START = 0
AZIMUTH_END = 360
AZIMUTH_STEP = 5

ELEVATION = 5

FOLDER_REAL = './real'
FOLDER_IMAG = './imag'
FOLDER_ABS  = './abs'

GIF_NAME = 'output.gif'

IMAGE_WIDTH = 240
IMAGE_HEIGHT = 180

FPS = 10
NR_LOOPS = 0 # eternal

def f(z):

    #return z.real
    #return np.sin(z)
    #return z.conjugate()

    return z ** 2

def make_gif(frames, filename, fps=30, loop=0):
    imageio.mimsave(filename, frames, 'GIF', fps=fps, loop=loop)

def main():

    argv = sys.argv
    argc = len(argv)

    print('%s generates a perspective views of the function' % argv[0])
    print('[usage] python %s ... function is ispecified by def f(z):' % argv[0])
    print('[usage] python %s <f(z)> ... function is specified by argument' % argv[0])

    xs = np.linspace(-XRANGE, XRANGE, 100)
    ys = np.linspace(-YRANGE, YRANGE, 100)
    
    x, y = np.meshgrid(xs, ys)
    
    z = x + 1j * y

    if argc < 2:
        w = f(z)
    else:
        w = eval(argv[1])
   
    if not os.path.exists(FOLDER_REAL):
        os.mkdir(FOLDER_REAL)

    if not os.path.exists(FOLDER_IMAG):
        os.mkdir(FOLDER_IMAG)

    if not os.path.exists(FOLDER_ABS):
        os.mkdir(FOLDER_ABS)

    #    
    # rendering u(x,y)
    #

    ax = plt.axes(projection='3d')
    
    plt.title('u(x,y)')
    
    plt.tight_layout()
    
    ax.plot_surface(x, y, w.real)
    
    elevation = ELEVATION 
    
    for i, azimuth in enumerate(range(AZIMUTH_START, AZIMUTH_END, AZIMUTH_STEP)):
    
        ax.view_init(elev=elevation, azim=azimuth)
    
        dst_path = os.path.join(FOLDER_REAL, '%04d.png' % (i+1))
        plt.savefig(dst_path)
        print('save %s' % dst_path)

    #
    # rendering v(x,y)
    #

    plt.clf()

    ax = plt.axes(projection='3d')
    
    plt.title('v(x,y)')
    
    plt.tight_layout()
    
    ax.plot_surface(x, y, w.imag)
    
    elevation = ELEVATION 
    
    for i, azimuth in enumerate(range(AZIMUTH_START, AZIMUTH_END, AZIMUTH_STEP)):
    
        ax.view_init(elev=elevation, azim=azimuth)
    
        dst_path = os.path.join(FOLDER_IMAG, '%04d.png' % (i+1))
        plt.savefig(dst_path)
        print('save %s' % dst_path)

    #
    # rendering abs(w)
    #

    plt.clf() 
    
    ax = plt.axes(projection='3d')

    plt.title('abs(w)')
    
    plt.tight_layout()
    
    ax.plot_surface(x, y, np.abs(w))
    
    elevation = ELEVATION 
    
    for i, azimuth in enumerate(range(AZIMUTH_START, AZIMUTH_END, AZIMUTH_STEP)):
    
        ax.view_init(elev=elevation, azim=azimuth)
    
        dst_path = os.path.join(FOLDER_ABS, '%04d.png' % (i+1))
        plt.savefig(dst_path)
        print('save %s' % dst_path)

    #
    # concatenate images and create gif
    #

    path_real = glob.glob(os.path.join(FOLDER_REAL, '*.png'))
    path_imag = glob.glob(os.path.join(FOLDER_IMAG, '*.png'))
    path_abs = glob.glob(os.path.join(FOLDER_ABS, '*.png'))

    nrImgs = np.min((len(path_real), len(path_imag), len(path_abs)))

    frames = []

    for i in range(nrImgs):

        print('creating gif (%d/%d)' % ((i+1), nrImgs))

        imgReal = cv2.imread(path_real[i])
        imgImag = cv2.imread(path_imag[i])
        imgAbs = cv2.imread(path_abs[i])

        imgReal = cv2.resize(imgReal,(IMAGE_WIDTH,IMAGE_HEIGHT))
        imgImag = cv2.resize(imgImag,(IMAGE_WIDTH,IMAGE_HEIGHT))
        imgAbs = cv2.resize(imgAbs,(IMAGE_WIDTH,IMAGE_HEIGHT))

        dst = np.empty((IMAGE_HEIGHT, IMAGE_WIDTH * 3, 3), np.uint8)
        
        left = 0
        right = left + IMAGE_WIDTH
        dst[:,left:right] = imgReal

        left = IMAGE_WIDTH
        right = left + IMAGE_WIDTH
        dst[:,left:right] = imgImag

        left = IMAGE_WIDTH * 2
        right = left + IMAGE_WIDTH
        dst[:,left:right] = imgAbs

        frames.append(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))

    make_gif(frames, GIF_NAME, fps = FPS, loop = NR_LOOPS)
    print('save %s' % GIF_NAME)

if __name__ == '__main__':
    main()
