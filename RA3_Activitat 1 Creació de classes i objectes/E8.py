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

# Exemple d'ús
animal1 = Animal("Luna", "Gos")
animal1.fer_soroll()
