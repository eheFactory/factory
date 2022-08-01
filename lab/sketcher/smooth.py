import os

import numpy as np
import cv2

imagesDir = os.path.join(os.path.dirname(__file__), "../images")
def imagePath(fileName: str):
    return os.path.join(imagesDir, fileName)


# Parameters 
blur = 21 # affects the “smoothness” of the dividing line between the background and foreground
canny_low = 15 # the minimum intensity value along which edges will be drawn
canny_high = 150 # the maximum intensity value along which edges will be drawn
min_area = 0.0005 # the minimum area a contour in the foreground may occupy. Taken as a value between 0 and 1
max_area = 0.95 # the maximum area a contour in the foreground may occupy. Taken as a value between 0 and 1
dilate_iter = 10 # the number of iterations of dilation will take place on the mask
erode_iter = 10 # the number of iterations of erosion will take place on the mask
mask_color = (0.0,0.0,0.0) # the color of the background once it is removed

  
# define a video capture object
vid = cv2.VideoCapture(0)
  
def edgeDetector1(img):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)[:, :, 2]
    kern_size = 11
    gray_blurred = cv2.medianBlur(gray, kern_size)
    threshold_lower = 30
    threshold_upper = 220
    edged = cv2.Canny(gray_blurred, threshold_lower, threshold_upper)
    return edged

def edgeDetector2(img):
    # convert the image to grayscale format
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply binary thresholding
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
                                        
    # draw contours on the original image
    img_copy = img.copy()
    cv2.drawContours(image=img_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    return img_copy
                

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    # img = edgeDetector1(frame)
    img = edgeDetector2(frame)
    cv2.imshow('frame', img)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()