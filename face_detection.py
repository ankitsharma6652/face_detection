import cv2
#Load the cascade
face_cascade=cv2.CascadeClassifier('face_detector.xml')
#Read imageFile
img=cv2.imread('elonmusk.jpg')
#convert to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Detect the faces
faces=face_cascade.detectMultiScale(gray,1.1,4)
#Draw Rectange around eacg face
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#show the image
cv2.imshow('img', img)
cv2.waitKey()