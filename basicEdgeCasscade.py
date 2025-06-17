import cv2 as cv

cap = cv.VideoCapture(0,cv.CAP_DSHOW)

while True:
    ret,frame = cap.read()
    #blur
    blur = cv.GaussianBlur(frame,(7 ,7),cv.BORDER_DEFAULT)

    #edge casscade
    canny = cv.Canny(blur, 100,125)
    cv.imshow('canny',canny)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()