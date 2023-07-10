import cv2
import os

path = "PRO_1-1_C105_ImagensProjeto-main/"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    print(name)
    print(ext)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)
        images.append(file_name)

count = len(images)
frame = cv2.imread(images[0])
h,w,l = frame.shape
size = (w,h)
print(size)
out = cv2.VideoWriter('projeto105.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for x in range(0, count-1):
    frame = cv2.imread(images[x])
    out.write(frame)
