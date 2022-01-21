import cv2 as cv
import numpy as np

img=cv.imread('Images/manzara.jpg')
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
#Every image consists of three main color channels (red, green, blue)
b,g,r = cv.split(img) #splitting the image into blue, green and red components

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#Merging the splitted parts of an image
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

#Coloring the image with specific colors
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Red', red)
cv.imshow('Green', green)
cv.waitKey(0)