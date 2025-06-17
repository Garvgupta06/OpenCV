import cv2 as cv

cap = cv.VideoCapture(0,cv.CAP_DSHOW)

while True:
    ret,frame = cap.read()
    cv.imshow('normal',frame)
    #blur
    blur = cv.GaussianBlur(frame, (7,7), cv.BORDER_DEFAULT)
    cv.imshow('webcam',blur)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break
cap.release()
cv.destroyAllWindows()
