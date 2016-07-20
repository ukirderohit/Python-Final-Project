from Tkinter import *
from sqlite3 import dbapi2 as sqlite

columns=('Sl No', 'Name', 'Type', 'Quantity Left', 'Cost', 'Purpose', 'Expiry Date', 'Rack location', 'Manufacture')

def stock():
    global cur, c, columns, accept, flag, sto, application
    flag='sto'
    accept=['']*10
    sto=Tk()
    sto.title('STOCK ENTRY')
    Label(sto,text='ENTER NEW PRODUCT DATA TO THE STOCK').grid(row=0,column=0,columnspan=2)
    Label(sto,text='-'*50).grid(row=1,column=0,columnspan=2)
    for i in range(1,len(columns)):
        Label(sto,width=15,text=' '*(14-len(str(columns[i])))+str(columns[i])+':').grid(row=i+2,column=0)
        accept[i]=Entry(sto)
        accept[i].grid(row=i+2, column=1)
    Button(sto,width=15,text='Submit').grid(row=12,column=1)
    Label(sto,text='-'*165).grid(row=13,column=0,columnspan=7)
    Button(sto,width=15,text='Reset').grid(row=12,column=0)
    Button(sto,width=15,text='Refresh stock').grid(row=12,column=4)
    for i in range(1,6):
        Label(sto,text=columns[i]).grid(row=14,column=i-1)
    Label(sto,text='Exp           Rack   Manufacturer                      ').grid(row=14,column=5)
    Button(sto,width=10,text='Main Menu').grid(row=12,column=5)
    # ref()
    sto.mainloop()
    