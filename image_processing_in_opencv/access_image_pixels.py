import numpy as np
import cv2
img = cv2.imread('/home/sheron/Pictures/pikachu.png')

# access pixels of image
px = img[100, 100]
print px

# accessing only blue pixel
blue = img[100,100, 0]
print blue

# modify pixels like this

img[100,100] = [255,255,255]
print img[100, 100]

# accessing RED value
img.item(10,10,2)


# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

# access image properties
print (img.shape)

# Total number of pixels is accessed by img.size:
print (img.size)

# Image datatype is obtained by img.dtype:
print (img.dtype)

