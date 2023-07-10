import cv2
import numpy as np

black = np.zeros([600,600])
black[150:450, 150:450] = 40
print(black)
cv2.imshow("Preto", black)
cv2.waitKey(0)

