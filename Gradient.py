import cv2
import numpy as np

img = cv2.imread('Hasil Smoothing.jpg',0)
kernel = np.ones((5,5),np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Hasil', gradient)
cv2.imwrite('Hasil Gradient.jpg', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
