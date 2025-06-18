import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0,cv.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    cv.imshow("cam footage", frame)
    blank = np.zeros(frame.shape[:2],dtype = 'uint8')

    b,g,r = cv.split(frame)

    blue = cv.merge([b,blank,blank])
    red = cv.merge([blank,blank,r])
    green = cv.merge([blank,g,blank])

    cv.imshow('blue',blue)
    cv.imshow('red',red)
    cv.imshow('green',green)

    #merged = cv.merge([b,g,r])
    #cv.imshow('merged',merged)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

print(frame.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cap.release()
cv.destroyAllWindows()