import cv2
#Load the cascade
face_cascade=cv2.CascadeClassifier('face_detector.xml')
#Start the video capturing
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#For using video file-->cap=cv2.VideoCapture('filename.mp4')
while True:
    _,img=cap.read()
    #convert to grayscale
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #detect the faces
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    #Draw the rectangle around each face
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #Display
    cv2.imshow('img',img)
#Stop if escape key is pressed
k=cv2.waitKey(30) & oxff
if k==27:
    break
#release video capture object
cap.release()