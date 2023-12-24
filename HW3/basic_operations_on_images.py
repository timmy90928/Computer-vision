import numpy as np
import cv2
image_file='./HW3/messi5.jpg'
img = cv2.imread(image_file)
# 342 rows x 548 column
cv2.imshow('Origal image', img)
img2 = cv2.imread('./HW3/opencv-logo.png')
cv2.imshow('Origal opencv-logo.png', img2)
img2 = cv2.resize(img2, (548, 342))
# resize opencv-logo.png as 342 rows x 548 column
# cv2.resize(image, (width, height))
# cv2.resize - resize the image
# save resized img as messi512.jpg
print(img.shape)
# img.shape returns a tuple of number of rows, columns, and channels
print(img.size)
# img.size returns Total number of pixels is accessed
print(img.dtype)
# img.dtype returns Image datatype is obtained
b, g, r = cv2.split(img)
# cv2.split(img) - output vector of arrays; the arrays themselves are reallocated, if needed
img = cv2.merge((b, g, r))
# cv2.merge((b,g,r)) - The number of channels will be the total number of channels in the matrix array.
img = cv2.imread(image_file) # 342 行 x 548 列 cv2.imshow（'Origal image'， img） img2 = cv2.imread（'opencv-logo.png'） cv2.imshow（'Origal opencv-logo.png'， img2） img2 = cv2.resize（img2， （548， 342）） # 調整 opencv-logo.png 為 342 行 x 548 列 # cv2.resize（圖像， （寬度， 高度）） # cv2.resize - 調整圖像大小 # 將調整大小的 img 保存為 messi512.jpg print（img.shape） # img.shape 返回行數、列數、 和通道 print（img.size） # img.size 返回 訪問的像素總數 print（img.dtype） # img.dtype 傳回 獲得圖像數據類型 b， g， r = cv2.split（img） # cv2.split（img） - 數組的輸出向量;如果需要，陣列本身將被重新分配 img = cv2.merge（（b， g， r）） # cv2.merge（（b，g，r）） - 通道數將是矩陣陣列中的通道總數。
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
# dst = cv2.add(img, img2) # Calculates the per-element sum of two arrays or an array and a scalar.
dst = cv2.addWeighted(img, .9, img2, .1, 0)
# dst = cv2.addWeighted(img, .2, img2, .8, 0) - Calculates the weighted sum of two arrays.
cv2.imshow('ball', ball)
cv2.imshow('Messi with OpenCv logo', dst)
cv2.imwrite('Messi_play_with_2_balls.jpg', img)
# Save img as Messi_play_with_2_balls.jpg in your project directory
cv2.waitKey(0)
cv2.destroyAllWindows()

# ball = img[280：340， 330：390] #img[273：333， 100：160] = ball # dst = cv2.add（img， img2） 
# 計算兩個陣列或一個數組和一個標量的每個元素的總和。dst = cv2.addWeighted（img， .9， img2， .1， 0） # dst = cv2.addWeighted（img， .2， img2， .8， 0） - 計算兩個陣列的加權和。cv2.imshow（'Messi with OpenCv logo'， dst） cv2.imwrite（'Messi_play_with_2_balls.jpg'， img） # 將 img 另存為專案目錄中的Messi_play_with_2_balls.jpg cv2.waitKey（0） cv2.destroyAllWindows（）