

# Source Code to convert GMIT image to grayscale using OpenCV: 
    # https://extr3metech.wordpress.com/2012/09/23/convert-photo-to-grayscale-with-python-opencv/

import cv2
import numpy as np
from matplotlib import pyplot as plt

# print("Hello World!")

# Original image taken from the mother folder
img = cv2.imread('GMIT.jpg',)
cat = cv2.imread('funny_kitty.jpg')

# To convert to gray-scale image and store it to another variable named "gray_image" 
# use the function cv2.cvtColor() with parameters as  the "image" variable and  "cv2.COLOR_BGR2GRAY" :
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_cat = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)
# fix subplot colour issues, 
# plot "cv2.cvtColor(img, cv2.COLOR_BGR2RGB)"" rather than "img" when dealing with colour images. 
orig_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
orig_cat = cv2.cvtColor(cat, cv2.COLOR_BGR2RGB) 

# Now, to write/save the converted gray-scale image to the hard disk, 
# we use the function "cv2.imwrite()" with parameters as "the name of converted image" 
# and the variable "gray_image" to which the converted image was stored:
cv2.imwrite('GMIT_gray.png',gray_image)
cv2.imwrite('kitty_gray.png',gray_cat)


# To display the original and the gray-scale,
# we use function "cv2.imshow()" with parameters 
# as the "window title" and the "image variable" :	
cv2.imshow('color_image',orig_image)             
cv2.imshow('gray_image',gray_image) 
cv2.imshow('color_cat',orig_cat)             
cv2.imshow('gray_cat',gray_cat) 

cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows

# Initialize number of rows and number of columns
nrows = 2
ncols = 2

# To plot multiple images in a window, 
# we will use Matplotlib’s "plt.subplot" function. 
# This method can plot a number of images in a figure as follows. 
# orig_image should correspond to the original image loaded in 
# gray_image should correspond to the grayscale version
plt.subplot(nrows, ncols,1),plt.imshow(orig_image, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,3),plt.imshow(orig_cat, cmap = 'gray')
plt.title('Original Cat'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,4),plt.imshow(gray_cat, cmap = 'gray')
plt.title('GrayScale Cat'), plt.xticks([]), plt.yticks([])
plt.show()

# Images can be filtered with various low-pass filters (LPF), high-pass filters (HPF), etc. 
    # A LPF helps in removing noise, or blurring the image. 
    # A HPF filtershelps in finding edges in an image. 
# OpenCV provides a function, cv2.GaussianBlur(), to convolve a kernel with an image.
# Create a new variable to use for the blurring of the gray image
# imgOut = cv2.GaussianBlur(imgIn,(KernelSizeWidth, KernelSizeHeight),0)

imgIn = gray_image
imgInCat = gray_cat

# Use these variables for the blurring 
imgOut3x3 = cv2.GaussianBlur(imgIn,(3, 3),0)
imgOut13x13 = cv2.GaussianBlur(imgIn,(13, 13),0)
imgCatOut3x3 = cv2.GaussianBlur(imgInCat,(3, 3),0)
imgCatOut13x13 = cv2.GaussianBlur(imgInCat,(13, 13),0)

# imgOut5x5 = cv2.GaussianBlur(imgIn,(5, 5),0)
# imgOut9x9 = cv2.GaussianBlur(imgIn,(9, 9),0)


# Initialize number of rows and number of columns
nrows = 2
ncols = 4

# Original
plt.subplot(nrows, ncols,1),plt.imshow(orig_image, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
# GrayScale
plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
# 3x3 Blur
plt.subplot(nrows, ncols,3),plt.imshow(imgOut3x3, cmap = 'gray')
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])
# 13x13 Blur
plt.subplot(nrows, ncols,4),plt.imshow(imgOut13x13, cmap = 'gray')
plt.title('13x13 Blur'), plt.xticks([]), plt.yticks([])
# Original
plt.subplot(nrows, ncols,5),plt.imshow(orig_cat, cmap = 'gray')
plt.title('Original Cat'), plt.xticks([]), plt.yticks([])
# GrayScale
plt.subplot(nrows, ncols,6),plt.imshow(gray_cat, cmap = 'gray')
plt.title('GrayScale Cat'), plt.xticks([]), plt.yticks([])
# 3x3 Cat Blur
plt.subplot(nrows, ncols,7),plt.imshow(imgCatOut13x13, cmap = 'gray')
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])
# 13x13 Cat Blur
plt.subplot(nrows, ncols,8),plt.imshow(imgCatOut3x3, cmap = 'gray')
plt.title('13x13 Blur'), plt.xticks([]), plt.yticks([])
plt.show()

# Next, we’ll perform edge detection using the Sobel operator. 
# The Sobel operator detects horizontal and vertical edges 
# by multiplying each pixel by the two kernels Gx and Gy
sobelHorizontal = cv2.Sobel(imgIn,cv2.CV_64F,1,0,ksize=5) # x dir
sobelVertical = cv2.Sobel(imgIn,cv2.CV_64F,0,1,ksize=5) # y dir
sobelSum = sobelHorizontal + sobelVertical

# Perform Canny edge detection and plot the result. 
# Set the cannyThreshold to 100 initially. 
# Set cannyParam2 to be 200 initially.
# cannyParam2 should be roughly 2 to 3 times the magnitude of cannyThreshold
# canny = cv2.Canny(imgIn,cannyThreshold,cannyParam2)
cannyEdge = cv2.Canny(imgIn,100,200)

# Initialize number of rows and number of columns
nrows = 2
ncols = 3

# Original
plt.subplot(nrows, ncols,1),plt.imshow(orig_image, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
# GrayScale
plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])
# Sobel X
plt.subplot(nrows, ncols,3),plt.imshow(sobelHorizontal, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# Sobel Y
plt.subplot(nrows, ncols,4),plt.imshow(sobelVertical, cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# Sobel Sum
plt.subplot(nrows, ncols,5),plt.imshow(sobelSum, cmap = 'gray')
plt.title('Sobel Sum'), plt.xticks([]), plt.yticks([])
# Canny Edge Image
plt.subplot(nrows, ncols,6),plt.imshow(cannyEdge, cmap = 'gray')
plt.title('Canny Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
