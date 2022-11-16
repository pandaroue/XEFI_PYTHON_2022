
from math import ceil


class NbCars_nbPlacesVides:
    def __init__(self, nb_eleves, nb_adultes, nb_places):
        self.nb_eleves = nb_eleves
        self.nb_adultes = nb_adultes
        self.nb_places = nb_places
        self.nb_cars = self.nb_cars()
        self.nb_place_vides = self.nb_place_vides()
    
    def nb_cars(self):
        return ceil((self.nb_eleves + self.nb_adultes) / self.nb_places)
    def nb_place_vides(self):
        return self.nb_cars * self.nb_places - (self.nb_eleves + self.nb_adultes)

    def __str__(self):
        return (f"Il y a {self.nb_cars} cars et {self.nb_place_vides} places vides.")
