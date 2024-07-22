from tkinter import *
from tkinter import messagebox, simpledialog
import tkinter.simpledialog as simpledialog

def call_students(userName, user_table, con, cur, root):
    root.withdraw()

    def logout():
        win.destroy()
        root.deiconify()
        return

    def editNote():
        def save_note():
            new_note = note_text.get("1.0", "end-1c")  # Get the text from the Text widget
            cur.execute(f"UPDATE {user_table} SET Notes = %s WHERE Username = %s", (new_note, userName))
            con.commit()
            messagebox.showinfo(title='Note Saved', message='Your note has been updated!')
            note_win.destroy()

        cur.execute(f"SELECT Notes FROM {user_table} WHERE Username = %s", (userName,))
        note = cur.fetchone()[0]

        note_win = Toplevel(win)
        note_win.title('Edit Notes')
        note_win.geometry('+400+200')
        note_win.resizable(0,0)
        note_win.config(bg='sky blue')

        Label(note_win, text='Your Notes:', font=('Arial', 20), bg='sky blue', fg='dark blue').pack(padx=10, pady=10)
        note_text = Text(note_win, wrap='word', width=50, height=15)
        note_text.insert('1.0', note if note else '')
        note_text.pack(padx=10, pady=10)

        Button(note_win, text='Save', font=('Arial', 20), command=save_note, width=20, border=5).pack(padx=5, pady=5)
        Button(note_win, text='Cancel', font=('Arial', 20), command=note_win.destroy, width=20, border=5).pack(padx=5, pady=5)

    def sendMessage():
        def send():
            recipient = simpledialog.askstring("Recipient", "Enter the username of the recipient:")
            message = simpledialog.askstring("Message", "Enter your message:")
            if recipient and message:
                cur.execute(f"SELECT Username FROM {user_table} WHERE Username = %s", (recipient,))
                if cur.fetchone():
                    cur.execute(f"UPDATE {user_table} SET Messages = CONCAT(Messages, %s) WHERE Username = %s", 
                                (f"{userName}: {message}\n", recipient))
                    con.commit()
                    messagebox.showinfo(title='Message Sent', message='Your message has been sent!')
                else:
                    messagebox.showwarning(title='Error!', message='Recipient not found!')
            send_win.destroy()

        send_win = Toplevel(win)
        send_win.title('Send Message')
        send_win.geometry('+400+200')
        send_win.resizable(0,0)
        send_win.config(bg='sky blue')

        Button(send_win, text='Send Message', font=('Arial', 20), command=send, width=20, border=5).pack(padx=10, pady=10)
        Button(send_win, text='Cancel', font=('Arial', 20), command=send_win.destroy, width=20, border=5).pack(padx=10, pady=10)

    def checkInbox():
        def delete_message():
            selected_message = inbox_listbox.get(ACTIVE)
            if selected_message:
                cur.execute(f"SELECT Messages FROM {user_table} WHERE Username = %s", (userName,))
                messages = cur.fetchone()[0]
                updated_messages = messages.replace(f"{inbox_sender.get()}: {selected_message}\n", "")
                cur.execute(f"UPDATE {user_table} SET Messages = %s WHERE Username = %s", (updated_messages, userName))
                con.commit()
                messagebox.showinfo(title='Message Deleted', message='The selected message has been deleted!')
                populate_inbox()
        
        def populate_inbox():
            inbox_listbox.delete(0, END)
            cur.execute(f"SELECT Messages FROM {user_table} WHERE Username = %s", (userName,))
            messages = cur.fetchone()[0]
            if messages:
                for message in messages.split('\n'):
                    if message:
                        inbox_listbox.insert(END, message)

        inbox_win = Toplevel(win)
        inbox_win.title('Inbox')
        inbox_win.geometry('+400+200')
        inbox_win.resizable(0,0)
        inbox_win.config(bg='sky blue')

        Label(inbox_win, text='Select Sender:', font=('Arial', 15), bg='sky blue', fg='dark blue').pack(pady=5)
        inbox_sender = StringVar()
        sender_menu = OptionMenu(inbox_win, inbox_sender, *get_usernames())
        sender_menu.pack(pady=5)
        
        inbox_listbox = Listbox(inbox_win, width=70, height=15)
        inbox_listbox.pack(pady=10)
        
        Button(inbox_win, text='Delete Message', font=('Arial', 15), command=delete_message, width=20, border=5).pack(pady=5)
        Button(inbox_win, text='Close', font=('Arial', 15), command=inbox_win.destroy, width=20, border=5).pack(pady=5)
        
        populate_inbox()
    
    def get_usernames():
        cur.execute(f"SELECT Username FROM {user_table}")
        return [row[0] for row in cur.fetchall()]

    def ch_pass():
        def change():
            if e2.get()=='' or e1.get()=='':
                messagebox.showwarning(title='Error!', message='Please Enter a Password!')
                return
            if len(e2.get()) < 10:
                messagebox.showwarning(title='Error!', message='Password Length should be >= 10!')
                return

            cur.execute(f"select Password from {user_table} WHERE Username='{userName}'")
            rec=cur.fetchall()
            if rec[0][1]==e1.get():
                cur.execute(f'update {user_table} set Password=\'{e2.get()}\' where Username=\'{userName}\';')
                con.commit()
                messagebox.showinfo(title='Done!', message='Password Changed!')
                p.destroy()
            else:
                messagebox.showwarning(title='Error!', message='Incorrect Old Password!')
                return

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

    win = Tk()
    win.geometry('+380+210')
    win.resizable(0,0)
    win.title(userName)
    win.config(bg='sky blue')

    Label(win, text='Welcome ' + userName, font=('Times New Roman', 30), bg='sky blue', fg='dark blue').grid(row=0, column=0, columnspan=2)
    Button(win, text='Make Notes', font=('Arial', 20), bg='green', fg='white', command=editNote, width=20, border=5).grid(row=1, column=0, padx=5, pady=5)
    Button(win, text='Send Message', font=('Arial', 20), bg='blue', fg='white', command=sendMessage, width=20, border=5).grid(row=1, column=1, padx=5, pady=5)
    Button(win, text='Check Inbox', font=('Arial', 20), bg='red', fg='white', command=checkInbox, width=20, border=5).grid(row=2, column=0, padx=5, pady=5)
    Button(win, text='CHANGE PASSWORD', font=('Arial', 20), bg='black', fg='white', command=ch_pass, width=20, border=5).grid(row=2, column=1, padx=5, pady=5)
    Button(win, text='LOG OUT', font=('Arial', 20), bg='red', fg='white', command=logout, width=20, border=5).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    win.mainloop()
