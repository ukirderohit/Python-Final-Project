from Tkinter import *
from sqlite3 import dbapi2 as sqlite


columns=('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date','Manufactured_By')

c=sqlite.connect("grocery.sqlite")
cur=c.cursor()



def autoincre():
    
    cur.execute("select max(Item_No) from grocerylist")
    incval = cur.fetchone()
    incval = incval[0] + 1
    # print incval
    return incval
    
    
def stock():
    
    global cur, c, columns, value, flag, sto, application
    
    flag='sto'
    value = ['']*len(columns)
    sto=Tk()
    sto.title('Add Stock')
    Label(sto,text='Enter a New Item to the Grocery Stock').grid(row=0,column=0,columnspan=2)
    Label(sto,text='-'*50).grid(row=1,column=0,columnspan=2)
    
    
    Label(sto,width=15,text=str(columns[0])+':',justify=LEFT).grid(row=3,column=0,sticky=W)
    autovalue = autoincre()
    value[0]=Entry(sto)
    value[0].grid(row=3, column=1)
    Label(sto,text='The New Value Should be :- ' + str(autovalue)).grid(row=3,column=2)
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
    

    
    
    


def chk(): #for new stock submission
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
    Label(top,width=20, text='Success!').pack()
    top.mainloop()
    # mainmenu()
    

def deletestock():
    global cur, c, flag, lb1, d, valuex
    # apt.destroy()
    valuex = ''
    flag='delsto'
    d=Tk()
    d.title("Delete grocery item from Stock")
    Label(d,text='Enter the Item No to Delete').grid(row=1,column=0)
    valuex=Entry(d)
    valuex.grid(row=1, column=1)
    # Label(d,text='',width=30,bg='white').grid(row=0,column=1)
    Label(d,text='Item').grid(row=2,column=0)
    Label(d,text='Qty Remain').grid(row=2,column=1)
    Label(d,text='Cost').grid(row=2,column=2)
    Label(d,text='Expiry Date').grid(row=2,column=3)
    
    displayren()
    b=Button(d,width=20,text='Delete',command=deletestockbutton).grid(row=1,column=3)
    b=Button(d,width=20,text='Main Menu',command=mainmenu).grid(row=5,column=3) 
    d.mainloop()

def deletestockbutton():
    global p,c,cur,d,valuex
    string = valuex.get()
    print string
    cur.execute("delete from grocerylist where Item_No=?",string)
    c.commit()
    displayren()
    
def displayren():
    global lb1,d,cur,c
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)
    
    index=0
    vsb=Scrollbar(orient='vertical',command=onvsb)
    lb1=Listbox(d,width=25, yscrollcommand=vsb.set)
    lb2=Listbox(d,width=7,yscrollcommand=vsb.set)
    lb3=Listbox(d,width=7,yscrollcommand=vsb.set)
    lb4=Listbox(d,width=13,yscrollcommand=vsb.set)
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
    
    
       
    
    
    
    
         
        
def ref(): # creates a multi-listbox manually to show the whole database 
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
    if flag=='sto':
        sto.destroy()
    elif flag=='delsto':
        d.destroy()  
# stock()