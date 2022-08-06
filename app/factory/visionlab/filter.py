import cv2 as cv
import numpy as np

class Blur:
    @classmethod
    def ablur(cls, img, ksize=(3,3)):
        """averaging blur"""
        return cv.blur(img,ksize)
    
    @classmethod
    def gblur(cls, img, ksize=(3,3)):
        """gaussian blur"""
        # return cv.GaussianBlur(img, ksize, 0)
        return cv.GaussianBlur(img, ksize, cv.BORDER_DEFAULT)

    @classmethod
    def mblur(cls, img, ksize=15):
        """median blur"""
        return cv.medianBlur(img, ksize)

    @classmethod
    def blblur(cls, img, krad=10, sColor=35, sSpace=25, dst=None, bType=None):
        """ bilateral filtering
                krad : kernel radius
                sColor : sigma color 
                sSpace : sigma space
                dst : ?
                bType : ?
        """
        return cv.bilateralFilter(img, krad, sColor, sSpace, dst, bType)

    @classmethod
    def dilate(cls, img, ksize=(5,5), iters=2):
        kernel = np.ones(ksize, np.uint8)
        return cv.dilate(img, kernel, iterations=iters)

    @classmethod
    def erode(cls, img, ksize=(5,5), iters=2):
        kernel = np.ones(ksize, np.uint8)
        return cv.erode(img, kernel, iterations=iters)