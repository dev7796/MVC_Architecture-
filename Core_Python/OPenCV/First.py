import cv2 as cv
import datetime
import numpy as np

img = cv.imread(r'butterfly.jpeg')
#cv.imshow('img', img)
#cv.waitKey(0)
x = 0
y = 0

# cv.imshow('image',img)

# cv.waitKey(0)

# print pixel
# px=img[100,100]
# print(px) #Gives in BGR Value

# get blue value of a specific pixel
# blue = img[100,100,0] #green is 1 and red is 2
# print(blue)

# change colour of pixel
# img[100,100] = [0,0,255]
# print( img[100,100] )

# cv.imshow('image',img)
# cv.waitKey(0)

# change colour of a a particular part in the image
# for i in range(100,1000):
#    for j in range(400,1000):
#        img[i,j] = [255,255,255]
# print(img[i,j])
# cv.imshow('image',img)
# cv.waitKey(0)

# print the shape of the image in height, width and colour image indicator
print(img.shape)

# print total number of pixels
print(img.size)

# Image datatype is obtained by it
print(img.dtype)

# create a black image
# img= np.zeros((512,512,3),np.uint8)

# draw a daigonal blue line with thickness 5 px
# img=cv.line(img,(0,0),(511,511),(255,0,0),5)
# cv.imshow('image',img)
# cv.waitKey(0)


# draw a rectangle
img = cv.rectangle(img,(0, 50), (50, 50), (0, 255, 0), 5)
cv.imshow('image', img)
cv.waitKey(0)

# draw a circle centre point, raadius, color, thickness
# img=cv.circle(img,(477,63),63,(0,255,0),-1)
# cv.imshow('image',img)
# cv.waitKey(0)

# Print caption
# date1 = datetime.datetime.now()
# font=cv.FONT_HERSHEY_COMPLEX
# cv.putText(img,str(date1),(10,500),font,1,(255,255,255),2,cv.LINE_AA)
# cv.imshow('img',img)
# cv.waitKey(0)

# print current date and time
print("date is", datetime.datetime.now())

# save image
cv.imwrite(r"/Users/dgs/Desktop/Videos/mount.png", img)
