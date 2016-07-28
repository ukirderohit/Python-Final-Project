from Tkinter import *
from sqlite3 import dbapi2 as sqlite


columns=('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date','Manufactured_By')

c=sqlite.connect("grocery.sqlite")
cur=c.cursor()



def autoincre():
    ''' To auto-generate item No '''
    cur.execute("select max(Item_No) from grocerylist")
    incval = cur.fetchone()
    incval = incval[0] + 1
    # print incval
    return incval
    
    
def stock():
    ''' Stock User GUI here '''
    global cur, c, columns, value, flag, sto, application
    
    flag='sto'
    value = ['']*len(columns)
    sto=Tk()
    sto.title('Add Stock')
    sto.wm_iconbitmap('favicon.ico')
    Label(sto,text='Enter a New Item to the Grocery Stock').grid(row=0,column=0,columnspan=2)
    Label(sto,text='-'*50).grid(row=1,column=0,columnspan=2)
    
    
    Label(sto,width=15,text=str(columns[0])+':',justify=LEFT).grid(row=3,column=0,sticky=W)
    autovalue = autoincre()
    value[0]=Entry(sto)
    value[0].grid(row=3, column=1)
    
    # Label(sto,text='The New Value Should be :- ' + str(autovalue)).grid(row=3,column=2)
    value[0].insert(0,str(autovalue))
    # Entry.configure(state='disabled')
    
    Label(sto,width=15,text=str(columns[1])+':',justify=LEFT).grid(row=4,column=0,sticky=W)
    value[1]=Entry(sto)
    value[1].grid(row=4, column=1)
    Label(sto,width=15,text=str(columns[2])+':',justify=LEFT).grid(row=5,column=0,sticky=W)
    value[2]=Entry(sto)
    value[2].grid(row=5, column=1)
    Label(sto,width=15,text=str(columns[3])+':',justify=LEFT).grid(row=6,column=0,sticky=W)
    value[3]=Entry(sto)
    value[3].grid(row=6, column=1)
    Label(sto,width=15,text=str(columns[4])+':',justify=LEFT).grid(row=7,column=0,sticky=W)
    value[4]=Entry(sto)
    value[4].grid(row=7, column=1)
    Label(sto,width=15,text=str(columns[5])+':',justify=LEFT).grid(row=8,column=0,sticky=W)
    value[5]=Entry(sto)
    value[5].grid(row=8, column=1)
    Label(sto,width=15,text=str(columns[6])+':',justify=LEFT).grid(row=9,column=0,sticky=W)
    value[6]=Entry(sto)
    value[6].grid(row=9, column=1)
    ref()
    
    
    
    Button(sto,width=15,text='Submit',command=chk).grid(row=12,column=1)
    Label(sto,text='-'*165).grid(row=13,column=0,columnspan=7)
    
    Button(sto,width=15,text='Refresh stock',command=ref).grid(row=12,column=4)
    for i in range(1,7):
        Label(sto,text=columns[i]).grid(row=14,column=i-1)
    
    
    Button(sto,width=10,text='Main Menu',command=mainmenu).grid(row=12,column=5)
    
    
    
    sto.mainloop()
    

def updatestock():
    ''' Which item to Update GUI '''
    global cur, c, flag, lb1, updatesto, valueupx
    # apt.destroy()
    valueupx = ''
    flag='updatesto'
    updatesto=Tk()
    updatesto.title("Update grocery item from Stock")
    updatesto.wm_iconbitmap('favicon.ico')
    Label(updatesto,text='Enter the Item No to Update').grid(row=1,column=0)
    valueupx=Entry(updatesto)
    valueupx.grid(row=1, column=1)
    # Label(updatesto,text='',width=30,bg='white').grid(row=0,column=1)
    Label(updatesto,text='Item').grid(row=2,column=0)
    Label(updatesto,text='Qty Remain').grid(row=2,column=1)
    Label(updatesto,text='Cost').grid(row=2,column=2)
    Label(updatesto,text='Expiry Date').grid(row=2,column=3)
    
    displayupdate()
    b=Button(updatesto,width=20,text='Update',command=updatestockbutton).grid(row=1,column=3)
    b=Button(updatesto,width=20,text='Main Menu',command=mainmenu).grid(row=5,column=3) 
    updatesto.mainloop()
  
