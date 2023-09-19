# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:05:43 2021

@author: sheet
"""

import sqlite3

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        abc=file.write(data)
        
    print("Stored blob data into: ", filename, "\n")

def readBlobData(empId):
    try:
        sqliteConnection = sqlite3.connect('evaluation (1).db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            #resumeFile = row[3]

            print("Storing employee image and resume on disk \n")
            photoPath = "D:/Number_plate_recognization/Number_plate_recognization/profile images//" + name + ".jpg"
            #resumePath = "E:/Number_plate_recognization/profile images/1.jpg\\" + name + "_resume.txt"
            writeTofile(photo, photoPath)
            #writeTofile(resumeFile, resumePath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

readBlobData(1)
#readBlobData(2)
