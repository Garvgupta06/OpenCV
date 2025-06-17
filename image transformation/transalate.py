import cv2 as cv 
import numpy as np

img = cv.imread("C:\\Users\\garvg\\OneDrive\\Desktop\\desktop apps\\kshitij certificate.JPG")
img = cv.resize(img,(1000,750))

def transalate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

'''
note :
    -x --> left
    +x --> right 
    -y --> up
    +y --> down 
'''

transalated = transalate(img,-100,-100)
cv.imshow('transalted',transalated)
cv.waitKey(0)