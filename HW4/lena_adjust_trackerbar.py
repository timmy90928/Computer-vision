import cv2 as cv
import numpy as np
alpha = 0.3
beta = 80
img_path = "lena.jpg"
img = cv.imread(img_path)
img2 = cv.imread(img_path)
def updateAlpha(x):
    global alpha, img, img2
    alpha = cv.getTrackbarPos('Alpha', 'image')
    alpha = alpha *0.01
    img = np.uint8(np.clip((alpha * img2 + beta), 0, 255))
def updateBeta(x):
    global beta, img, img2
    beta = cv.getTrackbarPos('Beta', 'image')
    img = np.uint8(np.clip((alpha * img2 + beta), 0, 255))

cv.namedWindow('image')
cv.createTrackbar('Alpha', 'image', 0, 300, updateAlpha)
cv.createTrackbar('Beta', 'image', 0, 255, updateBeta)

cv.setTrackbarPos('Alpha', 'image', 100)
cv.setTrackbarPos('Beta', 'image', 10)

while(True):
    cv.imshow('image', img)
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()