import cv2 as cv 

cap = cv.VideoCapture(0,cv.CAP_DSHOW)

while True:
    ret,frame = cap.read()
    frame = cv.flip(frame,1)

    cropped = frame[50:200, 200:400]
    cv.imshow('cropped',cropped)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()