import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('lena_noise.jpg')
# Read the test image 'lena_noise.jpg'
# kernel = np.ones((3, 3), np.float32)/9
kernel = np.ones((5, 5), np.float32)/25
# Define the kernel, using a N×N NumPy array, where N is odd.
dst = cv.filter2D(img, -1, kernel)
# Use the cv2.filter2D() function in OpenCV to perform the linear filtering operation.
cv.imshow("Original", img)
cv.imshow("Averaging", dst)
# Display the original and filtered images, using cv2.imshow() function.
cv.imwrite('lena_noise_average.jpg', dst)
# Save the filtered image to disk, using cv2.imwrite() function.
# In command line, type 'pip install matplotlib' to install matplotlib before running this program.
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()