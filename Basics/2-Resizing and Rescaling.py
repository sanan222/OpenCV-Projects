import cv2 as cv

#img = cv.imread('Photos/cat_large2.img')
#cv.imshow('Cat', img)

#rescaleFrame function works for Images, Videos, Live Videos
def rescaleFrame(frame, scale=0.75): #function takes frame and default scale value
    width = int(frame.shape[1]*scale) #frame.shape[1] is width of image and we change its size
    height = int(frame.shape[0]*scale) #frame.shape[0] is height of an image and we change its size
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#changeRes function works only for Live videos
def changeRes(width, height): #changing resolution of video
    capture.set(3, width)
    capture.set(4, height)

#Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame=capture.read()
    frame.resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)