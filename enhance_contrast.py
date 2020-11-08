import cv2

img = cv2.imread('grayscale.jpg')
cv2.normalize(img, img, alpha=20, beta=200, norm_type=cv2.NORM_MINMAX)
cv2.namedWindow('Test Hasil Window', cv2.WINDOW_AUTOSIZE)
cv2.imwrite('Hasil Contrast.jpg', img)
cv2.imshow('Test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
