import cv2

cascade_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, 0)
    detections = cascade_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    print("detections>>>>>>>>>>>>>>>>", detections)
    if len(detections) > 0:
        print("detections[0]>>>>>>>>>>>>>>>>", detections[0])
        (x, y, w, h) = detections[0]
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # for (x,y,w,h) in detections:
    # 	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# image	Matrix of the type CV_8U containing an image where objects are detected.
# objects	Vector of rectangles where each rectangle contains the detected object, the rectangles may be partially outside the original image.
# scaleFactor	Parameter specifying how much the image size is reduced at each image scale.
# minNeighbors	Parameter specifying how many neighbors each candidate rectangle should have to retain it.
# flags	Parameter with the same meaning for an old cascade as in the function cvHaarDetectObjects. It is not used for a new cascade.
# minSize	Minimum possible object size. Objects smaller than that are ignored.
# maxSize	Maximum possible object size. Objects larger than that are ignored. If maxSize == minSize model is evaluated on single scale.
# The function is parallelized with the TBB library.
