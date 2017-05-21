import numpy as np
import cv2

# images are not being blended because of different sizes and a lot more

img1 = cv2.imread('ml.png')
img2 = cv2.imread('opencv_logo.jpg')

# weight of img1 here is 0.7 and weight of img2 is 0.3
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
