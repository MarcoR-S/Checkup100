import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture("4f.jpg")

while True:
    ret, frame = video.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey,1.1,5)
    print(faces)
    
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
    
    cv2.imshow("Resultado", frame)

    if cv2.waitKey(0) == 32: #colocar em 1 para fazer videos
        break

video.release()
cv2.destroyAllWindows()
