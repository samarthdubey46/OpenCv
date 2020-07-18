import cv2
img = cv2.imread("photo.jpg")
# cv2.imshow("Output",img)
# # cv2.waitKey(0)
# cap = cv2.VideoCapture("video.mp4")
cap = cv2.VideoCapture(0)
cap.set(3,640) # WIDTH
cap.set(4,480) # HEIGHT
cap.set(10,100)
while True:
    sucess,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break