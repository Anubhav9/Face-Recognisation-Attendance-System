import cv2
import os
import numpy as np
from PIL import Image

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_recognizer=cv2.face.LBPHFaceRecognizer_create()

def detect_face(img):
    print("Face detection started....")
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray)
    if(len(face)==0):
        print("None Returned")
        return None,None
    (x,y,w,h)=face[0]
    return gray[y:y+w,x:x+h],face[0]

def predict(imgoriginal):
    img=imgoriginal.copy()
    print("Predicting...")
    name=[]
    face,rect=detect_face(img)
    index=0
    try:
        if(face==None):
            print("Returned")
            return img
    except:
        print("Except ran")
    try:
        index=face_recognizer.predict(face)
    except:
        print("face_recognizer error")
    print(index)
    fobject=open("names.txt","r")
    name.append("")
    while(True):
        var=fobject.readline()
        if(var==''):
            break
        name.append(var)
    fobject.close()
    print(name)
    print(face)
    (x,y,w,h)=rect
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img,name[index[0]],(x,y-5),cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    return img

def train():
    faces=[]
    labels=[]
    count=0
    maindirs="data"
    innerfolder=os.listdir(maindirs)
    print(innerfolder)
    for imgfolder in innerfolder:
        count+=1
        print(count)
        imgpath=os.listdir(maindirs+"/"+imgfolder)
        print(imgpath)
        for imgname in imgpath:
            if imgname.startswith("."):
                continue
            img=cv2.imread(maindirs+"/"+imgfolder+"/"+imgname)
            cv2.imshow("Matching...",img)
            cv2.waitKey(100)
            face,rect=detect_face(img)
            if face is not None:
                faces.append(face)
                labels.append(count)
    print(face,labels)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces,labels
def getImagesAndLabels(path):


    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]

    faceSamples=[]

    Ids=[]


    for imagePath in imagePaths:

        pilImage=Image.open(imagePath).convert('L')

        imageNp=np.array(pilImage,'uint8')

        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        

        faces=face_cascade.detectMultiScale(imageNp)

        for (x,y,w,h) in faces:

            faceSamples.append(imageNp[y:y+h,x:x+w])

            Ids.append(Id)

    return faceSamples,Ids





def getPhoto(x):
    count=0
    cap=cv2.VideoCapture(0)
    while(cap.isOpened()):
        rect,frame=cap.read()
        frame=cv2.flip(frame,1)
        if(x==0):
            cv2.imshow("Capturing",frame)
            if(cv2.waitKey(1) & 0xFF==ord('s')):
                count=count+1
                filename=username
                cv2.imwrite("data/"+username+"/"+filename+str(count)+".jpg",frame)
                if(count>=5):
                    break
        else:
            if(cv2.waitKey(1) & 0xFF==ord('q')):
                break
            img=predict(frame)
            cv2.imshow("Matching...",img)

    cap.release()
    cv2.destroyAllWindows()

choose=int(input("Enter 1 for saving photo: \nEnter 2 for recognizion: "))

if(choose==1):
    username=input("Enter your name: ")
    if os.path.exists("data/"+username):
        print("Directory exists!!")
    else:
        os.makedirs("data/"+username)
        fobject=open("names.txt","a")
        name=username
        fobject.write(name)
        fobject.write("\n")
        fobject.close()
        getPhoto(0)
else:
    faces,Ids = getImagesAndLabels('G:\Projects(self)\logging\Image Database')

s = face_recognizer.train(faces, np.array(Ids))

print("Successfully trained")

face_recognizer.write('trainer.yml')
