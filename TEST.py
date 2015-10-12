import qrcode
import requests

def nsAPI():
    """
    Doormiddel van deze functie worden de stations uit nsAPI gehaald.
    Deze stations worden later in de functie controleerstations() gebruikt
    om de input van de gebruiker te controleren
    """
    auth_details = ("hjr.tielemans@gmail.com", "sz3XpDnQ5EVcA8Gg4FhuWICzhJgmMOnehAIoElLW3iVP1wyJ5p8OuQ")
    response = requests.get('http://webservices.ns.nl/ns-api-stations-v2',
    auth=auth_details)
    global stations
    stations = response.text
nsAPI()

def welkomprint():
    print("Welkom bij de NS. \nVoer nu onderstaande informatie in om verder te gaan.")
welkomprint()

def input_integer(prompt):
    """
    De input moet bestaan uit enkel getallen, als dit niet het geval is wordt dit aangegeven.
    De functie zal dan vragen om een nieuwe input.
    """
    invoer = input(prompt)
    if invoer and invoer.isdigit():
        return int(invoer)
    else:
        print("De invoer is niet correct. Probeer het opnieuw.")
        return input_integer(prompt)

def input_character(prompt):
    """
    De input moet bestaan uit enkel letters, als dit niet het geval is wordt dit aangegeven.
    De functie zal dan vragen om een nieuwe input.
    """
    invoer = input(prompt)
    if invoer and invoer.isalpha():
        return str(invoer)
    else:
        print("De invoer is niet correct. Probeer het opnieuw.")
        return input_character(prompt)

def controleerstations():
    """
    In deze functie worden de:
    naam, ovnummer, beginstation en eindstation ingevoerd door de gebruiker.
    Bij ovnummer is alleen een input geldig van nummers
    Daarnaast moet het begin en eindstation niet hetzelfde zijn en moeten beide in nsAPI voorkomen
    Al deze bovenstaande gegevens worden opgeslagen in gegevens

    """
    naam = input("Voer uw naam in: ")
    ovnummer = input_integer("Voer uw ov-chipkaartnummer in: ")
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
    global gegevens
    gegevens = naam,ovnummer,beginstation,eindstation
controleerstations()

def generateQR():
    """
    Deze functie genereert een QR-code op basis van de bovenstaande code(controleerstations())
    Dit gebeurt op basis van de input van de gebruiker. De input is opgeslagen in gegevens.
    """
    global gegevens
    qr = qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
            )
    qr.add_data(gegevens)
    qr.make(fit=True)
    print(qr.get_matrix())
    img = qr.make_image()
    img.show()
generateQR()