# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        self.preu -= self.preu * (percentatge / 100)
        return self.preu

# Exemple d'ús
producte1 = Producte("Portàtil", 1000)
print("Preu abans del descompte:", producte1.preu)
print("Preu després del descompte:", producte1.aplicar_descompte(10))
