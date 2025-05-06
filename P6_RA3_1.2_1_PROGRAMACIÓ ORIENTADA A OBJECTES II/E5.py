# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

class Sensor:
    def __init__(self, valor=0):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor
        else:
            print("Error: El valor ha de ser entre 0 i 100.")

# Exemple d'ús
sensor1 = Sensor()
print("Valor del sensor:", sensor1.valor)

sensor1.valor = 75
print("Nou valor del sensor:", sensor1.valor)

sensor1.valor = 120  # No permet valors fora del rang
