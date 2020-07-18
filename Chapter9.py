import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,490)
cap.set(10,100)
# img = cv2.imread("faceimg.jpg")

while True:
    sucess,img = cap.read()

    face = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
    eye = cv2.CascadeClassifier("haarcascades/haarcascade_eye_tree_eyeglasses.xml")

    print(face)
    imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(imggray,1.1,4)
    eyes = eye.detectMultiScale(imggray,1.1,4)
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("result",img)
    if len(eyes) == 0:
        print("No Eyes")
    else:
        print("Eyes")
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break