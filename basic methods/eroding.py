import cv2 as cv

cap = cv.VideoCapture(0,cv.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    frame = cv.flip(frame,1)
    blur = cv.GaussianBlur(frame,(7,7),cv.BORDER_DEFAULT)
    canny = cv.Canny(blur,125,150)
    dilated = cv.dilate(canny, (7,7), iterations= 3)
    eroded = cv.erode(dilated,(7,7,), iterations = 1)

    cv.imshow('cam footage',eroded)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()