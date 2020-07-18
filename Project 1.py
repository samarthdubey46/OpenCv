import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640) # WIDTH
cap.set(4,480) # HEIGHT
cap.set(10,100)

mycolours = [[5,107,0,19,255,255],
             [133,56,0,159,156,255]]
def findimg(img,mucolours):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for i in mucolours:
        lower = np.array(i[:3])
        upper = np.array(i[3:6])
        mask = cv2.inRange(hsv, lower, upper)
        x,y = getContours(mask)
        cv2.circle(img_copy,(x,y),10,(255,0,0),cv2.FILLED)
        cv2.imshow(str(i[0]),mask)
def getContours(img):
    contors,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contors:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(img_copy, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+(w//2),y

while True:
    sucess,img = cap.read()
    img_copy = img.copy()
    cv2.imshow("Video",img_copy)
    findimg(img_copy,mycolours)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break