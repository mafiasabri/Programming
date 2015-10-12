from tkinter import *

def incheckzuil2():
    global e1
    master = Tk()
    Label(master, text="Voer ov-chipkaartnummer in").grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Show', command=Incheckzuil).grid(row=3, column=1, sticky=W, pady=4)
    mainloop( )

def incheckzuil():
    global e1
    print("Ov-chipkaartnummer is " +  e1.get())

incheckzuil()