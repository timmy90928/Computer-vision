#Threholding is a segmentation techique which is use to separate selected object from an image.
#Image Thresholding -  If pixel value is greater than a threshold value
#it is assigned one value (may be white),
#else it is assigned another value (may be black).
#thresholding is use to subtract image from background
#Thresholding is of  3 type -  Simple thresholding, Adaptive thresholding, Otsu’s thresholding
#image should be in gray scale
#simple thresholding(img,pixel_thresh,_max_thresh_pixel,style)
#it return 2 values - one is random data , second is threshold
import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt
def nothing(x):
    pass
cap = cv.VideoCapture(0)
cv.namedWindow('Settings')
cv.createTrackbar('Threshold', 'Settings', 0, 255, nothing)
cv.createTrackbar('Maxvalue', 'Settings', 0, 255, nothing)

while True:
    #img = cv.imread('gradient.png',0)
    img = cv.imread('lena.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, (300, 300))
    th = cv.getTrackbarPos('Threshold', 'Settings')
    maxvalue = cv.getTrackbarPos('Maxvalue', 'Settings')
    ret,thresh1 = cv.threshold(img,th,maxvalue,cv.THRESH_BINARY)
    ret,thresh2 = cv.threshold(img,th,maxvalue,cv.THRESH_BINARY_INV)
    ret,thresh3 = cv.threshold(img,th,maxvalue,cv.THRESH_TRUNC)
    ret,thresh4 = cv.threshold(img,th,maxvalue,cv.THRESH_TOZERO)
    ret,thresh5 = cv.threshold(img,th,maxvalue,cv.THRESH_TOZERO_INV)
    cv.imshow("0 - Original", img)
    cv.imshow("1 - THRESH_BINARY",thresh1)
    cv.imshow("2 -THRESH_BINARY_INV ", thresh2)
    cv.imshow("3- THRESH_TRUNC", thresh3)
    cv.imshow("4 - THRESH_TOZERO", thresh4)
    cv.imshow("5 - THRESH_TOZERO_INV", thresh5)
    key = cv.waitKey(1)
    if key == 27:
        # 27 represents esc key
        break
#cap.release()
cv.destroyAllWindows()