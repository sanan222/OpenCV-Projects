import cv2 as cv

img = cv.imread('Images/image.jpg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 1) Simple Thresholding (Black White mainly Black)
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY) #looks at the image compares each threshold value
cv.imshow('Simple Thresholded', thresh)

#Inverse Thresholding (Black WHite mainly White)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow ('Simple Threshold Inverse', thresh_inv)

# 2) Adaptive Thresholding (Corner white black)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,
11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)



cv.waitKey(0)