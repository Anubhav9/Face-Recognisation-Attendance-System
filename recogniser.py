import cv2
import os
import numpy as np
from PIL import Image


import pickle
import sqlite3
conn=sqlite3.connect("StuInfo.db")
c=conn.cursor()

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("trainer.yml")

def getprofile(ID):
    c.execute("SELECT * FROM getinfo WHERE ID=(?);",(ID,))
    
    profile=None
              


    for row in c:
        profile=row
    c.close()
    conn.close()
    return profile
cap=cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, img = cap.read();

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

    faces = face_cascade.detectMultiScale(gray, 1.3, 7);

    for (x,y,w,h) in faces:

        roi_gray = gray[y:y + h, x:x + w]

        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);

        id,conf=face_recognizer.predict(roi_gray)
        profile=getprofile(id)
        if(profile!=None):
            cv2.cv.PutText(cv2.cv.fromarray(img),profile[1],(x,y+h+30),font,255)
            cv2.cv.PutText(cv2.cv.fromarray(img),profile[2],(x,y+h+60),font,255)
            cv2.cv.PutText(cv2.cv.fromarray(img),profile[3],(x,y+h+90),font,255)
            cv2.cv.PutText(cv2.cv.fromarray(img),profile[4],(x,y+h+120),font,255)
        
        cv2.imshow("frame",img)
        cv2.waitkey(10)
cap.release()
cv2.destroyAllWindows()
