import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Hasil Reduction Noise Max Filter.jpg')

median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Smoothing')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('Hasil Smoothing.jpg', median)
