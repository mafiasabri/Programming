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
        c.execute("CREATE TABLE ReizigersDB(ID CHAR(100), Naam TEXT, OVnummer INT, Beginstation TEXT, Eindstation TEXT)")
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
        uniekID = (date + ',' + gegevens[1] + ',' + gegevens[0] + ',' + gegevens[2] + ',' + gegevens[3])
        c.execute("INSERT INTO ReizigersDB (ID, Naam, OVnummer, Beginstation, Eindstation) VALUES (?, ?, ?, ?, ?)",
                  (uniekID, gegevens[0], gegevens[1], gegevens[2], gegevens[3]))
    return uniekID




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
    print("De invoer is niet correct en moet bestaan uit cijfers. Probeer het opnieuw.")
    return input_integer(prompt)


def input_character(prompt):
    """
    De input moet bestaan uit enkel letters, als dit niet het geval is wordt dit aangegeven.
    De functie zal dan vragen om een nieuwe input.
    :return:str(invoer)
    """
    invoer = input(prompt)
    while invoer and invoer.isalpha() == True:
        return str(invoer)
    print("De invoer is niet correct. Probeer het opnieuw.")
    return input_character(prompt)


def controle_gegevens():
    """
    In deze functie wordt er gevraagd om de input van de gebruikers, met als criteria:
    naam, ovnummer, beginstation en eindstation.
    Bij ovnummer is alleen een input geldig van nummers.
    Het beginstation en eindstation moet voorkomen in de nsAPI.
    Daarnaast mogen het begin en eindstation niet hetzelfde zijn.
    Als de bovenstaande gegevens correct zijn worden opgeslagen in gegevens
    :return:gegevens
    """
    stations = nsAPI()
    naam = input("Voer uw naam in: ")
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
    img = qrcode.make(dataEntry())
    img.show()

f = os.path.isfile("Reizigers.db")
conn = sqlite3.connect("Reizigers.db")
c = conn.cursor()
tableCreate(f, c)
nsAPI()
welkomprint()
gegevens = controle_gegevens()
generateQR(gegevens)

