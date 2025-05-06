# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

class Termostat:
    def __init__(self, temperatura=20):  # Valor per defecte
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 10 <= valor <= 30:
            self.__temperatura = valor
        else:
            print("Error: La temperatura ha de ser entre 10 i 30 °C.")

# Exemple d'ús
termostat = Termostat()
print("Temperatura actual:", termostat.temperatura)

termostat.temperatura = 25
print("Temperatura ajustada a:", termostat.temperatura)

termostat.temperatura = 35  # No permet valors fora del rang
