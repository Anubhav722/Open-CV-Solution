import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags

# FOR MORE INFO SEE: 
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces


# FOR COLOR CONVERSION:
# cv2.cvtColor(input_image, flag)
# where flag determines the type of conversion
