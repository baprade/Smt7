import cv2

img = cv2.imread('1.jpg')
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale.jpg', grayImage)
cv2.imshow('Tampilkan Gambar', grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
