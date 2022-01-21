import cv2 as cv
import numpy as np

img = cv.imread('Images/manzara.jpg')

cv.imshow('Boston', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #Making gray
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 125) #Finding edges
cv.imshow('Canny', canny)

blank = np.zeros(img.shape, dtype = 'uint8')

#Finding Contours
contours, hierarchjes = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

#Finding Contours Second method
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #makes the photo white black high contrast
contours, hierarchjes = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
cv.imshow('Thresh', thresh)

#Drawing contours
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
