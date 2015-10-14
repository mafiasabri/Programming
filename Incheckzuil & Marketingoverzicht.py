from tkinter import *
import sqlite3
import collections

def connector():
    conn = sqlite3.connect('Reizigers.db')
    cursor = conn.cursor()
    return cursor

def invoer_incheckzuil():
    """
    Invoer in de incheckzuil via TKinter
    :return: invoer
    """
    TKintermenu = Tk()
    Label(TKintermenu, text="Voer ov-chipkaartnummer in").grid(row=0)
    invoerveld = Entry(TKintermenu)
    invoerveld.grid(row=0, column=1)
    Button(TKintermenu, text='Invoeren', command=TKintermenu.quit).grid(row=0, column=4 , sticky=W, pady=20)
    mainloop()
    invoer = invoerveld.get()
    return invoer


def vergelijk_database(invoer,cursor):
    """
    Vergelijkt invoer van de vorige functie in de database en aan de hand van de invoer informatie aan de gebruiker
    :param invoer:
    :return: None
    """
    waardeinvoer = (invoer,)
    databasewaarden = cursor.execute('SELECT * FROM ReizigersDB WHERE OVnummer =?', waardeinvoer)
    resultaten = databasewaarden.fetchall()
    teller = len(resultaten)
    if teller == 0:
        print("Dit OVnummer is nog niet in onze database bekend.")
    for row in resultaten:
        print ("\n")
        for i in row:
            print(i)

def populairste_vertrekstation(cursor):
    connector()
    database_eindstation = cursor.execute('SELECT Eindstation FROM ReizigersDB')
    eindstation = []
    for row in database_eindstation:
        eindstation += row
    print("Het populairste vertrekstation is: " + max(eindstation))


def populairste_bestemming(cursor):
    connector()
    database_beginstation = cursor.execute('SELECT Beginstation FROM ReizigersDB')
    beginstation = []
    for row in database_beginstation:
        beginstation += row
    print("De populairste bestemming is: " + max(beginstation))

def aantal_reizen_per_ov(cursor):
    databasewaarden = cursor.execute('SELECT OVnummer FROM ReizigersDB')
    resultaten = databasewaarden.fetchall()
    ovnummer= []
    for row in resultaten:
        ovnummer += row
    counter = collections.Counter(ovnummer)
    for letter in counter:
        print (letter, counter[letter])

aantal_reizen_per_ov(connector())
print()
populairste_bestemming(connector())
populairste_vertrekstation(connector())
print()
vergelijk_database(invoer_incheckzuil(),connector())