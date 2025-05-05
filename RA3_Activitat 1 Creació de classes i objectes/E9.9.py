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
        return math.pi * self.radi ** 2

cercles = [Cercle(4), Cercle(8), Cercle(6)]

print("Cercles amb àrea superior a 50:")
for cercle in cercles:
    if cercle.area() > 50:
        print(f"Radi: {cercle.radi}, Àrea: {cercle.area():.2f}")
