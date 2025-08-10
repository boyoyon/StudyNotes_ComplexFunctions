import cv2
import numpy as np

SIZE = 512
SCALE = 2

ESC_KEY = 27
COLOR_Z = (255, 0, 0)
COLOR_W = (0, 0, 255)
R = 10

fRANGE = False
UBIAS = -1
USCALE = -1
VBIAS = -1
VSCALE = -1

mouse_x = -1
mouse_y = -1
ldown = False

def f(z):

    return z ** 2

def create_plane():

    plane = np.ones((SIZE, SIZE, 3),np.uint8)
    plane *= 255

    cv2.line(plane, (0, SIZE//2),(SIZE-1, SIZE//2),(0,0,0),1)
    cv2.line(plane, (SIZE//2, 0),(SIZE//2, SIZE-1),(0,0,0),1)

    return plane

def mouse_event(event, x, y, flags, param):

    global mouse_x, mouse_y, ldown

    mouse_x = x
    mouse_y = y
    
    if event == cv2.EVENT_LBUTTONDOWN:
        ldown = True

    if event == cv2.EVENT_LBUTTONUP:
        ldown = False

def Z2W(X, Y):

    global fRANGE, UBIAS, USCALE, VBIAS, VSCALE

    x = (X - SIZE/2) / (SIZE/2) * SCALE
    y = (Y - SIZE/2) / (SIZE/2) * SCALE

    if fRANGE == False:

        w0 = f(0)

        z1 = -SCALE + 1j * (-SCALE) 
        w1 = f(z1)

        z2 = SCALE + 1j * (-SCALE) 
        w2 = f(z2)

        z3 = -SCALE + 1j * SCALE 
        w3 = f(z3)

        z4 = SCALE  + 1j * SCALE 
        w4 = f(z4)

        UMIN = np.min((w0.real, w1.real, w2.real, w3.real, w4.real))
        USCALE = np.max((w0.real, w1.real, w2.real, w3.real, w4.real)) - UBIAS

        VMIN = np.min((w0.imag, w1.imag, w2.imag, w3.imag, w4.imag))
        VSCALE = np.max((w0.imag, w1.imag, w2.imag, w3.imag, w4.imag)) - VBIAS

        fRANGE = True

    z = x + 1j * y
    w = f(z)

    U = int((w.real - UBIAS) * USCALE * SIZE // 4)
    V = int((w.imag - VBIAS) * VSCALE * SIZE // 16)

    return U, V

def main():

    zplane = create_plane()
    wplane = create_plane()

    cv2.imshow('z-plane', zplane)
    cv2.imshow('w-plane', wplane)

    cv2.setMouseCallback('z-plane', mouse_event)

    prev_mouse_x = -1
    prev_mouse_y = -1
    prev_ldown = False

    fTerminal = False

    while not fTerminal:

        if ldown and (mouse_x != prev_mouse_x or mouse_y != prev_mouse_y):

            if prev_ldown == False:
                zclone = zplane.copy()
                wclone = wplane.copy()

            cv2.circle(zclone, (mouse_x, mouse_y), R, COLOR_Z, -1)
            cv2.imshow('z-plane', zclone)

            U,V = Z2W(mouse_x, mouse_y)
            print(U,V)
            cv2.circle(wclone, (U, V), R, COLOR_W, -1)
            cv2.imshow('w-plane', wclone)

            prev_mouse_x = mouse_x
            prev_mouse_y = mouse_y

        if ldown == False and prev_ldown == True:

            zclone = zplane.copy()
            cv2.imshow('z-plane', zclone)

            wclone = wplane.copy()
            cv2.imshow('w-plane', wclone)

            cv2.imshow('z-plane', zclone)

        prev_ldown = ldown

        key = cv2.waitKey(100)

        if key == ESC_KEY:
            fTerminal = True
        

if __name__ == '__main__':
    main()