def updatestockbutton():
    ''' Update Stock Button GUI '''
    global valueupx,cur,valueupxy,updateitemno,flag,updatestobut 
    index=0
    
    updateitemno = valueupx.get()
    print updateitemno
    
    updatesto.destroy()
    
    flag='updatestobut'
    updatestobut=Tk()
    updatestobut.title("Update grocery item from Stock")
    updatestobut.wm_iconbitmap('favicon.ico')
    Label(updatestobut,text='Enter the Item to update to the Grocery Stock').grid(row=0,column=0,columnspan=2)
    col = ('ItemName','QtyRem','Cost','Expiry')
    valueupxy=['']*len(col)
    
    
    
    Label(updatestobut,text='Item_Name').grid(row=2,column=0)
    valueupxy[0]=Entry(updatestobut)
    valueupxy[0].grid(row=2, column=1)
    Label(updatestobut,text='Quantity_Remain').grid(row=4,column=0)
    valueupxy[1]=Entry(updatestobut)
    valueupxy[1].grid(row=4, column=1)
    Label(updatestobut,text='Cost').grid(row=6,column=0)
    valueupxy[2]=Entry(updatestobut)
    valueupxy[2].grid(row=6, column=1)
    Label(updatestobut,text='Expiry_Date').grid(row=8,column=0)
    valueupxy[3]=Entry(updatestobut)
    lb4 = valueupxy[3].grid(row=8, column=1)
    ''' This will automatically show data of respective itemno in the textbox '''
    cur.execute('select * from grocerylist where Item_No=?',updateitemno)
    for i in cur:
        index+=1
        valueupxy[0].insert(index,i[1])
        valueupxy[1].insert(index,i[3])
        valueupxy[2].insert(index,i[4])
        valueupxy[3].insert(index,i[5])
    c.commit() 
    
    b=Button(updatestobut,width=20,text='Update',command=updatesql).grid(row=11,column=0)
    b=Button(updatestobut,width=20,text='Main Menu',command=mainmenu).grid(row=11,column=1) 
    updatestobut.mainloop()
    
def updatesql():
    ''' Update in the database '''
    global updatestobut,valueupxy,updateitemno,cur,c
    itemno=updateitemno
    upitemname=valueupxy[0].get()
    upqtyremai=valueupxy[1].get()
    upcost=valueupxy[2].get()
    upexpiry=valueupxy[3].get()
    print itemno
    print upitemname
    print upqtyremai
    print upcost
    print upexpiry
    cur.execute('update grocerylist set Item_Name=?,Quantity_Remain=?,Item_Cost=?,Expiry_Date=? where Item_No=?',(upitemname,upqtyremai,upcost,upexpiry,itemno))
    top = Tk()
    top.wm_iconbitmap('favicon.ico')
    Label(top,width=20, text='Modified!').pack()
    c.commit()
    top.mainloop()
    
    
  
def displayupdate():
    ''' Display data from database for Update '''
    global lb1,updatesto,cur,c
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
    
    index=0
    vsb=Scrollbar(orient='vertical',command=onvsb)
    lb1=Listbox(updatesto,width=25, yscrollcommand=vsb.set)
    lb2=Listbox(updatesto,width=7,yscrollcommand=vsb.set)
    lb3=Listbox(updatesto,width=7,yscrollcommand=vsb.set)
    lb4=Listbox(updatesto,width=13,yscrollcommand=vsb.set)
    vsb.grid(row=3,column=2,sticky=N+S)
    lb1.grid(row=3,column=0)
    lb2.grid(row=3,column=1)
    lb3.grid(row=3,column=2)
    lb4.grid(row=3,column=3)
    
    cur.execute("select * from grocerylist")
    for i in cur:
        index+=1
        lb1.insert(index,str(i[0])+')  '+i[1])
        lb2.insert(index,i[3])
        lb3.insert(index,i[4])
        lb4.insert(index,i[5])
    c.commit()    


def chk():
    ''' Add new Stock Item '''
    global value, c, cur, columns, sto
    
    x=['']*10
    cur.execute("select * from grocerylist")
    for i in cur:
        y=int(i[0])
        y=autoincre()
    for i in range(1,7):
        x[i]=value[i].get()
    sql="insert into grocerylist values('%s','%s','%s','%s','%s','%s','%s')" % (y,x[1],x[2],x[3],x[4],x[5],x[6])
    cur.execute(sql)
    cur.execute("select * from grocerylist")
    c.commit()
    
    top=Tk()
    top.wm_iconbitmap('favicon.ico')
    Label(top,width=20, text='Success!').pack()
    top.mainloop()
    # mainmenu()
    

