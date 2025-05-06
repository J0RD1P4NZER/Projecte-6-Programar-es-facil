# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu if preu > 0 else 0  # Assegura que el preu inicial sigui vàlid

    @property
    def preu(self):
        return self.__preu

    @preu.setter
    def preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
        else:
            print("Error: El preu ha de ser superior a 0.")

# Exemple d'ús
producte1 = Producte("Ordinador", 1200)
print("Preu inicial:", producte1.preu)

producte1.preu = 800
print("Preu actualitzat:", producte1.preu)

producte1.preu = -100  # No permet preus negatius
