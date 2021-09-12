# Image operations

# It has functions to read images from disk into numpy arrays, to write numpy arrays to disk as images, and to resize images.
import scipy

from imageio import *

# Read an JPEG image into a numpy array
img = imread('giraffe.jpg')
print(img.dtype, img.shape)
print("===========")

# We can tint the image by scaling each of the color channels
# by a different scalar constant. The image has shape (500, 500, 3);
# we multiply it by the array [1, 0.95, 0.9] of shape (3,);
# numpy broadcasting means that this leaves the red channel unchanged,
# and multiplies the green and blue channels by 0.95 and 0.9
# respectively.
img_tinted = img * [0, 1, 0]

print("+++++++",img_tinted)

# Resize the tinted image to be 300 by 300 pixels.
#img_tinted = imresize(img_tinted, (300, 300))

# Write the tinted image back to disk
imsave('giraffe_tinted.jpg', img_tinted)
