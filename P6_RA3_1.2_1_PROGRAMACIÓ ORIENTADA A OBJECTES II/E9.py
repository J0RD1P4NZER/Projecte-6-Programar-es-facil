# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

class Joc:
    def __init__(self):
        self.__puntuacio = 0  # Atribut privat inicialitzat a 0

    def sumar_punts(self, punts):
        if punts > 0:
            self.__puntuacio += punts
            print(f"S'han sumat {punts} punts. Puntuació actual: {self.__puntuacio}")
        else:
            print("Error: Els punts han de ser positius.")

    def reiniciar_puntuacio(self):
        self.__puntuacio = 0
        print("Puntuació reiniciada.")

    @property
    def puntuacio(self):
        return self.__puntuacio

# Exemple d'ús
joc1 = Joc()
joc1.sumar_punts(10)
print(f"Puntuació: {joc1.puntuacio}")
joc1.reiniciar_puntuacio()
print(f"Puntuació després del reinici: {joc1.puntuacio}")
