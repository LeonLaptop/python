import sys
import tkinter
from tkinter.constants import W, WORD
from tkinter import messagebox
from typing import Text

def bezugskalkulation():
    preis = textfield.get()
    rabatt = textfield1.get()
    skonto = textfield2.get()
    bezugskosten = textfield3.get()

    if(float(preis) > 0):
        zieleinkaufspreis = float(rabatt) * float(preis)
        zieleinkaufspreis =float(preis) - float(zieleinkaufspreis)
        bareinkaufspreis = float(skonto) * float(zieleinkaufspreis)
        bareinkaufspreis = float(zieleinkaufspreis) - float(bareinkaufspreis)   
        bezugspreis = float(bareinkaufspreis) + float(bezugskosten)
        messagebox.showinfo("Ergebnis", "Bezugskalkulation:\n" + "\nPreis: " + str(preis) +" €" + "\nZieleinkaufspreis:" + str(round(zieleinkaufspreis,2)) + " €" + "\nBareinkaufspreis: " + str(round(bareinkaufspreis,2))+ " €" + "\nBezugspreis: " + str(round(bezugspreis,2)) + " €")
    else:
        messagebox.showerror("Error", "Bitte füllen Sie alle Eingaben aus.")

def verkaufskalkulation():
    preis = textfield4.get()
    handlungsgemeinkosten = textfield5.get()
    gewinn = textfield6.get()
    skonto = textfield7.get()
    rabatt = textfield8.get()
    mwst = textfield9.get()

    if(float(preis) > 0):
        selbstkostenpreis = float(handlungsgemeinkosten) * float(preis)
        selbstkostenpreis = float(preis) + float(selbstkostenpreis)
        barverkaufspreis = float(gewinn) * float(selbstkostenpreis)
        barverkaufspreis = float(selbstkostenpreis) + float(barverkaufspreis)
        zielverkaufspreis = float(skonto) * float(barverkaufspreis)
        zielverkaufspreis = float(barverkaufspreis) + float(zielverkaufspreis)
        listenverkaufspreis = float(zielverkaufspreis) * float(rabatt)
        listenverkaufspreis = float(listenverkaufspreis) + float(zielverkaufspreis)
        brutoListenverkaufspreis = float(mwst) * float(listenverkaufspreis)
        brutoListenverkaufspreis = float(listenverkaufspreis) + float(brutoListenverkaufspreis)
        messagebox.showinfo("Ergebnis","Verkaufskalkulation:\n" + "\nBezugspreis: \n" + str(preis) +" €" + "\n\nSelbstkostenpreis: \n" + str(round(selbstkostenpreis,2)) + " €" +  "\n\nBarverkaufspreis: \n" + str(round(barverkaufspreis,2)) + " €"+ "\n\nZielverkaufspreis:\n" + str(round(zielverkaufspreis,2)) + " €" + "\n\nNetto Listenverkaufspreis:\n" + str(round(listenverkaufspreis,2)) + " €" + "\n\nBruto Listenverkaufspreis: \n" + str(round(brutoListenverkaufspreis,2)) + " €")
    else:
         messagebox.showerror("Error", "Bitte füllen Sie alle Eingaben aus.")


def close_window():
    window.destroy()
    exit()

window = tkinter.Tk()
window.title("Python Aufgabe AE")

#=============== BEZUGSKALKULATION ================#
tkinter.Label (window, text="Bezugskalkulation",font="none 15 bold" ) .grid(row=1,column=0, sticky=W)
tkinter.Label (window, text="Bitte füllen Sie alle Felder aus.",font="none 9" ) .grid(row=2,column=0, sticky=W)
tkinter.Label (window, text="Die Prozente müssen in dezimal angegeben werden.",font="none 9" ) .grid(row=3,column=0, sticky=W)
tkinter.Label (window, text="===================",font="none 12" ) .grid(row=4,column=0, sticky=W)

#========= Textfield Listeneinkaufspreis ==========#
tkinter.Label (window, text="Brutolisteneinkaufspreis: ",font="none 12" ) .grid(row=5,column=0, sticky=W)
textfield = tkinter.Entry(window, width=15,)
textfield.grid(row=5, column=1, sticky=W)
tkinter.Label (window, text="€",font="none 12 bold" ) .grid(row=5,column=2, sticky=W)

