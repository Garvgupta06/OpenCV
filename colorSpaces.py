import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    frame = cv.flip(frame,1)
    # BGR ro GRAYSCALE
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('cam', gray)

    #BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow('hsv',hsv)

    #BGR to L*a*b
    lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    cv.imshow('LAB',lab)

    #BGR to RGB

    rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    cv.imshow('RGB',rgb)



    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()