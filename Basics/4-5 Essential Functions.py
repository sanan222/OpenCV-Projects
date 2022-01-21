import cv2 as cv
img = cv.imread('Images/manzara.jpg')
cv.imshow('Cat', img)

# Converting to grayscale (coloring gray)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blurring image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', img)

#Edge Cascade
cany = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', cany)

#Dilating the image (increase thickness of edges)
dilated = cv.dilate(cany, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

#Eroding (decreasing thickness of edges)
eroded = cv.erode(dilated, (3,3), iterations = 1)
cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA)
cv.imshow('Resized', resized)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)