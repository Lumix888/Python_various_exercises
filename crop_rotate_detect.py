import cv2

img = cv2.imread('sun.jpg')

print(img.shape[0:2])
startRow = int(177*.15)
startCol = int(284*.15)
endRow = int(177*.85)
endCol = int(284*.85)
croppedImmage = img[startRow:endRow, startCol:endCol]

cv2.imshow('Original Immage', img)
cv2.imshow('Cropped Image', croppedImmage)

cv2.waitKey(0)

print(croppedImmage.shape[0:2])
rotationMatrix = cv2.getRotationMatrix2D((242/2, 124/2), 60, 1)
rotatedImage = cv2.warpAffine(croppedImmage, rotationMatrix, (284,177))

cv2.imshow('Rotated Image', rotatedImage)

cv2.waitKey(0)

edge_img = cv2.Canny(img,100,200)

cv2.imshow('Detected Edges', edge_img)

cv2.waitKey(0)
