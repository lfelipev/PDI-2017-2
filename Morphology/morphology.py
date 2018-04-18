# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:16:54 2018

@author: felipe

OBS: Comentar e descomentar as funções na main() para testá-las individualmente

"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

def callBack(x):
    pass

def interactive():
    img = cv2.imread('finger.tif', 0)
    img2 = img.copy()

    cv2.namedWindow('Image')
    cv2.createTrackbar('(0)Dilatation (1)Erosion (2)Opening (3)Closing', 'Image', 1, 3, callBack)
    cv2.createTrackbar('(0) Rectangle (1) Elipse (2) Cross', 'Image', 1, 2, callBack)
    cv2.createTrackbar('wsize', 'Image', 1, 21, callBack)

    while(1):
        cv2.imshow('Image', img2)

        w = cv2.getTrackbarPos('wsize', 'Image')

        k = cv2.getTrackbarPos('(0) Rectangle (1) Elipse (2) Cross', 'Image')
        
        n = cv2.getTrackbarPos('(0)Dilatation (1)Erosion (2)Opening (3)Closing', 'Image')

        if(w == 0):
            w = 1

        if(k == 0):
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(w,w))
        elif(k == 1):
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(w,w))
        elif(k == 2):
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(w,w))

        if(n == 0):
            img2 = cv2.erode(img, kernel, iterations = 1)
        elif(n==1):
            img2 = cv2.dilate(img, kernel, iterations = 1)
        elif(n==2):
            img2 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        else:
            img2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

        k = cv2.waitKey(0) & 0xFF
        if k == 27:    
            break

    cv2.destroyAllWindows()
        
## Comentar e descomentar as funções na main() para testá-las individualmente
def main():
    interactive()
        
if __name__ == '__main__':
    main()