import cv2, sys
import numpy as np

def save_ply(path_ply, img):

    H = img.shape[0]
    W = img.shape[1]

    with open(path_ply, mode='w') as f:

        line = 'ply\n'
        f.write(line)

        line = 'format ascii 1.0\n'
        f.write(line)

        line = 'element vertex %d\n' % (H * W)
        f.write(line)

        line = 'property float x\n'
        f.write(line)

        line = 'property float y\n'
        f.write(line)

        line = 'property float z\n'
        f.write(line)

        line = 'property uchar red\n'
        f.write(line)

        line = 'property uchar green\n'
        f.write(line)

        line = 'property uchar blue\n'
        f.write(line)

        line = 'end_header\n'
        f.write(line)

        for y in range(H):
            for x in range(W):

                X = (x - W//2) / W
                Y = (y - H//2) / H
                D = X ** 2 + Y ** 2 + 1

                xi = X / D
                eta = Y / D
                zeta = (X ** 2 + Y ** 2) / D 

                b = img[y][x][0]
                g = img[y][x][1]
                r = img[y][x][2]

                line = '%f %f %f %d %d %d\n' % (xi, eta, zeta, r, g, b)
                f.write(line)

def main():

    argv = sys.argv
    argc = len(argv)

    print('%s projects image into stereographics and outputs RGB ply' % argv[0])
    print('[usage] python %s <image file>' % argv[0])

    if argc < 2:
        quit()

    img = cv2.imread(argv[1])

    save_ply('stereographics.ply', img)
    print('save stereographics.ply')

if __name__ == '__main__':
    main()