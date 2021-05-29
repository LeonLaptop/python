def Auswahl():
    Auswahl = input(" Anwendungsentwicklung: \n \n Bitte wählen Sie eine Zahl. \n 1 = Bezugskalkulation \n 2 = Verkaufskalkulation \n Eingabe: ")
    print("")
    if(Auswahl == "2"):
        Verkaufskalkulation()
    elif(Auswahl == "1"):
        Bezugskalkulation()
    else:
        print("Du musst eine Auswahl treffen.")


def Bezugskalkulation():
    print("Bezugskalkulation: \n")
    preis = float(input("Bitte geben Sie ihren Listeneinkaufspreis ein: \n")) # 1875 €
    rabatt = float(input("Bitte geben Sie ihren Rabatt ein: \n")) # 0.05 %
    skonto = float(input("Bitte geben Sie ihren Skonto ein: \n")) # 0.03 %
    bezugskosten = float(input("Bitte geben Sie ihren Bezugskosten ein: \n")) # 56 €

    print("Listeneinkaufspreis: " + str(round(preis, 2)))
    zieleinkaufspreis = rabatt * preis
    zieleinkaufspreis = preis - zieleinkaufspreis
    print("Zieleinkaufspreis: " + str(round(zieleinkaufspreis, 2)))
    bareinkaufspreis = skonto * zieleinkaufspreis
    bareinkaufspreis = zieleinkaufspreis - bareinkaufspreis
    print("Bareinkaufspreis: " + str(round(bareinkaufspreis)))
    bezugspreis = bareinkaufspreis + bezugskosten
    print("Bezugspreis: " + str(round(bezugspreis, 2)))

def Verkaufskalkulation():
    print("Verkaufskalkulation: \n")
    preis = float(input("Bezugspreis in €: \n"))
    handlungsgemeinkosten = float(input("Handlungskosten in dezimal: \n"))
    gewinn = float(input("Gewinn in dezimal: \n"))
    skonto = float(input("Skonto in dezimal: "))
    rabatt = float(input("Rabatt in dezimal: \n"))

    selbstkostenpreis = handlungsgemeinkosten * preis
    print(round(selbstkostenpreis, 2))
    selbstkostenpreis = preis + selbstkostenpreis
    print(round(selbstkostenpreis, 2))
    barverkaufspreis = gewinn * selbstkostenpreis
    barverkaufspreis = selbstkostenpreis + barverkaufspreis
    print(round(barverkaufspreis, 2))
    zielverkaufspreis = skonto * barverkaufspreis
    zielverkaufspreis = barverkaufspreis + zielverkaufspreis
    print(zielverkaufspreis)
    listenverkaufspreis = zielverkaufspreis * rabatt
    listenverkaufspreis = listenverkaufspreis + zielverkaufspreis
    print(listenverkaufspreis)

Auswahl()