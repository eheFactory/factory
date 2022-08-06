
import cv2 as cv
import numpy as np

"""
imgPath = "xxx"
img = cv.imread(imgPath)

vidPath = "xxx"
vidCapture = cv.VideoCapture(vidPath)
while True:
    _, frame = vidCapture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
vidVapture.release()
cv.destroyAllWindows()
"""


def gray(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def ghist(img, colored=True):
    """ gray histogram calculator"""
    if colored:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    grayHist = cv.calcHist([gray], [0], None, [256], [0,256])
    # import matplotlib.pyplot as plt
    # plt.figure()
    # plt.title('Grayscale Histogram')
    # plt.xlabel('Bins')
    # plt.ylabel(' # of pixels')
    # plt.plot(grayHist)
    # plt.xlim([0,256])
    # plt.show()
    return grayHist

def chist(img):
    """colored histogram calculator"""
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv.calcHist([img], [i], None, [256], [0,256])
        # import matplotlib.pyplot as plt
        # plt.figure()
        # plt.title('Colour Histogram')
        # plt.xlabel('Bins')
        # plt.ylabel(' # of pixels')
        # plt.plot(grayHist)
        # plt.xlim([0,256])
        # plt.show()
    return hist

class Bitwise:
    """
        blank = np.zeros((400,400), dtype='uint8')
        rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
        circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
        
        # bitwiseAnd : intersecting regions
        bitwiseAnd = cv.bitwise_and(rectangle, circle)
    
        # bitwiseOr : non-intersecting and intersecting regions
        bitwiseOr = cv.bitwise_or(rectangle, circle)

        # bitwiseXor : non-intersecting regions
        bitwiseCor = cv.bitwise_xor(rectangle, circle)

        # bitwiseNot : 
        bitwiseNot = cv.bitwise_not(rectangle, circle)
    """
    class Mask:
        """
            img = cv.imread('cats.png')
            blank = np.zeros(img.shape([:2]), dtype='uint8')
            mask = cv.circle(blank, img.shape([1]//2), img.shape([0]//2), 100, 255, -1)
            masked = cv.bitwise_and(img, img, mask=mask)
        """


def findContourBlured(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
    edges = cv.Canny(img, 125, 175)
    contours, hierarchies = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # contours, hierarchies = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    return contours, hierarchies

def findContourThres(img):
    pass