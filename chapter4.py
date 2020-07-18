import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img.shape)
# img[100:200,:] = (255,0,21)
cv2.line(img,(0,0) , (img.shape[1],img.shape[0]),(0,255,0),4)
cv2.rectangle(img,(50,20),(250,350),(0,0,255),2)
cv2.circle(img,(400,60),39,(0,213,32),2)
cv2.putText(img,"HAGRI",(150,250),cv2.LINE_AA,2,(0,150,0),2)
cv2.imshow("Black",img)

cv2.waitKey(0)