import cv2
import sqlite3
import numpy
import os
count=0

def data(ID,NAME,BATCH):
    conn=sqlite3.connect("StuInfo.db")
    c=conn.cursor()
    c.execute("INSERT INTO getinfo VALUES(?,?,?)",(ID,NAME,BATCH))
    conn.commit()
    

ID=int(input("Enter your Id"))
NAME=input("Enter your name")
BATCH=input("Enter your Batch")
data(ID,NAME,BATCH)

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        print(faces)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,"Terrorist Identified",(x,y-3),font,0.6,(0,0,255),1,cv2.LINE_AA)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        count=count+1
        cv2.imwrite("Image Database/user." + str(ID)+"."+str(count)+".jpg", gray[y:y+h,x:x+w])
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        print("Successfully Captured")

        break
    elif(count==30):
        print("Successfull")
        break
        

cap.release()
cv2.destroyAllWindows()











       
