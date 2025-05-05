# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print(f"{self.nom} ({self.especie}) fa un soroll.")

class Gos(Animal):
    def fer_soroll(self):
        print(f"{self.nom} diu: Bup bup!")

gos1 = Gos("Rocky", "Gos")
gos1.fer_soroll()
