# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 5/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES I

class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def ingressar(self, quantitat):
        self.saldo += quantitat
        print(f"Has ingressat {quantitat} €. Saldo actual: {self.saldo} €")

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
            print(f"Has retirat {quantitat} €. Saldo restant: {self.saldo} €")
        else:
            print("Saldo insuficient.")

    def veure_saldo(self):
        print(f"Saldo actual: {self.saldo} €")

# Exemple d'ús
compte = CompteBancari(100)
compte.ingressar(50)
compte.retirar(30)
compte.veure_saldo()
