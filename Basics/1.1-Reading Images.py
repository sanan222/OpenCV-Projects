#Reading Images
import cv2 as cv #importing opencv library

img - cv.imread('Images/cat.jpg') #reading image

cv.imshow('Cat', img) #displaying image
cv.waitKey(0) #delay for infinity