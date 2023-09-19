import tkinter as tk
from PIL import Image , ImageTk
import os
from tkinter.filedialog import askopenfilename
from google.cloud import vision
import sqlite3
from textblob import TextBlob 
from PIL import Image


root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Number Plate Recognization")
car_no=tk.StringVar()

image2 =Image.open(r'i7.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)
lbl = tk.Label(root, text="Number Plate Recognization", font=('Broadway', 30,'bold'), height=1, width=30,bg="#98AFC7",fg="white")
lbl.place(x=300, y=35)

global file
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='D:/Number_plate_recognization/eighth-zenith-307507-d2981f2defff.json'



def Choose():
    global file
    file = askopenfilename(initialdir=r'', title='Select Image',
                                       filetypes=[("all files", "*.*")])
    
    image3 =Image.open(file)
    image3 =image3.resize((450,280), Image.ANTIALIAS)
    
    choosen_image=ImageTk.PhotoImage(image3)
    
    display = tk.Label(root, image=choosen_image)
    
    display.image= choosen_image
    
    display.place(x=10, y=100)
    

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
    # print('Texts:'+texts)
    # print('here {}'.format(texts.description))

    for text in texts:
       # print('')
        print('""'.format(text.description))
        
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

    #detect_text(file)
#detect_text(r'E:\OMKARS\OMKARS1\Electricity Theft\marathi3.jpg')
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        abc=file.write(data)
        #return abc
    
    print("Stored blob data into: ", filename, "\n")
    return filename
def remove(result):
            global result1
            result1 = result.replace(" ", "")
            return result1
def Text_Label():
        
        result = detect_text()
        print(result)
        print(type(result))
        result1 = result.replace(" ", "")
        #result_label = tk.Label(root,text=str(result),font=('Times New Roman',15,'bold'),width=30,height=10,bg='#F08080',fg='white')
        #button2 = tk.Button(root,text="show info",command=Text_Label,font=('Times New Roman',15,'bold'),width=14,bg='#FF8040',fg='black')
        #button2.place(x=600,y=250)
        # t1 = tk.Entry(root, text=Text_Label, width=20, font=('', 15))
        # t1.place(x=600, y=200)
        #result_label.place(x=500,y=100)
        #result = car_no.get()
        #carno = car_no.get()
        # sqliteConnection = sqlite3.connect('evaluation (1).db')
        # cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        # # Driver Program
        #string = "c a r_n o"
        #string = result
        # string1=(remove(result))
        # print(string1)
        # print(type(string1))
        # print(str(string1))
        # result1=7777
        # sql_fetch_blob_query = "select * from registration where car_no = ?"
        # cursor.execute(sql_fetch_blob_query, ( str(result1),))
        my_conn = sqlite3.connect('evaluation_1.db')
        print("Connection Done")
        print("Result1:"+result1)
        print(type(result1))
        res = ''.join(filter(lambda i: i.isdigit(), result1))
        print(res)
        r_set = my_conn.execute("Select * From reg where car ="+res);
       
        
        for row in r_set:
                print("Fullname = ", row[0], "address = ", row[1], "Email =", row[2],"Phoneno =", row[3],"Gender =", row[4],"age =", row[5],"photo =", row[6],"car_no =", row[9],"chassis_no =", row[8])
                Fullname = row[0]
                address = row[1]
                Email = row[2]
                Phoneno = row[3]
                Gender = row[4]
                age = row[5]
                photo = row[6]
                car_no = row[9]
                chassis_no = row[8]
                photoPath = r"D:\Number_plate_recognization\profile images\\" + Fullname + ".jpg"
                ph=writeTofile(photo, photoPath)
                load = Image.open(ph)
                render = ImageTk.PhotoImage(load)
                
                #img.place(x=0, y=0)
                #resumeFile = row[3]
                frame_alpr = tk.LabelFrame(root, text=" ---------------------------------Profile Details-------------------------------------", width=650, height=500, bd=5, font=('times', 15, ' bold '),bg="#FF8040")
                frame_alpr.grid(row=0, column=0, sticky='nw')
                frame_alpr.place(x=600, y=150)
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
                #cursor.close()
            #     except sqlite3.Error as error:
            # print("Failed to read blob data from sqlite table", error)
            # finally:
            #  if sqliteConnection:
            #      sqliteConnection.close()
            #      print("sqlite connection is closed")
    

        
            

#readBlobData("hh") 
        

def Exit():
    root.destroy()

button1 = tk.Button(root,text='Choose Image',command=Choose,font=('Times New Roman',15,'bold'),width=14,bg='#FF8040',fg='black')
button1.place(x=50,y=450)

button2 = tk.Button(root,text="Detect Text",command=Text_Label,font=('Times New Roman',15,'bold'),width=14,bg='#FF8040',fg='black')
button2.place(x=50,y=500)

# button3 = tk.Button(root,text="Detect Language",command=Detect_Language,font=('Times New Roman',12,'italic'),width=14,bg='black',fg='linen')
# button3.place(x=50,y=550)

# button4 = tk.Button(root,text="Convert to English",command=To_English,font=('Times New Roman',12,'italic'),width=14,bg='black',fg='linen')
# button4.place(x=50,y=600)

exit = tk.Button(root,text="Exit",command=Exit,font=('Times New Roman',15,'bold'),width=14,bg='red',fg='linen')
exit.place(x=50,y=550)


root.mainloop()

