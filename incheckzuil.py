from tkinter import *
import sqlite3
conn = sqlite3.connect('database1.sql')

def invoer_incheckzuil():
    global e1
    master = Tk()
    Label(master, text="Voer ov-chipkaartnummer in").grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    Button(master, text='Invoeren', command=master.quit).grid(row=0, column=4 , sticky=W, pady=20)
    mainloop()
    f = e1.get()
    return f

def vergelijk_database():
    global f
    global conn
    # for row in conn:
    #     if f == row:
    #         print( row[0])
    #     else:
    #         print("werkt niet")
    #
    with conn:

        cur = conn.cursor()
        cur.execute("SELECT * FROM NSReizigers")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        print(row[0], row[1], row[2])

invoer_incheckzuil()
vergelijk_database()
