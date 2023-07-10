import cv2
import numpy as np

img = cv2.imread("butterfly.jpg")
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Image Display", img)

img = np.array(img) 
print(np.shape(img))

print(img)
cv2.waitKey(0)