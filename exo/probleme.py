# Problème 1
# 142 élèves 9 adultes
# cars 58 places
# tous pleins sauf 1
# combien reste t-il de places vides

from math import ceil
nb_eleves = 142
nb_adultes = 9
nb_places = 58

nb_cars = ceil((nb_eleves + nb_adultes) / nb_places)
nb_places_vides = nb_cars * nb_places - (nb_eleves + nb_adultes)
print("Il reste", nb_places_vides, "places vides")

def nb_places_vides(nb_eleves, nb_adultes, nb_places):
    nb_cars = ceil((nb_eleves + nb_adultes) / nb_places)
    nb_places_vides = nb_cars * nb_places - (nb_eleves + nb_adultes)
    return nb_places_vides

print("Il reste", nb_places_vides(nb_eleves,nb_adultes,nb_places), "places vides")

# créer une class qui affiche nb_cars et le nombres de places vides

print(NbCars_nbPlacesVides(nb_eleves, nb_adultes, nb_places))

if __name__ == "__main__":
    from exo.view.gui_probleme import *

