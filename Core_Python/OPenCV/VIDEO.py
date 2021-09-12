import cv2 as cv
import matplotlib.pyplot as p

#0 is for webcam
cap = cv.VideoCapture(r"/Users/dgs/Desktop/video.mp4")
i = 0
print(cap)
videoOn = True
while (videoOn):
       ret, frame = cap.read()
       print(ret, frame)

       #cannot write imshow and imwrite here because if it is false the last frame will give an error

       if (ret == False):
        break
        cv.imshow('video',frame)
       p.show()

       #to save each individual frame
       cv.imwrite(r'/Users/dgs/PycharmProjects/Core_Python/Video package/video frames'+str(i)+'.jpg',frame)

       #To crop the image
       #CropImage = frame[10:30 , 10:50]

       #to save cropped image [y:y+h , x:x+h]
      # cv.imwrite(r'/Users/dgs/PycharmProjects/Core_Python/Video package/CropImage' + str(i) + '.jpg', frame)

      # frame = cv.rectangle(frame,(100,300),(300,100),(0,255,0),3)
       cv.imshow("video",frame)
       i+= 1
       if cv.waitKey(1) & 0xFF == ord('q'):
           break


cap.release()
cv.destroyAllWindows()
