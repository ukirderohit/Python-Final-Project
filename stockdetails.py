from Tkinter import *
from sqlite3 import dbapi2 as sqlite

columns=('Sl No', 'Name', 'Type', 'Quantity Left', 'Cost', 'Purpose', 'Expiry Date', 'Rack location', 'Manufacture')

c=sqlite.connect("grocery.sqlite")
cur=c.cursor()

def stock():
    global cur, c, columns, accept, flag, sto, application
    flag='sto'
    accept=['']*10
    sto=Tk()
    sto.title('Add Stock')
    Label(sto,text='Enter a New Item to the Grocery Stock').grid(row=0,column=0,columnspan=2)
    Label(sto,text='-'*50).grid(row=1,column=0,columnspan=2)
    
    
    Label(sto,width=15,text=str(columns[0])+':',justify=LEFT).grid(row=3,column=0,sticky=W)
    accept[0]=Entry(sto)
    accept[0].grid(row=3, column=1)
    Label(sto,width=15,text=str(columns[1])+':',justify=LEFT).grid(row=4,column=0,sticky=W)
    accept[1]=Entry(sto)
    accept[1].grid(row=4, column=1)
    Label(sto,width=15,text=str(columns[2])+':',justify=LEFT).grid(row=5,column=0,sticky=W)
    accept[2]=Entry(sto)
    accept[2].grid(row=5, column=1)
    Label(sto,width=15,text=str(columns[3])+':',justify=LEFT).grid(row=6,column=0,sticky=W)
    accept[3]=Entry(sto)
    accept[3].grid(row=6, column=1)
    Label(sto,width=15,text=str(columns[4])+':',justify=LEFT).grid(row=7,column=0,sticky=W)
    accept[4]=Entry(sto)
    accept[4].grid(row=7, column=1)
    Label(sto,width=15,text=str(columns[5])+':',justify=LEFT).grid(row=8,column=0,sticky=W)
    accept[5]=Entry(sto)
    accept[5].grid(row=8, column=1)
    Label(sto,width=15,text=str(columns[6])+':',justify=LEFT).grid(row=9,column=0,sticky=W)
    accept[6]=Entry(sto)
    accept[6].grid(row=9, column=1)
    Label(sto,width=15,text=str(columns[7])+':',justify=LEFT).grid(row=10,column=0,sticky=W)
    accept[7]=Entry(sto)
    accept[7].grid(row=10, column=1)
    Label(sto,width=15,text=str(columns[8])+':',justify=LEFT).grid(row=11,column=0,sticky=W)
    accept[8]=Entry(sto)
    accept[8].grid(row=11, column=1)
    
    
    
    Button(sto,width=15,text='Submit').grid(row=12,column=1)
    Label(sto,text='-'*165).grid(row=13,column=0,columnspan=7)
    Button(sto,width=15,text='Reset').grid(row=12,column=0)
    Button(sto,width=15,text='Refresh stock').grid(row=12,column=4)
    for i in range(1,6):
        Label(sto,text=columns[i]).grid(row=14,column=i-1)
    Label(sto,text='Exp           Rack   Manufacturer                      ').grid(row=14,column=5)
    Button(sto,width=10,text='Main Menu').grid(row=12,column=5)
    ref()
    sto.mainloop()
    
    
    
def chk(): #checks if the medicine is already present so that can be modified
    global cur, c, accept, sto
    cur.execute("select * from med")
    for i in cur:
        if accept[6].get()==i[6] and i[1]==accept[1].get():
            sql="update med set qty_left = '%s' where name = '%s'" % (str(int(i[3])+int(accept[3].get())),accept[1].get())
            cur.execute(sql)
            c.commit()
            top=Tk()
            Label(top,width=20, text='Modified!').pack()
            top.mainloop()
            main_menu()
        else:
            submit()
    c.commit()
    
    
    
def reset():
    global sto, accept
    for i in range(1,len(columns)):
        Label(sto,width=15,text=' '*(14-len(str(columns[i])))+str(columns[i])+':').grid(row=i+2,column=0)
        accept[i]=Entry(sto)
        accept[i].grid(row=i+2, column=1)
        
        
def ref(): # creates a multi-listbox manually to show the whole database 
    global sto, c, cur
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
        lb3.yview(*args)
        lb4.yview(*args)
        lb5.yview(*args)
        lb6.yview(*args)

    def onmousewheel():
        lb1.ywiew=('scroll',event.delta,'units')
        lb2.ywiew=('scroll',event.delta,'units')
        lb3.ywiew=('scroll',event.delta,'units')
        lb4.ywiew=('scroll',event.delta,'units')
        lb5.ywiew=('scroll',event.delta,'units')
        lb6.ywiew=('scroll',event.delta,'units')
        
        return 'break'
    cx=0
    vsb=Scrollbar(orient='vertical',command=onvsb)
    lb1=Listbox(sto,yscrollcommand=vsb.set)
    lb2=Listbox(sto,yscrollcommand=vsb.set)
    lb3=Listbox(sto,yscrollcommand=vsb.set,width=10)
    lb4=Listbox(sto,yscrollcommand=vsb.set,width=7)
    lb5=Listbox(sto,yscrollcommand=vsb.set,width=25)
    lb6=Listbox(sto,yscrollcommand=vsb.set,width=37)
    vsb.grid(row=15,column=6,sticky=N+S)
    lb1.grid(row=15,column=0)
    lb2.grid(row=15,column=1)
    lb3.grid(row=15,column=2)
    lb4.grid(row=15,column=3)
    lb5.grid(row=15,column=4)
    lb6.grid(row=15,column=5)
    lb1.bind('<MouseWheel>',onmousewheel)
    lb2.bind('<MouseWheel>',onmousewheel)
    lb3.bind('<MouseWheel>',onmousewheel)
    lb4.bind('<MouseWheel>',onmousewheel)
    lb5.bind('<MouseWheel>',onmousewheel)
    lb6.bind('<MouseWheel>',onmousewheel)
    cur.execute("select * from grocerylist")
    for i in cur:
        cx+=1
        lb1.insert(cx,str(i[0])+'. '+str(i[1]))
        lb2.insert(cx,i[2])
        lb3.insert(cx,i[3])
        lb4.insert(cx,i[4])
        lb5.insert(cx,i[5])
        # lb6.insert(cx,i[6]+'    '+i[7]+'    '+i[8])
    c.commit()
stock()