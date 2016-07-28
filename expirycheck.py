#Name - Rohit Shankarrao Ukirde
#Email - rukir2@uis.edu
#Python 2.7

from Tkinter import *
from sqlite3 import dbapi2 as sqlite
import time


columns=('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date','Manufactured_By')

c=sqlite.connect("grocery.sqlite")
cur=c.cursor()



def expiry():
    ''' Expiry GUI '''
    global expirychk, expdate,c, cur, flag
    total=0.0
    today=str(time.localtime()[2])+'/'+str(time.localtime()[1])+'/'+str(time.localtime()[0])
    
    flag='expirychk'
    groitem=[]
    cur.execute("select * from grocerylist")
    for i in cur:
        groitem.append(i[1])
    c.commit()
    expirychk=Tk()
    expirychk.title('Check Expiry of the Items')
    expirychk.wm_iconbitmap('favicon.ico')
    Label(expirychk,text='Today: '+today).grid(row=0,column=0,columnspan=3)
    Label(expirychk,text='Its Illegal to sell expired items').grid(row=1, column=0,columnspan=3)
    Label(expirychk,text='-'*80).grid(row=2, column=0,columnspan=3)
    expdate=Spinbox(expirychk,values=groitem)
    expdate.grid(row=3, column=0)
    Button(expirychk,text='Check Expiry date', command=chkexpiry).grid(row=3, column=1)
    Label(expirychk,text='-'*80).grid(row=4, column=0,columnspan=3)
    
    Button(expirychk,text='Main Menu',command=mainmenu).grid(row=5, column=2)
    expirychk.mainloop()
    
def chkexpiry():    
    ''' Check Expiry Date button will navigate here '''
    global c, cur, expdate, expirychk
    cur.execute("select * from grocerylist")
    for i in cur:
        if(i[1]==expdate.get()):
            Label(expirychk, text=i[5]).grid(row=3, column=2)
    c.commit()
    
    
def mainmenu():
    if flag=='expirychk':
        expirychk.destroy()
    
    

# expiry()