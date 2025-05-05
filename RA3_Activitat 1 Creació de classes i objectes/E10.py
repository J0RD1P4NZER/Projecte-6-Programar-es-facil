# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre_punt):
        return math.sqrt((altre_punt.x - self.x)**2 + (altre_punt.y - self.y)**2)

# Exemple d'ús
punt1 = Punt(3, 4)
punt2 = Punt(7, 1)

print(f"La distància entre els dos punts és: {punt1.distancia(punt2):.2f}")
