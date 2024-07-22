from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox, simpledialog
import tkinter.simpledialog as simpledialog
import mysql.connector as myscon
from datetime import datetime
from tkinter import simpledialog

def call_users(userName, user_table, con, cur, root):


    # root.withdraw()
    root.destroy()
    splitter = ["✪𓂀₪⚡ཀ"]
    cur.execute(f"UPDATE {user_table} SET Messages = %s WHERE Username = %s", 
                (f"348923rbb{splitter[0]}asdklfj{splitter[0]}asdjfkfsdaj{splitter[0]}r\n\\n\n\n\n\n\nn\n\n\n\n\n\n\n\neuiyhtiuewr\nBAU\nBBA\nUB\nA\nU\nB\nA\nU\n\n\nBAUBA\n{splitter[0]}[2024-07-22 22:36:01]{splitter[0]}1234567890{splitter[0]}123456789012345678790@12D{splitter[0]}4758921374\nBAUBBAUBAUBAUBAUBA\n{splitter[0]}", userName3))

    def logout():
        win.destroy()
        # root.deiconify()
        return

    def editNote():
        win.withdraw()
        cur.execute(f"SELECT Notes FROM {user_table} WHERE Username = %s", (userName,))
        note = cur.fetchone()[0]
        matching = [note]
        
        def cancel():
            note_win.destroy()
            win.deiconify()

        def save_note():
            new_note = note_text.get("1.0", "end-1c")
            if matching[0] != new_note:
                cur.execute(f"UPDATE {user_table} SET Notes = %s WHERE Username = %s", (new_note, userName))
                con.commit()
            messagebox.showinfo(title='Note Saved', message='Your note has been updated!')

            note_win.destroy()
            win.deiconify()


        note_win = Toplevel(win)
        note_win.title('Edit Notes')
        note_win.geometry('+380+210')
        note_win.resizable(0, 0)
        note_win.config(bg='sky blue')

        Label(note_win, text='Your Notes:', font=('Arial', 20, 'bold'), bg='sky blue', fg='dark blue').pack(padx=10, pady=10)

        frame = Frame(note_win)
        frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        note_text = Text(frame, wrap='word', yscrollcommand=scrollbar.set, width=50, height=15)
        note_text.insert('1.0', note if note else '')
        note_text.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.config(command=note_text.yview)

        Button(note_win, text='Save', font=('Arial', 20), command=save_note, width=20, border=5).pack(padx=5, pady=5)
        Button(note_win, text='Cancel', font=('Arial', 20), command=cancel, width=20, border=5).pack(padx=5, pady=5)


    def sendMessage():
        win.withdraw()
        def cancel():
            send_win.destroy()
            win.deiconify()
        def send():
            recipient = recipient_entry.get().strip()
            subject = subject_entry.get().strip()
            message = message_text.get("1.0", "end-1c").strip()
            
            if recipient and message:
                cur.execute(f"SELECT Username FROM {user_table} WHERE Username = %s", (recipient,))
                if cur.fetchone():
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    formatted_message = f"[{current_time}]{splitter[0]}{userName}{splitter[0]}{subject}{splitter[0]}{message}{splitter[0]}"
                    cur.execute(f"UPDATE {user_table} SET Messages = CONCAT(IFNULL(Messages, ''), %s) WHERE Username = %s", 
                                (formatted_message, recipient))
                    con.commit()
                    messagebox.showinfo(title='Message Sent', message='Your message has been sent!')
                    send_win.destroy()
                    win.deiconify()
                else:
                    messagebox.showwarning(title='Error!', message='Recipient not found!')
            else:
                messagebox.showwarning(title='Error!', message='Please enter both recipient and message!')

        send_win = Toplevel(win)
        send_win.title('Send Message')
        send_win.geometry('+380+210')
        send_win.resizable(0, 0)
        send_win.config(bg='sky blue')

        Label(send_win, text='Message Composer', font=('Arial', 20, 'bold'), bg='sky blue', fg='dark blue').grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        Label(send_win, text='Recipient Username:', font=('Arial', 14), bg='sky blue', fg='dark blue').grid(row=1, column=0, padx=10, pady=10, sticky=W)
        recipient_entry = Entry(send_win, font=('Arial', 14), width=30)
        recipient_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        Label(send_win, text='Subject:', font=('Arial', 14), bg='sky blue', fg='dark blue').grid(row=2, column=0, padx=10, pady=10, sticky=W)
        subject_entry = Entry(send_win, font=('Arial', 14), width=30)
        subject_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        Label(send_win, text='Message:', font=('Arial', 14), bg='sky blue', fg='dark blue').grid(row=3, column=0, padx=10, pady=10, sticky=NW)

        message_frame = Frame(send_win, bg='sky blue')
        message_frame.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        message_text = Text(message_frame, wrap='word', font=('Arial', 14), width=30, height=10)
        message_text.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(message_frame, command=message_text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        message_text.config(yscrollcommand=scrollbar.set)

        cancel_button = Button(send_win, text='Cancel', font=('Arial', 14), command=cancel, width=15, border=5, bg='red', activebackground='light coral')
        cancel_button.grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky=W)

        send_button = Button(send_win, text='Send Message', font=('Arial', 14), command=send, width=28, border=5, bg='green', activebackground='light green')
        send_button.grid(row=4, column=1, columnspan=1, padx=10, pady=10, sticky=W)



    def checkInbox():
        win.withdraw()
        messages_all = [[""]]
        cachedmessages = [""]
        
        def closeinbox():
            updated_messages = ""
            for item in treeview.get_children():
                values = treeview.item(item, 'values')
                if values:
                    date_time, user, sub, msg = values
                    updated_messages += f"{date_time}{splitter[0]}{user}{splitter[0]}{sub}{splitter[0]}{msg}{splitter[0]}"

            if updated_messages != cachedmessages[0]:
                cur.execute(f"UPDATE {user_table} SET Messages = %s WHERE Username = %s", 
                            (updated_messages, userName))
                con.commit()
                messagebox.showinfo(title='Inbox Closed', message='Changes saved successfully!')
            
            win.deiconify()
            inbox_win.destroy()

        def delete_message():
            selected_item = treeview.selection()
            if selected_item:
                treeview.delete(selected_item)
                text_box.config(state='normal')
                text_box.delete('1.0', 'end')
                text_box.config(state='disabled')
            else:
                messagebox.showwarning(title='Error!', message='No message selected for deletion!')

        def update_message_display(event):
            selected_item = treeview.selection()
            if selected_item:
                values = treeview.item(selected_item, 'values')
                if values:
                    date_time, user, sub, msg = values
                    formatted_text = f"{date_time}\nFrom: {user}\nSubject: {sub}\n\nMessage:\n\n{msg}"
                    text_box.config(state='normal')
                    text_box.delete('1.0', 'end')
                    text_box.insert('1.0', formatted_text)

                    text_box.tag_configure('bold', font=('Arial', 11, 'bold'))
                    text_box.tag_configure('blue', font=('Arial', 11, 'bold'), foreground='blue')
                    text_box.tag_configure('red', font=('Arial', 11, 'bold'), foreground='red')
                    text_box.tag_configure('green', font=('Arial', 11, 'bold'), foreground='green')
                    
                    text_box.tag_add('bold', '2.0', '2.5')
                    text_box.tag_add('bold', '3.0', '3.8')
                    text_box.tag_add('bold', '5.0', '5.8')
                    text_box.tag_add('blue', '1.0', f'1.{len(date_time)}')
                    text_box.tag_add('red', '2.6', f'2.{7+len(user)}')
                    text_box.tag_add('green', '3.9', f'3.{10+len(sub)}')

                    text_box.config(state='disabled')

        def populate_inbox():
            cur.execute(f"SELECT Messages FROM {user_table} WHERE Username = %s", (userName,))
            cachedmessages[0] = cur.fetchone()[0]
            messages = cachedmessages[0].split(splitter[0])
            messages_all[0] = [messages[i:i+4] for i in range(0, len(messages), 4)]

            for msg in messages_all[0]:
                if len(msg) == 4:
                    treeview.insert("", "end", values=msg)

        inbox_win = Toplevel(win)
        inbox_win.title('Inbox')
        inbox_win.geometry('+380+210')
        inbox_win.resizable(0, 0)
        inbox_win.config(bg='sky blue')

        Label(inbox_win, text='Your Inbox', font=('Arial', 20, 'bold'), bg='sky blue', fg='dark blue').grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        frame = Frame(inbox_win, bg='sky blue')
        frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        columns = ('DateTime', 'Username', 'Subject')
        treeview = ttk.Treeview(frame, columns=columns, height=15, show='headings')
        treeview.column('DateTime', width=150, minwidth=150, anchor='w')
        treeview.column('Username', width=150, minwidth=150, anchor='w')
        treeview.column('Subject', width=300, minwidth=300, anchor='w')
        treeview.heading('DateTime', text='DateTime')
        treeview.heading('Username', text='Username')
        treeview.heading('Subject', text='Subject')

        vsb = Scrollbar(frame, orient="vertical", command=treeview.yview)
        treeview.configure(yscrollcommand=vsb.set)
        treeview.grid(row=0, column=0)
        vsb.grid(row=0, column=1, sticky='ns')

        text_frame = Frame(frame)
        text_frame.grid(row=0, column=2, padx=10, sticky='ns')

        text_box = Text(text_frame, height=15, width=60, wrap='word', state='disabled')
        text_box.pack(side='left', fill='both', expand=True)

        text_vsb = Scrollbar(text_frame, orient="vertical", command=text_box.yview)
        text_box.config(yscrollcommand=text_vsb.set)
        text_vsb.pack(side='right', fill='y')

        Button(inbox_win, text='Delete Message', font=('Arial', 15), command=delete_message, width=52, border=5, fg='white', bg='red', activebackground='light coral').grid(row=2, column=0, padx=10, pady=5, sticky='w')
        Button(inbox_win, text='Close', font=('Arial', 15), command=closeinbox, width=42, border=5, fg='white', bg='red', activebackground='light coral').grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky='w')

        treeview.bind('<<TreeviewSelect>>', update_message_display)

        populate_inbox()

    
    def ch_pass():
        def change():
            old_password = e1.get()
            new_password = e2.get()
            
            if not old_password or not new_password:
                messagebox.showwarning(title='Error!', message='Please Enter a Password!')
                return

            cur.execute(f"SELECT Password FROM {user_table} WHERE Username=%s", (userName,))
            rec = cur.fetchone()
            
            if rec and rec[0] == old_password:
                if len(new_password) < 10:
                    messagebox.showwarning(title='Error!', message='Password Length should be >= 10!')
                    return
                cur.execute(f"UPDATE {user_table} SET Password=%s WHERE Username=%s", (new_password, userName))
                con.commit()
                messagebox.showinfo(title='Done!', message='Password Changed!')
                p.destroy()
                win.deiconify()
            else:
                messagebox.showwarning(title='Error!', message='Incorrect Old Password!')
                return

        def toggle_password1():
            e1.config(show='' if c1_var.get() else '*')
            
        def toggle_password2():
            e2.config(show='' if c2_var.get() else '*')
            
        def on_close():
            p.destroy()
            win.deiconify()

        win.withdraw()
        
        p = Toplevel(win)
        p.resizable(0, 0)
        p.geometry('+380+210')
        p.config(bg='lightblue')
        p.protocol("WM_DELETE_WINDOW", on_close)
        p.title("Change Password")

        Label(p, text='Enter Old Password: ', bg='lightblue', font=('Arial', 20), width=20).grid(row=0, column=0, padx=5, pady=5)
        e1 = Entry(p, font=('Arial', 20), width=20, show='*')
        e1.grid(row=0, column=1, padx=5, pady=5)

        c1_var = BooleanVar(value=False)
        c1 = Checkbutton(p, text='Show Password', bg='lightblue', variable=c1_var, command=toggle_password1)
        c1.grid(row=0, column=2, padx=5)

        Label(p, text='Enter New Password: ', bg='lightblue', font=('Arial', 20), width=20).grid(row=1, column=0, padx=5, pady=5)
        e2 = Entry(p, font=('Arial', 20), width=20, show='*')
        e2.grid(row=1, column=1, padx=5, pady=5)

        c2_var = BooleanVar(value=False)
        c2 = Checkbutton(p, text='Show Password', bg='lightblue', variable=c2_var, command=toggle_password2)
        c2.grid(row=1, column=2, padx=5)

        Button(p, text='Change', font=('Arial', 20), bg='green', fg='white', activebackground='lightgreen', command=change, width=20, border=5).grid(row=2, column=0, padx=5, pady=5)
        Button(p, text='Cancel', font=('Arial', 20), bg='red', fg='white', activebackground='light coral', command=on_close, width=20, border=5).grid(row=2, column=1, padx=5, pady=5)


    win = Tk()
    win.geometry('+380+210')
    win.resizable(0,0)
    win.title(userName)
    win.config(bg='sky blue')

    Label(win, text='Welcome ' + userName, font=('Times New Roman', 30), bg='sky blue', fg='dark blue').grid(row=0, column=0, columnspan=2)
    Button(win, text='Send Message', font=('Arial', 20), bg='blue', fg='white', activebackground='lightblue', command=sendMessage, width=20, border=5).grid(row=1, column=0, padx=5, pady=5)
    Button(win, text='Check Inbox', font=('Arial', 20), bg='blue', fg='white', activebackground='lightblue', command=checkInbox, width=20, border=5).grid(row=2, column=0, padx=5, pady=5)
    Button(win, text='Make Notes', font=('Arial', 20), bg='green', fg='white', activebackground='lightgreen', command=editNote, width=20, border=5).grid(row=1, column=1, padx=5, pady=5)
    Button(win, text='Change Password', font=('Arial', 20), bg='green', fg='white', activebackground='lightgreen', command=ch_pass, width=20, border=5).grid(row=2, column=1, padx=5, pady=5)
    Button(win, text='LOG OUT', font=('Arial', 20), bg='red', fg='white', activebackground='light coral', command=logout, width=20, border=5).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    

    win.mainloop()
