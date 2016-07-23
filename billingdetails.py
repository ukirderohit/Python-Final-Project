from Tkinter import *
from sqlite3 import dbapi2 as sqlite
import win32api


columns=('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date','Manufactured_By')

c=sqlite.connect("grocery.sqlite")
cur=c.cursor()

def billingitems():
    global c, cur, flag, t, name, name1, add, billingsto, names, qty, sl, qtys,n, namee, lb1
    t=0
    
    names=[]
    qty=[]
    sl=[]
    n=[]
    qtys=['']*10
    cur.execute("select * from grocerylist")
    for i in cur:
        n.append(i[1])
    c.commit()
    # apt.destroy()
    flag='billingsto'
    billingsto=Tk()
    billingsto.title('BILLING')
    Label(billingsto,text='-'*48+'Billing'+'-'*49).grid(row=0,column=0,columnspan=7,sticky='W')
    Label(billingsto,text='Enter Name: ').grid(row=1,column=0)
    name1=Entry(billingsto)
    name1.grid(row=1, column=1)
    Label(billingsto,text='Enter Address: ').grid(row=2,column=0)
    add=Entry(billingsto)
    add.grid(row=2, column=1)
    
    Label(billingsto,text='-'*115).grid(row=6, column=0,columnspan=7,sticky='W')
    Label(billingsto,text='Select Item',relief='ridge',width=15).grid(row=7,column=0)
    Label(billingsto,text='Qty_Remain',relief='ridge',width=10).grid(row=7,column=1)
    Label(billingsto,text='Cost',relief='ridge',width=4).grid(row=7,column=2)
    Label(billingsto,text='Expiry Date',width=10,relief='ridge').grid(row=7,column=3)
   
    Button(billingsto,text='Add to bill',width=15,command=addtothebill).grid(row=8, column=6)
    Label(billingsto,text='QUANTITY',width=20,relief='ridge').grid(row=7, column=5)
    qtys=Entry(billingsto)
    qtys.grid(row=8,column=5)
    refresh()
    Button(billingsto,width=15,text='Main Menu', command= mainmenu).grid(row=1,column=6)
    Button(billingsto,width=15,text='Refresh Stock',command=refresh).grid(row=3,column=6)
    Button(billingsto,width=15,text='Reset Bill',command=resetbill).grid(row=4,column=6)
    Button(billingsto,width=15,text='Print Bill',command=printbill).grid(row=5,column=6)
    Button(billingsto,width=15,text='Save Bill').grid(row=7,column=6)
    
    billingsto.mainloop()

def refresh():
    global cur, c, billingsto, lb1, lb2, vsb
    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)

    def onmousewheel():
        lb1.ywiew=('scroll',event.delta,'units')
        lb2.ywiew=('scroll',event.delta,'units')
        return 'break'
    index=0
    vsb=Scrollbar(orient='vertical',command=onvsb)
    lb1=Listbox(billingsto,width=25, yscrollcommand=vsb.set)
    lb2=Listbox(billingsto ,width=7,yscrollcommand=vsb.set)
    lb3=Listbox(billingsto,yscrollcommand=vsb.set,width=7)
    lb4=Listbox(billingsto,yscrollcommand=vsb.set,width=20)
    
    
    vsb.grid(row=8,column=2,sticky=N+S)
    lb1.grid(row=8,column=0)
    lb2.grid(row=8,column=1)
    lb3.grid(row=8,column=2)
    lb4.grid(row=8,column=3)
    
    
    lb1.bind('<MouseWheel>',onmousewheel)
    lb2.bind('<MouseWheel>',onmousewheel)
    cur.execute("select * from grocerylist")
    for i in cur:
        index+=1
        lb1.insert(index,str(i[0])+' '+i[1])
        lb2.insert(index,i[3])
        lb3.insert(index,i[4])
        lb4.insert(index,i[5])
        
        
    c.commit()
    lb1.bind('<<ListboxSelect>>', select_mn)    

def select_mn(e): #store the selected medicine from listbox
    global billingsto, lb1, n ,p, sl1, nm
    p=lb1.curselection()
    x=0
    sl1=''
    cur.execute("select * from grocerylist")
    for i in cur:
        if x==int(p[0]):
            sl1=int(i[0])
            break
        x+=1
    c.commit()
    print sl1
    nm=n[x]
    print nm
    
def addtothebill(): # append to the bill
    global st, names, nm , qty, sl,cur, c, sl1
    sl.append(sl1)
    names.append(nm)
    qty.append(qtys.get())
    print qty
    print sl[len(sl)-1],names[len(names)-1],qty[len(qty)-1]
    
def printbill():
    win32api.hellExecute (0,"print",'bill.txt','/d:"%s"' % win32print.GetDefaultPrinter (),".",0)
    
    
def resetbill():
    global sl, names, qty
    sl=[]
    names=[]
    qty=[]
    
    

    
    
def mainmenu():
    if flag=='sto':
        sto.destroy()
    elif flag=='billingsto':
        billingsto.destroy()  
        
billingitems()