import cv2 as cv
import numpy as np
import glob

img_array = []
images = glob.glob(r'Users/dgs/PycharmProjects/Core_Python/Video package/*.jpg')
for filename in images:
    img = cv.imread(filename)
    img_array.append(img)

out = cv.VideoWriter('video.mp4', cv.VideoWriter_fourcc(*'MJPG'), 15, (848,480))

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

# to create video from images of different sizes from a folder
# cv.resize(images,(640,480))