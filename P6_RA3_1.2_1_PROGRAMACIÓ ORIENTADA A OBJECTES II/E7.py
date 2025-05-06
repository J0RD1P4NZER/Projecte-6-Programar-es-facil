# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

class Rellotge:
    def __init__(self, hores=0):
        self.__hores = hores if 0 <= hores <= 23 else 0  # Atribut privat amb validació inicial

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, valor):
        if 0 <= valor <= 23:
            self.__hores = valor
        else:
            print("Error: Les hores han de ser entre 0 i 23.")

    def mostrar_hora(self):
        print(f"{self.__hores:02d}:00")  # Format HH:00

# Exemple d'ús
rellotge = Rellotge()
rellotge.mostrar_hora()

rellotge.hores = 15
rellotge.mostrar_hora()

rellotge.hores = 25  # No permet valors fora del rang
