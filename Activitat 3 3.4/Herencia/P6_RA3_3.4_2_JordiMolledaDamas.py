# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 9/5/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"{self.marca} arrencant...")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")

# Creació d'una instància de Cotxe i crida dels mètodes
cotxe = Cotxe("Toyota")
cotxe.arrencar()
cotxe.tocar_claxon()