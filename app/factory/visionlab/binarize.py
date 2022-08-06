import cv2 as cv
import numpy as np

class Binarize:
    @classmethod
    def threshs(cls, img, thresh=150, maxVal=255, colored=True, inv=False):
        """ simple threshold calculator"""
        if colored:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        if inv:
            threshold, thresh = cv.threshold(img, thresh, maxVal, cv.THRESH_BINARY_INV)
        else:
            threshold, thresh = cv.threshold(img, thresh, maxVal, cv.THRESH_BINARY)
        return threshold, thresh

    @classmethod
    def thresha(cls, img, maxVal=255, blockSize=11, cVal=3, colored=True, inv=False):
        """ adaptive threshold calculator"""
        if colored:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        if inv:
            threshold, thresh = cv.adaptiveThreshold(img, maxVal, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, blockSize, cVal)
            # threshold, thresh = cv.adaptiveThreshold(gray, maxVal, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, blockSize, cVal)
        else:
            threshold, thresh = cv.adaptiveThreshold(img, maxVal, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize, cVal)
            # threshold, thresh = cv.adaptiveThreshold(gray, maxVal, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, blockSize, cVal)
        return threshold, thresh



