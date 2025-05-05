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

def aplicar_descompte_a_tots(productes):
    for producte in productes:
        producte.aplicar_descompte(10)
        print(f"Producte: {producte.nom}, Preu després del descompte: {producte.preu}")

productes = [Producte("Portàtil", 1000), Producte("Mòbil", 500), Producte("Auriculars", 100)]
aplicar_descompte_a_tots(productes)
