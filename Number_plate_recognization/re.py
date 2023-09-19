# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:09:00 2021

@author: sheet
"""

import sqlite3
import tkinter as tk
from PIL import Image , ImageTk
import os
from tkinter.filedialog import askopenfilename
from google.cloud import vision

from textblob import TextBlob 


root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Number plate recognization")

image2 =Image.open(r'i1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)
lbl = tk.Label(root, text="Number Plate Recognization", font=('Times', 30,'italic'), height=1, width=30,bg="#40BFFF",fg="black")
lbl.place(x=350, y=35)
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        abc=file.write(data)
        #return abc
    
    print("Stored blob data into: ", filename, "\n")
    return filename
global file
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'D:\Number_plate_recognization\Number_plate_recognization\eighth-zenith-307507-18bdc893bca2.json'


def readBlobData():
    car=carno.get()
    print(car)
    try:
        sqliteConnection = sqlite3.connect('evaluation (1).db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from registration where car_no = ?"""
        cursor.execute(sql_fetch_blob_query, (car,))
        record = cursor.fetchall()
        for row in record:
            print("Fullname = ", row[0], "address = ", row[1], "Email =", row[2],"Phoneno =", row[3],"Gender =", row[4],"age =", row[5],"photo =", row[6],"car_no =", row[7],"chassis_no =", row[8])
            Fullname = row[0]
            address = row[1]
            Email = row[2]
            Phoneno = row[3]
            Gender = row[4]
            age = row[5]
            photo = row[6]
            car_no = row[7]
            chassis_no = row[8]
            photoPath = r"D:\Number_plate_recognization\Number_plate_recognization\profile images\\" + Fullname + ".jpg"
            ph=writeTofile(photo, photoPath)
            load = Image.open(ph)
            render = ImageTk.PhotoImage(load)
            
            #img.place(x=0, y=0)
            #resumeFile = row[3]
            frame_alpr = tk.LabelFrame(root, text=" ---------------------------------Profile Details-------------------------------------", width=650, height=450, bd=5, font=('times', 15, ' bold '),bg="#FF8040")
            frame_alpr.grid(row=0, column=0, sticky='nw')
            frame_alpr.place(x=600, y=180)
            l1 = tk.Label(root, text="Full name :"+str(Fullname), 
                           font=("Times new roman", 15, "bold"), bg="snow")
            l1.place(x=640, y=225)
            l2 = tk.Label(root, text="Address :"+str(address), 
                           font=("Times new roman", 15, "bold"), bg="snow")
            l2.place(x=640, y=275)
            l3 = tk.Label(root, text="E-mail :"+str(Email), 
                          font=("Times new roman", 15, "bold"), bg="snow")
            l3.place(x=640, y=325)
            l4 = tk.Label(root, text="Phone no :"+str(Phoneno), 
                           font=("Times new roman", 15, "bold"), bg="snow")
            l4.place(x=640, y=375)
            l5 = tk.Label(root, text="Gender:"+str(Gender), 
                           font=("Times new roman", 15, "bold"), bg="snow")
            l5.place(x=640, y=425)
            l6 = tk.Label(root, text="Age:"+str(age), 
                           font=("Times new roman", 15, "bold"), bg="snow")
            l6.place(x=640, y=475)
            l7 = tk.Label(root, image=render, 
                           font=("Times new roman", 15, "bold"), bg="snow")
            l7.image = render
            l7.place(x=900, y=275)
            l8 = tk.Label(root, text="Car no :"+str(car_no), 
                           font=("Times new roman", 15, "bold"), bg="snow")
            l8.place(x=640, y=525)
            l9 = tk.Label(root, text="Chassis no :"+str(chassis_no), 
                           font=("Times new roman", 15, "bold"), bg="snow")
            l9.place(x=640, y=575)
           # print("Storing employee image and resume on disk \n")
            #photoPath = "E:/Number_plate_recognization/profile images\\" + name + ".jpg"
            #resumePath = "E:/Number_plate_recognization/profile images/1.jpg\\" + name + "_resume.txt"
          
            #writeTofile(resumeFile, resumePath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


#readBlobData("hh") 

def detect_text():
    global file
    """Detects text in the file."""
    from google.cloud  import vision
#    from google.cloud import types
    import io
    client = vision.ImageAnnotatorClient()
    #file = r'E:\OMKARS\OMKARS1\M.Tech\Data\china.jpg'
    with io.open(file, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')
    #print('here {}'.format(texts.description))

    for text in texts:
        print('')
        print('\n"{}"'.format(text.description))
        
        return text.description
        #print(type(text.description))
        #vertices = (['({},{})'.format(vertex.x, vertex.y)
                    #for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

def Text_Label():
    result_text = detect_text()
    result_label = tk.Label(root,text=str(result_text),font=('Times New Roman',12,'italic'),width=50,height=30,bg='#F08080',fg='white')
    result_label.place(x=475,y=50)

    
    



carno=tk.StringVar()

def Exit():
    root.destroy()


#button2 = tk.Button(root,text="Detect Text",command=Text_Label,font=('Times New Roman',12,'italic'),width=14,bg='black',fg='linen')
#button2.place(x=50,y=500)

l9 = tk.Label(root, text="Car Number Plate No. :", width=18, font=("Times new roman", 15, "bold"), bg="snow")
l9.place(x=50, y=205)
t9 = tk.Entry(root, textvar=carno, width=20, font=('', 15))
t9.place(x=300, y=205)
#car=carno.get()
sub = tk.Button(root,text="Submit",command=readBlobData,font=('Times New Roman',15,'bold'),width=14,bg='black',fg='linen')
sub.place(x=100,y=300)

exit = tk.Button(root,text="Exit",command=Exit,font=('Times New Roman',15,'bold'),width=14,bg='black',fg='linen')
exit.place(x=350,y=300)

root.mainloop()

from PIL import Image

