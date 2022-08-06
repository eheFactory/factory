import cv2 as cv
import numpy as np

class Geometric:
    @classmethod
    def blank1(cls, width, height):
        """
        Returns 1 channel blank image
        """
        return np.zeros((width, height, 1), dtype="uint8")

    @classmethod
    def blank3(cls, width, height):
        """
        Returns 3 channel blank image

        blankimg = blank3(500,500)
        blankimg[:] = 0,0,255
        blankimg[200:300, 300:400] = 0,0,255
        """
        return np.zeros((width, height, 3), dtype="uint8")

    @classmethod
    def line(cls, img, start=(0,0), end=(0,0), color=(255,255,255), thick=2):
        return cv.line(img, start, end, color, thickness=thick)

    @classmethod
    def rectangle(cls, img, start=(0,0), end=(50,50), color=(0,255,0), thick=2):
        return cv.rectangle(img, start, end, color, thickness=thick)
    
    @classmethod
    def circle(cls, img, center=(50,50), radius=10, color=(0,0,255), thick=2):
        return cv.circle(img, center, radius, color, thickness=thick)
    
    @classmethod
    def text(cls, img, text="enivicivokki", org=(10,10), font=cv.FONT_HERSHEY_SIMPLEX, fscale=1, color=(255, 0, 0), thick=2):
        return cv.putText(img, text, org, font, fscale, color, cv.cv2.LINE_AA)