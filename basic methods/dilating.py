import cv2 as cv 

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    ret,frame = cap.read()
    frame = cv.flip(frame,1)
    blur = cv.GaussianBlur(frame,(7,7),cv.BORDER_DEFAULT)
    canny = cv.Canny(blur, 100,125)
    # dilating the image
    dilated = cv.dilate(blur,(7,7), iterations = 5)
    cv.imshow('cam footage 1', canny)
    cv.imshow('cam footage 2', dilated)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()