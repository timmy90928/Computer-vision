import cv2

### Image file ###
image_file='./HW3/messi.jpg'
opencv_logo='./HW3/opencv-logo.png'

### Read image ###
img = cv2.imread(image_file)
opencv_logo_img = cv2.imread(opencv_logo)
opencv_logo_img = cv2.resize(opencv_logo_img, (700, 394))

### Screenshot ###
face = img[ 15:100,290:360] # messi face
img[0:85,170:240] = face    # other face
# print(img.shape)

### Overlay ###
result = cv2.addWeighted(img, .8, opencv_logo_img, .1, 0)

### Show image ###
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()