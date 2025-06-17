import cv2 as cv

cap = cv.VideoCapture(0,cv.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    #grayscale image
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('grayscale cam', frame)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()