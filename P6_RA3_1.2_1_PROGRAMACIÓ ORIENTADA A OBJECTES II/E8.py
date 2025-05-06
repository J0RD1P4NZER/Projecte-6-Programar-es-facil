# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 6/5/2025
# Activitat 1: Creació de classes i objectes
# PROGRAMACIÓ ORIENTADA A OBJECTES II

class Alumne:
    def __init__(self, nom, edat):
        self.nom = nom
        self.__edat = edat if edat >= 0 else 0  # Atribut privat amb validació

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, nova_edat):
        if nova_edat >= 0:
            self.__edat = nova_edat
        else:
            print("Error: L'edat no pot ser negativa.")

# Exemple d'ús
alumne1 = Alumne("Jordi", 20)
print(f"{alumne1.nom} té {alumne1.edat} anys.")

alumne1.edat = 25
print(f"Nova edat: {alumne1.edat}")

alumne1.edat = -5  # No permet valors negatius
