#Dit is de weekopdracht van programmeren.


# import list:
# Pillow
# PyQRCode
# qrcode
# pip

naam=input("Wat is uw naam? ")
id=input("Wat s uw OV-nummer?")

gegevens=naam,id

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