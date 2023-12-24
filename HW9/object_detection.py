import numpy as np
import cv2
object_cascade = cv2.CascadeClassifier('./HW9/cascade.xml') # cascade.xml was trained 14:30-15:00
# img = cv2.imread('tseng.jpg')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    object = object_cascade.detectMultiScale(gray, 1.07, 5)
    # object = object_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in object:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        font = cv2.FONT_HERSHEY_SIMPLEX
        object_name = 'WeiWen Wu'
        cv2.putText(img, object_name , (x, y), font, .5, (0, 255, 255), 2)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()