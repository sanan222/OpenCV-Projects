import os
import cv2 as cv
import numpy as np

people = ['Ben Affleck', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

#Finding the list we need for people alternative

#p = []

#for i in os.listdir(r'C:\Users\kanan\Desktop\project iturobotics\opencv\Youtube Course\Images'):
    #p.append()

#print(p)

DIR = r'C:\Users\kanan\Desktop\project iturobotics\opencv\Youtube Course\Resources\Faces\train'

haar_cascade = cv.CascadeClassifier('Face Detection/haar_face.xml')

features = [] #a list of faces
labels = [] #a list of labels of faces

def create_train():
    for person in people:
        path = os.path.join(DIR, person) #grabbing path of the folder 
        label = people.index(person) #creating labels

        #inside the folder to find images
        for img in os.listdir(path):
            img_path = os.path.join(path, img) 

            img_array = cv.imread(img_path) #reading that image from the path
            if img_array is None:
                continue
           
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY) #converting this image into gray scale

            faces_rect = haar_cascade.detectMultiScale (gray, scaleFactor = 1.1, minNeighbors = 4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training Done ----------------------')

features = np.array(features, dtype = 'object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the Recognizer on the features and the labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)