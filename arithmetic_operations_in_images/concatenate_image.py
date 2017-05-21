import numpy as np
import cv2

img1 = cv2.imread('/home/sheron/Pictures/atif.jpg')
img2 = cv2.imread('/home/sheron/Pictures/atif.jpg')

# To stack horizontally (img1 to the left of img2):
vis = cv2.concatenate((img1, img2), axis=1)

# To stack vertically (img1 over img2)
vid = cv2.concatenate((img1, img2), axis=0)

# for saving image

cv2.imwrite('horizontal.png', vis)
cv.imwrite('vertical.png', vid)

