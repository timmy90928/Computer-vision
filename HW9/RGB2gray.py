import cv2

for n in range(0,100):
    img = cv2.imread(f'./picture/n/{n}.jpg')
    # cv2.imshow('img',img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    cv2.imwrite('./picture/gray'+str(n)+'.jpg',gray)