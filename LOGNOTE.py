from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import for_students
import for_admin

def driverLognote(user_host, user_port, user_name, user_pass, user_db, user_table, con, cur):

    root = Tk()
    img  = ImageTk.PhotoImage(Image.open('bgimg.png'))
    root.geometry('+400+150')
    root.title('LOGNOTE')
    root.resizable(0,0)
    # root.iconbitmap('icon1.ico')

    Label(image=img).grid(row=0,column=0,columnspan=3,rowspan=4)

    # LOGIN
    def Login():
        u = user_enter.get().strip()
        p = pass_enter.get()

        if u=='admin' and p=='admin':
            root.destroy()
            for_admin.call_admin(user_host, user_port, user_name, user_pass, user_db, user_table, con, cur)
            return

        cur.execute(f'select * from {user_table};')
        rec  = cur.fetchall()
        flag = 0
        for i in rec:
            if i[4] == u and i[5] == p:
                root.destroy()
                for_students.call_students(u, p, i[1])
                flag = 1
        if flag == 0:
            messagebox.showwarning(title='Error!', message='Invalid Username/Password!')  
        return


    # OBJECTS

    Label(root,text='LOGIN', font=('Times New Roman',40),bg='sky blue').grid(row=0,column=0,columnspan=2)

    Label(root,text='Enter Username:', font=('Arial',20),bg='sky blue').grid(row=1,column=0,pady=5)
    user_enter=Entry(root,text='Enter Username:', font=('Calibri',20),width=20,border=5,bg='light blue')
    user_enter.grid(row=1,column=1,padx=5,pady=5)
    user_enter.focus()

    Label(root,text='Enter Password:', font=('Arial',20),bg='sky blue').grid(row=2,column=0,pady=5)
    pass_enter=Entry(root, font=('Calibri',20), width=20,border=5,bg='light blue',show='*')
    pass_enter.grid(row=2,column=1,padx=5,pady=5)

    login=Button(root,text='LOGIN',font=('Calibri',20),border=5,width=20,command=Login,bg='green',fg='white')
    login.grid(row=3,column=0,padx=6)
    root.bind('<Return>', lambda event=None: login.invoke())

    Button(root,text='CANCEL',font=('Calibri',20),border=5,width=20,command=root.destroy,bg='red',fg='white').grid(row=3,column=1)

    root.mainloop()
