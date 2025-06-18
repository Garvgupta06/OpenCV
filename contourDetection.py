import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0,cv.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    frame = cv.flip(frame,1)
    cv.imshow('camera', frame)
    blank = np.zeros(frame.shape, dtype = 'uint8')
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_CONSTANT )
    canny = cv.Canny(blur,100,125)

    contour, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(blank, contour, -1 , (0,255,0), 1)
    cv.imshow('webcam with contour',blank)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
cap.release()
cv.destroyAllWindows()