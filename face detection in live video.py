import  numpy as np
import matplotlib.pyplot as plt
import cv2

face_detect=cv2.CascadeClassifier('harrCascades\haarcascade_frontalface_default.xml')
eye_detect=cv2.CascadeClassifier('harrCascades\haarcascade_eye.xml')
'''def detect_face(img):
    face_image=img.copy()
    face_rectangle=face_detect.detectMultiScale(face_image)

    for(x,y,w,h) in face_rectangle:
        cv2.rectangle(face_image,(x,y),(x+w,y+h),(255,0,0),6)


    return face_image
'''

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,580)

while True:
    ret,frame=cap.read()


    face_rectangle = face_detect.detectMultiScale(frame)
    eye_rectangle=eye_detect.detectMultiScale(frame)
    for (x, y, w, h) in face_rectangle:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 6)

    for(ix,iy,iw,ih) in eye_rectangle:
        cv2.rectangle(frame,(ix,iy),(ix+iw,iy+ih),(0,0,255),4)

    cv2.imshow('facedetection',frame)

    if cv2.waitKey(5) and 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
