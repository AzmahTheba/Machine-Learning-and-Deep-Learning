# -*- coding: utf-8 -*-
"""Unit_4_working_on_computer_vision_with_python_slide_82_102.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18v_Xbz9BImn3iIchrHA20VLZbZGu_gSj
"""

#Working on Computer Vision with Python

!wget "https://www.duckietown.org/wp-content/uploads/2018/05/duckietown_nice-1024x683.jpg" -O dt.jpg

# np = common abbreviation for numpy
import numpy as np


# Big takeaway: numpy docs are your friend! Look before you write!

# Commented out IPython magic to ensure Python compatibility.
#OpenCV library in python
# %matplotlib inline
from matplotlib import pyplot as plt
import cv2

# Load in Grayscale
img = cv2.imread('./dt.jpg', 0)

# The underlying representation is a numpy array!
print(type(img))

plt.imshow(img)
plt.show()

img = cv2.imread('./dt.jpg')

plt.imshow(img)
plt.show()

# This would work normally, but it will crash the colab kernel, so don't.
# cv2.imshow('Image', img)

#In Colab, you cannot use the standard OpenCV 'imshow' function, so we use matplotlib.
imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(imgrgb)
plt.show()

# Or, use fun numpy functions / indexing!
imgrgb = img[:,:,::-1]
plt.imshow(imgrgb)
plt.show()

#Common Image Manipulations
#OpenCV is super useful for doing lots of image transformations, and we will experiment with some of the basic ones below.
# Expanding
res = cv2.resize(imgrgb, None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
plt.imshow(res)
plt.show()

# Shrinking
res = cv2.resize(imgrgb, None,fx=.1, fy=.1, interpolation = cv2.INTER_CUBIC)
plt.imshow(res)
plt.show()

# What are some practical constraints that have to do with image resizing?

#Transformation Parameters
#@title Transformation Parameters { run: "auto" }

theta_degrees = 60 #@param {type:"slider", min:0, max:360, step:10}
shift_x = 16 #@param {type:"slider", min:-100, max:100, step:2}
shift_y = -30 #@param {type:"slider", min:-100, max:100, step:2}

# We can also play around with rotations by defining our M matrix,
# which has the form:
"""
| cos(theta) -sin(theta) tx |
| sin(theta)  cos(theta) ty |
"""

rows, cols, _ = imgrgb.shape
radians = theta_degrees * np.pi / 180
M = [
        [np.cos(radians), -np.sin(radians), shift_x],
        [np.sin(radians),  np.cos(radians), shift_y]
    ]

M = np.array(M)
rows += int(shift_x)
cols += int(shift_y)

res = cv2.warpAffine(imgrgb, M, (cols,rows))

plt.imshow(res)
plt.show()

#Advanced Image Manipulation Techniques

# make things easier!
img = imgrgb

# Thresholding is cool
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# Blurring - smoothes the image out
blur = cv2.blur(img,(10, 10))
gblur = cv2.GaussianBlur(imgrgb,(5,5),0)

plt.imshow(img), plt.title('Original')
plt.show()
plt.imshow(blur), plt.title('Blurred')
plt.show()
plt.imshow(gblur),plt.title('Gaussian Blur')
plt.show()