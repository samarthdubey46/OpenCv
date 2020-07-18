import cv2
import  numpy as np
img = cv2.imread("cards.jpg")
width,height = 250,350
pts1 = np.float32([[99,46],[185,24],[125,188],[213,170]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
image = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Warp",image)
cv2.waitKey(0)