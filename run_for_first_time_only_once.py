# Run this file only once when using LOGNOTE for the first time.
# This file creates a database called 'records' for you.
# in that database, it automatically creates a table called 'students'.
# all the work will be done in this database and this table only.

import mysql.connector as m
import time

passw=input('Enter your MySQL Password: ')
user=input('Enter your MySQL Username: ')

with open('user-pass.txt','w') as f:
    f.write(passw+'\n'+user)
    
print('SET!')

time.sleep(0.5)

with open('user-pass.txt','r') as f:
    user_pass=f.readlines()
    mysqlpass=user_pass[0][:-1:1]
    mysqluser=user_pass[1]

try:
    con=m.connect(user=mysqluser,passwd=mysqlpass,host='localhost') 
    cur=con.cursor()
    cur.execute('CREATE DATABASE records;')
    cur.execute('USE records;')
    cur.execute('CREATE TABLE students\
                (SNo int,\
                 Name varchar(20),\
                 Class int,\
                 Section char(1),\
                 Username varchar(30) primary key,\
                 Password varchar(30));')
    con.close()
    print('DATABASE AND TABLE CREATED!')
    time.sleep(1.5)
    
except:
    print()
    input('DATABASE ALREADY EXISTS! Press ENTER to close this file...')
    time.sleep(1.5)










