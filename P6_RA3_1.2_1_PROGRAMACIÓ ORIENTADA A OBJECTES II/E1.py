# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

class CompteBancari:
    def __init__(self, saldo=0):
        self.__saldo = saldo  # Atribut privat

    def ingressar(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat
            print(f"Ingressats {quantitat} €. Saldo actual: {self.__saldo} €")
        else:
            print("Error: La quantitat ha de ser positiva.")

    def retirar(self, quantitat):
        if 0 < quantitat <= self.__saldo:
            self.__saldo -= quantitat
            print(f"Retirats {quantitat} €. Saldo restant: {self.__saldo} €")
        else:
            print("Error: Saldo insuficient o quantitat no vàlida.")

    def consultar_saldo(self):
        return f"Saldo actual: {self.__saldo} €"

# Exemple d'ús
compte = CompteBancari(100)
compte.ingressar(50)
compte.retirar(30)
print(compte.consultar_saldo())
