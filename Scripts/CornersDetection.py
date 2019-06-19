#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:11:33 2019

@author: Albert
"""


import cv2 #conda install -c menpo opencv
import numpy as np


# Load input image -- 'box.png'
input_file = ('/Users/Alf/Documents/GitHub/MlshapeSimplification/Scripts/filename.png') #sys.argv[1]
img = cv2.imread(input_file)
cv2.imshow('Input image', img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)


# Harris corner detector
#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html
#img - Input image, it should be grayscale and float32 type.
#blockSize - It is the size of neighbourhood considered for corner detection
#ksize - Aperture parameter of Sobel derivative used.
#k - Harris detector free parameter in the equation.
img_harris = cv2.cornerHarris(img_gray, 2, 1, 0.04)



# Resultant image is dilated to mark the corners
img_harris = cv2.dilate(img_harris, None)


#___________________________________________________________________________
dst = img_harris

ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(img_gray,np.float32(centroids),(5,5),(-1,-1),criteria)
print(corners)    
# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)

print(res)

#___________________________________________________________________________


 # Threshold the image
img[img_harris > 0.01 * img_harris.max()] = [0, 0, 0]

cv2.imshow('Harris Corners', img)
cv2.imwrite('subpixel.png',img)
cv2.waitKey()



