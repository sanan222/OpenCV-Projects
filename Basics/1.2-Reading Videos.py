#Reading Videos
import cv2 as cv #importing openCV library

capture = cv.VideoCapture('Videos/dog.mp4') #defining video for the program

while True:
    isTrue, frame = capture.read() #divides the video frame by frame
    cv.imshow('Video', frame) #reading frames of video

    if cv.waitKey(20)& 0xFF == ord('d'): #if letter d is pressed break the loop
        break

capture.release() #release capture device
cv.destroyALLWindows() #close the window