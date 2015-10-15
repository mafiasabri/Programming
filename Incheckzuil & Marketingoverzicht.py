from tkinter import *
import sqlite3
import collections

def connector():
    """
    Bij deze functie word er een verbinding gemaakt met de database (in dit geval "Reizigers.db").
    Hierna word een command toegeveogd om er bepaalde gegevens uit te halen en deze word vervolgens teruggeven om in volgende functies te gebruiken.
    :return: cursor
    """
    conn = sqlite3.connect("Reizigers.db")
    cursor = conn.cursor()
    return cursor

def invoer_incheckzuil():
    """
    Deze functie het Tkintermenu om een OV-nummer in te noteren.
    vervolgens geeft hij de invoer terug om er bij een volgende functie de bijpassende gevens bij te kunnen halen.
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
    Hier word de invoer van invoer_incheckzuil() erbij genomen om vervolgens te kijken of deze in de database voorkomt, en zo ja; hoe vaak.
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
    """
    Hier word de volledig database in een list gezet om vervolgens uit die list het populairste vertrekstation te halen.
    :param cursor:
    :return: populairste_vertrek
    """
    database_eindstation = cursor.execute('SELECT Eindstation FROM ReizigersDB')
    eindstation = []
    for row in database_eindstation:
        eindstation += row
    populairste_vertrek = ("Het populairste vertrekstation is: " + max(eindstation))
    return populairste_vertrek

def populairste_bestemming(cursor):
    """
    Hier word de volledig database in een list gezet om vervolgens uit die list de populairste bestemming te halen.
    :param cursor:
    :return: populairste_best
    """
    database_beginstation = cursor.execute('SELECT Beginstation FROM ReizigersDB')
    beginstation = []
    for row in database_beginstation:
        beginstation += row
    populairste_best =("De populairste bestemming is: " + max(beginstation))
    return populairste_best

def aantal_reizen_per_ov(cursor):
    """
    Hier word de volledig database in een list gezet om vervolgens alle aparte ovnummers eruit te halen
    en te laten zien hoevaak hiermee gereisd is.
    :param cursor:
    :return: str(minidatabase)
    """
    databasewaarden = cursor.execute('SELECT OVnummer FROM ReizigersDB')
    resultaten = databasewaarden.fetchall()
    ovnummer= []
    minidatabase =[]
    for row in resultaten:
        ovnummer += row
    counter = collections.Counter(ovnummer)
    for letter in counter:
        minidatabase += (letter, counter[letter])
    return(str(minidatabase))

def schrijven_naar_txt(minidatabase, populairste_best, populairste_vertek):
    """
    Hier worden de gegevens van populairste_vertrekstation(), populairste_bestemming() & aantal_reizen_per_ov() in een txt. bestand gezet.
    :param minidatabase:
    :param populairste_best:
    :param populairste_vertek:
    :return: None
    """
    file = open("Marketingverslag.txt","w")
    file.writelines(minidatabase + "\n")
    file.writelines(populairste_best + "\n")
    file.writelines(populairste_vertek)
    file.close()


aantal_reis = aantal_reizen_per_ov(connector())
print()
pop_best = populairste_bestemming(connector())
pop_vert = populairste_vertrekstation(connector())
print()
DB_vergelijk = vergelijk_database(invoer_incheckzuil(),connector())
schrijf_txt = schrijven_naar_txt(aantal_reis, pop_best, pop_vert)
