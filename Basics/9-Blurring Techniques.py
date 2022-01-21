import cv2 as cv

img=cv.imread('Images/manzara.jpg')
cv.imshow('Boston', img)
# Averaging Method (takes the specific part then gives the numbers
# and find the average of them to blur the image)
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur (less blur than average but more natural)
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur (finds the medium of the numbers that in average method)
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)