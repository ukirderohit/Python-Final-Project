from Tkinter import *
from sqlite3 import dbapi2 as sqlite

login=sqlite.connect("grocery.sqlite")
l=login.cursor()


def again():    #for login window-----------------------------------------------------------------------------LOGIN WINDOW
    global un, pwd, flag, root, apt
    root=Tk()
    root.title('INDIAN GROCERY STORE')
    Label(root,text='INDIAN GROCERY STORE').grid(row=0,column=0,columnspan=5)
    Label(root,text="1602 ,Chatham Hills, Springfield-62704, Illinois").grid(row=1,column=0,columnspan=5)
    Label(root,text='--------------------------------------------------------------').grid(row=2,column=0,columnspan=5)
    Label(root, text='Username').grid(row=3, column=1)
    un=Entry(root,width=10)
    un.grid(row=3, column=2)
    Label(root, text='Password').grid(row=4, column=1)
    pwd=Entry(root,width=10, show="*")
    pwd.grid(row=4, column=2)
    Label(root,text='').grid(row=5,column=0,columnspan=5)
    Button(root,width=6,text='Enter',command=check).grid(row=6, column=1)
    Button(root,width=6,text='Close',command=root.destroy).grid(row=6, column=2)
    root.mainloop()
    
def check():    #for enter button in login window
    global un, pwd, login, l, root
    u=un.get()
    p=pwd.get()
    l.execute("select * from logs")
    for i in l:     
        if i[0]==u and i[1]==p and u=='admin':
            root.destroy()
            open_win()
        elif i[0]==u and i[1]==p:
            root.destroy()
            open_cus()
        elif i[0]==u or i[1]==p:
            top=Tk()
            Label(top,width=30, text='Wrong Password or Username').grid(row=0, column=0)
            top.mainloop()
    login.commit()


    
    
again()