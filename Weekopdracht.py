import qrcode
import requests

def nsAPI():
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
    invoer = input(prompt)
    if invoer and invoer.isdigit():
        return int(invoer)
    else:
        print("De invoer is niet correct. Probeer het opnieuw.")
        return input_integer(prompt)

def controleerstations():
    naam = input("Voer uw naam in: ")
    ovnummer = input_integer("Voer uw ov-chipkaartnummer in: ")
    beginstation = input("Voer uw beginstation in: ")
    while beginstation not in stations:
        print("Het beginstation is niet bekend.")
        beginstation = input("Voer uw beginstation in: ")
    eindstation = input("Voer uw eindstation in: ")
    while eindstation not in stations:
        print("Het eindstation is niet bekend.")
        eindstation = input("Voer uw eindstation in: ")
    while beginstation == eindstation:
        print("Het eindstation mag niet hetzelfde zijn als het beginstation zijn.")
        eindstation = input("Voer uw eindstation in: ")
    global gegevens
    gegevens = naam,ovnummer,beginstation,eindstation
controleerstations()

def generateQR():
    global gegevens
    qr = qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
    qr.add_data(gegevens)
    qr.make(fit=True)
    print(qr.get_matrix())
    img = qr.make_image()
    img.show()
generateQR()




