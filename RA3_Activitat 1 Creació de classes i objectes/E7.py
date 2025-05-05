# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * (self.radi ** 2)

    def perimetre(self):
        return 2 * math.pi * self.radi

# Exemple d'ús
cercle1 = Cercle(5)
print("Àrea del cercle:", cercle1.area())
print("Perímetre del cercle:", cercle1.perimetre())
