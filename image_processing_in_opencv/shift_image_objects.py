import numpy as np
import cv2
img = cv2.imread('/home/sheron/Pictures/pikachu.png')

# ROI 
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# splitting and merging image channels

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# OR 
# b = img[:,:,0]

# If we want to make all red pixels 0.
# img[:,:,2] = 0

