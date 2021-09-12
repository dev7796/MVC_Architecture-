#Changing Color-space

import cv2 as cv
import numpy as np
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

#HSV or Hue Saturation Value is used to separate image luminance from color information

cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

#Scalling : Scaling is just resizing of the image. OpenCV comes with a function cv.resize() for this purpose.
# The size of the image can be specified manually, or you can specify the scaling factor.
# Different interpolation methods are used. Preferable interpolation methods are cv.INTER_AREA
# for shrinking and cv.INTER_CUBIC (slow) & cv.INTER_LINEAR for zooming. By default,
# the interpolation method cv.INTER_LINEAR is used for all resizing purposes.
# You can resize an input image with either of following methods:

img = cv.imread('image/img1.jpeg')
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
