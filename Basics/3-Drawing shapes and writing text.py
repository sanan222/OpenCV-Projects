import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3), dtype = 'uint8') #this draws blank image (siyah ekran)
cv.imshow('Blank', blank) 

#img = cv.imread('Photos/cat.jpg')
#cv.imshow ('Cat', img)

#1): Paint the blank image
blank [:]=0,255,0   #paint the whole blank page with green color
blank[200:300, 300:400] = 0, 0,255 #giving specific location for painted area
cv.imshow('Green', blank)

#2) Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) #draws a rectangle frame
cv.imshow('Rectangle', blank)

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (250,250,0), thickness = -1) #draws a rectangle in 1/4 region of the blank page
cv.imshow('Rectangle', blank)

#3) Draw a Circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness = 2) #if we give thickness = -1 then it will fullfil the circle
cv.imshow('Circle', blank)

#4) Draw a line
cv.line(blank, (0,0), (250,250), (255,255,255), thickness = 3)
cv.imshow('Line', blank)

#5) Write a text
cv.putText(blank, 'Azerbaycan', (50,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)