def deletestock():
    ''' Delete Stock GUI '''
    global cur, c, flag, lb1, delsto, valuex
    # apt.destroy()
    valuex = ''
    flag='delsto'
    delsto=Tk()
    delsto.title("Delete grocery item from Stock")
    delsto.wm_iconbitmap('favicon.ico')
    Label(delsto,text='Enter the Item No to Delete').grid(row=1,column=0)
    valuex=Entry(delsto)
    valuex.grid(row=1, column=1)
    # Label(delsto,text='',width=30,bg='white').grid(row=0,column=1)
    Label(delsto,text='Item').grid(row=2,column=0)
    Label(delsto,text='Qty Remain').grid(row=2,column=1)
    Label(delsto,text='Cost').grid(row=2,column=2)
    Label(delsto,text='Expiry Date').grid(row=2,column=3)
    
    displayren()
    b=Button(delsto,width=20,text='Delete',command=deletestockbutton).grid(row=1,column=3)
    b=Button(delsto,width=20,text='Main Menu',command=mainmenu).grid(row=5,column=3) 
    delsto.mainloop()

def deletestockbutton():
    ''' Deleting from the table '''
    global p,c,cur,delsto,valuex
    string = valuex.get()
    print string
    cur.execute("delete from grocerylist where Item_No=?",string)
    c.commit()
    displayren()
    
def displayren():
    global lb1,delsto,cur,c
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
    
    index=0
    vsb=Scrollbar(orient='vertical',command=onvsb)
    lb1=Listbox(delsto,width=25, yscrollcommand=vsb.set)
    lb2=Listbox(delsto,width=7,yscrollcommand=vsb.set)
    lb3=Listbox(delsto,width=7,yscrollcommand=vsb.set)
    lb4=Listbox(delsto,width=13,yscrollcommand=vsb.set)
    vsb.grid(row=3,column=2,sticky=N+S)
    lb1.grid(row=3,column=0)
    lb2.grid(row=3,column=1)
    lb3.grid(row=3,column=2)
    lb4.grid(row=3,column=3)
    
    cur.execute("select * from grocerylist")
    for i in cur:
        index+=1
        lb1.insert(index,str(i[0])+')  '+i[1])
        lb2.insert(index,i[3])
        lb3.insert(index,i[4])
        lb4.insert(index,i[5])
    c.commit()
    
    
       
    
    
    
    
         
        
def ref(): 
    ''' Multilistbox to show all the data in database '''
    global sto,cur,c
    
    def scrollbarv(*args):
        lb1.yview(*args)
        lb2.yview(*args)
        lb3.yview(*args)
        lb4.yview(*args)
        lb5.yview(*args)
        lb6.yview(*args)

    
    index=0
    sc_bar=Scrollbar(orient='vertical',command=scrollbarv)
    lb1=Listbox(sto,yscrollcommand=sc_bar.set)
    lb2=Listbox(sto,yscrollcommand=sc_bar.set)
    lb3=Listbox(sto,yscrollcommand=sc_bar.set,width=7)
    lb4=Listbox(sto,yscrollcommand=sc_bar.set,width=7)
    lb5=Listbox(sto,yscrollcommand=sc_bar.set,width=20)
    lb6=Listbox(sto,yscrollcommand=sc_bar.set,width=20)
    sc_bar.grid(row=15,column=6,sticky=N+S)
    lb1.grid(row=15,column=0)
    lb2.grid(row=15,column=1)
    lb3.grid(row=15,column=2)
    lb4.grid(row=15,column=3)
    lb5.grid(row=15,column=4)
    lb6.grid(row=15,column=5)
    
    cur.execute("select * from grocerylist")
    for i in cur:
        index+=1
        lb1.insert(index,str(i[0])+'. '+str(i[1]))
        lb2.insert(index,i[2])
        lb3.insert(index,i[3])
        lb4.insert(index,i[4])
        lb5.insert(index,i[5])
        lb6.insert(index,i[6])
        
    c.commit()   
    
def mainmenu():
    ''' Main Menu Button '''
    if flag=='sto':
        sto.destroy()
    elif flag=='delsto':
        delsto.destroy()  
    elif flag=='updatestobut':
        updatestobut.destroy()
    elif flag=='updatesto':
        updatesto.destroy()
# updatestock()
# stock()