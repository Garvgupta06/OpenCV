import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    frame = cv.flip(frame,1)

    resized = cv.resize(frame,(750,500),interpolation = cv.INTER_CUBIC)
    cv.imshow('cam footage', resized)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()