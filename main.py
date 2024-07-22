# This file creates a table called students for you
# all the work will be done in this table only.

import mysql.connector as myscon
import sys
import LOGNOTE

try:
    with open('credentials.txt','r') as f:
        credentials = f.readlines()
    user_host = credentials[0].rstrip("\n")
    user_port = credentials[1].rstrip("\n")
    user_name = credentials[2].rstrip("\n")
    user_pass = credentials[3].rstrip("\n")
    user_db   = credentials[4].rstrip("\n")
    user_table= credentials[5].rstrip("\n")

except FileNotFoundError:
    print("credentials.txt file does not exist!\
          The file has been created.\
          Enter the credentials:")

    user_host = input("Enter host: ")
    user_port = input("Enter port (leave blank for default):")
    user_name = input("Enter username:")
    user_pass = input("Enter password:")
    user_db   = input("Enter databse name (new/existing):")
    user_table= input("Enter table name (new/existing):")

    with open('credentials.txt','w') as f:
        f.writelines([user_host, user_port, user_name, user_pass, user_db, user_table])


try:
    if user_port:
        con = myscon.connect(user=user_name, passwd=user_pass, host=user_host, port=int(user_port)) 
    else:
        con = myscon.connect(user=user_name, passwd=user_pass, host=user_host) 

    cur = con.cursor()

    try:
        cur.execute(f"CREATE DATABASE {user_db}")
    except myscon.Error as err:
        if err.errno == 1007:
            print("Database exists.")
        else:
            print("An Exception occurred:")
            print(err)
            sys.exit("Exiting...")

    cur.execute(f"USE {user_db}")
    cur.execute(f'CREATE TABLE {user_table}\
                (SNo int,\
                    Name varchar(20),\
                    Class int,\
                    Section char(1),\
                    Username varchar(30) primary key,\
                    Password varchar(30));')
    con.commit()
    print('TABLE CREATED!')

except myscon.Error as err:
    if err.errno == 1050:
        print("Table exists.")
    else:
        print("An Exception occurred:")
        print(err)
        sys.exit("Exiting...")

LOGNOTE.driverLognote(user_host, user_port, user_name, user_pass, user_db, user_table, con, cur)
con.commit()
con.close()
print("graceful exit...")
