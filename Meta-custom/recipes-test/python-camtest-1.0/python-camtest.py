import tkinter as tk
from tkinter import filedialog, Text
import cv2, time
import numpy as np
from datetime import datetime

root = tk.Tk()

def vigilancia():
    haar_upper_body_cascade = cv2.CascadeClassifier("haarcascade_upperbody.xml")
    haar_lower_body_cascade = cv2.CascadeClassifier("haarcascade_lowerbody.xml")
    haar_full_body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
    haar_full_face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    haar_full_catface_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
    #haar_full_dog_cascade = cv2.CascadeClassifier("C:/Users/crisd/Downloads/dog.xml")

    cont=0 
    grupo=[]
    
    video_capture = cv2.VideoCapture(0)
    video_width = video_capture.get(3)
    video_height = video_capture.get(4)
    f= open("registro.txt","w+")

    while True:
        ret, frame = video_capture.read()

        #frame = imutils.resize(frame, width=1000) # resize original video for better viewing performance
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert video to grayscale

        #Para cuerpo superior   
        upper_body = haar_upper_body_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.01,
            minNeighbors = 10,
            minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        #Para cuerpo inferior
        lower_body = haar_lower_body_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.01,
            minNeighbors = 10,
            minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        #Para cuerpo completo
        full_body = haar_full_body_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.01,
            minNeighbors = 10,
            minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        #Para cara completa
        full_face = haar_full_face_cascade.detectMultiScale(
              gray,
              scaleFactor = 1.01,
              minNeighbors = 10,
              minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
              flags = cv2.CASCADE_SCALE_IMAGE
         )
        #Cara de gato
        full_catface = haar_full_catface_cascade.detectMultiScale(
              gray,
              scaleFactor = 1.01,
              minNeighbors = 10,
              minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
              flags = cv2.CASCADE_SCALE_IMAGE
         )
        #Perro
       # full_dog = haar_full_dog_cascade.detectMultiScale(
        #      gray,
          #    scaleFactor = 1.01,
           #   minNeighbors = 10,
            #  minSize = (50, 100), # Min size for valid detection, changes according to video size or body size in the video.
             # flags = cv2.CASCADE_SCALE_IMAGE
       # )
        #rectList, weights = cv2.groupRectangles(np.array(upper_body).tolist(), 1, 0.2)
       # combined_array = np.append(upper_body, lower_body, axis = 0)
        #combined_list = combined_array.tolist()
        #result = np.vstack((upper_body, full_face,))
        #result2 = cv2.groupRectangles(result, 2)
        # Draw a rectangle around the upper bodies
        for (x, y, w, h) in upper_body:
            verde=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
            cv2.putText(frame, "Human Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # creates green color text with text size of 0.5 & thickness size of 2
            cont=cont+1
            grupo=[grupo,verde]
            now = datetime.now()
            nows = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write("\n Intrusion humana  %s:" % nows )
            
        for (x, y, w, h) in lower_body :
            verde1=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
            cv2.putText(frame, "Human Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # creates green color text with text size of 0.5 & thickness size of 2
            cont=cont+1
            grupo=[grupo,verde1]
            now = datetime.now()
            nows = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write("\n Intrusion humana  %s:" % nows )

        for (x, y, w, h) in full_body :
            verde2=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
            cv2.putText(frame, "Human Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # creates green color text with text size of 0.5 & thickness size of 2
            cont=cont+1
            grupo=[grupo,verde2]
            now = datetime.now()
            nows = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write("\n Intrusion humana  %s:" % nows )
            
        for (x, y, w, h) in full_face :
            verde3=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
            cv2.putText(frame, "Human Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cont=cont+1
            grupo=[grupo,verde3]
            now = datetime.now()
            nows = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write("\n Intrusion humana  %s:" % nows )
            
        for (x, y, w, h) in full_catface :
            verde4=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # creates green color rectangle with a thickness size of 1
            cv2.putText(frame, "Cat Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cont=cont+1
            grupo=[grupo,verde4]
            now = datetime.now()
            nows = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write("\n Intrusion animal %s:" % nows )

        

        
            
        cv2.imshow('Video en vivo', frame) # Display video

        # stop script when "q" key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print (cont)
            f.close()
            f = open('registro.txt', 'r')
            file_contents = f.read()
            print (file_contents)
            f.close()
            break

    # Release capture
    video_capture.release()
    cv2.destroyAllWindows()
    
def VerReporte():
    global register
    with open ("registro.txt", "r") as f:
        tempreg = f.read()
        register = tk.Label(frame, text=tempreg, fg="black", bg="white")
        register.pack()

def Borrar():
    register.pack_forget()
        
canvas = tk.Canvas(root, height=600, width=600, bg="#263D76")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


watch = tk.Button(root, text="Ver en vivo", padx=10, pady=3, fg="white", bg="#263D76", command=vigilancia)
watch.pack()

rep = tk.Button(root, text="Ver reporte diario", padx=10, pady=3, fg="white", bg="#263D76", command=VerReporte).place(x=10, y=604)
#rep.pack()

borr = tk.Button(root, text="Dejar de ver reporte", padx=10, pady=3, fg="white", bg="#263D76", command=Borrar).place(x=460, y=604)
#borr.pack()

w = tk.Scrollbar(frame)
w.pack(side=tk.RIGHT, fill="y")

#ListBox = tk.Listbox(frame, yscrollcommand=w.set)
#TxtBox.pack(expand=0, fill=tk.BOTH)

#TxtBox.insert(tk.END, register)
w.config(command=canvas.yview)


root.mainloop()


