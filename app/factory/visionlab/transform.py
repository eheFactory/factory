
import cv2 as cv
import numpy as np

class Transform:
    @classmethod
    def resize(cls, img, size=(500,500)):
        # return cv.resize(img, size, interpolation=cv.INTER_AREA)
        # return cv.resize(img, size, interpolation=cv.INTER_LINEAR_EXAC)
        return cv.resize(img, size, interpolation=cv.INTER_CUBIC)

    @classmethod
    def rescale(cls, img, scaleX=0.75, scaleY=0.75):
        width = int(img.shape[1] * scaleX)
        height = int(img.shape[1] * scaleY)
        dimensions = (width, height)
        # return cv.resize(img, dimensions, interpolation=cv.cv.INTER_LINEAR)
        # return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
        return cv.resize(img, dimensions, interpolation=cv.INTER_CUBIC)

    @classmethod
    def translate(cls, img, x, y):
        translationMatrix = np.float32([1,0,x], [0,1,y])
        dimensions = (img.shape[1], img.shape[0])
        return cv.warpAffine(img, translationMatrix, dimensions)

    @classmethod
    def rotate(cls, img, angle, rPoint=None):
        """
            rPoint : rotation point
        """
        (height, width) = img.shape[:2]
        if rPoint is None:
            rPoint = (width//2, height//2)
        rotationMatrix = cv.getRotationMatrix2D(rPoint, angle, 1.0)
        dimensions = (width, height)
        return cv.warpAffine(img, rotationMatrix, dimensions)

    @classmethod
    def flipx(cls, img):
        return cv.flip(img,0)

    @classmethod
    def flipy(cls, img):
        return cv.flip(img,1)

    @classmethod
    def flipxy(cls, img):
        return cv.flip(img,-1)
