import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = "uint8")
cv.imshow("blank",blank)

# 1. paint the image a certain color 

blank[:] = 0,0,255
cv.imshow("green",blank)

# draw a rectangle

cv.rectangle(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness = -1)
cv.imshow('rectangle',blank)

# draw a circle 

cv.circle(blank,(250,250),40,(0,255,0),thickness = -1 )
cv.imshow('circle',blank)

#draw a line

cv.line(blank,(100,250),(350,390),(255,255,255),thickness = 3 )
cv.imshow('line',blank)

#write text on a image

cv.putText(blank,'hello my name is garv',(0,225), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),2)
cv.imshow('text',blank)
cv.waitKey(0)