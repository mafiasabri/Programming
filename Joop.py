import sqlite3
import qrcode
import requests
import os
import os.path
from tkinter import *
import datetime
import time



def tableCreate(f,c):
    """
    Deze functie maakt eenmalig een tabel aan in de database.
    :return: None
    """
    if not f:
        c.execute("CREATE TABLE ReizigersDB(ID CHAR(50), Naam TEXT, OVnummer INT, Beginstation TEXT, Eindstation TEXT)")
    else:
        print("")


def dataEntry():
    """
    Deze functie voegt de input(controle_gegevens()) van de gebruiker toe in de database. Daarnaast genereert de functie
    een unieke reizigersID.
    :return: None
    """
    with conn:
        date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime("%Y%m%d%H%M%S"))
        c.execute("INSERT INTO ReizigersDB (ID, Naam, OVnummer, Beginstation, Eindstation) VALUES (?, ?, ?, ?, ?)",
                  (date + gegevens[1], gegevens[0], gegevens[1], gegevens[2], gegevens[3]))


def nsAPI():
    """
    Doormiddel van deze functie worden de stations uit nsAPI gehaald.
    Deze stations worden later in de functie controle_gegevens() gebruikt.
    :return: stations
    """
    auth_details = ("hjr.tielemans@gmail.com", "sz3XpDnQ5EVcA8Gg4FhuWICzhJgmMOnehAIoElLW3iVP1wyJ5p8OuQ")
    response = requests.get("http://webservices.ns.nl/ns-api-stations-v2",
                            auth=auth_details)
    stations = response.text
    return stations


def welkomprint():
    """
    Toont introductie en instructie.
    :return:None
    """
    print("Welkom bij de NS. \nVoer nu onderstaande informatie in om verder te gaan.")


def input_integer(prompt):
    """
    De input moet bestaan uit enkel getallen, als dit niet het geval is wordt dit aangegeven.
    De functie zal dan vragen om een nieuwe input.
    :return:int(invoer)
    """
    invoer = input(prompt)
    while invoer and invoer.isdigit() == True:
        return int(invoer)
    else:
        print("De invoer is niet correct. Probeer het opnieuw.")
        return input_integer(prompt)


def input_character(prompt):
    """
    De input moet bestaan uit enkel letters, als dit niet het geval is wordt dit aangegeven.
    De functie zal dan vragen om een nieuwe input.
    :return:str(invoer)
    """
    invoer = input(prompt)
    while invoer and invoer.isalpha()== True:
        return str(invoer)
    else:
        print("De invoer is niet correct. Probeer het opnieuw.")
        return input_character(prompt)


def controle_gegevens():
    """
    In deze functie wordt er gevraagd om de input van de gebruikers, met als criteria:
    naam, ovnummer, beginstation en eindstation.
    Bij naam is alleen een input van letters geldig.
    Bij ovnummer is alleen een input geldig van nummers.
    Het beginstation en eindstation moet voorkomen in de nsAPI.
    Daarnaast mogen het begin en eindstation niet hetzelfde zijn.
    Als de bovenstaande gegevens correct zijn worden opgeslagen in gegevens
    :return:gegevens
    """
    stations = nsAPI()
    naam = input_character("Voer uw naam in: ")
    ovnummer = input_integer("Voer uw ov-chipkaartnummer in: ")
    ovnummer = str(ovnummer)
    while len(ovnummer) != 8:
        print("Error! Voer een geldige 8 cijferige ov-chipkaartnummer in!")
        ovnummer = input_integer("Voer uw ov-chipkaartnummer in: ")
        ovnummer = str(ovnummer)
    beginstation = input_character("Voer uw beginstation in: ")
    while beginstation not in stations:
        print("Het beginstation is niet bekend.")
        beginstation = input_character("Voer uw beginstation in: ")
    eindstation = input("Voer uw eindstation in: ")
    while eindstation not in stations:
        print("Het eindstation is niet bekend.")
        eindstation = input("Voer uw eindstation in: ")
    while beginstation == eindstation:
        print("Het eindstation mag niet hetzelfde zijn als het beginstation zijn.")
        eindstation = input_character("Voer uw eindstation in: ")
    gegevens = naam, ovnummer, beginstation, eindstation
    return gegevens


def generateQR(gegevens):
    """
    Deze functie genereert een QR-code op basis van de reizigersID
    Dit gebeurt op basis van de input van de gebruiker. De input is opgeslagen in gegevens.
    """
    img = qrcode.make((str("Uw naam is: ") + gegevens[0] + ("\n") + str("Uw OV-kaart nummer is: ") + gegevens[1] +("\n")
    + str("Uw beginstation is: ") + gegevens[2] + str("\n") + str("Uw eindstation is: ") + gegevens[3]))
    img.show()


def invoer_incheckzuil():
    master = Tk()
    Label(master, text="Voer ov-chipkaartnummer in").grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    Button(master, text="Invoeren", command=master.quit).grid(row=0, column=4 , sticky=W, pady=20)
    mainloop()
    Z = e1.get()
    return Z


def vergelijk_database(Z):
    with conn:
        c = conn.cursor()
        t = (Z,)
    for row in c.execute("SELECT * FROM ReizigersDB"):
        if row in c.execute("SELECT * FROM ReizigersDB WHERE OVnummer=?", t):
            print(row)
        else:
            print("U heeft nog geen reis gemaakt of een verkeerd OVnummer ingetyped")

# Zorg als laatste dat je voor de NS­marketingafdeling een (automatisch) overzicht genereert van:
# ● het aantal reizen per ov­chipkaart,
# ● de populairste bestemmingen, en
# ● de populairste vertrekstations.

# def database_leeghalen:

f = os.path.isfile("Reizigers.db")
conn = sqlite3.connect("Reizigers.db")
c = conn.cursor()
tableCreate(f,c)
nsAPI()
welkomprint()
gegevens = controle_gegevens()
dataEntry()
generateQR(gegevens)
vergelijk_database(invoer_incheckzuil())
