#import list:
#Pillow
#PyQRCode
#qrcode
#pip

naam = input("Voer uw naam in: ")
ovnummer = int(input("Voer uw ov-chipkaartnummer: "))
beginstation = input("Voer uw beginstation in: ")
eindstation = input("Voer uw eindstation in: ")

gegevens = naam,ovnummer,beginstation,eindstation

import qrcode
def generateQR():
    qr = qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )

    qr.add_data("QRcode Test")
    qr.make(fit=True)
    print(qr.get_matrix())
    img = qr.make_image()
    img.show()
generateQR()

