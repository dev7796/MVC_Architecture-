import cv2
import numpy as np

######################################## READING IMAGE,VIDEOS & WEB CAM ########################################

############## Reading Image
# img = cv2.imread('Resources/butterfly.jpg')
# cv2.imshow('Butterfly Image', img)
# cv2.waitKey(0)


############## Reading Video
# vdo = cv2.VideoCapture('Resources/Earth.mp4')
# while True:
#     success, img = vdo.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

############## Reading Web Cam
# cam = cv2.VideoCapture(0)  # 0 for default web cam or 1,2,3 id for any other input device
# cam.set(3,640)             # id 3 is for width
# cam.set(4,480)             # id 4 is for height
# cam.set(10,100)            # id 10 is for brightness
# while True:
#     success, img = cam.read()
#     cv2.imshow('Web Cam', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# ################################################ BASIC FUNCTIONS ###################################################
# #
# img = cv2.imread('Resources/butterfly.jpg')
# imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting to grey scale
# cv2.imshow('Grey Image', imgGrey)
# cv2.waitKey(0)
#
# imgBlur = cv2.GaussianBlur(img, (7, 7), 100)  # Bluring Image
# cv2.imshow('Blur Image', imgBlur)
# cv2.waitKey(0)
#
# imgCanny = cv2.Canny(img, 200, 200)  # Detecting Edges
# cv2.imshow('Canny Image', imgCanny)
# cv2.waitKey(0)
#
# kernel = np.ones((5, 5), np.uint8)
# imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # increasing thickness of edges
# cv2.imshow('Dialation Image', imgDialation)
# cv2.waitKey(0)
#
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)    # opposite of dialation
# cv2.imshow('Eroded Image',imgEroded)
# cv2.waitKey(0)


######################################### OpenCV Convention/ resizing and croping images ###################################################
#
# img = cv2.imread('Resources/butterfly.jpg')
# print('Size of Original Image-->',img.shape)                      # will return (height, width, No. of channels(r/g/b))
# cv2.imshow('Butterfly', img)
# cv2.waitKey(0)
#
# imgResized = cv2.resize(img,(200,600)) # pass (width,height)
# cv2.imshow('Butterfly Resized', imgResized)
# print('Size of Resized Image-->',imgResized.shape)
# cv2.waitKey(0)
#
# imgCropped = img[0:200,150:300]
# cv2.imshow('Cropped Image', imgCropped)
# print('Size of Cropped Image-->',imgCropped.shape)
# cv2.waitKey(0)

######################################### Shapes And Texts ###################################################
#
# img = np.zeros((512, 512, 3), np.uint8)  # black image of 512/512 pixels
# # img[:] = 255, 0, 0  # Blue image(blue,green,red)
#
# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0),
#          3)  # arguments(image, starting_point(Width, Height), ending_point(Width,Height),color(B/G/R),thickness)
# cv2.imshow('Lined Image', img)
# cv2.waitKey(0)
#
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255),
#               3)  # arguments(image, starting_point(Width, Height), ending_point(Width,Height),color(B/G/R),thickness)
# cv2.imshow('Rectangle Image', img)
# cv2.waitKey(0)
#
# cv2.circle(img, (300, 400), 50, (255, 255, 0),
#            5)  # arguments(image, starting_point(Width, Height), radius, color(B/G/R),thickness)
# cv2.imshow('circled Image', img)
# cv2.waitKey(0)
#
# cv2.putText(img, " Hello ", (200, 500), cv2.FONT_ITALIC, 1, (0, 255, 255),
#             6)  # arguments(image,text, starting point, font_style,scale, color(B/G/R),thickness)
# cv2.imshow('Text on Image', img)  # scale is size of text
# cv2.waitKey(0)

######################################### WARP PRESPECTIVE ###################################################

# img = cv2.imread('Resources/cards.jpg')
# cv2.imshow('Cards', img)
# cv2.waitKey(0)
#
# width, height = 250, 350
# pts1 = np.float32([[437, 97], [581, 152], [503, 350], [356, 290]])
# pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
#
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgPerspective = cv2.warpPerspective(img, matrix, (width, height))
# cv2.imshow('Perspective Image', imgPerspective)
# cv2.waitKey(0)


######################################### Joining Images ###################################################

# imgButterfly = cv2.imread('Resources/butterfly.jpg')
# imgCards = cv2.imread('Resources/cards.jpg')
# # print(imgButterfly.shape, imgCards.shape)
#
# imgHorizontal = np.hstack((cv2.resize(imgButterfly,(493,356)), cv2.resize(imgCards,(493,356))))
# imgVertical = np.vstack((cv2.resize(imgButterfly,(493,356)), cv2.resize(imgCards,(493,356))))
#
# cv2.imshow('Horizontal Stacked Image', imgHorizontal)
# cv2.imshow('vertical Stacked Image', imgVertical)
#
# cv2.waitKey(0)


######################################### Color Detection ###################################################

# pathButterfly = "Resources/butterfly.jpg"
# imgButterfly = cv2.imread(pathButterfly)
#
# cv2.imshow('Butterfly', imgButterfly)
# cv2.waitKey(0)
#
# imgHSV = cv2.cvtColor(imgButterfly, cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV Image', imgHSV)
# cv2.waitKey(0)
