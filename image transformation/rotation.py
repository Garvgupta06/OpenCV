import cv2 as cv
import numpy as np 

img = cv.imread("C:\\Users\\garvg\\OneDrive\\Desktop\\desktop apps\\kshitij certificate.JPG")
img = cv.resize(img,(1000,750),interpolation = cv.INTER_LINEAR)
def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimesnions = (width,height)

    return cv.warpAffine(img,rotMat,dimesnions)

rotate = rotate(img,-45)
cv.imshow("rotated",rotate)
cv.waitKey(0)
