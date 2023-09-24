from tkinter import *
import datetime
import os
from tkinter import messagebox
import random
class Vehicle:
    def __init__(self, name, vno,dtime, tno, vtype):
        self.name = name
        self.vno = vno
        self.dtime=dtime
        self.tno = tno
        self.vtype = vtype


def clse():
    root.destroy()
    os.system('python option.py')

def verifier():
    if not menu.get() or not name.get() or not vno.get():
        messagebox.showwarning("Warning", "Fill in all the fields.")
        return False
    return True

def add_vehicle():
    if verifier():
        vehicle_type = menu.get()
        now = datetime.datetime.now()
        current_datetime = now.strftime("%Y:%m:%d %H:%M:%S")
        with open('vehicle_records.txt', 'r') as file:
            records = file.readlines()

        # Extract token numbers from existing records
        existing_tokens = set()
        for record in records:
            tokens = record.split('|')
            existing_tokens.add(int(tokens[3]))

        # Generate a unique random token number
        token = random.randint(1, 100)
        while token in existing_tokens:
            token = random.randint(1, 100)
        vehicle = f'{name.get()}|{vno.get()}|{current_datetime}|{token}|{vehicle_type}\n'

        with open('vehicle_records.txt', 'r') as file:
            records = file.readlines()

        records.append(vehicle)
        records.sort(key=lambda x: (int(x.split('|')[3]), x.split('|')[4]))

        with open('vehicle_records.txt', 'w') as file:
            file.writelines(records)

        messagebox.showwarning("Success", f"Added Successfully.\nYour token no is: {token}")

if __name__ == "__main__":
    root = Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("Parking")
    root.configure(bg='#FFC0CB')

    menu = StringVar()
    menu.set("Select Vehicle Type")

    drop = OptionMenu(root, menu, "TwoWheeler", "ThreeWheeler", "FourWheeler", "Others")
    drop.pack()
    drop.place(x=400, y=50)

    vno = StringVar()
    tno = StringVar()
    name = StringVar()

    label2 = Label(root, text=" Name:")
    label2.place(x=300, y=120)

    label1 = Label(root, text="Vehicle No:")
    label1.place(x=300, y=170)

   # label2 = Label(root, text="Token No:")
    #label2.place(x=300, y=220)

    e1 = Entry(root, textvariable=name, width=40)
    e1.place(x=420, y=120)

    e1 = Entry(root, textvariable=vno, width=40)
    e1.place(x=420, y=170)

    #e2 = Entry(root, textvariable=tno, width=40)
    #e2.place(x=420, y=220)

    b4 = Button(root, text="Submit", command=add_vehicle, activebackground="pink", bg="#68BBE3", width=30)
    b4.place(x=363, y=420)

    b3 = Button(root, text="Back", command=clse, bg="#68BBE3", activebackground="red", width=30)
    b3.place(x=700, y=420)

    root.mainloop()
