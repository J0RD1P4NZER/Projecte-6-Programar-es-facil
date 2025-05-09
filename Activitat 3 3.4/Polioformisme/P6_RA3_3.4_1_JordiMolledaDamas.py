# ************************************************************
# Administració de Sistemes Informatics en Xarxa
# Autor: Jordi Molleda Damas
# Data: 9/5/2025
# Versió: 1.0
# ************************************************************
# Descripció:
# 
# Especificacions d'entrada:
# 
# ************************************************************

class Animal:
    def fer_soroll(self):
        pass  # Mètode abstracte

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

def reproduir_soroll(animal):
    print(animal.fer_soroll())

# Creació d'instàncies i crida de la funció
gat = Gat()
vaca = Vaca()

reproduir_soroll(gat)
reproduir_soroll(vaca)