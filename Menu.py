from tkinter import *
import os
import cv2
def database():
    os.system('python newcamcapture.py')
def traindata():
    os.system('python TrainingandPrediction2.py')
def recognise():
    os.system('python xxy.py')
def openlist():
    os.startfile(os.getcwd()+"/Updated List.xlsx")
def aboutus():
    os.startfile(os.getcwd()+"/About Us.pptx")
root=Tk()
root.title("Face Recognisation System")
root.configure(background="#1adbcd")
root.geometry('440x490')
Label(root,font=("Helvetica",18,"bold"),text="Please select the desired option", fg="blue4", bg="#1adbcd").grid(row=0,column=0,padx=40,pady=20)
Button(root,font=("Helvetica",18,"bold"),text="Create Database",fg="white",bg="red",command=lambda:database()).grid(row=1,column=0)
Button(root,font=("Helvetica",18,"bold"),text="Train Database",fg="white",bg="red",command=lambda:traindata()).grid(row=2,column=0,pady=10)
Button(root,font=("Helvetica",18,"bold"),text="Recognise+Attendance",fg="white",bg="red",command=lambda:recognise()).grid(row=3,column=0,pady=10)
Button(root,font=("Helvetica",18,"bold"),text="Attendance Sheet",fg="white",bg="red",command=lambda:openlist()).grid(row=4,column=0,pady=10)
Button(root,font=("Helvetica",18,"bold"),text="About Developers",fg="white",bg="red",command=lambda:aboutus()).grid(row=5,column=0,pady=10)
Button(root,font=("Helvetica",18,"bold"),text="Quit",fg="springgreen4",bg="bisque2",command=quit).grid(row=6,column=0,pady=20)


root.mainloop()
