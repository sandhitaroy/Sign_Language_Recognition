import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy
import numpy as np
from keras.models import load_model
model=load_model('model.h5')
top=tk.Tk()
top.geometry('800x600')
top.title('Sign Language Recognizer')
top.configure(background='#CDCDCD')
label1=Label(top, background="#CDCDCD", font=('arial', 15, "bold"))
label2=Label(top, background="#CDCDCD", font=('arial', 15, 'bold'))
sign_image=Label(top)

def Detect(file_path):
    global label1, label2
    image = Image.open(file_path)
    image = image.resize((28, 28)) 
    image = np.array(image.convert('L'))  
    image = image.reshape((1,28,28,1))  
    image = image / 255.0  
    sign_labels = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    pred = model.predict(image)
    sign_index = np.argmax(pred)
    sign_label = sign_labels[sign_index]
    print("Predicted translation is " + sign_label)
    label1.configure(foreground="#011638", text="Predicted Translation: " + sign_label)

def show_Detect_button(file_path):
    Detect_b=Button(top, text="Detect Image",command=lambda: Detect(file_path), padx=10,pady=5)
    Detect_b.configure(background="#364156", foreground='white', font=('arial', 10, 'bold')) 
    Detect_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        show_Detect_button(file_path)
    except:
        pass
upload=Button(top, text="Upload an Image", command=upload_image,padx=10,pady=5)
upload.configure(background="#364156", foreground='white', font=('arial', 10, 'bold'))
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True)
label1.pack(side="bottom", expand=True)
label2.pack(side="bottom", expand=True)
heading=Label(top, text="Sign Language Recognizer", pady=20, font=("arial", 20,"bold"))
heading.configure(background="#CDCDCD", foreground="#364156")
heading.pack()
top.mainloop()


