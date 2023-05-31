# Parrot AR Drone 2.0 Video Feed To Computer for OpenCV Processing
# Wilson Dhalwani 
# 3/16/23 
# PROJEKT OVRSGHT

import cv2 #imports OpenCV Image Analysis Library

face_cascade = cv2.CascadeClassifier("HaarscascadeLibrary\haarcascade_frontalface_default.xml") #FaceReadLibrary
print("Attempting to Ping Drone")
cap = cv2.VideoCapture("tcp://192.168.1.1:5555")  #Replace with the ip of the drone
running = True   #allows to constantly run

#Face Recognition Function
def FaceRec(img): 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert to gray scale of each frames
  
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  #Detects faces of different sizes in the input image
  
    for (fx,fy,fw,fh) in faces:
        #To draw a rectangle around faces
        cv2.rectangle(img,(fx,fy),(fx+fw,fy+fh),(255,255,0),2) 
        roi_gray = gray[fy:fy+fh, fx:fx+fw]
        roi_color = img[fy:fy+fh, fx:fx+fw]

while running:
    #get current frame of video
    running, frame = cap.read()

    if running:
        print("Drone Pinged Successfully")
        print("Initializing Video")
        
        #Insert Facial Recognition Software
        FaceRec()

        #Live Feed Display PC
        img = cv2.resize(frame, (1000, 800))
        cv2.imshow('Live Drone Feed', img)

        # Wait for Esc key to stop 
        k = cv2.waitKey(30) & 0xff
        if k == 27: 
            break
    else:
        print("Video Receive Error!")  #throw error reading frame
    
cap.release() #closes window    
cv2.destroyAllWindows() #de-allocates any assigned memory


    