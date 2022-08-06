import numpy as np
import cv2 as cv
import os
import base64

rootDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
imagesDir = os.path.join(rootDir, "images")

def saveImage(fileName :str, imageData):
    filePath = os.path.join(imagesDir, fileName)
    with open(filePath, 'wb') as f:
        f.write(imageData)

def imagePath(fileName:str):
    return os.path.join(imagesDir, fileName)

def decodeBase64(base64str: str):
    # return base64.b64decode(base64str)
   encoded_data = base64str.split(',')[1]
   nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
   img = cv.imdecode(nparr, cv.IMREAD_COLOR)
   return img

def encodeBase64(img):
    # return base64.b64encode(img)
    # Convert captured image to JPG
    retval, buffer = cv.imencode('.jpg', img)
    # Convert to base64 encoding and show start of data
    jpg_as_text = base64.b64encode(buffer)
    return jpg_as_text

def saveBase64(fileName: str, base64Str:str):
    img = decodeBase64(base64Str)
    saveImage(fileName,img)