import cv2 as cv
import numpy as np

class Edge:
    @classmethod
    def edgesl(cls, img, colored=True):
        """ laplacian edge detection"""
        if colored:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        lap = cv.Laplacian(img, cv.CV_64F)
        return np.uint8(np.absolute(lap))

    @classmethod
    def edgess(cls, img, colored=True):
        """ sobel edge detection"""
        if colored:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
        sobely = cv.Sobel(img, cv.CV_64F, 0, 1)
        sobel = cv.bitwise_or(sobelx, sobely)
        return sobelx, sobely, sobel

    @classmethod
    def edgesc(cls, img, tlow=50, tup=150, colored=True):
        if colored:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return cv.Canny(img, tlow, tup)
