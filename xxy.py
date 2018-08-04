import numpy as np

import os

import cv2

from PIL import Image

import pickle, sqlite3

import xlwt

from xlwt import Workbook

import datetime

num=2

date=datetime.datetime.now().date()
time=datetime.datetime.now().time()

attendance=Workbook()
n=attendance.add_sheet("Attendance Record",cell_overwrite_ok=True)
n.write(0,0,str(date))
n.write(0,1,str(time))
n.write(1,0,"ID")
n.write(1,1,"Name")
n.write(1,2,"Attendance")





face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("trainer.yml")







def getProfile(Id):

    conn=sqlite3.connect("StuInfo.db")

    query="SELECT * FROM getinfo WHERE ID="+str(Id)

    cursor=conn.execute(query)

    profile=None

    for row in cursor:

        profile=row

    conn.close()

    return profile



#to train using frames from video

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_COMPLEX

while True:

    

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:



        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

        roi_gray = gray[y:y+h, x:x+w]

        roi_color = img[y:y+h, x:x+w]



        

        nbr_predicted, conf = recognizer.predict(gray[y:y+h, x:x+w])

        if conf < 70:

            profile=getProfile(nbr_predicted)

            if profile != None:

                cv2.putText(img, "ID: "+str(profile[0]), (x, y+h+30), font, 1.0, (0, 0, 255), 1);

                cv2.putText(img, "Name: " + str(profile[1]), (x, y + h + 60), font, 1.0, (0, 0, 255), 1);
                cv2.putText(img, "Batch: " + str(profile[2]),(x, y + h + 90), font, 1.0, (0, 0, 255), 1);

                n.write(num,0,str(profile[0]))
                n.write(num,1,str(profile[1]))
                n.write(num,2,str(profile[2]))
                n.write(num,3,"Present")
                
                
                
                
                        

                
               

        else:

            cv2.putText(img, "Name: Unknown", (x, y + h + 30), font, 0.4, (0, 0, 255), 1);

            cv2.putText(img, "Age: Unknown", (x, y + h + 60), font, 0.4, (0, 0, 255), 1);

            cv2.putText(img, "Gender: Unknown", (x, y + h + 70), font, 0.4, (0, 0, 255), 1);

            cv2.putText(img, "Criminal Records: Unknown", (x, y + h + 90), font, 0.4, (0, 0, 255), 1);



    
    cv2.imshow('img', img)

    if(cv2.waitKey(1) == ord('q')):

        break
num=num+1
attendance.save("Updated List.xlsx")

cap.release()

cv2.destroyAllWindows()
