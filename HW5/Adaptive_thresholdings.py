# Threholding is a segmentation techique which is use to separate selected object from an image.
# Image Thresholding -  If pixel value is greater than a threshold value
# it is assigned one value (may be white),
# else it is assigned another value (may be black).
# thresholding is use to subtract image from background
# Thresholding is of  3 type -  Simple thresholding, Adaptive thresholding, Otsu’s thresholding
# image should be in gray scale
# simple thresholding(img,pixel_thresh,_max_thresh_pixel,style)
# it return 2 values - one is random data , second is threshold
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
    # img = cv.imread('gradient.png',0)
    # img = cv.imread('sudoku.jpg')
    # img = cv.imread('lena_noise3.jpg')
    img = cv.imread('lena.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, (512, 512))
    img = cv.GaussianBlur(img,(5, 5), 0)
    img = cv.medianBlur(img, 5)
    th = cv.getTrackbarPos('Threshold', 'Settings')
    maxvalue = cv.getTrackbarPos('Maxvalue', 'Settings')
    ret, thresh1 = cv.threshold(img, th, maxvalue, cv.THRESH_BINARY)
    thresh2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 19, 0)
    thresh3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 19, 0)
    cv.imshow("1 - THRESH", thresh1)
    cv.imshow("2 -THRESH_MEAN_C ", thresh2)
    cv.imshow("3- THRESH_GAUSSIAN_C", thresh3)
    key = cv.waitKey(1)
    if key == 27:
        # 27 represents esc key
        break
# cap.release()
cv.destroyAllWindows()