from tkinter import *
import os
def clse():
    root.destroy()
    os.system('python index.py')
def login():
    root.destroy()
    os.system('python login.py')
def add():
    root.destroy()
    os.system('python vehicleadd.py')
def search():
    root.destroy()
    os.system('python search.py')
def view():
    root.destroy()
    os.system('python view.py')
def checkout():
    root.destroy()
    os.system('python delet.py')
        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("Parking")
    root.configure(bg='#FFC0CB')

    b1=Button(root,text="ADD VEHICLE",command=add,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=50)
    b1=Button(root,text="VIEW ALL",command=view,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=100)
    b1=Button(root,text="SEARCH",command=search,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363, y=150)
    b1 = Button(root, text="CHECKOUT", command=checkout, activebackground="pink", bg="#68BBE3", width=30)
    b1.place(x=363, y=200)
    b1 = Button(root, text="LOGOUT", command=clse, activebackground="pink", bg="#68BBE3", width=30)
    b1.place(x=363, y=250)
    
    root.mainloop()

