# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:50:59 2021

@author: srcdo
"""
import tkinter as tk
from PIL import Image , ImageTk
import os
from tkinter.filedialog import askopenfilename
from google.cloud import vision
import sqlite3
from textblob import TextBlob 
from PIL import Image
import mysql.connector
# my_conn = sqlite3.connect('evaluation_1.db')
# print("Connection Done")

# string1 = "5YJSA1DG9DFPDFP14705"
# r_set = my_conn.execute("""Select * From reg Where chassis_no = """,(str(string1)));
      
# print("Query_Result:"+str(r_set))
db=MySQLdb.connect(
   user="root"
  ,passwd=""
  ,db="my_db"
  ,unix_socket="/opt/lampp/var/mysql/mysql.sock")
