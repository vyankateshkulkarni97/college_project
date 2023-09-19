# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:25:37 2021

@author: srcdo
"""

# import required modules
import mysql.connector
  
# create connection object
con = mysql.connector.connect(
  host="localhost", user="root",
  password="", database="car")
  
# create cursor object
cursor = con.cursor()
  

result1="IT20BOM"
# executing cursor
r_set=cursor.execute("Select * From car where car_no =" +result1)
print("Query_Result:"+str(r_set))
  