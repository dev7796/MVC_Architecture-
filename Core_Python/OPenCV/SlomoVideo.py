import cv2 as cv

slomo_frame = int(input(""))
#0 is for webcam
cap = cv.VideoCapture(r"/Users/dgs/Desktop/video.mp4")

#3 = width , 4 = height , 5 = fps
frame_width = int(cap.get(3))
print(frame_width)
frame_height = int(cap.get(4))
print(frame_height)
fps = int(cap.get(5)) #number of frames in video
print(fps)

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow('frame',frame)
        if cv.waitKey(slomo_frame) & 0xFF == ord('q'):
            break
        else:
            break

cap.release()
cap.destroyAllWindows()