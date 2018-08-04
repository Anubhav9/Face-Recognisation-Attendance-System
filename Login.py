from tkinter import *
import os

root=Tk()

root.title("Welcome")
root.configure(background="#1adbcd")
root.geometry('400x220')
Label(root,font=("Helvetica",18,"bold"),text="Username", fg="red", bg="#1adbcd").grid(row=0,column=2,padx=145,pady=20)
e1=Entry(root,font=("Helvetica",10,"bold"),width=35)
e1.grid(row=1,column=2,padx=105)
Label(root,font=("Helvetica",18,"bold"),text="Password", fg="red", bg="#1adbcd").grid(row=2,column=2,padx=145,pady=7)
e2=Entry(root,font=("Helvica",10,"bold"),show="*",width=35)
e2.grid(row=3,column=2,padx=105)
Button(root,font=("Helvetica",14,"bold"),text="Login",fg="#a1dbcd",bg="#383a39",command=lambda:login()).grid(row=4,column=2,padx=120,pady=7)

def login():
    if(e1.get()=="navnirman" and e2.get()=="fosters"):
        print("Login Successful")
        os.system('python Menu.py')

        return "logged"
root.mainloop()
