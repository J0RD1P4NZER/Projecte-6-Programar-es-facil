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

class Empleat:
    def __init__(self, nom):
        self.nom = nom

    def calcular_sou(self):
        pass  # Mètode abstracte

class Fixe(Empleat):
    def __init__(self, nom, sou_mensual):
        super().__init__(nom)
        self.sou_mensual = sou_mensual

    def calcular_sou(self):
        return self.sou_mensual

class Autonom(Empleat):
    def __init__(self, nom, hores, tarifa_hora):
        super().__init__(nom)
        self.hores = hores
        self.tarifa_hora = tarifa_hora

    def calcular_sou(self):
        return self.hores * self.tarifa_hora

def mostrar_sous(llista_empleats):
    for empleat in llista_empleats:
        print(f"{empleat.nom}: {empleat.calcular_sou()} €")

# Creació d'instàncies i crida a la funció
empleats = [Fixe("Daniel", 2000), Autonom("Maria", 160, 15)]
mostrar_sous(empleats)