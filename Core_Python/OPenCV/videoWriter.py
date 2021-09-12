import cv2 as cv


#0 is for webcam
cap = cv.VideoCapture(r"/Users/dgs/Desktop/video.mp4")

#3 = width , 4 = height , 5 = fps
frame_width = int(cap.get(3))
print(frame_width)
frame_height = int(cap.get(4))
print(frame_height)
fps = int(cap.get(5)) #number of frames in video
print(fps)
fps=10

out = cv.VideoWriter('video1.mp4', cv.VideoWriter_fourcc(*'MJPG'), fps, (frame_width, frame_height))

i = 0
print(cap)
videoOn = True
while (videoOn):
    ret, frame = cap.read()
    print(ret, frame)

       #cannot write imshow and imwrite here because if it is false the last frame will give an error

    if (ret == False):
        break
    out.write(frame)
    cv.imshow('video',frame)



cap.release()
cv.destroyAllWindows()

