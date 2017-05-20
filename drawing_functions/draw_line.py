import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# ARGUMENTS:
# Here img is the image on which we want to draw
# (0,0), (511, 511) are coordinates specified for the length of the line
# (255, 0,0) is the BGR code for color blue
# 5 is the thickness of the line
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
