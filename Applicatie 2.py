__author__ = 'Owner'


def invoer_incheckzuil():
    master = Tk()
    Label(master, text="Voer ov-chipkaartnummer in").grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    Button(master, text='Invoeren', command=master.quit).grid(row=0, column=4 , sticky=W, pady=20)
    mainloop()
    Z = e1.get()
    return Z


def vergelijk_database(Z):
    with conn:
        c = conn.cursor()
        t = (Z,)
    for row in c.execute('SELECT * FROM ReizigersDB'):
        if row in c.execute('SELECT * FROM ReizigersDB WHERE OVnummer=?', t):
            print(row)
        else:
            print("U heeft nog geen reis gemaakt of een verkeerd OVnummer ingetyped")