import wx

#Python- Programm zur Berechnung des Brutto-Listenverkaufspreises. Eingabedaten sind Bezugspreis, 
# Handlungskostenzuschlag, Gewinnzuschlag, Rabattsatz, Skontosatz und MWST-Satz. Ausgegeben werden sollen Barverkaufspreis, 
# Zielverkaufspreis und Listenverkaufspreis netto und Listenverkaufspreis brutto. 

#create Parent wrapper
class MyFrame (wx.Frame) :
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

class MyApp (wx.App) :
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Our first Window.")
        self.frame.show()

        return True

app = MyApp
app.MainLoop()

#write my app!