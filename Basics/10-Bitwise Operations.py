import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 250, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#Bitwise AND operator --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle) #takes the intersection of two figures
cv.imshow('Bitwise AND', bitwise_and)

#Bitwise OR operator --> nonintersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle) #takes both of them and display on same page
cv.imshow('Bitwise_OR', bitwise_or)

#Bitwise NOT operator --> converting black pixels to white
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitwise_not)

#Bitwise XOR operator --> non intersecting regions (only)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)


cv.waitKey(0)
