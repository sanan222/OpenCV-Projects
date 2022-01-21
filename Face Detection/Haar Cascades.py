import cv2 as cv

img = cv.imread('Images/people.jpg')
cv.imshow('People', img)

#Converting the image to gray tone
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

#Reading xml file
haar_cascade = cv.CascadeClassifier('Face Detection/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3) #This code collects scaleFactor variables and collect them in the list and return rectangular coordinates as a list

print(f'Number of faces found = {len(faces_rect)}') #this prints the number of faces in the photo

#Drawing rectangular shape on the face
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)
cv.imshow('Detected Faces', img)




cv.waitKey(0)