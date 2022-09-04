import cv2

img = cv2.imread("noisy.jpg")

reduced_noise_immage = cv2.fastNlMeansDenoisingColored(img, None, 20, 10, 7, 21)

cv2.imshow('Original Immage', img)
cv2.imshow('Reduced Noise Image', reduced_noise_immage)

cv2.waitKey(0)
