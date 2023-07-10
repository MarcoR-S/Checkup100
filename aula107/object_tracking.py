import cv2
import math

p1 = 530
p2 = 300

xs = []
ys = []

video = cv2.VideoCapture("bb3.mp4")
tracker = cv2.TrackerCSRT_create()
ret, frame = video.read()
box = cv2.selectROI("Rastreando", frame, False)
tracker.init(frame,box)
print(box)


def draw_box(image, roi):
    x,y,w,h = int(roi[0]), int(roi[1]), int(roi[2]), int(roi[3])
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 3,1)
    cv2.putText(image, "Rastreando", (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

def goal_track(image,roi):
    x,y,w,h = int(roi[0]), int(roi[1]), int(roi[2]), int(roi[3])
    c1 = x+w/2
    c2 = y+h/2
    cv2.circle(image, (c1,c2), 2, (0,0,0),5)
    cv2.circle(image, (p1,p2), 2, (0,0,0),5)
    dist = math.sqrt(((c1-p1)**2)+((c2-p2)**2))
    if dist <= 20:
        cv2.putText(image, "Cesta", (300,90 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    xs.append(c1)
    ys.append(c2)
    for i in range(0,len(xs)-1):
        cv2.circle(image, (xs[i],ys[i]), 2, (0,0,255),5)


while True:
    ret,img = video.read()
    success, box = tracker.update(img)
    draw_box(img,box)
    goal_track(img,box)
    if cv2.waitKey(1) == 32:
        break

video.release()
cv2.destroyAllWindows()

          

