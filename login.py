#Name - Rohit Shankarrao Ukirde
#Email - rukir2@uis.edu
#Python 2.7


from Tkinter import *
from sqlite3 import dbapi2 as sqlite
from PIL import ImageTk, Image
import ttk

login=sqlite.connect("grocery.sqlite")
l=login.cursor()
WinStat = ''


def stock():
    
    application.destroy()
    
    login.close()
    
    import stockdetails
    a = stockdetails.stock()
    
    open_win()

def dailyincome():
    
    application.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.dailyincome()
    
    open_win()    
    
def billingitems():
    
    application.destroy()
    
    login.close()
    
    import billingdetails
    a = billingdetails.billingitems()
    
    open_win()
    
def delstock():
    
    application.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import stockdetails
    a = stockdetails.deletestock()
    
    open_win()
    
def updatestock():
    
    application.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import stockdetails
    a = stockdetails.updatestock()
    
    open_win()
    
def expirycheck():
    
    application.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    login.close()
    
    import expirycheck
    a = expirycheck.expiry()
    
    open_win()
    
def again():   
    ''' Main Login Window'''
    global un, pwd, WinStat, root, application
    if WinStat=='application':
        application.destroy()
    root=Tk()
    root.title('INDIAN GROCERY STORE')
    root.wm_iconbitmap('favicon.ico')
    root.configure(background="#a1dbcd")
    img = ImageTk.PhotoImage(Image.open('indian.gif'))
    panel = Label(root, image = img).grid(row=0, column=0,columnspan=5)
   
    Label(root,text='INDIAN GROCERY STORE',background="#a1dbcd").grid(row=1,column=0,columnspan=5)
    Label(root,text="1602 ,Chatham Hills, Springfield-62704, Illinois",background="#a1dbcd").grid(row=2,column=0,columnspan=5)
    Label(root,text='--------------------------------------------------------------',background="#a1dbcd").grid(row=3,column=0,columnspan=5)
    Label(root, text='Username',background="#a1dbcd").grid(row=4, column=1)
    un=Entry(root,width=10)
    un.grid(row=4, column=2)
    Label(root, text='Password',background="#a1dbcd").grid(row=5, column=1)
    pwd=Entry(root,width=10, show="*")
    pwd.grid(row=5, column=2)
    Label(root,text='',background="#a1dbcd").grid(row=6,column=0,columnspan=5)
    Button(root,width=6,text='Enter',command=check).grid(row=7, column=1)
    Button(root,width=6,text='Close',command=root.destroy).grid(row=7, column=2)
    root.mainloop()
    
def check():   
    ''' Check Button for Login Window '''
    global un, pwd, root
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    u=un.get()
    p=pwd.get()
    if 'admin'!=u and 'admin'!=p:
        top=Tk()
        Label(top,width=30, text='Wrong Username or Password').grid(row=0, column=0)
        top.destroy()
        top.mainloop()
    else:
        root.destroy()
        # login.close()
        open_win()
    
    
        
    

def open_win(): 
    ''' Opens Main Window '''
    global application, WinStat
    WinStat='application'
    application=Tk()
    application.wm_iconbitmap('favicon.ico')
    
  
    application.title("INDIAN GROCERY STORE")
    application.geometry("800x600")
    
    ''' Main Window Picture '''
    img = ImageTk.PhotoImage(Image.open('collage.jpg'))
    panel = Label(application, image = img).grid(row=0, column=0,columnspan=5)
    
   

    
    menu_bar = Menu(application)
    stock_menu = Menu(menu_bar,tearoff=0)
    expiry_menu = Menu(menu_bar,tearoff=0)
    billing_menu = Menu(menu_bar,tearoff=0)
    '''Stock Maintainance'''
    stock_menu.add_command(label="Add Items", command=stock)
    stock_menu.add_command(label="Delete Items", command=delstock)
    stock_menu.add_command(label="Update Items", command=updatestock)
    '''Expiry Check'''
    expiry_menu.add_command(label="Check Expiry", command=expirycheck)
    '''Billing'''
    billing_menu.add_command(label="Billing", command=billingitems)
    billing_menu.add_command(label="Check Today's Income", command=dailyincome)
    
    
    menu_bar.add_cascade(label="Stock Maintainance", menu=stock_menu)
    menu_bar.add_cascade(label="Expiry", menu=expiry_menu)
    menu_bar.add_cascade(label="Billing", menu=billing_menu)
    menu_bar.add_cascade(label="Logout",command=again)
    application.config(menu=menu_bar)
    
    
    
        
    application.mainloop()

    

    
    
    
    
again()