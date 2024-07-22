from tkinter import *
import os
import mysql.connector as m
from tkinter import messagebox
import LOGNOTE

def create_file(u,p):
    file=open(os.getcwd()+'/student_info/'+u+'.txt','w')
    file.write(u+'\n'+p+'\n')
    file.close()

def delete_file(u):
    os.remove(os.getcwd()+'\\student_info\\'+u+'.txt')

def call_students(u,p,un):
    def logout():
        win.destroy()
        LOGNOTE.driver()
        
    def make():
        def done1():
            if len(entry.get(1.0,END))==1:
                return
            else:
                file=open(os.getcwd()+'\\student_info\\'+u+'.txt','a')
                file.write(entry.get(1.0,END)+'\n')
                file.close()
                entry.delete(1.0,END)

        m=Toplevel(win)
        m.resizable(0,0)
        entry=Text(m,font=('Calibri',15),height=15)
        entry.grid(row=0,column=0)
        Button(m,text='SAVE',font=('Arial',30),bg='green',fg='white',command=done1).grid(row=1,column=0)
        scroll=Scrollbar(m,orient=VERTICAL,command=entry.yview)
        scroll.grid(row=0,column=1,sticky=NS)
        entry.configure(yscrollcommand=scroll.set)
   
    def edit():
        def done2():
            file=open(os.getcwd()+'\\student_info\\'+u+'.txt','w')
            file.write(entry.get(1.0,END))
            file.close()

        file=open(os.getcwd()+'\\student_info\\'+u+'.txt')    
        e=Toplevel(win)
        e.resizable(0,0)
        entry=Text(e,font=('Calibri',15),height=15)
        entry.grid(row=0,column=0)
        entry.insert(END,file.read())
        Button(e,text='SAVE',font=('Arial',30),bg='green',fg='white',command=done2).grid(row=1,column=0)
        scroll=Scrollbar(e,orient=VERTICAL,command=entry.yview)
        scroll.grid(row=0,column=1,sticky=NS)
        entry.configure(yscrollcommand=scroll.set)
        file.close()

    def ch_pass():
        def change():
            if e2.get()=='' or e1.get()=='':
                messagebox.showwarning(title='Error!', message='Please Enter a Password!')
                return
            con=m.connect(user=mysqluser,passwd=mysqlpass,host='localhost',database='records')
            cur=con.cursor()
            cur.execute('select * from students order by class,name')
            rec=cur.fetchall()
            for i in rec:
                if i[4]==u:
                    if i[5]==e1.get():
                        cur.execute(f'update students set Password=\'{e2.get()}\' where Username=\'{u}\';')
                        con.commit()
                        messagebox.showinfo(title='Done!', message='Password Changed!')
                        con.close()
                        p.destroy()
                    else:
                        messagebox.showwarning(title='Error!', message='Incorrect Old Password!')
            con.close()
        def toggle_password1():
            if c1.var.get():
                e1['show'] = ""
            else:
                e1['show'] = "*"
        def toggle_password2():
            if c2.var.get():
                e2['show'] = ""
            else:
                e2['show'] = "*"
        global c1,c2,e1,e2        
        p=Toplevel(win)
        p.resizable(0,0)
        p.geometry('+380+100')
        Label(p,text='Enter Old Password: ',font=('Arial',20),width=20).grid(row=0,column=0,padx=5,pady=5)
        e1=Entry(p,font=('Arial',20),width=20)
        e1.default_show_val=e1['show']
        e1['show']='*'
        e1.grid(row=0,column=1,padx=5,pady=5)
        
        c1=Checkbutton(p,text='Show Password',onvalue=True,offvalue=False,command=toggle_password1)
        c1.grid(row=0,column=2)
        c1.var=BooleanVar(value=False)
        c1['variable']=c1.var
        

        Label(p,text='Enter New Password: ',font=('Arial',20),width=20).grid(row=1,column=0,padx=5,pady=5)
        e2=Entry(p,font=('Arial',20),width=20)
        e2.default_show_val=e2['show']
        e2['show']='*'
        e2.grid(row=1,column=1,padx=5,pady=5)
        
        c2=Checkbutton(p,text='Show Password',onvalue=True,offvalue=False,command=toggle_password2)
        c2.grid(row=1,column=2)
        c2.var=BooleanVar(value=False)
        c2['variable']=c2.var
        

        Button(p,text='Change',font=('Arial',20),command=change,width=20,border=5).grid(row=2,column=0,padx=5,pady=5)
        Button(p,text='Cancel',font=('Arial',20),command=p.destroy,width=20,border=5).grid(row=2,column=1,padx=5,pady=5)
        
       
    win=Tk()
    win.geometry('+380+210')
    win.iconbitmap('icon1.ico')
    win.resizable(0,0)
    win.title(u)
    win.config(bg='sky blue')
    
    Label(win,text='Welcome '+un,font=('Times New Roman',30),bg='sky blue',fg='dark blue').grid(row=0,column=0,columnspan=2)
    Button(win,text='Make Notes',font=('Arial',20),bg='green',fg='white',command=make,width=20,border=5).grid(row=1,column=0,padx=5,pady=5)
    Button(win,text='Edit Notes',font=('Arial',20),bg='blue',fg='white',command=edit,width=20,border=5).grid(row=1,column=1,padx=5,pady=5)
    
    Button(win,text='CHANGE PASSWORD',font=('Arial',20),bg='black',fg='white',command=ch_pass,width=20,border=5).grid(row=2,column=0,padx=5,pady=5)
    Button(win,text='LOG OUT',font=('Arial',20),bg='red',fg='white',command=logout,width=20,border=5).grid(row=2,column=1,padx=5,pady=5)

    win.mainloop()
