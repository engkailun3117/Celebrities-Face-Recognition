import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('E:\\python\\opencv\\haar_face.xml')

people = ['anne hathaway', 'christian bale', 'jennifer connelly', 'obama', 'the rock']

##features = np.load('features.npy')
##labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('E:\\python\\opencv\\face_trained.yml')

img = cv.imread('E:\\python\\opencv\\people pic validation\\christian bale\\bale4.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)


# Detect the face in the image

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0,
               (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)