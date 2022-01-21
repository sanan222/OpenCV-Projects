import cv2 as cv

img=cv.imread('Images/manzara.jpg')
cv.imshow('Boston', img)

#BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV (Huge Saturation Value (how humans think and conceive color))
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB (RGB is the format that is seen outside opencv)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR', hsv)

#There is no way to convert from grayscale to bgr we have to do every attempt.
cv.waitKey(0)