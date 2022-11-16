""" * Problème 1
142 élèves 9 adultes 
car 58 place
tous plein sauf 1
combien reste t-il de palces vides?
"""
"""Problème 1
98 élèves 4 adultes 
car 58 place
tous plein sauf 1
combien reste t-il de palces vides?
"""
"""Problème 3
376 élèves 12 adultes 
car 52 place
tous plein sauf 1
combien reste t-il de palces vides?
"""
import tkinter as tk
from tkinter import ttk
from math import ceil

"""def fonctionProbleme(nombreEleve,nombreAdulte,placeDansCar):
    placeVides = (ceil((nombreEleve + nombreAdulte)/placeDansCar)*placeDansCar)- (nombreEleve + nombreAdulte)
    print(f'Le nombres de places vide est : {placeVides}') """

class Probleme(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.style = ttk.Style()
        self.style.configure('lfBlocInfosCar.TLabelframe', background='#7AC5CD')
        
        self.fInformations = ttk.Frame(self)
        self.fValidation = ttk.Frame(self)
        
        self.bValider = ttk.Button(self.fValidation, text='Valider')
        self.bValider.pack( side = tk.LEFT, padx=20, pady=20)

        self.__createBlockInfo()
        self.__place()
        self.__bind()

    def __place(self):
        self.fInformations.pack(fill=tk.X)
        self.fValidation.pack(fill=tk.X)

        self.lNombreEleve.grid(column=0, row=1, sticky=tk.W)
        self.eNombreEleve.grid(column=1, row=1, sticky=tk.E)

        self.lNombreAdultes.grid(column=0, row=2, sticky=tk.W)
        self.eNombreAdultes.grid(column=1, row=2, sticky=tk.E)

        self.lNombrePlaceMaxCar.grid(column=0, row=3, sticky=tk.W)
        self.eNombrePlaceMaxCar.grid(column=1, row=3, sticky=tk.E)

        self.lReponse.grid(column=0, row=4, sticky=tk.W)


    def __createBlockInfo(self):
            # Création du premier block 
        self.lfBlocInfos = ttk.Labelframe(self.fInformations, text='Infos', style='lfBlocInfosCar.TLabelframe')
        self.lfBlocInfos.pack(side=tk.LEFT, padx=20, pady=20, ipady=5)

        self.lNombreEleve = ttk.Label(self.lfBlocInfos, text='veuillez saisir le nombre d\'élèves')
        self.eNombreEleve = ttk.Entry(self.lfBlocInfos)
        self.lNombreAdultes = ttk.Label(self.lfBlocInfos, text='veuillez saisir le nombre d\'adultes')
        self.eNombreAdultes= ttk.Entry(self.lfBlocInfos)
        self.lNombrePlaceMaxCar = ttk.Label(self.lfBlocInfos, text='veuillez saisir le nombre de place dans le car')
        self.eNombrePlaceMaxCar = ttk.Entry(self.lfBlocInfos) 

        self.lReponse = ttk.Label(self.lfBlocInfos, text='Reponse')

    def __bind(self):
        self.bValider.bind("<Button-1>", self.reponse)

    def nombreCar(self, nb_eleve, nb_adulte, nb_place_car):
        return ceil((nb_eleve+nb_adulte)/nb_place_car)

    def nombrePlaceVides(self, nb_eleve, nb_adulte, nb_place_car):
        return (self.nombreCar(nb_eleve,nb_adulte,nb_place_car)*nb_place_car)- (nb_eleve + nb_adulte)

    def reponse(self, event=None):
        try:
            nb_eleve = int(self.eNombreEleve.get())
            nb_adulte = int(self.eNombreAdultes.get())
            nb_place_car = int(self.eNombrePlaceMaxCar.get())
            self.lReponse.configure(text=f'Le nombre de cars est de {str(self.nombreCar(nb_eleve, nb_adulte, nb_place_car))} \n le nombre de place vide est de {str(self.nombrePlaceVides(nb_eleve, nb_adulte, nb_place_car))}')
        except:
            self.lReponse.configure(text="Erreur de saisie")
        

#fonctionProbleme(142,9,58)
app = Probleme()
#probleme.__str__()
app.mainloop()
