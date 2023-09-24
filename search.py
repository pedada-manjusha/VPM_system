from tkinter import *
import os
from tkinter import messagebox

def clse():
    root.destroy()
    os.system('python option.py')

def ver():
    a = 0
    if not tno.get():
        messagebox.showwarning("Warning", "Fill in the blank spaces.")
        a = 1
    return a

def ser():
    t = ver()
    if t == 0:
        search_token = tno.get()
        vehicle_type = menu.get()
        with open("vehicle_records.txt", "r") as file:
            lines = file.readlines()

        records_found = []
        for line in lines:
            record = line.strip().split("|")
            if record[3] == search_token:
                if record[4] == vehicle_type:
                    records_found.append(record)

        if records_found:
            for record in records_found:
                for field in record:
                    t1.insert(END, field + "\t")
                t1.insert(END, "\n")
        else:
            messagebox.showinfo("Not Found", "No records found for the given token number.")

if __name__ == "__main__":
    root = Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("Parking")
    root.configure(bg='#FFC0CB')

    label = Label(root, text="SEARCH", font="bold", fg="Red")
    label.place(x=450, y=50)

    tno = StringVar()

    menu = StringVar()
    menu.set("Select Vehicle Type")

    drop = OptionMenu(root, menu, "TwoWheeler", "ThreeWheeler", "FourWheeler", "Others")
    drop.pack()
    drop.place(x=400, y=50)
    label2 = Label(root, text="Token No:")
    label2.place(x=300, y=170)

    e2 = Entry(root, textvariable=tno, width=40)
    e2.place(x=420, y=170)

    b4 = Button(root, text="Search", command=ser, activebackground="red", bg="#68BBE3", width=30)
    b4.place(x=363, y=240)

    t1 = Text(root, width=80, height=10)
    t1.place(x=10, y=280)

    b3 = Button(root, text="Back", command=clse, bg="#68BBE3", activebackground="red", width=30)
    b3.place(x=700, y=420)

    root.mainloop()
