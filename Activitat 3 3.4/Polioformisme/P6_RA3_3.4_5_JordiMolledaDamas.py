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

class Vehicle:
    def moure(self):
        pass  # Mètode abstracte

class Cotxe(Vehicle):
    def moure(self):
        print("🚗 El cotxe està circulant per la carretera")

class Bicicleta(Vehicle):
    def moure(self):
        print("🚴 La bicicleta està pedalejant pel camí")

class Barca(Vehicle):
    def moure(self):
        print("⛵ La barca està navegant per l'aigua")

def simular_moviment(vehicles):
    for vehicle in vehicles:
        vehicle.moure()

# Creació d'instàncies i crida a la funció
Vehicle