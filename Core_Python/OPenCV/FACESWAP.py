import cv2 as cv

img = cv.imread(r'image/img1.jpeg')
cv.imshow('img',img)
cv.waitKey(0)


# to crop the img
#crop_image = img[y:y+h, x:x+w]
face = img[100:100+120, 120:120+150]

cv.imshow('face',face)
cv.waitKey(0)

#relocating the cropped image
img[120:240, 140:290]=face
cv.imshow('face',face)
cv.waitKey(0)