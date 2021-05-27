import sys

def Handelskalkulation():
    bzp1 = float(input("Geben Sie ihren Bezugspreis in € ein: \n"))
    hkz = float(input("Handlungskosten in % eingeben: \n"))
    rs = float(input("Höhe des Rabattsatzes in %: \n"))
    sks_hk = float (input("Skonto in %: \n"))
    mwsts_hk = 19

    # Verkaufskalkulation
    bvkp = bzp1*(hkz/100+1)
    print("Barverkaufspreis in €: ", round(bvkp, 2))
    zvkp = ((bvkp * 100)/(100-sks_hk))
    print("Zielverkaufspreis in €: ", round(zvkp, 2))
    nvkp = ((zvkp*100)/(100-rs))
    print("Listenverkaufspreis netto in €: ", round(nvkp, 2))
    bvkp = ((nvkp*100)/(100-mwsts_hk))
    print("Listenverkaufspreis bruto in €: ", round(bvkp, 2))

def Bezugskalkulation():
    blp = float(input("Listeneinkaufspreis in €: \n"))
    mwsts_bz = 19
    rbs = float(input("Lieferrabatt: \n"))
    sks_bz = float (input("Skonto in %: \n"))
    bk = float(input("Bezugskosten: \n"))

    # Bezugskalkulation
    nlp = blp*((100-mwsts_bz)/100)
    print("Listeneinkaufspreis in €: ", round(nlp, 2))
    zep = nlp*((100-rbs)/100)
    print("Zieleinkaufspreis in €: ", round(zep, 2))
    bek = zep * ((100-sks_bz)/100)
    print("Bareinkaufspreis on €: ", round(bek, 2))
    esp = bek + bk
    print("Bezugspreis in €: ", round(esp, 2))


Handelskalkulation()