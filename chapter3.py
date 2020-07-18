import  cv2
img = cv2.imread("lambo.jpg")
imgresize = cv2.resize(img,(200,200))
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgcropped = img[0:200,200:500]

cv2.imshow("Lambo",img)
cv2.imshow("Lambo resize",imgresize)
cv2.imshow("Lambo Gray",imggray)
cv2.imshow("Lambo cropped",imgcropped)
cv2.waitKey(0)