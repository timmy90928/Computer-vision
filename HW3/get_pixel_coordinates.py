import cv2
image_file='./HW3/messi.jpg'
# def click_event(event, x, y, ):
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        xy = str(x) + ', ' + str(y)
        cv2.putText(img, xy, (x, y), font, .5, (255, 255, 0), 1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        bgr = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, bgr, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)


img = cv2.imread(image_file)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()