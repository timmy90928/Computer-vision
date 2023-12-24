from numpy import ndarray
import cv2
from typing import Optional
FONT:int = cv2.FONT_HERSHEY_SIMPLEX

def bgr2gray(img:ndarray) -> ndarray:
    """Convert bgr to gray and remove noise points."""
    return cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)) # BGR to gray.

def plot_from_cascade(img:ndarray,object_name:str,object:ndarray) -> Optional[tuple[ndarray,ndarray]]:
    """Read cascade data and draw pictures."""
    if len(object)==0: return None
    for (x, y, w, h) in object:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.putText(img, object_name , (x, y), FONT, .5, (0, 255, 255), 2)
    return roi_gray,roi_color

## https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_smile.xml
folder = "./HW10/Haar cascade classifier xml files"
object_cascade = cv2.CascadeClassifier(f'{folder}/haarcascade_smile.xml')
cap = cv2.VideoCapture(0)
cv2.namedWindow("cascade")

### Create a track bar ### cv2.createTrackbar('Slider name', 'window name', min, max, fn)
cv2.createTrackbar("scaleFactor", "cascade", 150, 500, lambda _:_) 
cv2.createTrackbar("minNeighbors", "cascade", 0, 20, lambda _:_) 
cv2.setTrackbarPos("scaleFactor", "cascade", 400)
cv2.setTrackbarPos("minNeighbors", "cascade", 18)

while True:
    ret, img = cap.read()
    gray = bgr2gray(img)

    ### Get trackbar position. ### cv2.setTrackbarPos('Slider name', 'window name', default)
    scaleFactor= cv2.getTrackbarPos('scaleFactor','cascade')
    minNeighbors= cv2.getTrackbarPos('minNeighbors','cascade')

    # smile = object_cascade.detectMultiScale(gray, scaleFactor/100, minNeighbors)
    smile = object_cascade.detectMultiScale(gray, 1.3, 5)
    
    plot_from_cascade(img,"smile",smile)
    cv2.imshow('cascade', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()