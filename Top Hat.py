
import cv2
import numpy as np

img = cv2.imread('Hasil Smoothing.jpg',0)
kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('Hasil', tophat)
cv2.imwrite('Hasil Top Hat.jpg', tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
