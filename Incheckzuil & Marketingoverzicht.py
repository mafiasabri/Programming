from tkinter import *
import sqlite3


def invoer_incheckzuil():
    TKintermenu = Tk()
    Label(TKintermenu, text="Voer ov-chipkaartnummer in").grid(row=0)
    invoerveld = Entry(TKintermenu)
    invoerveld.grid(row=0, column=1)
    Button(TKintermenu, text='Invoeren', command=TKintermenu.quit).grid(row=0, column=4 , sticky=W, pady=20)
    mainloop()
    invoer = invoerveld.get()
    return invoer


def vergelijk_database(invoer):
    conn = sqlite3.connect('Reizigers.db')
    cursor = conn.cursor()
    waardeinvoer = (invoer,)
    databasewaarden = cursor.execute('SELECT * FROM ReizigersDB WHERE OVnummer =?', waardeinvoer)
    resultaten = databasewaarden.fetchall()
    teller = len(resultaten)
    if teller == 0:
        print("Dit OVnummer is nog niet in onze database bekend.")
    for row in resultaten:
        print(row)

vergelijk_database(invoer_incheckzuil())

