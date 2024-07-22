from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import for_students
import LOGNOTE

def call_admin(user_host, user_port, user_name, user_pass, user_db, user_table, con, cur):

    global status

    win=Tk()
    win.geometry('+150+150')
    win.title('WELCOME ADMIN!')
    win.resizable(0,0)
    win.config(bg='sky blue')
    # win.iconbitmap('icon1.ico')


    # COMMANDS

    def cancel():
        win.destroy()
        LOGNOTE.driverLognote(user_host, user_port, user_name, user_pass, user_db, user_table, con, cur)
        
    def clear_fields():
        nam.delete(0,END)
        cla.set('Select')
        se.set('Select')

    def add():
        global status
        if nam.get()=='':
            status.destroy()
            status=Label(win,text='STATUS: ENTER NAME.',bg='sky blue',fg='dark blue')
            status.grid(row=1,column=0,sticky=W)
            return
        if cla.get()=='Select' or se.get()=='Select':
            status.destroy()
            status=Label(win,text='STATUS: SELECT CLASS/SECTION.',bg='sky blue',fg='dark blue')
            status.grid(row=1,column=0,sticky=W)
            return

        global st_user
        global st_pass
        st_name=(nam.get()).title().strip()
        st_list=st_name.lower().split(' ')
        st_pass=''

        for i in st_list:
            st_pass+=i
        st_user=(st_pass+'@'+str(cla.get())+se.get()).lower()
        t=(0,st_name,cla.get(),se.get().title(),st_user,st_pass)

        try:
            cur.execute(f'insert into {user_table} values{t}')
            con.commit()
        except:
            status.destroy()
            status=Label(win,text='STATUS: RECORD ALREADY EXISTS.',bg='sky blue',fg='dark blue')
            status.grid(row=1,column=0,sticky=W)
            return
        
        show_table()
        status.destroy()
        status=Label(win,text='STATUS: RECORD ADDED.',bg='sky blue',fg='dark blue')
        status.grid(row=1,column=0,sticky=W)

        # CREATE STUDENT FILE
        # for_students.create_file(st_user,st_pass)
        clear_fields()
        

    def show_table():
        tree.delete(*tree.get_children())
        cur.execute(f'select * from {user_table} order by Class desc, Section desc, Name desc;')
        rec = cur.fetchall()
        snum = len(rec)
        for i in range(len(rec)):
            tree.insert('',0,text=snum,values=(rec[i][1],rec[i][2],rec[i][3],rec[i][4],rec[i][5]))
            snum -= 1

    def delete_record():
        global status
        try:
            selection=tree.selection()
            selmon=tree.item(selection)['values'][3]
        except IndexError:
            status.destroy()
            status=Label(win,text='STATUS: SELECT RECORD TO DELETE.',bg='sky blue',fg='dark blue')
            status.grid(row=1,column=0,sticky=W)
            return
        except:
            status.destroy()
            status=Label(win,text='STATUS: SELECT ONE RECORD ONLY.',bg='sky blue',fg='dark blue')
            status.grid(row=1,column=0,sticky=W)
            return
        confirm=messagebox.askquestion("Confirm",f"Are you sure you want to delete the record of {selmon}?")  
        if confirm=='yes':
            cur.execute(f'delete from {user_table} where Username=\'{selmon}\';')
            con.commit()
        else:
            return
        eee.delete(0,END)
        show_table()
        status.destroy()
        status=Label(win,text='STATUS: RECORD DELETED.',bg='sky blue',fg='dark blue')
        status.grid(row=1,column=0,sticky=W)

        # CREATE STUDENT FILE
        # for_students.delete_file(selmon)

    # TREE

    tree=ttk.Treeview(win)
    tree.grid(row=2,column=3,rowspan=5,columnspan=2,padx=10,pady=10)
    tree['columns']=('Name','Class','Section','Username','Password')
    tree.column('#0',width=40,minwidth=40)
    tree.column('Name',width=150,minwidth=150)
    tree.column('Class',width=70,minwidth=70)
    tree.column('Section',width=70,minwidth=70)
    tree.column('Username',width=150,minwidth=150)
    tree.column('Password',width=150,minwidth=150)

    tree.heading('#0',text='SNo:',anchor=W)
    tree.heading('Name',text='Name:',anchor=W)
    tree.heading('Class',text='Class:',anchor=W)
    tree.heading('Section',text='Section:',anchor=W)
    tree.heading('Username',text='Username:',anchor=W)
    tree.heading('Password',text='Password:',anchor=W)
    show_table()

    # OBJECTS

    Label(win,text='THE AIR FORCE SCHOOL',font=('Times New Roman',30),bg='sky blue',fg='dark blue').grid(row=0,column=0,columnspan=5)
    status=Label(win,text='STATUS: None.',bg='sky blue',fg='dark blue')
    status.grid(row=1,column=0,sticky=W)


    Label(win, text='Enter Name:'.ljust(25),font=('Arial',15),bg='sky blue',fg='dark blue').grid(row=2,column=0,sticky=W,padx=5,pady=5)
    nam=Entry(win,width=15,font=('Arial',15),border=5)
    nam.grid(row=2,column=1,padx=10)
    nam.focus()

    Label(win, text='Select Class:'.ljust(25),font=('Arial',15),bg='sky blue',fg='dark blue').grid(row=3,column=0,sticky=W,padx=5,pady=5)

    cla=ttk.Combobox(win,width=16,font=('Arial',14),state='readonly')
    cla['values']=(1,2,3,4,5,6,7,8,9,10,11,12)
    cla.grid(row=3,column=1,padx=10)
    cla.set('Select')

    Label(win, text='Select Section:'.ljust(25),font=('Arial',15),bg='sky blue',fg='dark blue').grid(row=4,column=0,sticky=W,padx=5,pady=5)

    se=ttk.Combobox(win,width=16,font=('Arial',14),state='readonly')
    se['values']=('A','B','C','D','E')
    se.grid(row=4,column=1,padx=10)
    se.set('Select')

    Label(win,bg='sky blue',fg='dark blue').grid(row=5,column=0)

    add=Button(win,text='ADD STUDENT',font=('Calibri',15),command=add,width=15,border=5)
    add.grid(row=5,column=0,padx=5,pady=5)
    win.bind('<Return>',lambda event=None: add.invoke())
    Button(win,text='CLEAR FIELDS',font=('Calibri',15),command=clear_fields,width=15,border=5).grid(row=5,column=1,padx=5,pady=5)

    Button(win,text='DELETE RECORD',font=('Calibri',15),command=delete_record,width=15,border=5).grid(row=6,column=0,padx=5,pady=5)
    ddd=Label(win,text='NOTES:',bg='sky blue',fg='dark blue')
    ddd.grid(row=1,column=3)
    eee=Entry(win,width=69)
    eee.grid(row=1,column=4)

    Button(win,text='LOG OUT',font=('Calibri',15),command=cancel,width=15,border=5).grid(row=6,column=1,padx=5,pady=5)

    show_table()
    win.mainloop()
