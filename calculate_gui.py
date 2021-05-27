import sys
import tkinter
from tkinter.constants import W, WORD
from tkinter import messagebox
from typing import Text

def click_bk():
    blp=textfield.get()
    mwsts_bz = 19
    lr=textfield1.get()
    sk_bz=textfield2.get()
    bk=textfield3.get()

    if(float(blp) > 0):
        nlp = float(blp)*((100-float(mwsts_bz))/100)
        zep = float(nlp)*((100-float(lr))/100)
        bek = float(zep) * ((100-float(sk_bz))/100)
        esp = float(bek) + float(bk)  
        messagebox.showinfo("Ergebnis","BEZUGSKALKULATION" + "\n Listeneinkaufpreis: " + str(round(nlp)) + " €" + "\n Zieleinkaufspreis: " + str(round(zep)) + " €" + "\n Bareinkaufspreis: " + str(round(bek)) + " €"+ "\n Bezugspreis: " + str(round(esp)) + " €")
    else:
        messagebox.showerror("Error", "Dein Brutolistenpreis muss größer als 0 sein.")

def click_hk():
    mwsts_hk = 19
    blp = textfield4.get()
    hkz = float(textfield5.get())
    rs = textfield6.get()
    sks_hk = textfield7.get()
    if (float(blp) > 0):
        bvkp = float(blp)*(hkz/100+1)
        zvkp = ((float(bvkp) * 100)/(100-float(sks_hk)))
        nvkp = ((float(zvkp)*100)/(100-float(rs)))
        bvkp = ((float(nvkp)*100)/(100-float(mwsts_hk)))
        messagebox.showinfo("Ergebnis", "Barverkaufspreis: " + str(round(bvkp)) + " €" + "\n Zielverkaufspreis: " + str(round(zvkp)) + " €" + "\n Listenverkaufspreis netto: " + str(round(nvkp)) + " €"+ "\n Listenverkaufspreis bruto: " + str(round(bvkp)) + " €")
    else:
        messagebox.showerror("Error", "Dein Bezugspreis muss größer als 0 sein.")


def close_window():
    window.destroy()
    exit()

window = tkinter.Tk()
window.title("Python Aufgabe AE")

#=============== BEZUGSKALKULATION ================#
tkinter.Label (window, text="Bezugskalkulation",font="none 15 bold" ) .grid(row=1,column=0, sticky=W)
tkinter.Label (window, text="*Bitte füllen Sie alle Felder aus.",font="none 8" ) .grid(row=2,column=0, sticky=W)
tkinter.Label (window, text="===================",font="none 12" ) .grid(row=3,column=0, sticky=W)

#========= Textfield Listeneinkaufspreis ==========#
tkinter.Label (window, text="Brutolisteneinkaufspreis: ",font="none 12" ) .grid(row=4,column=0, sticky=W)
textfield = tkinter.Entry(window, width=15,)
textfield.grid(row=4, column=1, sticky=W)
tkinter.Label (window, text="€",font="none 12" ) .grid(row=4,column=2, sticky=W)

#============= Textfield Lieferrabatt =============#
tkinter.Label (window, text="Lieferrabatt: ",font="none 12" ) .grid(row=5,column=0, sticky=W)
textfield1 = tkinter.Entry(window, width=15,)
textfield1.grid(row=5, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12" ) .grid(row=5,column=2, sticky=W)

#================ Textfield Skonto ================#
tkinter.Label (window, text="Skonto: ",font="none 12" ) .grid(row=6,column=0, sticky=W)
textfield2 = tkinter.Entry(window, width=15,)
textfield2.grid(row=6, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12" ) .grid(row=6,column=2, sticky=W)

#============== Textfield Bezugskosten ============#
tkinter.Label (window, text="Bezugskosten: ",font="none 12" ) .grid(row=7,column=0, sticky=W)
textfield3 = tkinter.Entry(window, width=15,)
textfield3.grid(row=7, column=1, sticky=W)
tkinter.Label (window, text="€",font="none 12" ) .grid(row=7,column=2, sticky=W)

#===================== Button =====================#
tkinter.Button(window, text="Berechnen", width=10, command=click_bk, bg="SpringGreen2", fg="black") .grid(row=8, column=0, sticky=W)

#===================== Spacer =====================#
tkinter.Label (window, text="",font="none 12" ) .grid(row=10,column=0, sticky=W)

#=============== HANDELSKALKULATION ===============#
tkinter.Label (window, text="Handelskalkulation",font="none 15 bold" ) .grid(row=11,column=0, sticky=W)
tkinter.Label (window, text="*Bitte füllen Sie alle Felder aus.",font="none 8" ) .grid(row=12,column=0, sticky=W)
tkinter.Label (window, text="===================",font="none 12" ) .grid(row=13,column=0, sticky=W)

#========= Textfield Barverkaufspreis ==========#
tkinter.Label (window, text="Bezugspreis: ",font="none 12" ) .grid(row=30,column=0, sticky=W)
textfield4 = tkinter.Entry(window, width=15,)
textfield4.grid(row=30, column=1, sticky=W)
tkinter.Label (window, text="€",font="none 12" ) .grid(row=30,column=2, sticky=W)

#========= Textfield Handlungskostenzuschlag ==========#
tkinter.Label (window, text="Handlungskostenzuschlag: ",font="none 12" ) .grid(row=31,column=0, sticky=W)
textfield5 = tkinter.Entry(window, width=15,)
textfield5.grid(row=31, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12" ) .grid(row=31,column=2, sticky=W)

#========= Textfield Rabatsatz ==========#
tkinter.Label (window, text="Rabatsatz: ",font="none 12" ) .grid(row=33,column=0, sticky=W)
textfield6 = tkinter.Entry(window, width=15,)
textfield6.grid(row=33, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12" ) .grid(row=33,column=2, sticky=W)

#========= Textfield Skonto ==========#
tkinter.Label (window, text="Skonto: ",font="none 12" ) .grid(row=34,column=0, sticky=W)
textfield7 = tkinter.Entry(window, width=15,)
textfield7.grid(row=34, column=1, sticky=W)
tkinter.Label (window, text="%",font="none 12" ) .grid(row=34,column=2, sticky=W)

tkinter.Button(window, text="Berechnen", width=10, command=click_hk, bg="SpringGreen2", fg="black") .grid(row=35, column=0, sticky=W)

tkinter.Label (window, text="",font="none 12" ) .grid(row=36,column=0, sticky=W)
tkinter.Button(window, text=" Exit", width=4, command= close_window, bg="firebrick2", fg="black") .grid(row=40,column=2, sticky=W)
tkinter.Label (window, text="created by Leon Schmidt",font="none 8" ) .grid(row=40,column=0, sticky=W)


window.mainloop()

