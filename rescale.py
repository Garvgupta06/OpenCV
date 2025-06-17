import cv2 as cv 
def rescaleFrame(frame, scale = 0.4):
    height = int(frame.shape[0] *scale)
    width = int(frame.shape[1] *scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

cap = cv.VideoCapture(0,cv.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    frame = rescaleFrame(frame)
    cv.imshow("webcam feed", frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()



