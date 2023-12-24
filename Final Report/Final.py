from utils import bgr2gray,imshow,cv2



img = bgr2gray("./lena.jpg")
cv2.namedWindow("lena")
### Create a track bar ###
cv2.createTrackbar("minimum", "lena", 0, 255, lambda _:_) 
cv2.createTrackbar("maximum", "lena", 0, 255, lambda _:_) 
cv2.setTrackbarPos("minimum", "lena", 0)
cv2.setTrackbarPos("maximum", "lena", 255)
# cv2.setMouseCallback('lena', show_xy)  # Set functions and windows for detecting events.

while True:
        ### Get trackbar position. ###
        min= cv2.getTrackbarPos('minimum','lena')
        max= cv2.getTrackbarPos('maximum','lena')
        ret, output = cv2.threshold(img, max, 255, cv2.THRESH_TOZERO_INV)    
        ret, output = cv2.threshold(output, min, 255, cv2.THRESH_TOZERO)    # THRESH_TOZERO/THRESH_BINARY
        cv2.imshow("lena",output)
        key = cv2.waitKey(1)
        if  key == ord('q') or key == 27:
            break

cv2.destroyAllWindows()