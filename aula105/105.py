import cv2
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    (b, g, r) = frame[200, 200]
    frame[196:204, 196:204] = (20,40,255)
    frame[10:90, 10:90] = (0, g, 0)

    cv2.imshow("Resultado", frame)

    if cv2.waitKey(1) == 32:
        break

video.release()
cv2.destroyAllWindows()