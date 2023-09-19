import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 

##############################################+=============================================================

root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('face.db')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Number Plate Recognization")


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('i4.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Number Plate Recognization", font=('times', 32,' bold '), height=1, width=30,bg="#F75D59",fg="white")
lbl.place(x=300, y=15)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=280, height=200, bd=5, font=('times', 15, ' bold '),bg="#99C68E")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=30, y=200)


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
#################################################################################################################
def Number_Plate_Recognization():
   # print("Handwritten_recognisation")
    from subprocess import call
    call(["python", "image_to_text_multilang.py"]) 





def window():
    root.destroy()


button1 = tk.Button(frame_alpr, text="Number Plate Recognization", command=Number_Plate_Recognization,width=20, height=1, font=('times', 15, ' bold '),bg="#FF8040",fg="white")
button1.place(x=10, y=30)



exit = tk.Button(frame_alpr, text="Exit", command=window, width=10, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=60, y=100)



root.mainloop()