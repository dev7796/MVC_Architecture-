import cv2 as cv
import sys
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(cv.samples.findFile("mount.png"))
if img is None:
    sys.exit("Could not read the image.")
#cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("mount.jpg", img)

#You can access a pixel value by its row and column coordinates. For BGR image, it returns an array of
# Blue, Green, Red values. For grayscale image, just corresponding intensity is returned

px = img[200,200]
print("pixel value>>>>>>>>>>",px)

# accessing only blue pixel
blue = img[100,100,0]
print("Only blue pixel>>>>>>>>>>",blue)

#modify the pixel values the same way
img[100,100] = [255,255,255]
print("MOdified pixel value>>>>>>>>>>>",img[100,100])

#The above method is normally used for selecting a region of an array, say the first 5 rows and last 3 columns.
# For individual pixel access, the Numpy array methods, array.item() and array.itemset() are considered better.
# They always return a scalar, however, so if you want to access all the B,G,R values,
# you will need to call array.item() separately for each value.

# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

#The shape of an image is accessed by img.shape. It returns a tuple of the number of rows,
# columns, and channels (if the image is color):

print( img.shape )

#If an image is grayscale, the tuple returned contains only the number of rows and columns,
# so it is a good method to check whether the loaded image is grayscale or color.

#Total number of pixels is accessed by img.size:
print(img.size)

#Image datatype is obtained by `img.dtype`:
print(img.dtype)

#copying a certain part of image and pasting it into another part
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
cv.imshow("Display window",img)
k = cv.waitKey(0)

#Splitting and Merging Image Channels

b,g,r = cv.split(img)
print(b)
img = cv.merge((b,g,r))

#Image Border
BLUE = [255,0,0]
img1 = cv.imread('mount.jpg')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()

#Image Addition
#There is a difference between OpenCV addition and Numpy addition. OpenCV addition is a
# saturated operation while Numpy addition is a modulo operation.

img1 = cv.imread('mount.jpg')
img2 = cv.imread('mount.png')
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()

#Bitwise Operations

#Load two images
img1 = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo-white.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()

