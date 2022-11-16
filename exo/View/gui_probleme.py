from tkinter import *
from Controller import nbcars_nbplacesvides

class Gui_probleme:
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry("200x200")
        self.parent.title('coucou')
        #icone = PhotoImage(file='./View/@bus.ico')
        #self.parent.iconphoto(True, icone)
        self.parent.iconbitmap("./img/bus.ico")
        self.frame = Frame(parent)
        self.frame.pack()
        
        self.interfaceGUI()
        self.packGUI()

    def interfaceGUI(self):
        self.labNbEleves = Label(self.frame, text="Nombre d'élèves")
        self.enNbEleves = Entry(self.frame)
        self.labNbAdultes = Label(self.frame, text="Nombre d'adultes")
        self.enNbAdultes = Entry(self.frame)
        self.labNbPlacesCars = Label(self.frame, text="Nombre de places par cars")
        self.enNbPlacesCars = Entry(self.frame)
        self.retourBtn = Button(self.frame, text="Calcul", command=self.calcul)
        self.labNbCars = Label(self.frame, text="Nombre de cars")

    def packGUI(self):
        self.labNbEleves.pack()
        self.enNbEleves.pack()
        self.labNbAdultes.pack()
        self.enNbAdultes.pack()
        self.labNbPlacesCars.pack()
        self.enNbPlacesCars.pack()
        self.retourBtn.pack()
        self.labNbCars.pack()

    def calcul(self):
        try:
            nb_eleve = int(self.enNbEleves.get())
            nb_adulte = int(self.enNbAdultes.get())
            nb_place = int(self.enNbPlacesCars.get())
            self.labNbCars.config(text=nbcars_nbplacesvides.NbCars_nbPlacesVides(nb_eleve, nb_adulte, nb_place), fg="green")
        except:
            self.labNbCars.config(text="Erreur de saisie", fg="red")