#============= Textfield Lieferrabatt =============#
tkinter.Label (window, text="Lieferrabatt: ",font="none 12" ) .grid(row=6,column=0, sticky=W)
textfield1 = tkinter.Entry(window, width=15,)
textfield1.grid(row=6, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12 bold" ) .grid(row=6,column=2, sticky=W)

#================ Textfield Skonto ================#
tkinter.Label (window, text="Skonto: ",font="none 12" ) .grid(row=7,column=0, sticky=W)
textfield2 = tkinter.Entry(window, width=15,)
textfield2.grid(row=7, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12 bold" ) .grid(row=7,column=2, sticky=W)

#============== Textfield Bezugskosten ============#
tkinter.Label (window, text="Bezugskosten: ",font="none 12" ) .grid(row=8,column=0, sticky=W)
textfield3 = tkinter.Entry(window, width=15,)
textfield3.grid(row=8, column=1, sticky=W)
tkinter.Label (window, text="€",font="none 12 bold" ) .grid(row=8,column=2, sticky=W)

#===================== Button =====================#
tkinter.Button(window, text="Berechnen", width=10, command=bezugskalkulation, bg="SpringGreen2", fg="black") .grid(row=9, column=0, sticky=W)

#===================== Spacer =====================#
tkinter.Label (window, text="",font="none 12" ) .grid(row=10,column=0, sticky=W)

#=============== HANDELSKALKULATION ===============#
tkinter.Label (window, text="Handelskalkulation",font="none 15 bold" ) .grid(row=11,column=0, sticky=W)
tkinter.Label (window, text="Bitte füllen Sie alle Felder aus.",font="none 9" ) .grid(row=12,column=0, sticky=W)
tkinter.Label (window, text="===================",font="none 12" ) .grid(row=13,column=0, sticky=W)

#========= Textfield Barverkaufspreis ==========#
tkinter.Label (window, text="Bezugspreis: ",font="none 12" ) .grid(row=30,column=0, sticky=W)
textfield4 = tkinter.Entry(window, width=15,)
textfield4.grid(row=30, column=1, sticky=W)
tkinter.Label (window, text="€",font="none 12 bold" ) .grid(row=30,column=2, sticky=W)

#========= Textfield Handlungskostenzuschlag ==========#
tkinter.Label (window, text="Handlungskostenzuschlag: ",font="none 12" ) .grid(row=31,column=0, sticky=W)
textfield5 = tkinter.Entry(window, width=15,)
textfield5.grid(row=31, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12 bold" ) .grid(row=31,column=2, sticky=W)

#========= Textfield Gewinn ==========#
tkinter.Label (window, text="Gewinn: ",font="none 12" ) .grid(row=33,column=0, sticky=W)
textfield6 = tkinter.Entry(window, width=15,)
textfield6.grid(row=33, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12 bold" ) .grid(row=33,column=2, sticky=W)

#========= Textfield Skonto ==========#
tkinter.Label (window, text="Skonto: ",font="none 12" ) .grid(row=34,column=0, sticky=W)
textfield7 = tkinter.Entry(window, width=15,)
textfield7.grid(row=34, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12 bold" ) .grid(row=34,column=2, sticky=W)

#========= Textfield Verkaufsrabatt ==========#
tkinter.Label (window, text="Wiederverkäuferrabatt: ",font="none 12" ) .grid(row=35,column=0, sticky=W)
textfield8 = tkinter.Entry(window, width=15,)
textfield8.grid(row=35, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12 bold" ) .grid(row=35,column=2, sticky=W)

#========= Textfield Mwstr ==========#
tkinter.Label (window, text="Mwst: ",font="none 12" ) .grid(row=36,column=0, sticky=W)
textfield9 = tkinter.Entry(window, width=15,)
textfield9.grid(row=36, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12 bold" ) .grid(row=36,column=2, sticky=W)

tkinter.Button(window, text="Berechnen", width=10, command=verkaufskalkulation, bg="SpringGreen2", fg="black") .grid(row=37, column=0, sticky=W)

tkinter.Label (window, text="",font="none 12" ) .grid(row=37,column=0, sticky=W)
tkinter.Button(window, text=" Exit", width=4, command= close_window, bg="firebrick2", fg="black") .grid(row=40,column=2, sticky=W)
tkinter.Label (window, text=" Erstellt von Leon Schmidt | 29.05.2021",font="none 8" ) .grid(row=40,column=0, sticky=W)


window.mainloop()

